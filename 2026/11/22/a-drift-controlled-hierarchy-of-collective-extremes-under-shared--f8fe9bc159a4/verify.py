"""Reproducible numeric checks for common-catastrophe geometric Brownian extremes.

Requires scipy and Python >=3.9. Tests independent renewal integrals,
stationary marginal tails and high-threshold asymptotics. Theorem is analytic.
"""
import math
from scipy.integrate import quad
from scipy.special import log_ndtr


def constants(a, sigma, r, n):
    assert sigma > 0 and r > 0 and n >= 1
    v = sigma*sigma
    d = math.sqrt(a*a + 2*r*v)
    s = math.sqrt(a*a + 2*r*v/n)
    k = (d-a)/v
    kn = n*(s-a)/v
    cn = (r*sigma**(n+1) * s**((n-3)/2) / (
        (2*math.pi)**((n-1)/2) * math.sqrt(n) * (s-a)**n))
    return k,kn,cn


def scaled_renewal(y,a,sigma,r,n):
    # Independent numerical quadrature after t=y*z.
    k,kn,cn=constants(a,sigma,r,n)
    center=1/math.sqrt(a*a + 2*r*sigma*sigma/n)
    def fun(z):
        if z <= 0: return 0.
        h=(a*z-1)*math.sqrt(y)/(sigma*math.sqrt(z))
        log_val=math.log(r*y)-r*y*z+kn*y+n*log_ndtr(h)
        return 0. if log_val < -742 else math.exp(log_val)
    cut=sorted({0.,center/4,center/2,.8*center,center,1.2*center,2*center,4*center,max(10*center,10/r)})
    val=sum(quad(fun,cut[i],cut[i+1],epsabs=1e-10,epsrel=1e-8,limit=200)[0] for i in range(len(cut)-1))
    val+=quad(fun,cut[-1],math.inf,epsabs=1e-10,epsrel=1e-8,limit=200)[0]
    return val


def main():
    checks=0
    for a,sigma,r in [(-2.,1.,1.),(-.5,1.3,.8),(0.,1.,1.),(.5,.75,3.),(2.,1.,1.)]:
        k,_,c1=constants(a,sigma,r,1)
        delta=math.sqrt(a*a+2*r*sigma*sigma)
        assert math.isclose(c1,(delta+a)/(2*delta),rel_tol=3e-13);checks+=1
        for y in [3.,15.,35.]:
            assert math.isclose(scaled_renewal(y,a,sigma,r,1),c1,rel_tol=2e-7);checks+=1
        old_alpha=0
        for n in [2,3,4,6]:
            k1,kn,cn=constants(a,sigma,r,n)
            s=math.sqrt(a*a+2*r*sigma*sigma/n)
            alpha=kn/k1
            assert 1<alpha<n,(a,n,alpha);checks+=1
            assert alpha>old_alpha;checks+=1
            old_alpha=alpha
            assert math.isclose(alpha,(delta+a)/(s+a),rel_tol=3e-13);checks+=1
            # Saddle normalization in joint tails (comparison with unrelated numerical integration)
            vals=[scaled_renewal(y,a,sigma,r,n)/(cn*y**((1-n)/2)) for y in [30.,70.,140.]]
            assert abs(vals[-1]-1)<abs(vals[0]-1),(a,n,vals);checks+=1
            assert 0<vals[-1]<1.15,(a,n,vals);checks+=1
        # Strict drift monotonicity of joint exponent after one-dimensional standardization
    for n in [2,3,4,6]:
        grid=[constants(a,1.,1.,n)[1]/constants(a,1.,1.,n)[0] for a in [-10.,-3.,-1.,0.,1.,3.,10.]]
        assert all(u>v for u,v in zip(grid,grid[1:])),(n,grid);checks+=1
        assert math.isclose(constants(0.,1.,1.,n)[1]/constants(0.,1.,1.,n)[0],math.sqrt(n),rel_tol=3e-14);checks+=1
    print(f'PASS: {checks} assertions including renewal integral, saddle asymptotics, and strict exponent hierarchy')
if __name__=='__main__':main()
