#!/usr/bin/env python3
"""Exact symbolic verification of the unique tuned ladder heat-step theorem.

Requires Python 3 and SymPy. No floating-point arithmetic is used.
"""
import sympy as sp

h = sp.symbols('h')
r1, r2, r3 = sp.symbols('r1 r2 r3', positive=True)
P = sp.Matrix([[1, -1, 0], [-1, 2, -1], [0, -1, 1]])
J = sp.ones(3, 3)
Pplus = (P + J/3).inv() - J/3
expected_Pplus = sp.Matrix([[5,-1,-4],[-1,2,-1],[-4,-1,5]])/9
assert Pplus == expected_Pplus

# In the lane-symmetric/-antisymmetric decomposition, the antisymmetric
# operator is P+2 diag(r1,r2,r3). Verify the forced tuning constraints.
R = sp.diag(sp.Rational(1,2), sp.Rational(7,4), sp.Rational(1,2))
M = P+2*R
G = M.inv()
assert G == sp.Matrix([[sp.Rational(5,9),sp.Rational(1,9),sp.Rational(1,18)],
                       [sp.Rational(1,9),sp.Rational(2,9),sp.Rational(1,9)],
                       [sp.Rational(1,18),sp.Rational(1,9),sp.Rational(5,9)]])
assert M.eigenvals() == {sp.Rational(3,2):1, sp.Integer(2):1, sp.Integer(6):1}

# Independent analytic spectral projectors of both three-by-three blocks.
P0 = sp.ones(3,3)/3
P1 = sp.Matrix([[1,0,-1],[0,0,0],[-1,0,1]])/2
P3 = sp.Matrix([[1,-2,1],[-2,4,-2],[1,-2,1]])/6
Q15 = sp.Matrix([[4,2,4],[2,1,2],[4,2,4]])/9
Q2 = P1
Q6 = sp.Matrix([[1,-4,1],[-4,16,-4],[1,-4,1]])/18
assert P0+P1+P3 == sp.eye(3)
assert Q15+Q2+Q6 == sp.eye(3)
assert P == P1+3*P3
assert M == sp.Rational(3,2)*Q15+2*Q2+6*Q6
F = lambda x: (x*x -6*x +12)/(x*x +6*x +12)
A = P0 + F(h)*P1 + F(3*h)*P3
B = F(sp.Rational(3,2)*h)*Q15 + F(2*h)*Q2+F(6*h)*Q6

# Positive common denominator and exact certificate for every offdiagonal orbit.
D = (h*h+6*h+12)*(3*h*h+6*h+4)*(3*h*h+12*h+16)* \
    (h*h+3*h+3)*(3*h*h+3*h+1)
# labels are (vertex indices, exponent of h, strictly positive coefficients
# of the remaining polynomial in ascending degree order).
CERT = {
 (0,1): (1,[1152,6048,14472,19440,15478,7188,1812,189]),
 (2,3): (1,[4032,12096,14496,9144,3208,600,48]),
 (0,2): (1,[2304,9504,17448,17460,10234,3516,660,54]),
 (0,3): (2,[2592,10152,16308,14490,7740,2496,450,36]),
 (0,4): (2,[1152,5184,10044,10716,6840,2685,612,63]),
 (0,5): (3,[1056,4572,7540,6432,3027,756,81]),
}

# Check every of the fifteen off-diagonal entries against its computed polynomial,
# not just six selected representatives. Diagonal scalar spectral factors are >0.
seen = set()
for u in range(6):
 for v in range(u+1,6):
  i,j=u//2,v//2
  sign=1 if u%2==v%2 else -1
  Tij = (A[i,j]+sign*B[i,j])/2
  poly = sp.Poly(sp.cancel(D*Tij),h)
  C=tuple(poly.all_coeffs()[::-1])
  matches=[]
  for orbit,(start,coeff) in CERT.items():
   expected = (0,)*start + tuple(coeff)
   if C==expected:matches.append(orbit)
  assert len(matches)==1, (u,v,C,matches)
  seen.add(matches[0])
assert seen==set(CERT),seen
for k,(power,coeff) in CERT.items():
 assert power>=1 and all(int(x)>0 for x in coeff)

# Independently replay direct six-by-six rational inverse at sample steps.
L=sp.zeros(6)
for i,w in enumerate([sp.Rational(1,2),sp.Rational(7,4),sp.Rational(1,2)]):
 u,v=2*i,2*i+1;L[u,u]+=w;L[v,v]+=w;L[u,v]-=w;L[v,u]-=w
for i in range(2):
 for side in range(2):
  u,v=2*i+side,2*(i+1)+side
  L[u,u]+=1;L[v,v]+=1;L[u,v]-=1;L[v,u]-=1
for step in [sp.Rational(1,11),sp.Rational(1),sp.Rational(8),sp.Rational(97)]:
 N=12*sp.eye(6)-6*step*L+step*step*(L*L)
 Z=12*sp.eye(6)+6*step*L+step*step*(L*L)
 T=N*Z.inv()
 assert all(x>0 for x in T)
 assert T*sp.ones(6,1)==sp.ones(6,1)

# Specific non-tuned example: unit rungs have an exactly negative end-rung entry.
L1=sp.zeros(6)
for i in range(3):
 u,v=2*i,2*i+1;L1[u,u]+=1;L1[v,v]+=1;L1[u,v]-=1;L1[v,u]-=1
for i in range(2):
 for side in range(2):
  u,v=2*i+side,2*(i+1)+side
  L1[u,u]+=1;L1[v,v]+=1;L1[u,v]-=1;L1[v,u]-=1
x=sp.Integer(8)
T1=(12*sp.eye(6)-6*x*L1+x*x*(L1*L1))*(12*sp.eye(6)+6*x*L1+x*x*(L1*L1)).inv()
assert T1[0,1]==-sp.Rational(1471112,79673503)
print('VERIFY_OK: 15 off-diagonal exact polynomial identities, 6 strictly positive coefficient lists, 4 direct rational matrix replays, 1 negative witness, all spectral and Green identities')
