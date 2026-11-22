"""Independent numerical quadrature checks for Cauchy-wavelet ambiguity laws.

Requires scipy and numpy. This script tests finite parameter instances only;
the all-parameter assertions follow from the beta/gamma integral proof.
"""
import math
from scipy.integrate import quad
from scipy.special import beta, gamma


def c(a, lam):
    return 2**(4*a+1)*a*lam**(4*a+1)/math.pi


def m_formula(a, lam, q):
    return (2*lam)**q*gamma((q+1)/2)*gamma(2*a+1-q)/(math.sqrt(math.pi)*gamma(2*a+1-q/2))


def m_independent(a, lam, q):
    # Independent integration over t after evaluating only the y integral.
    nu=2*a+1
    by=beta((q+1)/2, nu-(q+1)/2)
    val,err=quad(lambda t:c(a,lam)*t**(2*a-1)*(lam*(1+t))**(q+1-2*nu)*by,
                 0,math.inf,epsabs=1e-10,epsrel=1e-10)
    return val


def p_scaled(a,lam,B):
    # B^(2a+2) times the y-marginal at y=B, with t=Bu/lam.
    delta=lam/B
    integ,err=quad(lambda u:u**(2*a-1)/(1+(u+delta)**2)**(2*a+1),
                   0,math.inf,epsabs=5e-11,epsrel=5e-11)
    return c(a,lam)*lam**(-2*a)*integ


def tail_const(a,lam):
    return 2**(2*a)*a*gamma(a)*lam**(2*a+1)/(math.sqrt(math.pi)*gamma(a+.5))


def conditional_cdf(a,lam,B,x):
    delta=lam/B
    g=lambda u:u**(2*a-1)/(1+(u+delta)**2)**(2*a+1)
    return quad(g,0,x,epsabs=1e-11)[0]/quad(g,0,math.inf,epsabs=1e-11)[0]


def limit_cdf(a,x):
    return quad(lambda u:2*u**(2*a-1)/(beta(a,a+1)*(1+u*u)**(2*a+1)),
                0,x,epsabs=1e-11)[0]


def check(x,y,rtol=2e-8):
    assert math.isfinite(x) and math.isfinite(y)
    assert abs(x-y)<rtol*max(1,abs(x),abs(y)),(x,y)


def run():
    tests=0
    for a,lam,q in [(.3,1.1,0),(.3,1.1,.5),(.55,.8,1),(.8,1.3,1.5),
                    (1.0,1.0,1),(1.0,1.0,2),(1.5,2.0,2),(2.0,.7,3),
                    (2.5,1.7,4)]:
        check(m_independent(a,lam,q),m_formula(a,lam,q))
        tests+=1
    for a,lam in [(.3,.7),(.8,1.1),(1,1),(2,2)]:
        # Exact normalization via beta-integrals independently of probability factorization.
        normal=(c(a,lam)*beta(.5,2*a+.5)*lam**(-4*a-1)*beta(2*a,2*a+1))
        check(normal,1)
        tests+=1
        for B in [1000,10000]:
            ratio=p_scaled(a,lam,B)/tail_const(a,lam)
            assert .985<ratio<1.001, (a,lam,B,ratio)
            tests+=1
        for x in [0.5,1,2]:
            check(conditional_cdf(a,lam,50000,x),limit_cdf(a,x),rtol=2e-4)
            tests+=1
    # Closed second moment for all a>1/2.
    for a in [.51, .75, 1, 1.5, 2, 10]:
        check(m_formula(a,1.3,2),2*1.3**2/(2*a-1))
        tests+=1
    print(f"PASS: {tests} finite quadrature, tail and limit diagnostics")

if __name__=='__main__':
    run()
