#!/usr/bin/env python3
"""Exact stationary moment and inverse-law checks for telegraph-driven harmonic transport."""
import sympy as s

a, lam, v, D = s.symbols('a lam v D', positive=True)
b = lam/a
q = 1 + 2*b
c = v/a
m = {0:s.Integer(1),1:s.Integer(0)}
h = {0:s.Integer(0)}
for n in range(1,7):
    if n not in h:
        h[n]=s.factor((n*v*m[n-1] + D*n*(n-1)*h.get(n-2,s.Integer(0)))/(n*a+2*lam))
    if n+1 not in m:
        k=n+1
        m[k]=s.factor((v*h[k-1]+D*(k-1)*m[k-2])/a)
# Verify identities independently from Markov-generator moment recurrence.
assert s.simplify(m[2]-(D/a+c**2/q))==0
K4=s.factor(m[4]-3*m[2]**2)
K6=s.factor(m[6]-15*m[4]*m[2]+30*m[2]**3)
assert s.simplify(K4+6*c**4/(q**2*(q+2)))==0
assert s.simplify(K6-240*c**6/(q**3*(q+2)*(q+4)))==0
R=s.factor(K6**2/(-K4)**3)
assert s.simplify(R-s.Rational(800,3)*(q+2)/(q+4)**2)==0
# Reconstruct an exactly solvable nondegenerate model.
params={a:2,lam:3,v:6,D:4}
vals=[s.factor(x.subs(params)) for x in (m[2],K4,K6,R)]
assert vals==[s.Rational(17,4),-s.Rational(81,16),s.Rational(3645,64),s.Integer(25)],vals
r=s.Rational(3,800)*vals[3]
qhat=s.factor((1-8*r+s.sqrt(1-8*r))/(2*r))
assert qhat==4
c2hat=s.simplify(qhat*s.sqrt((-vals[1])*(qhat+2)/6))
assert c2hat==9
assert s.simplify(2*(vals[0]-c2hat/qhat))==4
assert s.simplify(s.Rational(2,2)*(qhat-1))==3
# Strict derivative, endpoint and positivity certificates.
Q=s.symbols('Q',positive=True)
f=s.Rational(800,3)*(Q+2)/(Q+4)**2
assert s.factor(s.diff(f,Q))==-s.Rational(800,3)*Q/(Q+4)**3
assert f.subs(Q,1)==32
assert s.limit(f,Q,s.oo)==0
print('PASS: symbolic generator moment recursion, cumulant identities, strict-ratio monotonicity,')
print('      exact witness, algebraic inverse and endpoint range.')
print('witness: k2={}, k4={}, k6={}, R={}'.format(*vals))
