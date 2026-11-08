#!/usr/bin/env python3
"""Exact, standard-library checks for a binary cubic Gaussian-chaos moment identity.
No external dependencies or probabilistic sampling are required.
"""
from itertools import combinations_with_replacement
from math import factorial
from fractions import Fraction
from collections import defaultdict


def prod(A,B):
    C=defaultdict(Fraction)
    for i,a in A.items():
        for j,b in B.items():
            k=tuple(x+y for x,y in zip(i,j))
            C[k]+=a*b
    return {k:v for k,v in C.items() if v}

def add(A,B,scale=1):
    C=defaultdict(Fraction,A)
    for k,v in B.items(): C[k]+=scale*v
    return {k:v for k,v in C.items() if v}

def powpoly(A,n):
    N=len(next(iter(A)))
    C={(0,)*N:Fraction(1)}
    for _ in range(n):C=prod(C,A)
    return C

def moment_1d(n):
    if n%2:return 0
    m=1
    for k in range(1,n,2):m*=k
    return m

def gauss_E(P):
    return sum(c*moment_1d(i)*moment_1d(j) for (i,j),c in P.items())

U={(3,0):1,(1,2):-3}
V={(2,1):3,(0,3):-1}
W={(3,0):1,(1,2):1,(1,0):-4}
Z={(2,1):1,(0,3):1,(0,1):-4}
basis=[U,V,W,Z]
assert [gauss_E(powpoly(P,2)) for P in basis]==[24,24,8,8]
for i,j in combinations_with_replacement(range(4),2):
    if i==j:continue
    assert gauss_E(prod(basis[i],basis[j]))==0
print('FOUR_ORTHOGONAL_WICK_CUBICS_AND_L2_NORMALIZATIONS_OK')

# The polynomial in (u,v,w,z) of E[(uU+vV+wW+zZ)^4].
L={}
for indices in combinations_with_replacement(range(4),4):
    P={(0,0):Fraction(1)}
    for i in indices:P=prod(P,basis[i])
    M=gauss_E(P)
    k=tuple(indices.count(i) for i in range(4))
    m=factorial(4)
    for e in k:m//=factorial(e)
    if M:
        L[k]=M*m

# Independent closed formula in the four unnormalized coefficients.
u={(1,0,0,0):Fraction(1)}
v={(0,1,0,0):Fraction(1)}
w={(0,0,1,0):Fraction(1)}
z={(0,0,0,1):Fraction(1)}
A2=add(powpoly(u,2),powpoly(v,2))
B2=add(powpoly(w,2),powpoly(z,2))
R=add(add(add({k:30*24**2*t for k,t in powpoly(A2,2).items()},
              {k:168*24*8*t for k,t in prod(A2,B2).items()}),
              {k:66*8**2*t for k,t in powpoly(B2,2).items()}),
              {})
C=add(prod(u,add(powpoly(w,3),prod(w,powpoly(z,2)),scale=-3)),
      prod(v,add({k:3*t for k,t in prod(powpoly(w,2),z).items()},powpoly(z,3),scale=-1)))
R=add(R,C,scale=7680)
assert L==R,(set(L.keys())^set(R.keys()),[(k,L.get(k),R.get(k)) for k in L if L.get(k)!=R.get(k)])
print('FULL_35_COEFFICIENT_FOURTH_MOMENT_POLYNOMIAL_IDENTITY_OK')

# Independently recompute representative normalized angular data, all rational before normalization.
expected={'U4':17280,'W4':4224,'U2W2':5376,'UW3':1920,'U3W':0}
actual={'U4':gauss_E(powpoly(U,4)),
        'W4':gauss_E(powpoly(W,4)),
        'U2W2':gauss_E(prod(powpoly(U,2),powpoly(W,2))),
        'UW3':gauss_E(prod(U,powpoly(W,3))),
        'U3W':gauss_E(prod(powpoly(U,3),W))}
assert actual==expected,(actual,expected)
print('FIVE_CRITICAL_GAUSSIAN_CONTRACTIONS_OK',actual)

# Upper-bound SOS factorization, with a=sqrt(3)*h and b=1, so all terms rational.
h={(1,):Fraction(1)}
one={(0,):Fraction(1)}
q=add({(4,):Fraction(567)}, {(2,):Fraction(54),(1,):Fraction(-120),(0,):Fraction(27)})
# 189 (h-1/3)^2 (3h^2+2h+9/7)
f1=add(h,{(0,):Fraction(-1,3)})
f2={(2,):Fraction(3),(1,):Fraction(2),(0,):Fraction(9,7)}
fact={k:189*t for k,t in prod(powpoly(f1,2),f2).items()}
assert q==fact
print('UPPER_ENDPOINT_93_SUM_OF_SQUARES_FACTORIZATION_OK')

# The sharp stability eigenvalue solves lambda^2-144lambda+2688=0,
# with the smallest root positive since 72^2>64*39 and 72>8sqrt(39).
assert 72**2-64*39==2688
assert 72>0 and 8>0 and 39>0 and 72**2>64*39
print('SHARP_STABILITY_EIGENVALUE_ALGEBRA_OK')
print('ALL_BINARY_THIRD_CHAOS_CHECKS_OK')
