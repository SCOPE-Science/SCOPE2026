#!/usr/bin/env python3
"""Reproduce exact polynomial identities and a normalized numerical example.
Scientific theorem requires the analytic proof in RESULT.md, not finite testing.
Run: python verify.py (requires SymPy and mpmath; see requirements.txt).
"""
from sympy import Matrix, eye, diag, symbols, factor, simplify, Rational
import mpmath as mp

k, p, v, s = symbols('k p v s', positive=True)
L = Matrix([[1,-1,0],[-1,2,-1],[0,-1,1]])
M1 = v*eye(3) + k*L + p*diag(1,0,0)
M2 = v*eye(3) + k*L + p*diag(0,1,0)
D1 = (s*eye(3)+M1).det()
D2 = (s*eye(3)+M2).det()
assert simplify(D1-D2-p*k*(s+v)) == 0
assert simplify((s*eye(3)+M1).inv()[2,0]-k*k/D1)==0
assert simplify((s*eye(3)+M2).inv()[2,0]-k*k/D2)==0
assert simplify(k*k/D2-k*k/D1 - p*k**3*(s+v)/(D1*D2))==0
L2 = Matrix([[1,-1],[-1,1]])
A1 = v*eye(2)+k*L2+p*diag(1,0)
A2 = v*eye(2)+k*L2+p*diag(0,1)
assert simplify((s*eye(2)+A1).inv()[1,0] - (s*eye(2)+A2).inv()[1,0]) == 0
assert simplify((M2.inv()[2,0] - M1.inv()[2,0]) - p*k**3*v/(D1.subs(s,0)*D2.subs(s,0)))==0
assert factor(D1.subs({k:1,p:1,v:1})) == s**3+8*s**2+19*s+13
assert factor(D2.subs({k:1,p:1,v:1})) == (s+2)*(s*s+6*s+6)
assert simplify((M2.inv()[2,0]-M1.inv()[2,0]).subs({k:1,p:1,v:1}) - Rational(1,156))==0

mp.mp.dps=70
B1=mp.matrix([[3,-1,0],[-1,3,-1],[0,-1,2]])
B2=mp.matrix([[2,-1,0],[-1,4,-1],[0,-1,2]])
rates=sorted([*mp.eigsy(B1,eigvals_only=True),*mp.eigsy(B2,eigvals_only=True)])
assert all(x > 1 for x in rates)
residues = [1/mp.fprod([rates[j]-rates[i] for j in range(6) if i!=j]) for i in range(6)]
def h(t):
 return mp.fsum(residues[i]*mp.exp(-rates[i]*t) for i in range(6))
def differential(t):
 return mp.fsum(residues[i]*(1-rates[i])*mp.exp(-rates[i]*t) for i in range(6))
assert h(mp.mpf('0.1')) > 0
assert differential(1) > 0
assert differential(6) > 0
assert differential(8) < 0
assert differential(12) < 0
lo, hi=mp.mpf(6),mp.mpf(8)
for _ in range(250):
 mid=(lo+hi)/2
 if differential(mid)>0: lo=mid
 else: hi=mid
root=(lo+hi)/2
assert 6 < root < 8 and abs(differential(root)) < mp.mpf('1e-60')
# Independent direct matrix-exponential check of receiving room at two times.
for t in [1,6,8,12]:
 d=(mp.expm(-B2*t)-mp.expm(-B1*t))[2,0]
 assert abs(d-differential(t)) < mp.mpf('1e-65')
print('Exact symbolic determinant/transfer/dose identities: PASS')
print('Two-compartment degeneracy: PASS')
print('Independent matrix exponentials and six-exponential reconstruction: PASS')
print('Normalized crossover t* =',mp.nstr(root,35))
print('At t=1, delta=',mp.nstr(differential(1),18))
print('At t=8, delta=',mp.nstr(differential(8),18))
print('Full cumulative difference at v=k=p=1 = 1/156')
print('Analytic proof of the all-parameter uniqueness is in RESULT.md')
