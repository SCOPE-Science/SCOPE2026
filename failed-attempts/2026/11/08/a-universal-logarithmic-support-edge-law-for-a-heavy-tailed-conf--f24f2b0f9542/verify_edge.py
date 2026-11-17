import numpy as np
import sympy as sp
from math import sqrt,exp,log

t, tau=sp.symbols('t tau',positive=True)
g=tau**2/(t**2+tau**2)**sp.Rational(3,2)
S=1-t/sp.sqrt(t**2+tau**2)
H=sp.sqrt(t**2+tau**2)-t
assert sp.simplify(sp.diff(S,t)+g)==0
assert sp.simplify(sp.diff(H,t)+S)==0
assert sp.simplify(H.subs(t,0)-tau)==0
assert sp.limit(t*H/tau**2,t,sp.oo)==sp.Rational(1,2)
print('symbolic half-t density/survival/age-tail checks: PASS')

rng=np.random.default_rng(51268); n=600_000; k=1.; B=1.; tauv=1.
U=rng.random(n)
ages=(1-U*U)/(2*U)
signs=np.where(rng.random(n)<0.5,1.,-1.)
# Work from oldest of 96 completed runs to immediate preceding run.
pre=np.zeros(n)
for j in reversed(range(96)):
    # j=0 most recent (opposite sign to present)
    w=rng.random(n)
    dur=(1-w)/np.sqrt(w*(2-w))
    previous_sign=signs*(-1 if (j%2==0) else 1)
    damp=np.exp(-dur)
    pre=previous_sign*(-np.expm1(-dur))+damp*pre
# deficit normalized by full width 2B
entry=(1-pre)/2
# current positive: deficit / 2B = entry * exp(-A)
# current negative: deficit / 2B = 1-exp(-A) + entry*exp(-A)
damp=np.exp(-ages)
deficit=np.where(signs>0,entry*damp,1-damp+entry*damp)
assert np.all((0 <= deficit)&(deficit<=1))
for T in (6.,10.,16.,24.):
    p=np.mean(deficit<exp(-T))
    age_lower=.5*(sqrt(T*T+1)-T)
    print(f'log_edge={T:>4}: empirical={p:.8g}, theorem_leading={age_lower:.8g}, ratio={p/age_lower:.5f}, count={int(n*p)}')
    eta=.4
    h=(sqrt(((1-eta)*T)**2+1)-(1-eta)*T)/2
    u=-np.log1p(-np.exp(-eta*T))
    cdf=u/np.sqrt(1+u*u)
    age_threshold=-np.log1p(-np.exp(-T))
    upper=h + .5*cdf + age_threshold/2
    stderr=np.sqrt(max(p*(1-p),1/n)/n)
    assert p+5*stderr>=age_lower and p-5*stderr<=upper
    print(f'  rigorous half-t probability bracket: [{age_lower:.8g}, {upper:.8g}]')
# Stationary age survival inversion: P(A>T)=sqrt(T^2+1)-T.
for T in (0.2,1,4,16):
    prob=np.mean(ages>T)
    th=sqrt(T*T+1)-T
    assert abs(prob-th)<5*np.sqrt(max(th*(1-th),.0001)/n)
print('equilibrium-age sampling and truncated-filter diagnostics: PASS')
