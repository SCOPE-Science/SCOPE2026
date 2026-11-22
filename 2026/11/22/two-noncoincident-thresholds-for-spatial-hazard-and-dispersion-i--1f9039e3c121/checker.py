"""Reproducibility checks for an Erlang-two alternating-reset reflected diffusion.

Run: python checker.py. Dependencies: sympy, numpy and scipy. Symbolic identities are exact;
finite numerical checks supplement, but do not replace, the printed proof.
"""
import math
import numpy as np
import sympy as s

t, x = s.symbols('t x', real=True)
Q = 16*t**4+64*t**3+120*t**2+96*t+23
A = (t+1)**2*(16*t**4-8*t**2+7)/((t-1)**2*Q)
C = -4*t*(12*t**3+8*t**2-4*t-1)/((t-1)**2*Q)
E = -4*t**2*(2*t+1)*(2*t+3)/((t-1)*Q)
v = 4*(t+1)*(2*t+1)*(2*t+3)/Q
vp = -4*(4*t**3+8*t**2+6*t+1)/(t*Q)

check = lambda expr: s.cancel(s.factor(expr)) == 0
# Stationary density g=A exp(-x)+(C+E*x) exp(-t*x).
assert check(A+C/t+E/t**2-1)
assert check(v - A/(1+t) - C/(2*t) - E/(4*t**2))
assert check(vp + A/(1+t)**2 + C/(4*t**2) + E/(4*t**3))
assert check((t**2-1)*E+t**2*v)
assert check((t**2-1)*C-2*t*E-t**2*vp)
# Negative boundary derivative equals reset-to-zero probability.
assert check(-A-t*C+E+1-v+t*vp)

mu=s.factor(A+C/t**2+2*E/t**3)
m2=s.factor(2*A+2*C/t**3+6*E/t**4)
M=16*t**5+64*t**4+120*t**3+160*t**2+119*t+28
Pv=256*t**7+1088*t**6+1776*t**5+1280*t**4+184*t**3-308*t**2-191*t-34
assert check(mu - M/(t*Q))
assert check((m2/mu**2-2)+8*Pv/M**2) # CV^2-1=m2/mu^2-2
assert s.sign(Pv.subs(t,1))==1

# Survival S=A exp(-x)+(C/t+E*(x/t+1/t**2)) exp(-t*x).
f=C+E*x
G=f/t+E/t**2
K0=4*(8*t**3-4*t**2-15*t-4)/Q
K1=4*t*(t-1)*(2*t+1)*(2*t+3)/Q
Ph=128*t**7+448*t**6+464*t**5-160*t**4-720*t**3-604*t**2-217*t-28
assert check(E+(2-t)*f-G - K0 - K1*x)
assert check(A*K0+E**2/t**2 - 4*Ph/Q**2)
assert check(K1+(t-1)*K0-16*(t-1)**2*(t+1)*(3*t+1)/Q)
# At t=1 the removable resonant density and survival are polynomial-exponential.
# Algebraic Taylor expansions around t=1 verify pole cancellation.
for expr, expected in [(A+(C+E*x)*s.exp(-(t-1)*x), (30*x**2+68*x+191)/319),
                       (A+C/t*s.exp(-(t-1)*x)+E*(x/t+1/t**2)*s.exp(-(t-1)*x),
                        (30*x**2+128*x+319)/319)]:
    assert s.simplify(s.limit(expr,t,1)-expected)==0

import scipy.optimize as opt
Pvf=s.lambdify(t,Pv,'numpy');Phf=s.lambdify(t,Ph,'numpy')
tv=float(opt.brentq(Pvf,0.2,0.9,xtol=1e-14))
th=float(opt.brentq(Phf,1.0,2.0,xtol=1e-14))
assert 0.52416208436<tv<0.52416208439
assert 1.17158604348<th<1.17158604352
# Positive roots are unique by Descartes' one-sign-change rule.
assert s.polys.polytools.Poly(Pv,t).all_coeffs()[0]>0
assert s.polys.polytools.Poly(Ph,t).all_coeffs()[0]>0
for pol in (Pv,Ph):
    signs=[s.sign(c) for c in s.Poly(pol,t).all_coeffs()]
    assert sum(signs[i]!=signs[i+1] for i in range(len(signs)-1))==1

# Independent stationary Markov-chain Monte Carlo at Poisson review epochs.
# Reflection semigroup at exponential interval has folded-normal marginal.
rng=np.random.default_rng(211726)
for beta in (0.3,0.7,1.1,1.6):
    n=120000
    gamma=rng.gamma(2,1/beta,size=n)
    times=rng.exponential(size=n)
    z=rng.normal(size=n)
    current=0.0
    arr=np.empty(n)
    for i in range(n):
        post=max(0.0,gamma[i]-current)
        current=abs(post+math.sqrt(2*times[i])*z[i])
        arr[i]=current
    arr=arr[3000:]
    observed=(float(np.mean(arr)),float(np.mean(arr**2)))
    theoretic=(float(mu.subs(t,beta)),float(m2.subs(t,beta)))
    for obs,expected in zip(observed,theoretic):
        assert abs(obs-expected)/expected<0.025,(beta,observed,theoretic)
    print(f'beta/k={beta:.1f}, analytic mean and second moment={theoretic}, simulated={observed}')
print('Exact polynomial identities, unique-threshold sign changes and resonant limit passed.')
print(f'dispersion threshold={tv:.12f}; spatial-hazard threshold={th:.12f}')
