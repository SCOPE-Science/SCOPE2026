"""Exact cyclotomic verifier for dyadic three-by-three Fourier minor ranks.
No floating point arithmetic or external packages are used.
"""
from itertools import combinations, permutations
from math import comb
from fractions import Fraction


def valuation(x,k):
    x = x % (1<<k)
    assert x
    return (x & -x).bit_length()-1


def signature(T,k):
    vs=sorted(valuation(b-a,k) for a,b in combinations(T,2))
    assert vs[0]==vs[1]<vs[2]
    return vs[0],vs[2]


def predict(ra,co,k):
    a,b=signature(ra,k)
    c,d=signature(co,k)
    return 1 if a+c>=k else 2 if (b+c>=k or a+d>=k) else 3


def cyclotomic_determinant_zero(R,C,k):
    n=1<<k; half=n//2
    coeff=[0]*half
    for perm in permutations(range(3)):
        inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        sign=(-1)**inv
        e=sum(R[i]*C[perm[i]] for i in range(3))%n
        if e>=half: coeff[e-half]-=sign
        else:coeff[e]+=sign
    return not any(coeff)


def closed_counts(k):
    n=1<<k
    rank1 = (Fraction(n**2,9)+Fraction(k*n**3,8)
             +(Fraction(k,48)-Fraction(1,9))*n**4)
    singular = (Fraction(n**5,12)
                +(Fraction(5,36)-Fraction(13*k,96)-Fraction(k*k,32))*n**4
                -Fraction(n**3,3)+Fraction(n**2,9))
    assert rank1.denominator==singular.denominator==1
    return int(rank1),int(singular-rank1),comb(n,3)**2-int(singular)


def valuation_census(k):
    M={(a,b):1<<(3*k-a-b-3) for a in range(k) for b in range(a+1,k)}
    observed=[0,0,0]
    for (a,b),u in M.items():
        for (c,d),v in M.items():
            rk=1 if a+c>=k else (2 if b+c>=k or a+d>=k else 3)
            observed[rk-1]+=u*v
    return tuple(observed)

for k in range(2,14):
    assert valuation_census(k)==closed_counts(k),(k,valuation_census(k),closed_counts(k))

for k in [3,4]:
    n=1<<k
    triples=list(combinations(range(n),3))
    observed=[0,0,0]
    for R in triples:
        for C in triples:
            rank=predict(R,C,k)
            assert (rank<3)==cyclotomic_determinant_zero(R,C,k),(k,R,C,rank)
            if rank==1:
                assert all((r-R[0])*(c-C[0])%n==0 for r in R for c in C)
            observed[rank-1]+=1
    assert tuple(observed)==closed_counts(k)
    print('exact_DFT',n,'rank_counts',observed)
print('DYADIC_THIRD_ORDER_FOURIER_MINOR_CHECKS_OK')
