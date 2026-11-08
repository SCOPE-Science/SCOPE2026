"""Reproduce analytic-model consistency checks for the weak-sluggishness cost law.

Dependencies: Python 3, NumPy and SciPy. Numeric tests are not a replacement
for the analytic asymptotic proof in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln, kve

checks = 0

def require(statement, label):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(label)


def log_two_sided_density(x, alpha, rate=1.0):
    """Logarithm of twice the exact stationary probability density at x>0."""
    p = alpha + 2.0
    t = 2.0 * math.sqrt(rate) / p * x**(p / 2.0)
    log_a = ((2*alpha+3)/(2*p))*math.log(rate) - gammaln((alpha+1)/p) - ((alpha+1)/p)*math.log(p)
    return (math.log(2.0)+log_a+(alpha+.5)*math.log(x)
            +math.log(kve(1.0/p,t))-t)


def integrate_exponential_cost(alpha, lam, rate=1.0):
    """Direct original-density quadrature, suitable when the answer fits floats."""
    f = lambda x: math.exp(max(-740.0, log_two_sided_density(x,alpha,rate) + lam*x))
    return quad(f, 1.e-10, np.inf, epsrel=5.e-9, limit=500)[0] * rate


def critical_cost(alpha, rate=1.0):
    """At the critical lambda, rescale the full exact Bessel density."""
    b = 2.0/(math.sqrt(rate)*alpha*math.log(1.0/alpha))
    lam = math.sqrt(rate)
    def f(u):
        x = b*u
        return math.exp(max(-740., min(100., log_two_sided_density(x,alpha,rate)+lam*x))) * b * rate
    return quad(f,1.e-10,80.0,epsrel=2.e-8,limit=500)[0]


def saddle_ratio(alpha, lam=1.5, rate=1.0):
    """Compare original-density Laplace integral with full saddle equivalent."""
    p = alpha+2.0
    xstar = (lam/math.sqrt(rate))**(2.0/alpha)
    height = alpha*lam*xstar/p
    log_a = ((2*alpha+3)/(2*p))*math.log(rate) - gammaln((alpha+1)/p) - ((alpha+1)/p)*math.log(p)
    log_b = log_a + 0.5*math.log(math.pi*p/math.sqrt(rate))
    log_pred = (math.log(rate)+log_b+(3*alpha/4)*math.log(xstar)
                +0.5*math.log(4*math.pi*xstar/(alpha*lam))+height)
    def f(u):
        x=xstar*u
        log_val=log_two_sided_density(x,alpha,rate)+lam*x-height
        return math.exp(max(-740., min(200., log_val))) * xstar
    v = quad(f,.04,3.0,epsrel=2.e-9,limit=500)[0]
    log_actual=math.log(rate)+height+math.log(v)
    return math.exp(log_actual-log_pred)

# Check the normalization of the *original* two-sided Bessel law.
for alpha in (0.0,0.07,0.3,0.8,1.5):
    for rate in (0.3,1.0,2.7):
        mass=quad(lambda x: math.exp(log_two_sided_density(x,alpha,rate)),
                  1.e-9,np.inf,epsrel=3.e-9,limit=500)[0]
        require(abs(mass-1.0)<3.e-7, f"normalization {alpha} {rate} {mass}")

# At alpha=0, exact integration gives the bilateral exponential moment.
for rate in (0.3,1.0,2.7):
    for factor in (.2,.5,.75):
        lam=factor*math.sqrt(rate)
        actual=integrate_exponential_cost(0.0,lam,rate)
        wanted=rate/(1.0-factor)
        require(abs(actual/wanted-1.0)<3.e-7, "Brownian formula")

# Verify subcritical convergence without assuming its rate.
for lam in (.35,.6):
    target=1.0/(1.0-lam)
    errs=[]
    for alpha in (.12,.04,.012):
        actual=integrate_exponential_cost(alpha,lam)
        errs.append(abs(actual/target-1.0))
        require(math.isfinite(actual) and actual>0, "subcritical existence")
    require(errs[2]<errs[0], "subcritical convergence")

# The critical ratio converges only logarithmically. Numerical checks are
# deliberately qualitative; no finite alpha establishes its exact constant.
critical_ratios=[]
for alpha in (.08,.025,.008,.002, .0004):
    actual=critical_cost(alpha)
    asymptotic=2.0/(alpha*math.log(1.0/alpha))
    ratio=actual/asymptotic
    critical_ratios.append(ratio)
    require(math.isfinite(ratio) and 1.0<ratio<1.65, "critical range")
for left,right in zip(critical_ratios,critical_ratios[1:]):
    require(left>right, "critical convergence direction")

# The full prefactor matters: direct integration (not the tail substitute)
# approaches the predicted saddle equivalent for alpha decreasing.
ratios=[]
for alpha in (.16,.11,.085):
    ratio=saddle_ratio(alpha)
    ratios.append(ratio)
    require(.85<ratio<1.25, "full saddle comparison")
require(abs(ratios[-1]-1)<abs(ratios[0]-1), "full saddle convergence")

# Reconstruct the derivative and height algebra from independent numerical
# evaluations for several physical parameters.
for alpha in (.12,.4,1.1):
    for rate, lam in ((1.,1.3),(.25,.8),(1.7,2.)):
        p=2+alpha
        xstar=(lam/math.sqrt(rate))**(2/alpha)
        f=lambda x:lam*x-2*math.sqrt(rate)/p*x**(p/2)
        derivative=lam-math.sqrt(rate)*xstar**(alpha/2)
        curvature=-(alpha/2)*math.sqrt(rate)*xstar**(alpha/2-1)
        require(abs(derivative)<1.e-11*lam,"saddle derivative")
        require(abs((f(xstar) - alpha*lam*xstar/p)/f(xstar))<1.e-10,"saddle height")
        require(abs(curvature/(-alpha*lam/(2*xstar))-1)<1.e-10,"saddle curvature")

print(f"PASS: {checks} deterministic normalization, asymptotic and saddle checks")
print("Critical ratios:", [round(x,7) for x in critical_ratios])
print("Full supercritical ratios:", [round(x,7) for x in ratios])
