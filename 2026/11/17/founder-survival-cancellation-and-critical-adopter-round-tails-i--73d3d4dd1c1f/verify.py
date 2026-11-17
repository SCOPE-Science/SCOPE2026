"""Numerical checks for the early-adopter offspring law of a round-based contagion process.

Standalone standard-library checker; checks are finite corroboration, not proof.
"""
import math
from statistics import NormalDist


def quad(fun, a, b, steps=6000):
    width = (b-a)/steps
    return width/3*(fun(a)+fun(b)+4*sum(fun(a+i*width) for i in range(1, steps,2))+2*sum(fun(a+i*width) for i in range(2, steps,2)))


def pgf(s, lam, c, tau):
    z=lam+c*(1-s)
    return lam*(-math.expm1(-z*tau))/z+s*math.exp(-z*tau)


def pgf_integral(s, lam, c, tau):
    return quad(lambda t: lam*math.exp(-(lam+c*(1-s))*t),0,tau)+s*math.exp(-(lam+c*(1-s))*tau)


def finite_pgf(s, lam, nu, rho, p, tau, N):
    # Exact one-round finite-N PGF from one adopter, all other persons naive.
    m=nu*tau
    def contrib(t, survivor):
        exposure=rho*t/N
        q=exposure/(exposure+m)*(-math.expm1(-exposure-m))
        return (1-p*q*(1-s))**(N-1)*(s if survivor else 1)
    return quad(lambda t:lam*math.exp(-lam*t)*contrib(t,False),0,tau)+math.exp(-lam*tau)*contrib(tau,True)


def critical_tail_coefficient(lam,tau):
    kappa=-math.expm1(-lam*tau)
    et2=2*(1-math.exp(-lam*tau)*(1+lam*tau))/(lam*lam)
    v=lam*lam*et2+2*lam*tau*math.exp(-lam*tau)
    assert abs(v-2*kappa)<2e-14
    return 1/math.sqrt(math.pi*kappa)


def run():
    count=0
    for nu in (0.02,0.25,1.4):
        lam=1+nu
        for tau in (0.15,0.8,2.5):
            f=-math.expm1(-nu*tau)/(nu*tau)
            for ratio in (0.45,0.95,1.0,1.2,2.3):
                c=lam*ratio
                for s in (0,0.3,0.8,1):
                    assert abs(pgf(s,lam,c,tau)-pgf_integral(s,lam,c,tau))<1e-10
                    count+=1
                kappa=-math.expm1(-lam*tau)
                mean=1+kappa*(ratio-1)
                h=1e-5
                deriv=(pgf(1-2*h,lam,c,tau)-8*pgf(1-h,lam,c,tau)+8*pgf(1+h,lam,c,tau)-pgf(1+2*h,lam,c,tau))/(12*h)
                assert abs(deriv-mean)<1e-8,(deriv,mean)
                count+=1
                if ratio>1:
                    assert abs(pgf(1/ratio,lam,c,tau)-1/ratio)<2e-14
                    count+=1
                if ratio==1:
                    assert critical_tail_coefficient(lam,tau)>0
                    count+=1
                if ratio==1.2 and nu<1:
                    rho=c/(0.35*f)
                    ref=pgf(0.47,lam,c,tau)
                    for N in (500,2000,8000):
                        diff=abs(finite_pgf(0.47,lam,nu,rho,0.35,tau,N)-ref)
                        assert diff < 6.0/N,(diff,N)
                        count+=1
    print('VERIFY_OK numerical_pgf_and_moment_checks='+str(count)+' finite_population_one_round_limits=18 critical_variance_identities=9')

if __name__=='__main__':
    run()
