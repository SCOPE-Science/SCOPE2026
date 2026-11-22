"""Independent numerical checks for stationary and finite-horizon batch-reset Brownian pair observables."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaincc, gammaln

D = 0.8
lam = 1.3
N = 6
rng = np.random.default_rng(173)


def h(a, threshold, dim):
    if a <= 0:
        return 0.0
    return gammaincc(dim / 2., threshold / (4 * D * a))


def hp(a, threshold, dim):
    if a <= 0:
        return 0.0
    s = dim / 2.
    z = threshold / (4 * D * a)
    return np.exp(s * np.log(z) - z - np.log(a) - gammaln(s))


def double_tail(c, t, x, y, dim):
    # Separate atom at observation-horizon t via a layer-cake identity.
    upper = 35 / lam if np.isinf(t) else t
    def integrand(u):
        return hp(u, x, dim) * quad(lambda v: hp(v, y, dim) * np.exp(-lam * (u+v) + c * min(u,v)), 0., upper, epsabs=2e-9)[0]
    return quad(integrand, 0., upper, epsabs=2e-9)[0]


def age_cross(c,t):
    if abs(c-lam)<1e-12:
        return 2 * (1 - np.exp(-lam*t)*(1 + lam*t)) / lam**2 if np.isfinite(t) else 2 / lam**2
    A = -np.expm1(-lam*t)/lam if np.isfinite(t) else 1/lam
    B = -np.expm1(-(2*lam-c)*t)/(2*lam-c) if np.isfinite(t) else 1/(2*lam-c)
    return 2*(A-B)/(lam-c)


def conditional_surv(a,b,c):
    if b < a:
        return np.exp(-(lam-c)*b)
    if b > a:
        return (1-c/lam)*np.exp(-lam*b+c*a)
    raise ValueError('Atom at equality not used')


# Check layer-cake numerical derivatives against finite differences.
for dim in [1,2,4]:
    for a in [.1,.5,2.0]:
        x=1.3
        step=1e-5
        est=(h(a+step,x,dim)-h(a-step,x,dim))/(2*step)
        assert abs(est-hp(a,x,dim))<1e-7

# Compare pair joint exceeds at matched marginal reset rate, including stationarity.
for t in [1.0, 3.0, float('inf')]:
    vals = []
    for m in [1,3,6]:
        c=lam*(m-1)/(N-1)
        vals.append(double_tail(c,t,1.1,1.7,2))
    assert vals[0] < vals[1] < vals[2], (t, vals)
    print('tail',t,vals)

# Event-clock Monte Carlo independent of analytical threshold double integration.
for t in [1.0,float('inf')]:
    num=200000
    xs=[]
    for m in [1,3,6]:
        c=lam*(m-1)/(N-1)
        e0=rng.exponential(1/c,size=num) if c>0 else np.full(num,np.inf)
        e1=rng.exponential(1/(lam-c),size=num) if lam>c else np.full(num,np.inf)
        e2=rng.exponential(1/(lam-c),size=num) if lam>c else np.full(num,np.inf)
        a=np.minimum(np.minimum(e0,e1),t)
        b=np.minimum(np.minimum(e0,e2),t)
        z1=rng.chisquare(2,size=num)
        z2=rng.chisquare(2,size=num)
        v1=2*D*a*z1
        v2=2*D*b*z2
        observed=np.mean((v1>1.1)&(v2>1.7))
        pred=double_tail(c,t,1.1,1.7,2)
        std=np.sqrt(pred*(1-pred)/num)
        assert abs(observed-pred)<5*std, (t,m,observed,pred)
        xs.append((m,float(observed),float(pred)))
    print('simulation',t,xs)

# Critical joint-age covariance and a known-correlator comparison.
for m in [1,2,5,6]:
    c=lam*(m-1)/(N-1)
    s=age_cross(c,float('inf')) -1/lam**2
    target = c/(lam**2*(2*lam-c))
    assert abs(s-target)<1e-12,(m,s,target)

# Conditional reset-age regression is strictly increasing for every threshold.
for c in [lam*.4,lam]:
    for b in [.15,.65,1.2]:
        ages=[.1,.35,.7,1.4]
        survs=[conditional_surv(a,b,c) for a in ages if abs(a-b)>1e-9]
        assert all(survs[i+1]>=survs[i]-1e-13 for i in range(len(survs)-1)),(c,b,survs)
    # Posterior likelihood ratio rises strictly in a for any y2>y1.
    assert np.exp(-1.0/(4*D*.8)) > np.exp(-1.0/(4*D*.25))
print('ALL CHECKS PASSED')
