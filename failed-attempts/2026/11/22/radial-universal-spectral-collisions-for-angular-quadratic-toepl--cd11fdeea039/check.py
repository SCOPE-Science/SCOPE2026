#!/usr/bin/env python3
"""Finite exact checks for angular quadratic Toeplitz compressions.
These checks support, but cannot replace, the analytical proof.
"""
from fractions import Fraction
from math import comb
from itertools import product
from math import factorial


def occupations(d):
    return [(a, b, d-a-b) for a in range(d+1) for b in range(d-a+1)]


def expected_count(d, q):
    return comb(d+2,2) - (comb(d-q+2, 2) if d>=q else 0)


def spectrum_count(d,p,q):
    return len({p*a+q*b for a,b,_ in occupations(d)})

count = 0
for q in range(2, 21):
    for p in range(1,q):
        from math import gcd
        if gcd(p,q)!=1: continue
        for d in range(0, 2*q+3):
            assert spectrum_count(d,p,q)==expected_count(d,q),(p,q,d)
            count+=1

# Spherical angular integral normalized by surface Haar probability:
# integral_{S^5} |w_1|^(2a) |w_2|^(2b) |w_3|^(2c) dS
#       = 2! a! b! c! / (a+b+c+2)!.
def sphere_moment(exponent):
    return Fraction(2 * factorial(exponent[0])*factorial(exponent[1])*factorial(exponent[2]),
                    factorial(sum(exponent)+2))

for d in range(0, 7):
    for alpha in occupations(d):
        for i in range(3):
            bump = tuple(alpha[j]+int(j==i) for j in range(3))
            assert sphere_moment(bump)/sphere_moment(alpha)==Fraction(alpha[i]+1,d+3)
            count += 1
        for i in range(3):
            for j in range(3):
                if i!=j and alpha[j]>0:
                    beta = list(alpha);beta[j]-=1;beta[i]+=1
                    bump = tuple(alpha[h]+int(h==i) for h in range(3))
                    assert sphere_moment(bump)/sphere_moment(beta)==Fraction(alpha[j], d+3)
                    count+=1

# Conjugate diagonal/triangular matrix's trace and nilpotent part identity.
# We compare a direct monomial integral action (rational arithmetic) with
# algebraic differential-operator formula for nonsymmetric matrices.
from sympy import Matrix, Rational, eye, Symbol, simplify

def matrix_direct(M,d):
    occ=occupations(d)
    loc={x:i for i,x in enumerate(occ)}
    Z=Matrix.zeros(len(occ))
    k=3
    for j,alpha in enumerate(occ):
        for i in range(k):
            for l in range(k):
                if i==l:
                    Z[j,j]+= M[i,l]*Rational(alpha[i]+1,d+k)
                elif alpha[l]>0:
                    beta=list(alpha); beta[l]-=1; beta[i]+=1
                    Z[loc[tuple(beta)],j]+=M[i,l]*Rational(alpha[l],d+k)
    return Z

def matrix_derived(M,d):
    occ=occupations(d); loc={x:i for i,x in enumerate(occ)}
    Z=Matrix.zeros(len(occ))
    for j,alpha in enumerate(occ):
        Z[j,j]+= M.trace()
        for i in range(3):
            for l in range(3):
                if alpha[l]>0:
                    beta=list(alpha); beta[l]-=1; beta[i]+=1
                    Z[loc[tuple(beta)],j]+=M[i,l]*alpha[l]
    return Z/(d+3)

for M in [Matrix([[2,3,0],[0,1,4],[1,0,5]]),
          Matrix([[0,1,0],[0,0,1],[0,0,0]]),
          Matrix([[0,2,0],[2,3,1],[0,1,5]])]:
    for d in range(5):
        assert matrix_direct(M,d)==matrix_derived(M,d)
        count+=1

# Nilpotent 3-Jordan block: precise order on all homogeneous blocks.
M=Matrix([[0,1,0],[0,0,1],[0,0,0]])
for d in range(0,7):
    X=matrix_derived(M,d)
    assert X**(2*d+1)==Matrix.zeros(X.rows)
    if d>0:
        assert X**(2*d)!=Matrix.zeros(X.rows)
    count+=1

# rational spectrum via exact charpoly and diagonal test, avoiding floats
for lambdas in [(0,1,5),(0,2,5),(0,1,2),(2,2,5)]:
    M=Matrix.diag(*lambdas)
    for d in range(5):
        X=matrix_direct(M,d)
        occ=occupations(d)
        diag={sum((a+1)*l for a,l in zip(alpha,lambdas)) for alpha in occ}
        observed={X[i,i]*(d+3) for i in range(X.rows)}
        assert diag==observed
        count+=1
print(f'PASS: {count} finite exact assertions; not an infinite proof')
