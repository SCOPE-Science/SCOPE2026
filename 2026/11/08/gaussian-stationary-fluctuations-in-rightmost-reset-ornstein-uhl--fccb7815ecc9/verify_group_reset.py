"""Reproducible finite-parameter checks for collective rightmost-reset OU dynamics.

Requires Python 3, numpy, mpmath. These finite tests do not prove the asymptotic theorem.
"""
import math
import mpmath as mp
import numpy as np

mp.mp.dps = 65
checks = 0

def check(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1

def max_moments(n):
    density = lambda x: n * mp.exp(-x*x/2)/mp.sqrt(2*mp.pi) * (mp.erfc(-x/mp.sqrt(2))/2)**(n-1)
    mu = mp.quad(lambda x: x*density(x), [-mp.inf, 0, mp.inf])
    nu = mp.quad(lambda x: x*x*density(x), [-mp.inf, 0, mp.inf])
    return mu, nu

def stationary_moments(r, k, D, mu, nu):
    r, k, D = mp.mpf(r),mp.mpf(k),mp.mpf(D)
    z = r/(2*k)
    a = r/(r+k)
    a2 = r/(r+2*k)
    b = mu*mp.sqrt(D/k)*z*mp.beta(z, mp.mpf('1.5'))
    ab = mu*mp.sqrt(D/k)*z*mp.beta(z+mp.mpf('0.5'), mp.mpf('1.5'))
    m = b/(1-a)
    var = (D*nu/k*(1-a2)-2*m*(b-ab)+m*m*(1-2*a+a2))/(1-a2)
    return m, var

D,k=mp.mpf('1.7'),mp.mpf('0.9')
for n in (2, 3, 5):
    mu,nu=max_moments(n)
    check(mu>0, f'max mean positive n={n}')
    check(nu>mu*mu, f'max variance positive n={n}')
    if n==2:
        check(abs(mu-1/mp.sqrt(mp.pi)) < mp.mpf('1e-45'),'two-particle normal maximum mean')
        check(abs(nu-1)<mp.mpf('1e-45'),'two-particle normal maximum square moment')
    if n==3:
        check(abs(mu-mp.mpf('1.5')/mp.sqrt(mp.pi))<mp.mpf('1e-45'),'three-particle normal maximum mean')
    c=mu*mp.sqrt(mp.pi*D/2)/k
    V=D/k*(nu-mp.pi*mu*mu/4)
    check(V>0, f'limiting variance positive n={n}')
    for r in (20,50,200,1000,3000):
        m,v=stationary_moments(r,k,D,mu,nu)
        check(m>0 and v>0, f'finite stationary moments positive n={n} r={r}')
        # independent beta-function identity from exact stationary recursion
        z=mp.mpf(r)/(2*k)
        check(abs(m-mu*mp.sqrt(D/k)*z*mp.beta(z,mp.mpf('0.5')))<mp.mpf('1e-40'),f'closed beta mean n={n} r={r}')
    m,v=stationary_moments(3000,k,D,mu,nu)
    check(abs(m/mp.sqrt(3000)-c)/c<mp.mpf('2e-4'),f'mean asymptotic n={n}')
    check(abs(v-V)/V<mp.mpf('1e-3'),f'variance asymptotic n={n}')

# Sample the exact embedded resetting kernel, not a time-discretized diffusion.
# Repeated independent Poisson intervals E/r followed by the maximum of n Gaussians.
n, r, reps, steps=2, 250, 6000, 4500
rng=np.random.default_rng(2502026)
x=np.zeros(reps)
Df,kf=float(D),float(k)
for _ in range(steps):
    E=rng.exponential(size=reps)
    a=np.exp(-kf*E/r)
    maximum=rng.standard_normal((reps,n)).max(axis=1)
    x=a*x+np.sqrt((Df/kf)*(1-a*a))*maximum
mu,nu=max_moments(n)
m,v=stationary_moments(r,k,D,mu,nu)
mean_err=abs(float(x.mean()-m))
var_err=abs(float(x.var()-v))
check(mean_err<0.10, f'embedded stationary mean Monte Carlo error {mean_err}')
check(var_err<0.10, f'embedded stationary variance Monte Carlo error {var_err}')
# Quantile law at moderately high rate (coarse, stochastic diagnostic).
center=float(mu*mp.sqrt(mp.pi*D/2)/k)*math.sqrt(r)
V=float(D/k*(nu-mp.pi*mu*mu/4))
standardized=(x-center)/math.sqrt(V)
check(abs(float(np.median(standardized)))<0.11, 'near-normal stationary median')
check(abs(float(np.mean(standardized<=1))-0.841344746)<0.035,'near-normal upper normal quantile')
print(f'PASS {checks} checks; n={n} r={r} samples={reps}; sample_mean={x.mean():.7f} exact_mean={float(m):.7f}; sample_variance={x.var():.7f} exact_variance={float(v):.7f}; normal_limit_variance={V:.7f}')
