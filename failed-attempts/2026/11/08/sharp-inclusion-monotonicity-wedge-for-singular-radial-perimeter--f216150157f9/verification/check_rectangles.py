"""Numerical cross-checks for weighted-perimeter monotonicity of rectangles.

Run with Python 3 standard library: python verification/check_rectangles.py.
Numerics supplement the analytic proof; they do not prove universal claims.
"""
from __future__ import annotations
import math
import random


def integrate(f, a, b, tol=1e-11):
    fa, fb, fm = f(a), f(b), f((a+b)/2)
    S = (b-a)*(fa + 4*fm + fb)/6
    def recurse(l, r, fl, fr, fm, old, eps, depth):
        m=(l+r)/2
        f1=f((l+m)/2)
        f2=f((m+r)/2)
        L=(m-l)*(fl+4*f1+fm)/6
        R=(r-m)*(fm+4*f2+fr)/6
        if depth == 0 or abs(L+R-old) <= 15*eps:
            return L+R+(L+R-old)/15
        return (recurse(l,m,fl,fm,f1,L,eps/2,depth-1)
              + recurse(m,r,fm,fr,f2,R,eps/2,depth-1))
    return recurse(a,b,fa,fb,fm,S,tol,25)


def G(p,x):
    return (1+x*x)**(p/2)+p*integrate(lambda t:(1+t*t)**(p/2-1),0,x)


def threshold(p):
    assert -1<p<0
    hi=2.
    while G(p,hi)>0:
        hi*=2
    lo=1.
    for _ in range(58):
        mid=(lo+hi)/2
        if G(p,mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def E(p,a,b):
    return 4*(integrate(lambda y:(a*a+y*y)**(p/2),0,b)
             + integrate(lambda x:(b*b+x*x)**(p/2),0,a))


def derivative_a(p,a,b):
    return 4*a**p*G(p,b/a)


def check():
    rng=random.Random(812607)
    checks=0
    ps=[-.95,-.90,-.75,-.50,-.35,-.25]
    roots=[threshold(p) for p in ps]
    assert all(1<r for r in roots)
    assert all(roots[j]<roots[j+1] for j in range(len(roots)-1))
    for p,r in zip(ps,roots):
        assert abs(G(p,r))<2e-9
        assert G(p,1)>0 and G(p, r*.98)>0 and G(p,r*1.02)<0
        checks+=4
        # The aspect threshold is sharp: extending the short side can decrease E.
        a,b=1.15*r,1.0
        eps=1e-5
        assert derivative_a(p,b,a)<0
        assert E(p,a,b+eps)<E(p,a,b)
        checks+=2
        # All comparisons of nested rectangles retained in the balanced cone are strict.
        for _ in range(60):
            a=math.exp(rng.uniform(-1,1))
            b=a*math.exp(rng.uniform(-.65*math.log(r),.65*math.log(r)))
            # For a bounded aspect ratio, a common enlargement stays in the cone.
            f=math.exp(rng.uniform(.0002,.15))
            assert E(p,f*a,f*b)>E(p,a,b)
            checks+=1
    for p in [-.95,-.75,-.5,-.25,0,1,3]:
        for _ in range(70):
            a=math.exp(rng.uniform(-1,1));b=math.exp(rng.uniform(-1,1))
            h=1e-5*min(a,b)
            numerical=(E(p,a+h,b)-E(p,a-h,b))/(2*h)
            theoretical=derivative_a(p,a,b)
            assert abs(numerical-theoretical)<3e-6*max(1,abs(theoretical)),(p,a,b,numerical,theoretical)
            checks+=1
    for p in [-1,-.99,-.5,0,1]:
        a,b=1.,1.
        for s in [.5,1.3,2.7]:
            assert math.isclose(E(p,s*a,s*b),s**(p+1)*E(p,a,b),rel_tol=3e-10)
            checks+=1
    assert math.isclose(G(-1,2.),-1/math.sqrt(5),rel_tol=1e-10)
    checks+=1
    print('RECTANGLE_WEIGHTED_PERIMETER_OK',checks)
    for p,r in zip(ps,roots):
        print(f'p={p:.2f} critical_aspect={r:.9f}')

if __name__ == '__main__':
    check()
