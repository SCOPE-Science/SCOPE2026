"""Reproducibility checks for sparse-Poisson exponential Stein discrepancy theorem."""
import math
import numpy as np
from scipy.stats import poisson, multinomial

COUNT=0
def check(cond, message):
    global COUNT
    COUNT += 1
    if not cond:
        raise AssertionError(message)

def psi(k, lam, z):
    phi=z*math.exp(lam*(z-1))
    return k*z**k-lam*z**(k+1)-phi*(k-lam)

def cov(lam,z,w):
    return lam*z*w*(math.exp(lam*(z*w-1))*(1+lam*(1-z)*(1-w))-
                       math.exp(lam*(z+w-2)))

def var(lam,z):return cov(lam,z,z)

# Independent direct sum of discrete expectation and covariance
for lam in [0.008,0.03,0.1,0.7,2.0,5.0]:
    k=np.arange(0,max(40,int(lam+15*math.sqrt(lam+1))))
    probs=poisson.pmf(k,lam)
    for z in [0.1,0.3,0.6,0.85]:
        ps=np.array([psi(int(i),lam,z) for i in k])
        check(abs(np.dot(probs,ps))<1e-12,("mean",lam,z))
        direct=np.dot(probs,ps**2)
        check(abs(direct-var(lam,z))<1e-11,("var",lam,z,direct,var(lam,z)))
        for w in [0.2,0.5,0.9]:
            pw=np.array([psi(int(i),lam,w) for i in k])
            cross=np.dot(probs,ps*pw)
            check(abs(cross-cov(lam,z,w))<1e-11,("cov",lam,z,w))
# exact small-rate 2 coefficient and perfectly correlated normalized kernels
for z in [0.17,0.49,0.8]:
    for w in [0.2,0.5,0.85]:
        for lam in [1e-3,1e-4]:
            ratio=cov(lam,z,w)/(2*lam*lam*z*w*(1-z)*(1-w))
            check(abs(ratio-1)<0.02,("leading",lam,z,w,ratio))

# Sampling histograms instead of raw observations is exact (apart from an
# explicitly bounded negligible tail at k>=8).
rng=np.random.default_rng(7232026)
def simulate(n,lam,z,m):
    ks=np.arange(8)
    probs=poisson.pmf(ks,lam)
    probs=np.r_[probs,1-probs.sum()]
    check(probs[-1]>=-1e-12,"tail probability")
    out=rng.multinomial(n,probs,m)
    # x=8 is tail proxy; tail probability in checked runs is below 1e-12.
    vals=np.arange(9)
    xbar=(out@vals)/n
    a=(out@(vals*z**vals))/n
    b=(out@(z**(vals+1)))/n
    return n*(a-xbar*b)/(z*(1-z)),probs[-1]

for n,lam,m in [(30000,0.01,12000),(50000,0.05,5000),(2000,0.001,5000)]:
    t,tail=simulate(n,lam,0.45,m)
    check(n*tail<1e-8,"tail truncation")
    tau=n*lam**2
    if 0.5<tau<5:
        # P=0 and P=1 are largest two atoms of the centered Poisson law.
        p0=np.mean(abs(t-tau)<0.5)
        p1=np.mean(abs(t-(tau-2))<0.5)
        check(abs(p0-math.exp(-tau/2))<0.05,("P0",p0,tau))
        check(abs(p1-(tau/2)*math.exp(-tau/2))<0.05,("P1",p1,tau))
    if tau>25:
        std=t/math.sqrt(2*tau)
        check(abs(np.mean(std))<0.12,"high occupancy mean")
        check(abs(np.std(std)-1)<0.12,"high occupancy sd")
    if tau<0.01:
        check(np.mean(abs(t)<.2)>.97,"vanishing occupancy")

print(f"PASS: {COUNT} assertions; analytic cross-covariance, small-rate rank-one limit, three finite-regime simulations")
# Exact finite-sample expectation: E[U_n(z)] = -Cov(X,z^(X+1))/n.
for lam in [0.015,0.2,1.0,3.0]:
    for z in [0.2,0.4,0.7]:
        k=np.arange(0,60)
        p=poisson.pmf(k,lam)
        cov_xb=np.sum(p*k*z**(k+1))-lam*np.sum(p*z**(k+1))
        target=-lam*z*(1-z)*math.exp(lam*(z-1))
        check(abs(cov_xb-target)<1e-12,("finite bias",lam,z))
# At tau=0.3, the nominal 5% two-sided normal rule rejects iff P>=1.
tau=.3
rate=tau/2
cutoff=1.959963984540054
p=np.array([poisson.pmf(k,rate) for k in range(25)])
zv=np.array([(tau-2*k)/math.sqrt(2*tau) for k in range(25)])
size=float(p[np.abs(zv)>cutoff].sum())
check(abs(size-(1-math.exp(-.15)))<1e-14,("size",size))
samples,tail=simulate(30000,math.sqrt(tau/30000),.3,9000)
emp=float(np.mean(np.abs(samples)/math.sqrt(2*tau)>cutoff))
check(abs(emp-size)<.03,("sim size",emp,size))
print(f"ADDITIONAL PASS: {COUNT} cumulative assertions, critical two-sided size {size:.6f}, Monte Carlo {emp:.6f}")
