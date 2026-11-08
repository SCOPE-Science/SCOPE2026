"""Exact algebra and illustrative numerical checks for covariance quadrature order.
Run: python3 verify.py. Standard library only.
"""
from fractions import Fraction as F
from math import exp

def transpose(M): return [list(col) for col in zip(*M)]
def matmul(A,B): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def add(A,B): return [[x+y for x,y in zip(row1,row2)] for row1,row2 in zip(A,B)]
def scale(s,A): return [[s*x for x in row] for row in A]
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def outer(v): return [[x*y for y in v] for x in v]
def curvature(A,Q):
    At=transpose(A)
    return add(add(matmul(matmul(matmul(A,A),Q),eye(len(A))),matmul(Q,matmul(At,At))),scale(2,matmul(matmul(A,Q),At)))
def compare(A,a,b,Q):
    n=len(A)
    assert matmul(A,A)==add(scale(a,eye(n)),scale(b,A))
    C=add(A,scale(b/2,eye(n)))
    exact=curvature(A,Q)
    factor=add(scale(2,matmul(matmul(C,Q),transpose(C))),scale(2*a-b*b/2,Q))
    assert exact==factor

def defect_diagonal(lam,h):
    n=len(lam)
    return [[h/2*(1+exp((lam[i]+lam[j])*h)) - (exp((lam[i]+lam[j])*h)-1)/(lam[i]+lam[j]) if lam[i]+lam[j] else 0.0 for j in range(n)] for i in range(n)]

# Quadratic identity for the two safe non-scalar generators.
for A,a,b in [([[F(1),F(0)],[F(0),F(-2)]],F(2),F(-1)),
              ([[F(0),F(1)],[F(0),F(0)]],F(0),F(0))]:
    for v in [[F(1),F(0)],[F(1),F(1)],[F(2),F(-3)]]:
        compare(A,a,b,outer(v))

# Obstructed stable generator: Q=ones rank-one PSD, but curvature indefinite.
A=[[F(-1),F(0)],[F(0),F(-2)]]
H=curvature(A,outer([F(1),F(1)]))
assert H==[[F(4),F(9)],[F(9),F(16)]]
assert H[0][0]*H[1][1]-H[0][1]**2==F(-17)
for h in [0.1,0.05,0.02]:
    D=defect_diagonal([-1,-2],h)
    assert D[0][0]*D[1][1]-D[0][1]**2 < -1e-17, (h,D)

# The safe opposite-sign pair has a PSD defect on this rank-one input.
for h in [0.02,0.1,0.4,1.0,2.0]:
    D=defect_diagonal([1,-2],h)
    assert D[0][0]>=-1e-12 and D[1][1]>=-1e-12
    assert D[0][0]*D[1][1]-D[0][1]**2>=-1e-10

# 2x2 classification using Cayley-Hamilton: a=-det(A), b=tr(A).
for i in range(-2,3):
    for j in range(-2,3):
        A=[[F(i),F(0)],[F(0),F(j)]]
        if i==j: continue
        a,b=F(-i*j),F(i+j)
        assert (4*a>=b*b)==((i-j)**2 <= -8*i*j)

print('VERIFY_OK: exact factorization, negative stable witness, positive safe witnesses, 2x2 boundary')
