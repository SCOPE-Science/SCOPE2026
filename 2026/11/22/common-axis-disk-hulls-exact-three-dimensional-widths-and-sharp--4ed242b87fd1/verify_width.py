"""Independent numeric diagnostics for the common-axis disk-hull width theorem.
Requires Python >=3.9, NumPy and SciPy. Not a proof of an infinite statement.
"""
import math
import numpy as np
from scipy.special import gamma
from scipy.integrate import quad

RNG=np.random.default_rng(202611160631)

def width(u):
    u=np.asarray(u)
    return 2*np.sqrt(u[...,0]**2+np.max(u[...,1:]**2,axis=-1))

def f2(w):
    if w <= math.sqrt(2): return 0.
    if w >= 2.: return 1.
    s=math.sqrt(max(0.,1.-w*w/4))
    return (4/math.pi)*(math.atan(math.sqrt(max(0.,1.-2*s*s)))-s*math.acos(s/math.sqrt(1-s*s)))

def dens2(w):
    if w <= math.sqrt(2) or w >= 2: return 0.
    s=math.sqrt(1-w*w/4)
    return (w/(math.pi*s))*math.acos(s/math.sqrt(1-s*s))

def c_lower(m):
    return gamma((m+1)/2)*m**(m-.25)/(math.pi**(m/2)*math.sqrt(m-1)*gamma(m+.5))

# Compare against a directly integrated spherical density of |Y|,|Z| without differentiating F2.
def cdf_integral(w):
    if w<=math.sqrt(2): return 0.
    if w>=2: return 1.
    s=math.sqrt(1-w*w/4)
    # The unconditional |Y| density on the sphere is 1; given |Y|=y, |Z| is
    # abs(sin phi)*sqrt(1-y*y). The probability both exceed s is integrated.
    upper=math.sqrt(1-s*s)
    return quad(lambda y: (2/math.pi)*math.acos(s/math.sqrt(1-y*y)),s,upper,epsabs=2e-11)[0]

for w in np.linspace(math.sqrt(2)+.0001,1.9999,51):
    assert abs(f2(w)-cdf_integral(w))<3e-10,(w,f2(w),cdf_integral(w))
    h=min(1e-6,(2-w)/1000,(w-math.sqrt(2))/1000)
    assert abs((f2(w+h)-f2(w-h))/(2*h)-dens2(w))<1e-3,w
assert abs(f2(math.sqrt(2)))<1e-14 and f2(2)==1.

# Independent support-function numerical minimization on generating disks.
for m in [2,3,5]:
    for _ in range(12):
        u=RNG.normal(size=m+1);u=u/np.linalg.norm(u)
        theta=np.linspace(0,2*np.pi,4001)
        direct=max(np.max(u[0]*np.cos(theta)+u[j]*np.sin(theta)) for j in range(1,m+1))
        assert abs(width(u)/2-direct)<1.5e-6

# Direct sphere simulation checks the 3D full CDF and second moment.
n=500_000
z=RNG.normal(size=(n,3)); z/=np.linalg.norm(z,axis=1)[:,None]
w=width(z)
for c in [1.48,1.55,1.65,1.75,1.9,1.97]:
    p=f2(c); obs=np.mean(w<=c)
    assert abs(obs-p)<.005,(c,p,obs)
second=8/3*(1+1/math.pi)
assert abs(np.mean(w*w)-second)<.012,(np.mean(w*w),second)

# Three-dimensional lower-tail exponent/constant via Dirichlet integration.
# Sampling the exact transformed simplex avoids extremely rare Monte Carlo events.
def low_prob_quad(m,eta,n=120_000):
    base=2/math.sqrt(m)
    delta=(base+eta)**2/4-1/m
    Amax=m*delta/(m-1)
    # a/Amax~Beta(1/2,m), remaining simplex z_j = (m delta-(m-1)a) v_j
    # with v uniformly Dirichlet(1,...,1), to integrate the smooth density ratio.
    a=Amax*RNG.beta(.5,m,n)
    v=RNG.dirichlet(np.ones(m),size=n)
    b=1/m+delta-a
    y=b[:,None]-(m*delta-(m-1)*a)[:,None]*v
    assert np.min(y)>0.
    correction=np.mean(np.prod((m*y)**(-.5),axis=1))
    factor=gamma((m+1)/2)*m**((3*m-1)/2)/(math.pi**(m/2)*math.sqrt(m-1)*gamma(m+.5))
    return factor*delta**(m-.5)*correction
for m in [2,3,4]:
    for eta in [.005,.012]:
        ratio=low_prob_quad(m,eta)/(c_lower(m)*eta**(m-.5))
        assert abs(ratio-1)<.07,(m,eta,ratio)

# High-dimensional weak limit: compare the predicted mixed Gumbel--chi-square
# quantile levels from Gaussian simulation (G independent of Z).
m=2500
N=12000
qq=[]
for _ in range(12):
    zz=RNG.normal(size=(1000,m+1))
    q=(zz[:,0]**2+np.max(zz[:,1:]**2,axis=1))/(np.mean(zz*zz,axis=1))
    qq.append(q)
stat=(np.concatenate(qq)-(2*np.log(m)-np.log(np.log(m))-np.log(np.pi)))/2
ref=-np.log(-np.log(RNG.random(N)))+RNG.normal(size=N)**2/2
for pct in [.15,.35,.5,.7,.85]:
    assert abs(np.quantile(stat,pct)-np.quantile(ref,pct))<.23,(pct,np.quantile(stat,pct),np.quantile(ref,pct))

print('COMMON_AXIS_DISK_WIDTH_CHECKS_OK; 51 CDF, 51 density, 36 support, 6 empirical CDF, second moment, 6 lower-tail, 5 high-dimensional quantiles')
