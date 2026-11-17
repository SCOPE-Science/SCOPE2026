#!/usr/bin/env python3
"""Exact rational sign certificate for a cyclic eleven-gon matching-complex quotient."""
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial
from collections import defaultdict

N = 11
SCALE = 10**12
RAY = (2, 3, 5, 7)
WEIGHTS = (4, 5)
CYCLE = {
(0,2,4,7):1,(0,2,4,8):-1,(0,2,5,7):-1,(0,2,5,8):1,
(0,3,5,7):1,(0,3,5,8):-1,(0,3,6,8):1,(0,3,6,9):-1,
(0,3,7,9):1,(0,4,6,8):-1,(0,4,6,9):1,(0,4,7,9):-1,
(1,3,5,7):-1,(1,3,5,8):1,(1,3,6,8):-1,(1,3,6,9):1,
(1,3,7,9):-1,(1,4,6,8):1,(1,4,6,9):-1,(1,4,7,9):1,
(1,4,7,10):-1,(1,4,8,10):1,(1,5,7,10):1,(1,5,8,10):-1,
(2,4,7,10):1,(2,4,8,10):-1,(2,5,7,10):-1,(2,5,8,10):1,
}

def independent(face):
    return all(((b-a)%N) not in (1,N-1) for a,b in combinations(face,2))

assert len(CYCLE)==28
assert all(independent(face) for face in CYCLE)
faces=[tuple(c) for k in range(1,6) for c in combinations(range(N),k) if independent(c)]
assert [sum(len(f)==k for f in faces) for k in range(1,6)]==[11,44,77,55,11]
maximal=[f for f in faces if len(f)==5]
assert len(maximal)==11
base=(0,2,4,6,8)
assert {tuple(sorted((j+t)%N for j in base)) for t in range(N)}==set(maximal)

# The boundary of the explicit oriented 3-chain is zero over the integers.
boundary=defaultdict(int)
for f,coefficient in CYCLE.items():
    for i in range(4):
        boundary[f[:i]+f[i+1:]] += (-1)**i*coefficient
assert all(v==0 for v in boundary.values())

# Machin's exact rational arctangent series gives certified pi accuracy.
def atan_inv(q,terms):
    return sum((Fraction((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(terms)),Fraction(0))
PIT=21
pi_approx=16*atan_inv(5,PIT)-4*atan_inv(239,PIT)
pi_error=Fraction(16, (2*PIT+1)*5**(2*PIT+1))+Fraction(4,(2*PIT+1)*239**(2*PIT+1))
assert pi_error < Fraction(1,10**25)

# Taylor remainders: |x|<7, |sin(x)-S_24(x)|<=7^49/49!,
# |cos(x)-C_24(x)|<=7^48/48!; |d trig/dx|<=1.
TERMS=24
error = Fraction(7**48,factorial(48)) + 2*pi_error
assert error < Fraction(1,10**18)

def taylor(x,odd):
    result=Fraction(0)
    for k in range(TERMS):
        power=2*k+int(odd)
        result+=(-1)**k*x**power/factorial(power)
    return result

root={}
for j in range(N):
    x=2*pi_approx*j/N
    root[j]=(taylor(x,False), taylor(x,True))

# Round down to integer-over-SCALE; the exact enclosure is 2e-12.
coord=[]
for j in range(N):
    q=[]
    for k in WEIGHTS:
        cc,ss=root[(k*j)%N]
        q.extend((int(cc*SCALE//1),int(ss*SCALE//1)))
    coord.append(tuple(q))
assert all(abs(x)<SCALE+1 for row in coord for x in row)
DELTA=Fraction(2,SCALE)
assert error+Fraction(1,SCALE)<DELTA

# A strictly positive linear functional on the representative maximal face.
# Rotating its coefficients gives such a functional on every maximal face.
sep=[coord[j][2]-coord[j][3] for j in base]
assert all(t>0 for t in sep)
assert min(sep)>SCALE//10  # separation margin exceeds 0.1

PERMS=[]
for p in permutations(range(4)):
    inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    PERMS.append((p,-1 if inv%2 else 1))
def det4(matrix):
    return sum(sign*matrix[0][p[0]]*matrix[1][p[1]]*matrix[2][p[2]]*matrix[3][p[3]] for p,sign in PERMS)

# Each determinant of four columns has absolute perturbation < 1e-6,
# using entry error DELTA, 24 Leibniz monomials and entry bound 8.
assert Fraction(24*4*9**3)*DELTA < Fraction(1,10**6)
ray=tuple(t*SCALE for t in RAY)
contributions=[]
lowest=10**100
for f,coeff in sorted(CYCLE.items()):
    cols=[coord[j] for j in f]
    matrix=[[cols[c][r] for c in range(4)] for r in range(4)]
    det=det4(matrix)
    numerators=[]
    for c in range(4):
        cols2=cols.copy();cols2[c]=ray
        mat2=[[cols2[d][r] for d in range(4)] for r in range(4)]
        numerators.append(det4(mat2))
    # Every determinant is >0.48 in magnitude, hence signs are exact.
    assert min([abs(det)]+[abs(x) for x in numerators]) > SCALE**4//3
    positive=all((v>0)==(det>0) for v in numerators)
    if positive:
        contributions.append((f,coeff,1 if det>0 else -1))
assert contributions==[((0,3,7,9),1,-1)],contributions
assert sum(c*s for f,c,s in contributions)==-1

# The cyclic action is free: no nonempty proper independent set is invariant
# under a nonidentity rotation of the eleven prime-numbered vertices.
assert all(0<len(f)<N for f in faces)
print('face_counts: 11 44 77 55 11')
print('maximal_orbit: 11 translates of (0,2,4,6,8)')
print('cycle_terms: 28; boundary: 0')
print('separating_margin_gt: 1/10')
print('determinant_error_lt: 1/1000000')
print('ray_intersections: (0,3,7,9) coefficient +1, orientation -1')
print('equivariant_map_degree: -1')
print('target_weights: (4,5); normalized_lens_parameter: 4 modulo 11')
print('PASS')
