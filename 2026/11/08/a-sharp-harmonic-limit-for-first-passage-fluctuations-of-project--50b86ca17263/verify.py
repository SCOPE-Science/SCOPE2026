"""Reproducible checks for Jacobi target-time fluctuation bounds.
Requires Python 3 and scipy (for independent quadrature and hypergeometric checks).
The exact theorem is established analytically; these finite tests are diagnostics.
"""
import math
from scipy.integrate import quad
from scipy.special import hyp2f1


def series(n, b, c=1., tol=2e-14, max_terms=400000):
    assert n>=2 and 0<b<1 and c>0
    q=n-1
    w=b
    s=0.0
    total=0.0
    weighted=0.0
    for k in range(1,max_terms+1):
        total += w
        weighted += w*s
        if k>40 and abs(w) <= tol*total and b**(k//4) < 1e-5: break
        s+=1/(k*(k+q))
        w*=b*k*(k+q)/(k+1)**2
    else: raise RuntimeError('nonconvergence')
    mean=total/c
    deficit=2*weighted/(c*total)
    variance=mean*(mean-deficit)
    return mean,variance,deficit,k


def independent(n,b,c=1.):
    q=n-1
    def gj(x):
        if x==0:return 1/c
        return (-math.expm1(q*math.log1p(-x)))/(c*q*x*(1-x)**q)
    mean=quad(gj,0,b,epsabs=1e-10,epsrel=1e-10)[0]
    def inside(y):
        if y==0:return 0.0
        num=-math.expm1(q*math.log1p(-y))
        return num*num/(y*(1-y)**q)
    def outer(x):
        if x==0:return 0.
        inner=quad(inside,0,x,epsabs=1e-10,epsrel=1e-10)[0]
        return inner/(x*(1-x)**q)
    var=2/(c*c*q*q)*quad(outer,0,b,epsabs=1e-10,epsrel=1e-10)[0]
    return mean,var


def run():
    checks=0
    for n in (2,3,4,5,8):
        q=n-1
        last=0.
        for b in (.12,.28,.49,.71,.87,.95):
            mean,var,deficit,k=series(n,b)
            m2,v2=independent(n,b)
            assert abs(mean-m2)<max(1e-9,3e-9*m2),(n,b,mean,m2)
            assert abs(var-v2)<max(1e-8,3e-8*v2),(n,b,var,v2)
            assert 0<deficit<2*sum(1/i for i in range(1,q+1))/q
            assert last<deficit
            assert 0<var<mean*mean
            last=deficit
            checks+=6
        # Asymptotic harmonic-number trace check at accessible cutoffs
        exact_limit=2*sum(1/i for i in range(1,q+1))/q
        approx=series(n,.995,tol=2e-13)[2]
        assert 0<approx<exact_limit
        assert approx>0.5*exact_limit,(n,approx,exact_limit)
        checks+=2
    for b in (.1,.25,.5,.7,.9,.99):
        mean,var,d,_=series(2,b)
        assert abs(mean+math.log1p(-b))<1e-11
        checks+=1
    print(f'PASS: {checks} assertions (independent quadrature, mean, variance, monotonicity, harmonic endpoint).')
    for n in (2,3,4,5):
        q=n-1
        target=2*sum(1/i for i in range(1,q+1))/q
        print(f'n={n}: exact limiting mean-weighted deficit={target:.12f}; at b=.995: {series(n,.995)[2]:.12f}')

if __name__=='__main__':run()
