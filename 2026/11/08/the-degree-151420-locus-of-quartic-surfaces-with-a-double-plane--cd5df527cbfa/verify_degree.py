#!/usr/bin/env python3
"""Two exact, independent computations of the double-conic quartic locus degree.
No third-party dependencies; run with Python >= 3.9.
"""
from fractions import Fraction
from itertools import combinations_with_replacement
from math import comb

# Polynomial on two generators h,k: dictionary (i,j) -> coefficient.
def mul(A, B, bound=8):
    out = {}
    for (i,j), a in A.items():
        for (u,v), b in B.items():
            if i+j+u+v <= bound:
                out[i+u,j+v] = out.get((i+u,j+v),0) + a*b
    return out

def lin_pow_negative(ah,ak,r,limit=8):
    # (1 - (ah*h+ak*k))^(-r)
    d={}
    for n in range(limit+1):
        for j in range(n+1):
            d[(n-j,j)] = comb(r+n-1,n)*comb(n,j)*ah**(n-j)*ak**j
    return d

S={(0,0):1,(1,0):-2,(0,1):-1}  # numerator 1-2h-k
S=mul(S, lin_pow_negative(2,0,10))
S=mul(S, lin_pow_negative(1,1,4))
S=mul(S, lin_pow_negative(0,2,1))
weights=[(S.get((8-j,j),0), j) for j in range(5,9)]
assert weights == [(579040,5),(139412,6),(22992,7),(1981,8)],weights
# Projective-bundle relation: pi_* k^(5+j) = s_j(Sym^2 U) = (-1)^j * binomial(4,j)*h^j.
deg1=sum(coef*((-1)**(j-5))*comb(4,j-5) for coef,j in weights)
assert deg1==151420,deg1
print('SEGRE_COEFFICIENTS',weights)
print('SEGRE_DEGREE',deg1)

# Independent torus localization on P(Sym^2 U) -> P^3.
# Fixed points: 4 coordinate planes, each with 6 coordinate quadratic forms.
W=(0,1,7,23)
mon4=list(combinations_with_replacement(range(4),4))
def wt(mon):return sum(W[v] for v in mon)
def s8(eweights):
    coefficients=[0]*9
    coefficients[0]=1
    for w in eweights:
        for m in range(1,9):
            coefficients[m]-=w*coefficients[m-1]
    return coefficients[8]
result=Fraction(0)
nfixed=0
for i in range(4):
    others=[j for j in range(4) if j!=i]
    quadrics=list(combinations_with_replacement(others,2))
    for quad in quadrics:
        # monomial basis of H0(I_(x_i,quad)^2(4)), dimension 14.
        basis=[m for m in mon4 if m.count(i)>=2 or
               (m.count(i)>=1 and all(m.count(j)>=quad.count(j) for j in others)) or
               all(m.count(j)>=2*quad.count(j) for j in others)]
        assert len(basis)==14
        denom=1
        for j in others:denom*=W[j]-W[i]
        for other_quad in quadrics:
            if other_quad!=quad:denom*=wt(other_quad)-wt(quad)
        assert denom
        result+=Fraction(s8([wt(m) for m in basis]),denom)
        nfixed+=1
assert nfixed==24
assert result.denominator==1 and int(result)==151420,(result,deg1)
print('LOCALIZATION_FIXED_POINTS',nfixed)
print('LOCALIZATION_DEGREE',result)
print('ALL_CHECKS_PASSED')
