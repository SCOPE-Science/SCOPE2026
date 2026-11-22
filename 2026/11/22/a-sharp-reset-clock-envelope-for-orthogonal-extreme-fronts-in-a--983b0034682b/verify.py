"""Reproduce finite-size orthogonal-maximum and renewal-envelope checks.
Requires Python 3, NumPy, and SciPy. Run: python verify.py
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtri_exp, roots_laguerre
from scipy.stats import norm

checks = 0

def check(ok, explanation):
    global checks
    assert bool(ok), explanation
    checks += 1

def moments(n):
    """Integrate exact maximum density, stable at moderate population."""
    def dens(z):
        return n * norm.pdf(z) * norm.cdf(z)**(n-1)
    q0 = quad(dens, -12, 12, epsabs=2e-12)[0]
    m = quad(lambda z: z * dens(z), -12, 12, epsabs=2e-12)[0]
    m2 = quad(lambda z: z*z * dens(z), -12, 12, epsabs=2e-12)[0]
    return q0, m, m2-m*m

def max_moments_large(n):
    """Exact Exp(1) representation of a Gaussian sample maximum."""
    z, weight = roots_laguerre(100)
    x = ndtri_exp(-z/n)
    mu = np.dot(weight, x)
    var = np.dot(weight, (x-mu)**2)
    return mu, var

def rho(m, v, age_mean, root_age_mean):
    c = age_mean - root_age_mean**2
    return c*m*m/(c*m*m+age_mean*v)

def coefficient(a, b, c):
    # a=ES, b=ES^(3/2), c=ES^2, all positive
    return (math.pi**2/24)/(1-(8/9)*b*b/(a*c))

for n in [2,3,4,5,10,30,100,1000]:
    total, m, v = moments(n)
    check(abs(total-1)<1e-8, 'normalization')
    check(m>0, 'positive maximum expectation')
    check(v>0, 'non-degenerate maximum')
    rr = rho(m, v, 1, math.sqrt(math.pi)/2)
    check(0<rr<1, 'strict positive imperfect correlation')

q2, m2, v2 = moments(2)
check(abs(m2-1/math.sqrt(math.pi))<1e-10, 'two-sample maximum first moment')
check(abs(v2-(1-1/math.pi))<1e-10, 'two-sample maximum variance')
check(abs(rho(m2,v2,1,math.sqrt(math.pi)/2)-(4-math.pi)/(3*math.pi))<1e-11,'exact N=2 Poisson correlation')

lo=math.pi**2/24
hi=3*math.pi**2/8
cp=math.pi**2/(6*(4-math.pi))
check(abs(coefficient(1,1,1)-hi)<1e-12, 'periodic exact envelope endpoint')
check(abs(coefficient(1,math.gamma(2.5),2)-cp)<1e-12,'Poisson exact coefficient')
check(lo<cp<hi,'Poisson inside sharp clock envelope')

last=hi
for L in [10,100,1000,10**5,10**7,10**9]:
    e=L**(-1.75)
    a=1-e+e*L
    b=1-e+e*L**1.5
    c=1-e+e*L*L
    k=coefficient(a,b,c)
    check(lo<k<hi,'two-point clock admissibility')
    check(k<last,'two-point clock approaches lower endpoint')
    last=k
check(last-lo<0.003,'sharp lower endpoint approached')

# Check asymptotics using Gaussian-exponential quantile representation;
# corrections are slowly varying, so compare a sequence against the limit.
previous=float('inf')
for n in [10**4,10**6,10**8,10**12,10**18,10**26]:
    m,v=max_moments_large(n)
    rr=rho(m,v,1,math.sqrt(math.pi)/2)
    scaled=(1-rr)*math.log(n)**2
    check(rr>0.95,'large population synchronized extrema')
    check(cp<scaled<previous,'log-squared constant approached from above')
    previous=scaled
check(abs(previous-cp)<0.055,'correct limiting correlation coefficient')

# Direct analytic extreme-value CDF convergence at Gaussian-normalized levels.
for n in [10**5, 10**7, 10**9]:
    bn=norm.isf(1/n)
    for z in [-1,0,1]:
        cdf=norm.cdf(bn+z/bn)**n
        target=math.exp(-math.exp(-z))
        check(abs(cdf-target)<0.085, 'Gumbel extreme-value scaling')

# Difference of independent standard Gumbels has logistic law.
rng=np.random.default_rng(20261116)
g1=rng.gumbel(size=100000)
g2=rng.gumbel(size=100000)
for x in [-2,-1,0,1,2]:
    observed=np.mean((g1-g2)/2 <= x)
    theoretical=1/(1+math.exp(-2*x))
    check(abs(observed-theoretical)<0.008, 'half-logistic anisotropy')

# Random positive scales cancel exactly from directional extreme ratios.
for scale in [.001, .1, 1., 17., 1000.]:
    xx,yy=2.1,3.7
    check(abs((scale*xx)/(scale*yy)-xx/yy)<3e-15,'positive common-scale cancellation')

print('PASS:', checks, 'deterministic assertions')
print('clock-envelope lower/Poisson/periodic:', lo, cp, hi)
print('Poisson N=2 correlation:', (4-math.pi)/(3*math.pi))
print('last large-population log-squared coefficient:', previous)
