#!/usr/bin/env python3
"""Numerical and algebraic checks for Pareto min-characteristic high-bandwidth limits.
The checks supplement, but do not replace, the analytic convergence proofs.
Dependencies: Python 3, numpy, scipy.
"""
import math
import numpy as np
from numpy.polynomial.laguerre import laggauss
from scipy.integrate import quad

assertions=0
def check(ok,msg):
    global assertions
    assertions+=1
    if not bool(ok): raise AssertionError(msg)

# Covariance for Pareto(1) truncated at v>=1.
def crossmoment(v,w):
    a,b=sorted((v,w))
    return 2*a-1+a*math.log(b/a)
def var_trunc(v):
    return crossmoment(v,v)-(1+math.log(v))**2

def covariance_limit(u,v):
    a=max(u,v); b=min(u,v)
    return (2+math.log(a/b))/a

def fourth_cumulant_kernel(u,v):
    a=max(u,v); b=min(u,v)
    return 2/(a*a*b)-2/(3*a*a*a)

for u in [0.2,0.75,1.3,4.8]:
    for v in [0.3,0.95,2.7]:
        g=1.0e7
        a,b=g/u,g/v
        cv=crossmoment(a,b)-(1+math.log(a))*(1+math.log(b))
        check(abs(cv/g-covariance_limit(u,v)) < 6.e-5,'large-cutoff covariance')
        check(covariance_limit(u,v)>0,'positive covariance')

# Fourth-order Poisson cumulant integral from direct piecewise integration.
for u in [0.5, 1.2, 3.]:
    for v in [0.4,2.,5.]:
        z=min(1/u,1/v); Z=max(1/u,1/v)
        direct=z**3/3+z*z*(Z-z)+z*z*Z
        check(abs(direct-fourth_cumulant_kernel(u,v)) < 1.e-12,'fourth cumulant')

var_gauss=24*quad(lambda t:t*t*(2-math.log(t))**2/(1+t)**4,0,1,epsabs=2e-13)[0]
B=8*(1-math.log(2))/3
B_integral = 1-(8/3)*quad(lambda t:t*t/(1+t)**3,0,1,epsabs=2e-13)[0]
check(abs(var_gauss-6.704649979265374)<1e-10,'Gaussian quadratic variance')
check(abs(B-B_integral)<1e-12,'Poisson variance correction')
check(0<B<1,'positive cumulant correction')

# Identity for the exact Pareto null min-characteristic function.
for t in [0.01,0.1,0.42,0.9,1.,1.1,5.]:
    formula=t*(1-math.log(t)) if t<1 else 1.
    integral=quad(lambda y: min(1,t*y)/y**2,1,math.inf,epsabs=1e-10)[0]
    check(abs(formula-integral)<3e-8,'min characteristic function')

nodes,weights=laggauss(72)

def scaled_stat(log_y,gamma,fitted):
    # Returns gamma^2 * T_n,gamma using u=gamma*t and Gauss-Laguerre.
    n=len(log_y)
    if fitted:
        m=log_y.min(); beta=n/(log_y-m).sum()
        ly=beta*(log_y-m)
    else:
        ly=log_y
    y=np.exp(ly)
    mask=nodes<gamma
    u=nodes[mask]
    v=gamma/u
    centered=np.minimum(y[:,None],v[None,:]).mean(axis=0) -1-np.log(v)
    scaled=(n/gamma)*np.dot(weights[mask],u*u*centered**2)
    return scaled

rng=np.random.default_rng(40824)
for n,gamma in [(100,5.),(100,50.),(100,1e4),(400,40.),(400,400.),(400,400000.)]:
    ly=rng.exponential(size=n)
    a=scaled_stat(ly,gamma,False)
    b=scaled_stat(ly,gamma,True)
    check(math.isfinite(a) and a>=0,'oracle finite nonnegative')
    check(math.isfinite(b) and b>=0,'fitted finite nonnegative')

# Exact oracle expectation independent of sample size, asymptotic 2.
def scaled_expectation(gamma):
    i=nodes<gamma
    u=nodes[i]
    v=gamma/u
    variance=2*v-1-(1+np.log(v))**2
    return np.dot(weights[i],u*u*variance)/gamma
for gamma in [8.,20.,100.,500.,2000.]:
    val=scaled_expectation(gamma)
    check(0<val<2+1e-8,'positive and bounded scaled expectation')
check(abs(scaled_expectation(2000.)-2)<0.08,'mean tends to 2')

# Gaussian covariance via discretized quadratic form:
uw=nodes*nodes*weights
K=np.array([[covariance_limit(a,b) for b in nodes] for a in nodes])
mean_G=np.dot(uw,np.diag(K))
variance_G=2*np.dot(uw,(K*K)@uw)
check(abs(mean_G-2)<0.055,'Gauss quadrature mean')
check(abs(variance_G-var_gauss)<0.20,'Gauss quadrature variance')

# In the critical window, the limiting covariance and fourth cumulant yield
# E W_c=2, Var W_c=Var Q+c*(8/3)*(1-log2).
for c in [.2,.5,1.,3.,10.]:
    check(2+c*B>2,'critical variance strictly exceeds Gaussian')

print('PASS',assertions,'assertions')
print('Var(Gaussian quadratic) =',format(var_gauss,'.14f'))
print('Poisson critical linear variance slope =',format(B,'.14f'))
print('Gauss-Laguerre approximations: E=',mean_G,'Var=',variance_G)
print('Oracle scaled expectation at gamma=2000 =',scaled_expectation(2000.))
