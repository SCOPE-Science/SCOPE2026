"""Exact algebra and sampled numerical diagnostics for fourth moments on SU(4).

Run: python su4_fourth_checker.py
No external dependencies except numpy and sympy.
"""
from fractions import Fraction as F
from math import isclose
import random
import sympy as s

# Two-pair unitary Weingarten inversion is independent of spectral optimization.
n=s.symbols('n',integer=True,positive=True)
G=s.Matrix([[n*n,n],[n,n*n]])
W=s.simplify(G.inv())
assert s.simplify(W[0,0]-1/(n*n-1))==0
assert s.simplify(W[0,1]+1/(n*(n*n-1)))==0

# Fourth tensor projector onto the alternating 4-tensor: contraction of the
# normalized epsilon tensor with A^(tensor 4) equals det(A), not 4! det(A).
import itertools
from math import factorial
perms=list(itertools.permutations(range(4)))
def sign(p):
 return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
for diag in [(1,1,1,1),(1,2,-3,4),(2,0,3,5),(-2,3,2,1)]:
 eps_sum=sum(sign(p)*sign(p)*diag[0]*diag[1]*diag[2]*diag[3]
             for p in perms)/factorial(4)
 assert eps_sum==diag[0]*diag[1]*diag[2]*diag[3]

rng=random.Random(2145003)
exact=0
for _ in range(12000):
 a=[F(rng.randint(-13,13),rng.randint(1,12)) for j in range(4)]
 if not any(a): continue
 p2=sum(t*t for t in a)
 p4=sum(t**4 for t in a)
 det=a[0]*a[1]*a[2]*a[3]
 r=p4/p2**2
 d=det/p2**2
 # Exact SU4 fourth moment ratio for diagonal Hermitian A.
 K=F(16,5)-F(4,5)*r+8*d
 assert F(12,5)<=K<=F(7,2)
 if sum(a)==0:
  assert r==F(1,2)-4*d
  assert K==F(14,5)+F(56,5)*d
  assert -F(1,48)<=d<=F(1,16)
  assert F(77,30)<=K<=F(7,2)
 exact+=1
assert exact==12000
# Exact endpoint spectra, normalized by Frobenius length.
def kurtosis(vals):
 p2=sum(F(x)**2 for x in vals)
 p4=sum(F(x)**4 for x in vals)
 det=F(1)
 for x in vals: det*=F(x)
 return F(16,5)-F(4,5)*p4/p2**2+8*det/p2**2
assert kurtosis([1,0,0,0])==F(12,5)
assert kurtosis([1,1,1,-3])==F(77,30)
assert kurtosis([1,1,-1,-1])==F(7,2)
assert kurtosis([1,1,1,1])==F(7,2)
assert kurtosis([1,1,1, -1])>F(12,5)
# Independent non-diagonal integer Levi-Civita contraction tests.
for _ in range(32):
    mat=s.Matrix([[rng.randint(-3,3) for j in range(4)] for i in range(4)])
    contraction=sum(sign(ip)*sign(jp)*s.prod(mat[ip[t],jp[t]] for t in range(4))
                    for ip in perms for jp in perms)/factorial(4)
    assert s.expand(contraction-mat.det())==0
print('WEINGARTEN_GRAM_AND_EPSILON_PROJECTOR_PASSED')
print('EXACT_RATIONAL_MATRIX_PROFILES_PASSED', exact)
print('SHARP_ENDPOINT_SPECTRA_PASSED')

import numpy as np
rng=np.random.default_rng(454388)
def samples(n, count):
 g=(rng.standard_normal((count,n,n))+1j*rng.standard_normal((count,n,n)))/np.sqrt(2)
 Q,R=np.linalg.qr(g)
 phases=np.diagonal(R,axis1=-2,axis2=-1)
 phases=phases/abs(phases)
 Q=Q*phases[:,None,:]
 det=np.linalg.det(Q)
 Q=Q/np.exp(1j*np.angle(det)/n)[:,None,None]
 return Q
Q=samples(4,48000)
for name, A, target in [
 ('full',np.eye(4),3.5),
 ('rank_one',np.diag([1,0,0,0]),2.4),
 ('traceless_min',np.diag([1,1,1,-3]),77/30),
 ('traceless_max',np.diag([1,1,-1,-1]),3.5),
 ('opposite_determinant',np.diag([1,1,1,-1]),kurtosis([1,1,1,-1]))
]:
 X=np.real(np.einsum('ij,tij->t',A.conj(),Q))
 estimate=float(np.mean(X**4)/np.mean(X**2)**2)
 print('SU4_MONTE_CARLO',name,'%.7f'%estimate,'expected %.7f'%float(target))
 assert abs(estimate-float(target)) < .20
# A genuinely nonnormal complex coefficient matrix tests determinant-phase dependence.
A=np.array([[1+2j,2,0,-1j],[-1,0,1+1j,0],
            [0,1j,2,1],[1,-2j,0,1]],dtype=complex)
S=float(np.sum(np.abs(A)**2))
B=A.conj().T@A
r=float(np.trace(B@B).real/S**2)
d=float(np.linalg.det(A).real/S**2)
pred=16/5-4*r/5+8*d
Y=np.real(np.einsum('ij,tij->t',A.conj(),Q))
est=float(np.mean(Y**4)/np.mean(Y**2)**2)
assert abs(est-pred)<.2
print('NONNORMAL_COMPLEX_DETERMINANT_PHASE_CHECK_PASSED',round(est,7),round(pred,7))
print('ALL_SU4_FOURTH_MOMENT_CHECKS_PASSED')
