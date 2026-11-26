#!/usr/bin/env python3
"""Exact rational and algebraic checks for the eight-point quadratic phaseless sampling theorem.

Requires Python 3 and SymPy. No external files or network access.
The general-radius injectivity statement is proved analytically in RESULT.md;
this program checks the independent canonical finite-dimensional computations.
"""
from sympy import I, Matrix, Rational, sqrt, simplify, conjugate, zeros

S = [1,I,-1,-I,1+I,-1+I,-1-I,1-I]

# Frobenius-orthonormal real basis of Hermitian 3-by-3 matrices.
B = []
for j in range(3):
    h = zeros(3)
    h[j,j] = 1
    B.append(h)
for j,k in [(0,1),(1,2),(0,2)]:
    h=zeros(3);h[j,k]=h[k,j]=1/sqrt(2)
    B.append(h)
    h=zeros(3);h[j,k]=I/sqrt(2);h[k,j]=-I/sqrt(2)
    B.append(h)

def eval_hermitian(H,z):
    return simplify(sum(H[j,k]*z**j*conjugate(z)**k for j in range(3) for k in range(3)))

A=Matrix([[simplify(eval_hermitian(H,z)/2) for H in B] for z in S])
assert A.shape==(8,9)
assert A.rank()==8
expected_kernel=Matrix([2,-3,1,0,0,0,0,0,0])
assert A*expected_kernel==zeros(8,1)
assert A.nullspace()[0]==expected_kernel

G=A*A.T
expected={
    12-sqrt(130):1,
    12+sqrt(130):1,
    6-sqrt(34):2,
    6+sqrt(34):2,
    Rational(2):1,
    Rational(8):1,
}
assert G.eigenvals()==expected, (G.eigenvals(),expected)
assert (6-sqrt(34))>0
assert (12-sqrt(130))>(6-sqrt(34))

# Independent 4-point Fourier block decomposition of the lifted Gram spectrum.
D=Matrix([[1,1,1],[1,2,4]])
N=Matrix([[1,1],[sqrt(2),2*sqrt(2)]])
C=Matrix([[sqrt(2),0],[0,-2*sqrt(2)]])
assert (D*D.T).eigenvals()=={12-sqrt(130):1,12+sqrt(130):1}
assert (N*N.T).eigenvals()=={6-sqrt(34):1,6+sqrt(34):1}
assert (C*C.T).eigenvals()=={2:1,8:1}

# Polynomial intensity agrees exactly with the lifted Hermitian form.
for k in range(60):
    a=Matrix([(k+2)%9-4+I*((3*k+1)%11-5),
              (5*k+3)%13-6+I*((7*k+2)%9-4),
              (11*k+8)%17-8+I*((2*k+9)%13-6)])
    H=a*conjugate(a.T)
    for z in S:
        p=sum(a[j]*z**j for j in range(3))
        assert simplify(eval_hermitian(H,z)-p*conjugate(p))==0

# A rank-at-most-two Hermitian difference cannot be proportional to the
# rank-three kernel unless it is zero. Exact nullspace and inertia checks:
K=Matrix.diag(2,-3,1)
assert K.det()==-6
assert sum(abs(K[j,j])**2 for j in range(3))==14
assert min(abs(K[j,j]) for j in range(3))==1

print('PASS: exact Hermitian lifting; rank eight; one-dimensional full-rank kernel;')
print('      eight exact nonzero singular values with multiplicities;')
print('      60 coefficient triples times 8 exact intensity comparisons;')
print('      Fourier block spectra and rank-two separation parameters.')
