"""Reproducible finite checks for a two-level Poisson-probing tail theorem.

Uses only the Python standard library. Finite checks complement, but do not
replace, the analytical proof in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, isclose


def solve(mat, rhs):
    """Gaussian elimination over exact rational numbers."""
    n = len(rhs)
    m = [list(map(F, mat[i])) + [F(rhs[i])] for i in range(n)]
    for j in range(n):
        k = next(i for i in range(j, n) if m[i][j])
        m[j], m[k] = m[k], m[j]
        d = m[j][j]
        m[j] = [v / d for v in m[j]]
        for i in range(n):
            if i != j:
                a = m[i][j]
                m[i] = [m[i][h] - a*m[j][h] for h in range(n+1)]
    return [m[i][-1] for i in range(n)]


def resolvent(r, w, sin_theta, cos_theta, z, initial_return=False):
    """Independent no-click density-matrix master-equation resolvent.

    Coordinates (rho00,rho11,Re rho01,Im rho01). Detector is |1>.
    A transition experiment starts in |0>; a return experiment starts in |1>.
    """
    h = w * sin_theta / 2
    delta = w * cos_theta
    G = [[F(0),F(0),F(0),-2*h],
         [F(0),-r,F(0),2*h],
         [F(0),F(0),-r,delta],
         [h,-h,-delta,-r]]
    mat = [[(z if i==j else F(0))-G[i][j] for j in range(4)] for i in range(4)]
    rhs = [F(0),F(1) if initial_return else F(0),F(0),F(0)]
    if not initial_return:
        rhs[0] = F(1)
    return r * solve(mat, rhs)[1]


def transition_transform(r, w, p, z):
    den = 2*z**3+4*r*z**2+2*(r*r+w*w)*z+p*r*w*w
    return p*r*w*w/den


def return_transform(r,w,p,z):
    L=r+z
    a=p*r*w*w/(2*L*(L*L+w*w))
    return r/L-a+a*transition_transform(r,w,p,z)


def g(x,p,y):
    return 2*y*((x-y)**2+1)-p*x


def root(x,p):
    lo, hi = 0.0, x/2.0
    assert g(x,p,lo)<0<g(x,p,hi)
    for _ in range(110):
        mid=(lo+hi)/2
        if g(x,p,mid)>0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def optimum(p):
    return ((4-p)/(2*sqrt(2*(2-p))),p/(2*sqrt(2*(2-p))))


def check():
    count=0
    triples=[(F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(8,17),F(15,17)),(F(1),F(0))]
    for sint,cost in triples:
        p=sint*sint
        for r in [F(1,3),F(1),F(7,2),F(13)]:
            for w in [F(1,2),F(2),F(5)]:
                for z in [F(1,5),F(3,2),F(9)]:
                    ft=transition_transform(r,w,p,z)
                    fr=return_transform(r,w,p,z)
                    assert resolvent(r,w,sint,cost,z)==ft
                    assert resolvent(r,w,sint,cost,z,True)==fr
                    count += 2
    # Exact algebraic identity: the optimum satisfies both the cubic pole
    # equation and the envelope stationarity equation to numerical precision.
    for p in [0.001,0.01,0.05,0.2,0.37,0.65,0.9,1.0]:
        x,y=optimum(p)
        assert abs(g(x,p,y)) < 2e-14
        assert abs(4*y*(x-y)-p)<2e-14
        assert abs(x*x-y*y-1)<2e-14
        assert x>=1
        assert x<=3/(2*sqrt(2))+1e-14
        count +=5
        for ratio in [0.1,0.5,0.8,0.98,1.0,1.02,1.2,1.8,5.0,20.0]:
            y0=root(x*ratio,p)
            assert y0 <= y + 2e-14
            count+=1
    # Discriminant analytic bound is checked on a broad parameter mesh.
    for p in [0.01,0.25,0.5,0.75,1.0]:
        for x in [0.01,0.1,0.5,1,2,5,10,100]:
            disc=-27*p*p*x*x+8*p*x**4+72*p*x*x-16*x**4-32*x*x-16
            assert disc<0
            count+=1
    print('PASS: '+str(count)+' independent exact-rational resolvent and numerical sharpness checks')
    print('resonant optimum r/omega:',format(optimum(1)[0],'.15g'))
    print('resonant optimal tail exponent / omega:',format(optimum(1)[1],'.15g'))

if __name__=='__main__':
    check()
