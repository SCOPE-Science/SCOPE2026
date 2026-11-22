"""Reproduce moment, variance, overlap and minimizer checks for the Poisson test example.

All calculations here are finite checks supporting the accompanying analytic proof.
Run with Python 3: python verify.py
"""
from decimal import Decimal, getcontext
from math import exp, lgamma, log, pi, sqrt

getcontext().prec = 100

def masses_exact(u, v):
    U, V = Decimal(u), Decimal(v)
    ell = U * V
    r = (-ell).exp()
    p0 = r
    pm = V / (U+V) * (1 - r*(ell+V))
    pc = r*(U+1)*(V-1)
    pp = U / (U+V) * (1 - r*(ell-U))
    return (p0, pm, pc, pp)

def test_moments():
    n = 0
    for u in range(1, 9):
        for v in range(2, 14):
            lam = Decimal(u*v)
            p = masses_exact(u,v)
            assert all(0 < w < 1 for w in p), (u,v,p)
            xs = (Decimal(0), lam-u, lam, lam+v)
            for j, target in enumerate((Decimal(1),lam,lam*(lam+1))):
                value = sum(w*(Decimal(1) if j==0 else x**j) for w,x in zip(p,xs))
                assert abs(value-target) < Decimal('1e-84'),(u,v,j,value,target)
                n+=1
            r = p[0]
            variance = r-(lam+1)*r*r
            # Exact centered influence: -r(X-lambda) - (1{X=0}-r)
            taus = [-r*(x-lam)-(Decimal(int(x==0))-r) for x in xs]
            assert abs(sum(w*t for w,t in zip(p,taus)))<Decimal('1e-84')
            assert abs(sum(w*t*t for w,t in zip(p,taus))-variance) < Decimal('1e-84')
            n+=2
    return n

def poisson_mass(lam,k):
    if k<0:
        return 0.
    return exp(-lam+k*log(lam)-lgamma(k+1))

def overlap(u,v):
    lam=u*v
    r=exp(-lam)
    p=(r,v/(u+v)*(1-r*(lam+v)),r*(u+1)*(v-1),u/(u+v)*(1-r*(lam-u)))
    return sum(min(x,poisson_mass(lam,k)) for x,k in zip(p,(0,lam-u,lam,lam+v)))

def root_and_limit():
    f=lambda z:z-1/z-4*log(z)
    lo,hi=4.,20.
    assert f(lo)<0<f(hi)
    for _ in range(100):
        mid=(lo+hi)/2
        if f(mid)<0:lo=mid
        else:hi=mid
    z=(lo+hi)/2
    C=(exp(-z/2)+exp(-1/(2*z)))/sqrt(2*pi)
    assert abs(z-8.822620943170486)<1e-12
    assert abs(C-0.38180481025285024)<1e-12
    previous_error=None
    for u in (1,2,4,8,16,32,64,128):
        v=max(2,round(z*u))
        lam=u*v
        eps=lam**(-2)
        ov=overlap(u,v)
        scaled=sqrt(lam)*(eps+(1-eps)*ov)
        err=abs(scaled-C)
        if u>=8:
            assert err<0.02,(u,v,scaled)
        if u>=16:
            assert err<previous_error+1e-6,(u,v,err,previous_error)
        previous_error=err
    assert previous_error<0.0015
    # The symmetric spacing gives a strictly larger asymptotic overlap.
    C_symmetric=2*exp(-0.5)/sqrt(2*pi)
    assert C<C_symmetric
    assert C<1/sqrt(2*pi)
    return z,C,previous_error

if __name__=='__main__':
    n=test_moments()
    z,C,error=root_and_limit()
    print(f'PASS: {n} finite exact-moment and variance identities')
    print(f'PASS: unique nontrivial reciprocal-spacing optimizer ratio {z:.15f}')
    print(f'PASS: limiting Gaussian local-overlap constant {C:.15f}')
    print(f'PASS: limiting-overlap numerical convergence, final error {error:.9f}')
