"""Standalone checks for two-moment Brownian-bridge quadrature design.
Uses only the Python 3 standard library. Numerical checks supplement the analytic proof.
"""
from fractions import Fraction as F
from math import sqrt, isclose
from random import Random

def prior_cov(t):
    return t*(1-t)

def c0(t):
    return t*(1-t)/2

def c1(t):
    return t*(1-t)*(2*t-1)/6

def gain(t,w,noise):
    u=prior_cov(t)
    if u==0 and noise==0: return 0
    return (c0(t)**2+w*c1(t)**2)/(u+noise)

def ustar(w,noise):
    a=9+w-12*w*noise
    return min(.25,(a+sqrt(a*a+64*w*(9+w)*noise))/(16*w))

def opt(w,noise):
    u=ustar(w,noise)
    d=sqrt(max(0,.25-u))
    return (.5-d,.5+d)

def check():
    n=0
    # Independently evaluate weighted bridge Green-kernel moments by exact polynomials.
    # Integral 0^t (s-st)g(s) ds + integral t^1 (t-st)g(s) ds.
    for j in range(1,100):
        t=F(j,100)
        # g(s)=1, g(s)=2s-1, analytical antiderivatives integrated independently.
        a=(1-t)*t*t/F(2) + t*(F(1)-t)**2/F(2)
        b=(1-t)*(F(2)*t**3/F(3)-t*t/F(2))
        b += t*(-F(2,3)*(1-t**3)+F(3,2)*(1-t**2)-(1-t))
        assert a==c0(t) and b==c1(t),(t,b,c1(t))
        n+=2
    # Analytic exact derivative numerator P and central transition; verify sign crossovers.
    for w in (F(1),F(9),F(10),F(12),F(15),F(18),F(30)):
      for eta in (F(0),F(1,100),F(1,8),F(1,2),F(1),F(10)):
        P=lambda u: F(2)*eta*(9+w)+(9+w-12*eta*w)*u-8*w*u*u
        assert 4*P(F(1,4)) == 9-w+4*eta*(18-w)
        n+=1
    assert ustar(15,0)==.2
    x,y=opt(15,0)
    assert isclose(x,(1-1/sqrt(5))/2,abs_tol=1e-14)
    assert isclose(y,(1+1/sqrt(5))/2,abs_tol=1e-14)
    assert opt(15,.5)==(.5,.5)
    n+=4
    # Global comparisons independently brute-force objective across randomized parameters.
    rng=Random(35065)
    for k in range(700):
        w=10**rng.uniform(-1,2.3)
        eta=10**rng.uniform(-5,1) if k%7 else 0.
        x,y=opt(w,eta)
        value=gain(x,w,eta)
        assert isclose(value,gain(y,w,eta),rel_tol=1e-11,abs_tol=1e-13)
        for m in range(121):
            t=m/120
            assert gain(t,w,eta)<=value+3e-13,(w,eta,x,y,t,value,gain(t,w,eta))
            n+=1
    # Sharp local splitting at equal-variance weighting near critical noise.
    for delta in (1e-2,1e-3,1e-4,1e-5):
        x,y=opt(15,.5-delta)
        assert abs((.5-x)/sqrt(delta)-1/sqrt(42))<.2*sqrt(delta)
        n+=1
    print(f'PASS: {n} exact/algebraic/numerical comparisons (finite evidence, not a proof)')
if __name__=='__main__':check()
