"""Independent numerical diagnostics for conditional barycentric weights in Gaussian simplices."""
import math
import numpy as np
from scipy.integrate import dblquad, quad
from scipy.special import erfc
from scipy.stats import ks_2samp

rng = np.random.default_rng(20261111)


def simplex_density(lam, scales):
    m = len(scales)
    c = 2**(m-1) * math.gamma(m / 2) / math.pi**(m / 2)
    return c * np.prod(scales) / np.dot(scales * lam, scales * lam)**(m/2)

scales = np.array([0.4, 1.0, 1.0])
integ, err = dblquad(lambda b,a: simplex_density(np.array([a,b,1-a-b]),scales), 0,1, lambda a:0,lambda a:1-a,epsabs=1e-9)
assert abs(integ-1)<1e-8,(integ,err)

n=320000
G=rng.standard_normal((n,2,3))
G[:,:,0]*=scales[0]
ker=np.cross(G[:,0,:],G[:,1,:])
inside=np.logical_or(np.all(ker>0,axis=1), np.all(ker<0,axis=1))
frac=inside.mean()
assert abs(frac-.25)<.004, frac
lam=np.abs(ker[inside]);lam/=lam.sum(axis=1)[:,None]
half=rng.standard_normal((inside.sum(),3))
half=np.abs(half)/scales
half/=half.sum(axis=1)[:,None]
stat,pval=ks_2samp(lam[:,0],half[:,0])
assert stat <.013,(stat,pval)
# Density formula marginal: integration over other barycentric coordinate.
for z in [0.05, 0.25, 0.5, 0.8]:
    numerical,_=quad(lambda t:simplex_density(np.array([z,t,1-z-t]),scales),0,1-z,epsabs=2e-8)
    observed=(np.count_nonzero(abs(lam[:,0]-z)<.02)/(inside.sum()*.04))
    assert abs(numerical-observed)<.09,(z,numerical,observed)

# Distinguished-vertex critical window.
tau=1.2
n=27000
m=2049
summ=np.zeros(n)
for start in range(0,n,1500):
    nn=min(1500,n-start)
    summ[start:start+nn]=np.abs(rng.standard_normal((nn,m-1))).sum(axis=1)
x=np.abs(rng.standard_normal(n))
critical=x/(x+(tau/m)*summ)
limiting=x/(x+tau*math.sqrt(2/math.pi))
critstat=ks_2samp(critical,limiting).statistic
assert critstat<.023,critstat
fluctuation=np.sqrt(m)*(critical-limiting)
normal_mixture=-tau*x/(x+tau*math.sqrt(2/math.pi))**2 * rng.standard_normal(n)*math.sqrt(1-2/math.pi)
fluct_ks=ks_2samp(fluctuation,normal_mixture).statistic
assert fluct_ks < .028, fluct_ks
q=(critical>.5).mean()
target=erfc(tau/math.sqrt(math.pi))
assert abs(q-target)<.02,(q,target)

def limiting_density(z):
    return 2*tau/(math.pi*(1-z)**2)*math.exp(-tau**2*z*z/(math.pi*(1-z)**2))

gint,_=quad(limiting_density,0,1,epsabs=1e-9)
assert abs(gint-1)<1e-8,gint
sint,_=quad(limiting_density,.5,1,epsabs=1e-9)
assert abs(sint-target)<1e-8,(sint,target)

# Ordinary bulk normalized half-normal weights: effective inverse participation ratio.
s= np.abs(rng.standard_normal((2500,1000)))
w=s/s.sum(axis=1)[:,None]
scaled=1000*(w*w).sum(axis=1)
assert abs(scaled.mean()-math.pi/2)<.035, scaled.mean()

print('FINITE_DIMENSION_DENSITY_INTEGRAL_OK',integ)
print('ORIGIN_ABSORPTION_PROBABILITY_OK',frac)
print('CROSS_PRODUCT_BARYCENTRIC_DISTRIBUTION_OK',stat)
print('CRITICAL_WINDOW_AND_BULK_LIMITS_OK',critstat,fluct_ks,q,target,scaled.mean())
print('GAUSSIAN_SIMPLEX_CONDITIONAL_WEIGHTS_CHECKS_OK')
