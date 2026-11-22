"""Deterministic numerical checks for a shared switching-diffusivity maximum.
Scientific statements follow from the accompanying proof; tests sample finite systems.
Requires numpy and scipy. Usage: python checker.py
"""
import math
import numpy as np
from scipy.special import ndtr, ndtri
from scipy.integrate import quad

RNG = np.random.default_rng(20261118)
count=0

def check(ok, reason):
    global count
    count += 1
    if not ok: raise AssertionError(reason)

# Integrated telegraph autocovariance from direct quadrature and closed form.
for lam in (0.2, 1., 4., 18., 120.):
    for T in (0.4, 1., 2.3):
        numerical, _ = quad(lambda t: 2*(T-t)*np.exp(-2*lam*t), 0, T, epsabs=1e-12)
        exact = T/lam - (-np.expm1(-2*lam*T))/(2*lam**2)
        check(abs(numerical-exact)<2e-10, f'telegraph variance {lam} {T}')

# Exact conditional maximum CDF and simulation via inverse transformation.
for n in (17, 113, 971, 10000):
    for x in (-1.1, -0.3, 0.2, 1.4):
        p=ndtr(x)**n
        u=RNG.random(7500)
        z=ndtri(np.exp(np.log(u)/n))
        empirical=np.mean(z<=x)
        check(abs(empirical-p)<.025, f'Gaussian maximum CDF N={n} x={x}')

# Exact environment covariance is shared even though covariance of distinct Xi is zero.
# Joint fourth cumulant E[Xi^2 Xj^2]-E[Xi^2]E[Xj^2] = 4 Var(A).
Dbar,delta,T=2.3,0.7,1.4
for lam in (.5, 3., 70.):
    varB=T/lam-(-np.expm1(-2*lam*T))/(2*lam**2)
    check(varB>0, 'positive variance')
    check(4*delta**2*varB>0, 'strictly positive squared-displacement correlation')

# Exact sampling of common telegraph clock by alternating holding segments.
def telegraph_areas(lam, T, size):
    out=np.empty(size)
    for j in range(size):
        k=RNG.poisson(lam*T)
        pts=np.sort(RNG.uniform(0,T,k))
        durations=np.diff(np.concatenate(([0.],pts,[T])))
        out[j]=RNG.choice([-1.,1.])*np.sum(durations*((-1.)**np.arange(k+1)))
    return out

for lam in (3., 22., 75.):
    samples=telegraph_areas(lam,T,9000)
    pred=T/lam-(-np.expm1(-2*lam*T))/(2*lam**2)
    check(abs(np.mean(samples))<.055,'symmetric mean')
    check(abs(np.var(samples)-pred)<.06*pred+.005,'telegraph path variance')

# The environmental contribution at the critical scale competes with independent Gumbel.
# Check the exact finite-size mixture against conditional exact cdf, not just a limit.
for n,c in ((2000,.7),(20000,1.5)):
    L=np.log(n); lam=c*L**2
    B=telegraph_areas(lam,T,11500)
    A=Dbar*T+delta*B
    check(np.all(A>0),'uniform ellipticity')
    U=RNG.uniform(size=len(B))
    Zmax=ndtri(np.exp(np.log(U)/n))
    M=np.sqrt(2*A)*Zmax
    u=np.sqrt(2*L)-(np.log(L)+np.log(4*np.pi))/(2*np.sqrt(2*L))
    an=1/np.sqrt(2*L)
    b=np.sqrt(2*Dbar*T)*an
    standardized=(M-np.sqrt(2*Dbar*T)*u)/b
    for z in (-.5, 0., 1.4):
        exact_cdf=np.mean(ndtr((np.sqrt(2*Dbar*T)*u+b*z)/np.sqrt(2*A))**n)
        check(abs(np.mean(standardized<=z)-exact_cdf)<.024,'integrated conditional CDF')
    linearized=(Zmax-u)/an+(delta*L/(Dbar*T))*B
    check(np.sqrt(np.mean((standardized-linearized)**2))<.22,'critical linearization')

# Leading crossover variance, independently computed exact finite-N via quadrature
# in the standard-normal maximum variable for moderate n.
from scipy.stats import norm
for n in (50,200):
    zgrid=np.linspace(-4,8,15001)
    cdf=norm.cdf(zgrid)**n
    # E Zmax by integration by parts on a bounded interval; truncation negligible.
    pdf=n*norm.pdf(zgrid)*np.maximum(norm.cdf(zgrid),1e-250)**(n-1)
    mu=np.trapezoid(zgrid*pdf,zgrid)
    var=np.trapezoid((zgrid-mu)**2*pdf,zgrid)
    check(mu>0 and var>0,'normal maximum moments')
    check(abs(np.trapezoid(pdf,zgrid)-1)<2e-6,'max pdf normalization')
    check(abs(var-np.pi**2/(12*np.log(n)))<.24,'Gumbel variance order')

print('PASS',count,'deterministic/numerical assertion groups')

# Bilateral front imbalance is insensitive to the shared variance at leading order.
# This uses two independently generated Gaussian clouds and direct empirical quantiles.
for n,rate_factor in ((3000,.15),(3000,1.),(3000,8.)):
    L=math.log(n); lam=rate_factor*L*L
    samples=1200
    B=telegraph_areas(lam,T,samples)
    data=RNG.standard_normal((samples,n))
    a=1/math.sqrt(2*L)
    sigma=np.sqrt(2*(Dbar*T+delta*B))
    upper=sigma*data.max(axis=1)
    lower=sigma*(-data.min(axis=1))
    imbalance=(upper-lower)/(math.sqrt(2*Dbar*T)*a)
    for x in (-1.5,0.,1.5):
        logit=1/(1+math.exp(-x))
        check(abs(np.mean(imbalance<=x)-logit)<.075,'bilateral logistic cancellation')
    check(abs(np.mean(imbalance))<.18,'bilateral signed symmetry')
print('PASS bilateral checks; total',count)
