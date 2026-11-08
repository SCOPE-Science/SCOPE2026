#!/usr/bin/env python3
"""Check exact phase-space covariance and instantaneous gyrator SNR identities.

Requires Python >=3.9 and sympy >=1.10. No data files or network access.
The assertions are finite algebraic checks; the mathematical domain,
uniqueness and stationary existence are established in RESULT.md.
"""
import itertools
import sympy as sp

g, a, H, C = sp.symbols('g a H C', positive=True)
S, J = H + C, H - C
z = g*a*J / (2*(g*g+a*a))
vx = S/2 + J*g*g/(2*(g*g+a*a))
vy = S/2 - J*g*g/(2*(g*g+a*a))
xy = a*S/(2*(1-a*a))
Sigma = sp.Matrix([[vx+a*xy, xy, 0, z],
                   [xy, vy+a*xy, -z, 0],
                   [0, -z, vx, 0],
                   [z, 0, 0, vy]])
A = sp.Matrix([[0,0,1,0], [0,0,0,1],
               [-1,a,-g,0], [a,-1,0,-g]])
Q = sp.diag(0,0,2*g*H,2*g*C)
checks = 0
for element in (A*Sigma+Sigma*A.T+Q):
    assert sp.cancel(element) == 0
    checks += 1
mean = sp.factor(Sigma[0,3]-Sigma[1,2])
assert sp.cancel(mean-g*a*J/(g*g+a*a)) == 0
checks += 1
variance = sp.factor(Sigma[0,0]*Sigma[3,3]
        + Sigma[1,1]*Sigma[2,2]
        - 2*Sigma[0,1]*Sigma[2,3]
        + Sigma[0,3]**2 + Sigma[1,2]**2
        - 2*Sigma[0,2]*Sigma[1,3])
assert sp.cancel(variance -(S*S/(2*(1-a*a))
                         - J*J*g*g*(g*g-a*a)/(2*(g*g+a*a)**2))) == 0
checks += 1
alpha = 4*H*C + J*J*a*a
beta = a*a*(2*S*S+J*J*(1-a*a))
gamma = S*S*a**4
Den = alpha*g**4+beta*g*g+gamma
SNR2 = 2*J*J*a*a*(1-a*a)*g*g/Den
assert sp.cancel(mean**2/variance - SNR2) == 0
checks += 1
assert sp.cancel(sp.diff(SNR2,g)
        - 4*J*J*a*a*(1-a*a)*g*(gamma-alpha*g**4)/Den**2) == 0
checks += 1
maxsignal = 2*J*J*(1-a*a)/(2*S*S+J*J*(1-a*a)+2*S*sp.sqrt(alpha))
maxat = a*(S*S/alpha)**sp.Rational(1,4)
assert sp.simplify((SNR2.subs(g,maxat)-maxsignal)) == 0
checks += 1
# Independent direct Lyapunov residuals and Wick variance at diverse rational points.
for aa, hh, cc, gg in itertools.product(
        [sp.Rational(1,5),sp.Rational(1,2),sp.Rational(4,5)],
        [sp.Integer(2),sp.Integer(5),sp.Integer(13)],
        [sp.Integer(1),sp.Integer(3)],
        [sp.Rational(1,4),sp.Rational(2,3),sp.Integer(2)]):
    if hh == cc:
        continue
    param={a:aa,H:hh,C:cc,g:gg}
    state=Sigma.subs(param)
    assert state.det()>0  # physical covariance strictly positive
    assert all(sp.cancel(x)==0 for x in
           (A*Sigma+Sigma*A.T+Q).subs(param))
    n=sp.factor((state[0,3]-state[1,2])**2 / (
         state[0,0]*state[3,3] + state[1,1]*state[2,2]
         +state[0,3]**2+state[1,2]**2))
    assert sp.cancel(n-SNR2.subs(param))==0
    checks+=3
# Nonzero temperature contrast, stable coupling, and peak-location bounds.
for aa,hh,cc in itertools.product(
        [sp.Rational(1,6),sp.Rational(1,2),sp.Rational(5,6)],
        [sp.Integer(2),sp.Integer(7),sp.Integer(101)],
        [sp.Integer(1),sp.Integer(3)]):
    if hh==cc:
        continue
    p={a:aa,H:hh,C:cc}
    opt=sp.N(maxat.subs(p),30)
    assert float(opt)>float(aa)
    assert float(opt)<float(sp.sqrt(aa))
    checks+=2
print('PASS:',checks,'symbolic and rational checks')
