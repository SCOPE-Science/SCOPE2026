"""Independent numerical tests of the box-transit cadence theorem.
Run: python CHECKER.py.  Requires scipy and numpy.
These finite tests supplement, rather than replace, the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar, brentq


def objective(x, h, r):
    if x <= 0 or h <= 0 or r < 0:
        raise ValueError('x,h>0 and r>=0 are required')
    f = 1-x/3 if x <= 1 else 1/x-1/(3*x*x)
    return x*f/((x+h)*(1+r*x))


def optimum(h,r):
    p_at_one=h*(1-r)-1-3*r
    if p_at_one<=0:
        a=1+3*r+h*r
        return 3*h/(h+math.sqrt(h*h+3*h*a))  # derived? x=(-h+sqrt(...))/a =3h/(h+sqrt(...)); yes
    def cubic(x):
        return h+2*x-3*x*x+r*(2*h*x-3*h*x*x+3*x*x-6*x**3)
    hi=2.
    while cubic(hi)>0:
        hi*=2
    return brentq(cubic,1.,hi,xtol=1e-13)


def overlap(t,x):
    return max(0.,min(1.,t+x)-max(0.,t))/x


def phase_integral(x):
    pts=sorted(set([-x,0.,1.-x,1.]))
    return sum(quad(lambda t: overlap(t,x)**2,lo,hi,epsabs=1e-11)[0]
               for lo,hi in zip(pts,pts[1:]))


def run():
    n=0
    for x in np.geomspace(0.025,50,200):
        f=phase_integral(float(x))
        pred=1-x/3 if x<=1 else 1/x-1/(3*x*x)
        assert abs(f-pred)<3e-9*(1+abs(pred)),(x,f,pred)
        n+=1
    rng=np.random.default_rng(2026)
    for i in range(2000):
        h=float(10**rng.uniform(-3,3))
        r=0. if i%13==0 else float(10**rng.uniform(-3,3))
        x=optimum(h,r)
        assert x>0
        lower=min(x*0.2,1e-3)
        upper=max(100.,5*x,3*math.sqrt(h))
        numerical=minimize_scalar(lambda z: -objective(z,h,r),bounds=(lower,upper),method='bounded',options={'xatol':1e-11})
        assert numerical.success
        assert abs(x-numerical.x)<1e-4*(1+x),(h,r,x,numerical.x)
        samples=np.geomspace(max(x/10,1e-6),10*x,100)
        assert objective(x,h,r)>=max(objective(float(z),h,r) for z in samples)-2e-13
        threshold=(1+3*r)/(1-r) if r<1 else math.inf
        assert (x>1)==(h>threshold) or abs(x-1)<1e-9
        n+=1
    for r in [0.,0.03,0.25,0.8,1.,2.,10.]:
        for h in [0.01,0.3,1.,5.,100.]:
            eps=1e-4
            assert optimum(h*(1+eps),r)>optimum(h,r)
            assert optimum(h,r+eps)>0 and optimum(h,r+eps)<optimum(h,r)
            n+=2
    for r in [0.05,0.2,0.8,1.,2.,5.]:
        h=1e8
        lim=(1+math.sqrt(1+3/r))/3 if r<1 else (math.sqrt(1+3*r)-1)/r
        assert abs(optimum(h,r)-lim)<1e-4,(h,r,lim,optimum(h,r))
        n+=1
    for h in [1.,10.,10000.]:
        assert abs(optimum(h,0)-(1+math.sqrt(1+3*h))/3) < 1e-12 if h>1 else abs(optimum(h,0)-1)<1e-12
        n+=1
    # Symbolically reconstruct both derivative-numerator polynomials and their join.
    import sympy as sp
    X,H,R=sp.symbols('X H R',positive=True)
    D=(X+H)*(1+R*X)
    lo=X*(1-X/sp.Integer(3))/D
    hi=(1-1/(3*X))/D
    p_lo=3*H-2*H*X-(1+3*R+H*R)*X**2
    p_hi=H+2*X-3*X**2+R*(2*H*X-3*H*X**2+3*X**2-6*X**3)
    assert sp.simplify(sp.diff(lo,X)-p_lo/(3*D**2))==0
    assert sp.simplify(sp.diff(hi,X)-p_hi/(3*X**2*D**2))==0
    assert sp.simplify(lo.subs(X,1)-hi.subs(X,1))==0
    assert sp.simplify(sp.diff(lo,X).subs(X,1)-sp.diff(hi,X).subs(X,1))==0
    n+=4
    print(f'PASS {n} independent integral, calculus, optimization, monotonicity and limit checks')
if __name__=='__main__':run()
