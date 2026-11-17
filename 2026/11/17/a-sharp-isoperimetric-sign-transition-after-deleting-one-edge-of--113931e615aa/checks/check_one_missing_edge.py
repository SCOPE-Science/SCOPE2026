"""Independent convex-hull comparisons for one-defect bipartite root polytopes.

Run: python check_one_missing_edge.py
Requires NumPy, SciPy. All computations are finite-dimensional diagnostics.
"""
import math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.linalg import null_space


def formula(p, q):
    assert p >= 2 and q >= 2
    d = p + q - 2
    volume_full = math.sqrt(p*q)/(math.factorial(p-1)*math.factorial(q-1))
    A = (p-1)*math.sqrt((p-1)/p)
    B = (q-1)*math.sqrt((q-1)/q)
    C = math.sqrt(2 - 1/p - 1/q)
    surface_full = volume_full*(p*A + q*B)
    volume_cut = math.sqrt(p*q)/math.factorial(d)
    surface_cut = math.sqrt(p*q)/math.factorial(d-1)*(A+B-C)
    epsilon = volume_cut/volume_full
    z = d*(A+B-C)/(p*A+q*B)
    quotient_ratio = (1-z*epsilon)/(1-epsilon)**((d-1)/d)
    return volume_full-volume_cut, surface_full-surface_cut, quotient_ratio


def direct_hull(p, q):
    N = p+q
    constraints = np.zeros((2,N))
    constraints[0,:p] = 1
    constraints[1,p:] = 1
    basis = null_space(constraints)
    verts = []
    for i in range(p):
        for j in range(q):
            if i == p-1 and j == q-1:
                continue
            a = np.zeros(N)
            a[i] = 1
            a[p+j] = 1
            verts.append(a @ basis)
    hull = ConvexHull(np.array(verts))
    return hull.volume, hull.area


def verify():
    cases = [(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,4),(4,5),(5,5)]
    for p,q in cases:
        predicted_v, predicted_s, predicted_q = formula(p,q)
        actual_v, actual_s = direct_hull(p,q)
        assert math.isclose(predicted_v, actual_v, abs_tol=1e-8, rel_tol=2e-9), (p,q,'volume',predicted_v,actual_v)
        assert math.isclose(predicted_s, actual_s, abs_tol=1e-8, rel_tol=2e-9), (p,q,'surface',predicted_s,actual_s)
        if p == q == 2:
            assert math.isclose(predicted_q,(1+math.sqrt(2))/2,rel_tol=1e-12)
        if p == q and p>=3:
            assert predicted_q < 1
        print(f'{p}x{q}: V={predicted_v:.12g}, S={predicted_s:.12g}, Qratio={predicted_q:.12g}')
    print(f'ONE_DEFECT_ROOT_SURFACE_PASS cases={len(cases)}')

if __name__ == '__main__':
    verify()

# Integer-rational enclosures for the finite parameter boundary cases.
# These do not rely on floating-point comparisons of near-equal powers.
def exact_boundary_certificates():
    from fractions import Fraction as F
    def interval_sqrt(x, scale=10**12):
        t=math.isqrt((x.numerator*scale**2)//x.denominator)
        return (F(t,scale),F(t+1,scale))
    def add(a,b): return (a[0]+b[0],a[1]+b[1])
    def neg(a): return (-a[1],-a[0])
    def sub(a,b): return add(a,neg(b))
    def mul(a,b):
        pp=[x*y for x in a for y in b]
        return(min(pp),max(pp))
    def inv(a):
        assert a[0]>0
        return(F(1,1)/a[1],F(1,1)/a[0])
    def div(a,b):return mul(a,inv(b))
    def times(x,a):return mul((F(x),F(x)),a)
    def power(a,n):
        ret=(F(1),F(1))
        for _ in range(n):ret=mul(ret,a)
        return ret
    def cint(x):return (F(x),F(x))
    cases=[(2,q,1 if q<=5 else -1) for q in range(2,7)] +[(3,3,-1),(3,4,-1)]
    for p,q,sign in cases:
        d=p+q-2
        a=interval_sqrt(F(p-1,p))
        b=interval_sqrt(F(q-1,q))
        c=interval_sqrt(F(2)-F(1,p)-F(1,q))
        A=times(p-1,a);B=times(q-1,b)
        H=add(times(p,A),times(q,B))
        z=div(times(d,sub(add(A,B),c)),H)
        ep=F(1,math.comb(d,p-1))
        base=sub(cint(1),times(ep,z))
        assert base[0]>0
        L=power(base,d)
        R=cint((F(1)-ep)**(d-1))
        diff=sub(L,R)
        assert diff[0]>0 if sign==1 else diff[1]<0,(p,q,diff)
        print(f'RATIONAL_SIGN p={p} q={q} sign={sign} margin=({float(diff[0]):.9g},{float(diff[1]):.9g})')
    print('RATIONAL_BOUNDARY_PASS cases=7')

if __name__=='__main__':
    exact_boundary_certificates()
