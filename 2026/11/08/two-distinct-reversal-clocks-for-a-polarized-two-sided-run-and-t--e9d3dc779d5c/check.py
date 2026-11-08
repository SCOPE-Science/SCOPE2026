"""Independent numerical checks of a two-sided polarized telegraph step gas.
Scientific symbols are defined in RESULT.md. Requires scipy (>=1.8).
"""
import math
from scipy.special import ive, betainc
from scipy.optimize import brentq
from scipy.stats import poisson

# v=gamma=1 in dimensionless checks.
def Va(x):
    return x * (ive(0,x) + ive(1,x))
def Ma(x):
    return -math.expm1(-2*x)/2

def direct_finite_flip_abs(x):
    """Condition on Poisson flip count and integrate Dirichlet sojourn durations.
    N=n flips implies total positive-running fraction Beta(ceil((n+1)/2),floor((n+1)/2)).
    This independent derivation does not use the Bessel series.
    """
    nmax = int(max(85, x+22*math.sqrt(x)+35))
    total = poisson.pmf(0,x)
    for n in range(1,nmax+1):
        a=(n+2)//2
        b=(n+1)//2
        p=poisson.pmf(n,x)
        e=2*a/(a+b)-1-4*a/(a+b)*betainc(a+1,b,.5)+2*betainc(a,b,.5)
        assert -.0000001<=e<=1.0000001, (x,n,e)
        total+=p*e
    assert poisson.sf(nmax,x)<1e-12
    return x*total

for x in (.05,.2,1,3,7,18):
    v=Va(x)
    d=direct_finite_flip_abs(x)
    assert abs(v-d)<3e-12*max(1,v),(x,v,d)
    print('Flip-mixture E|X| check',x,round(v,12))

def R(x):
    # e^x cancels, numerator sinh(x)/exp(x)=(1-e^-2x)/2
    return -math.expm1(-2*x)/(2*x*(ive(0,x)+ive(1,x)))

def f_flux(x,c):
    # c=Delta/(-P), zero when e^x I0(x)=1/c
    return c*ive(0,x)-math.exp(-2*x)

for c in (.05,.1,.3,.5,.8,.98):
    j=brentq(lambda x:f_flux(x,c),1e-10,45,xtol=1e-13)
    q=brentq(lambda x:R(x)-c,1e-10,max(50,10/c**2),xtol=1e-11)
    assert 0<j<q
    assert abs(R(q)-c)<1e-9
    assert abs(f_flux(j,c))<1e-10
    print('Thresholds',c,'flux',round(j,9),'transfer',round(q,9))

# Exact initial and long-time sign for genuine physical density/polarization witness.
delta=2.; P=-4.
for x in (.1,.5,1.,3.,10.):
    mean=(delta*Va(x)+P*Ma(x))/2
    deriv=(delta*ive(0,x)+P*math.exp(-2*x))/2
    print('net transfer/current',x,round(mean,9),round(deriv,9))

# Strong monotonicity of key analytic ratios, diagnostic only.
for x in (.001,.01,.1,1,5,20,100):
    left=2*x/math.expm1(2*x) if x<300 else 0
    rhs=ive(0,x)/(ive(0,x)+ive(1,x))
    assert left<rhs, (x,left,rhs)
print('All checks passed')
