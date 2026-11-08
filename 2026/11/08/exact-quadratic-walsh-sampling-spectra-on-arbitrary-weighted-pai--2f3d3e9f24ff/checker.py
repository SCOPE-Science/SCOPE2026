"""Exact finite checks for the two-Hamming-layer degree-two Walsh restriction spectrum.
Run: python central_double_slices_checker.py (requires sympy).
"""
from itertools import combinations
from math import comb
import sympy as sp


def shell_moment(n, k, order):
    return sp.Rational(sum((-1)**j * comb(order,j) * (comb(n-order,k-j) if 0 <= k-j <= n-order else 0)
                           for j in range(order+1)), comb(n,k))


def predicted_components(n,k,l,t):
    a,b=n-2*k,n-2*l
    C=comb(n,2)
    def q(v): return sp.Rational(v*v-n,2)
    def beta(v,w): return 1+sp.Rational(v*w,n)+sp.Rational(q(v)*q(w),C)
    def c1(v): return sp.Rational(n*n-v*v,n*(n-1))
    def c2(v): return sp.Rational((n*n-v*v)*((n-2)**2-v*v),n*(n-1)*(n-2)*(n-3))
    tr0=t*beta(a,a)+(1-t)*beta(b,b)
    det0=t*(1-t)*(beta(a,a)*beta(b,b)-beta(a,b)**2)
    tr1=t*c1(a)*(1+sp.Rational(a*a,n-2))+(1-t)*c1(b)*(1+sp.Rational(b*b,n-2))
    det1=t*(1-t)*c1(a)*c1(b)*sp.Rational((a-b)**2,n-2)
    c2mix=t*c2(a)+(1-t)*c2(b)
    return tr0,det0,tr1,det1,c2mix


def exact_test(n,k,l,t):
    edges=list(combinations(range(n),2))
    chars=[()] + [(i,) for i in range(n)] + edges
    m=[t*shell_moment(n,k,j)+(1-t)*shell_moment(n,l,j) for j in range(5)]
    def distance(a,b):return len(set(a).symmetric_difference(b))
    G=sp.Matrix(len(chars),len(chars),lambda i,j:m[distance(chars[i],chars[j])])
    tr0,det0,tr1,det1,c2=predicted_components(n,k,l,t)
    K=sp.zeros(n,len(edges))
    for u,(i,j) in enumerate(edges):K[i,u]=K[j,u]=1
    assert K.rank()==n
    E=lambda v:sp.Matrix(v)
    base0=E([1]+[0]*n+[0]*len(edges))
    base1=E([0]+[1]*n+[0]*len(edges))
    base2=E([0]+[0]*n+[1]*len(edges))
    def lam(z):return n-2*z
    def q(a):return sp.Rational(a*a-n,2)
    def radial_image(value):
        out=sp.zeros(len(chars),1)
        for z,w in ((k,t),(l,1-t)):
            a=lam(z)
            out += w*value(a)*(base0+sp.Rational(a,n)*base1+q(a)/len(edges)*base2)
        return out
    assert G*base0==radial_image(lambda a:1)
    assert G*base1==radial_image(lambda a:a)
    assert G*base2==radial_image(q)
    c1=lambda a:sp.Rational(n*n-a*a,n*(n-1))
    r0=sum((w*c1(lam(z)) for z,w in ((k,t),(l,1-t))),sp.S.Zero)
    r1=sum((w*c1(lam(z))*lam(z) for z,w in ((k,t),(l,1-t))),sp.S.Zero)
    r2=sum((w*c1(lam(z))*lam(z)**2 for z,w in ((k,t),(l,1-t))),sp.S.Zero)
    for i in range(n-1):
        c=[0]*n;c[i]=1;c[n-1]=-1
        f=E([0]+c+[0]*len(edges))
        v=E([0]+[0]*n+[c[a]+c[b] for a,b in edges])
        assert G*f==r0*f+sp.Rational(r1,n-2)*v
        assert G*v==r1*f+sp.Rational(r2,n-2)*v
    for ker in K.nullspace():
        f=E([0]*(n+1)+list(ker))
        assert G*f==c2*f
    assert det0>0 and det1>0 and c2>0
    return len(chars)

count=0
for n,k,l,t in [(5,2,3,sp.Rational(1,2)), (6,2,3,sp.Rational(1,3)),
                (6,2,4,sp.Rational(2,3)),(7,2,4,sp.Rational(1,2)),
                (7,3,4,sp.Rational(1,2)),
                (8,2,5,sp.Rational(2,5)),(9,2,6,sp.Rational(3,7))]:
    count+=exact_test(n,k,l,t)
    print('exact invariant-block decomposition',n,k,l,t)
for n in [5,7,9,11,13,15,17]:
    k=(n-1)//2; l=k+1
    tr0,det0,tr1,det1,c2=predicted_components(n,k,l,sp.Rational(1,2))
    assert sp.factor(det0)==0 or sp.factor(det0)>0
    assert tr0==sp.Rational(3*n-1,2*n)+sp.Rational(1,n)
    assert sp.factor(det0)==sp.Rational(3*n-1,2*n*n)
    assert tr1==sp.Rational(n+1,n)+sp.Rational(n+1,n*(n-2))
    assert det1==sp.Rational((n+1)**2,n*n*(n-2))
    assert c2==sp.Rational(n*n-1,n*(n-2))
print('TWO_HAMMING_LAYERS_EXACT_CHECKS_PASS',count,'matrix directions and seven central families')
