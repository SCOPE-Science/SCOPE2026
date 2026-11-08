"""Numerical cross-checks for the stationary Pareto-reset tight-binding tail theorem.

All numerical checks supplement the analytic renewal/Bessel-integral proof.
Requires scipy and numpy. Run: python verify_stationary_tails.py
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import jv, gammaln

checks = 0

def require(condition, what):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(what)


def age(t, alpha, tau):
    return (alpha - 1) / (alpha * tau) if t < tau else (alpha-1)/alpha *tau**(alpha-1)*t**(-alpha)


def exact_mellin(n, alpha, gamma):
    """Integral of t^(-alpha)*J_n(gamma*t)^2 over (0, infinity)."""
    assert n + (1-alpha)/2 > 0
    logv = ((alpha-1)*math.log(gamma)+math.lgamma(alpha)-alpha*math.log(2)
            -2*math.lgamma((alpha+1)/2)
            +math.lgamma(n+(1-alpha)/2)-math.lgamma(n+(alpha+1)/2))
    return math.exp(logv)


def p(n, alpha, tau, gamma, sites, weights):
    """Exact Mellin integral with finite-interval correction (no finite-tail truncation)."""
    c = (alpha-1)*tau**(alpha-1)/alpha
    h0 = (alpha-1)/(alpha*tau)
    ans = 0
    for j,w in zip(sites, weights):
        order = abs(n-j)
        if order+(1-alpha)/2 <= 0:
            raise ValueError('n must be sufficiently large for full Mellin integral')
        sub = quad(lambda t: t**(-alpha)*jv(order,gamma*t)**2,0,tau,
                   epsabs=1e-12,epsrel=1e-10)[0]
        head = quad(lambda t: jv(order,gamma*t)**2,0,tau,
                    epsabs=1e-12,epsrel=1e-10)[0]
        ans += w*(c*(exact_mellin(order,alpha,gamma)-sub)+h0*head)
    return ans


def constant(alpha,tau,gamma):
    return ((alpha-1)/alpha*(gamma*tau)**(alpha-1)*
            math.exp(math.lgamma(alpha)-alpha*math.log(2)
                     -2*math.lgamma((alpha+1)/2)))


def test():
    sites=(-2,3); weights=(.38,.62); b=sum(j*w for j,w in zip(sites,weights))
    require(abs(b-1.1)<1e-12,'reset mean')
    for alpha in (1.4,2.3,3.,4.5):
        tau=.8; gamma=1.3; c=constant(alpha,tau,gamma)
        norm=quad(lambda t: age(t,alpha,tau),0,tau)[0]+quad(lambda t: age(t,alpha,tau),tau,np.inf)[0]
        require(abs(norm-1)<1e-10,'age normalization')
        for order in (4,8,14):
            if order+(1-alpha)/2 <= 0: continue
            # independent quadrature to a long finite cutoff; tail bounded by O(T^-alpha)
            for cutoff in (400.,1000.):
                v=quad(lambda t: t**(-alpha)*jv(order,gamma*t)**2,0,cutoff,
                       epsabs=1e-11,limit=2000)[0]
                truth=exact_mellin(order,alpha,gamma)
                require(abs(v-truth)<2e-12+6*cutoff**(-alpha)/(math.pi*gamma*alpha),
                        'Mellin-vs-quadrature alpha={} n={}'.format(alpha,order))
        errors=[]
        for n in (35,70,140):
            plus=p(n,alpha,tau,gamma,sites,weights)
            minus=p(-n,alpha,tau,gamma,sites,weights)
            lead=c*n**(-alpha)
            require(plus>0 and minus>0, 'positive occupation')
            require(abs(plus/lead-1-alpha*b/n)<200/n**2,'positive tail second order')
            require(abs(minus/lead-1+alpha*b/n)<200/n**2,'negative tail second order')
            discrepancy=abs((plus-minus)/(plus+minus)-alpha*b/n)
            errors.append(discrepancy)
            require(discrepancy<200/n**2,'relative asymmetry')
        require(errors[2] < errors[0] / 3, 'asymmetry converges')
        print('alpha=',alpha,'K=',format(c,'.12g'),'asym_err=',errors)
    # The stationary second moment requires the third inter-reset moment.
    for alpha in (3.5,4.5,8.):
        tau=.8
        target=(alpha-1)*tau*tau/(3*(alpha-3))
        integral=quad(lambda t:t*t*age(t,alpha,tau),0,tau)[0]+quad(
            lambda t:t*t*age(t,alpha,tau),tau,np.inf,epsabs=1e-10)[0]
        require(abs(integral-target)<1e-9,'age second moment exact identity')
    # The marginal case alpha=3 has the sharp truncated logarithmic coefficient.
    alpha=3.;tau=.8
    for tmax in (100.,1000.,10000.):
        val=quad(lambda t:t*t*age(t,alpha,tau),0,tau)[0]+quad(
            lambda t:t*t*age(t,alpha,tau),tau,tmax)[0]
        limit=(2./3.)*tau*tau*math.log(tmax/tau)
        require(abs(val-limit-(2./9.)*tau*tau)<1e-8,
                'critical truncated age-square logarithm')
    # Exact spatial second moment for a free tight-binding quantum walk.
    for t in (0.2,1.,3.5):
        gam=1.3
        nmax=80
        moments=sum(n*n*jv(n,gam*t)**2 for n in range(-nmax,nmax+1))
        require(abs(moments-.5*(gam*t)**2)<1e-10,'ballistic Bessel identity')
    print('PASS:',checks,'numerical assertions; non-numerical renewal and asymptotic steps are in RESULT.md')

if __name__=='__main__': test()
