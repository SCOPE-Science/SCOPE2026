"""Exact-rational checks for geometric spectral polynomial extrapolation."""
from fractions import Fraction
from itertools import combinations

def weight(q, ks, i):
    a = q ** ks[i]
    out = Fraction(1)
    for j,k in enumerate(ks):
        if i != j:
            out *= (-q**k)/(a-q**k)
    return out

def spectral_lebesgue(q,ks):
    return sum((abs(weight(q,ks,i)) for i in range(len(ks))),Fraction(0))

def product(q,m):
    z=Fraction(1)
    for r in range(1,m):
        z *= (1+q**r)/(1-q**r)
    return z

def eval_weight(q,ks,i,n):
    x=q**n
    a=q**ks[i]
    z=Fraction(1)
    for j,k in enumerate(ks):
        if i!=j:z*=(x-q**k)/(a-q**k)
    return z

def proj_error(q,N,j):
    K=N-j
    numer=q**(K*(K+1)//2)
    denom=Fraction(1)
    for s in range(1,j+1):denom*=1-q**s
    for s in range(1,K+1):denom*=1-q**s
    return numer/denom

checks=0
for q in (Fraction(1,5),Fraction(1,2),Fraction(2,3)):
    for m in range(1,6):
        assert spectral_lebesgue(q,tuple(range(m)))==product(q,m);checks+=1
        for ks in combinations(range(10),m):
            if m>4:break
            W=[weight(q,ks,i) for i in range(m)]
            assert sum(W)==1;checks+=1
            assert [1 if w>0 else -1 for w in W] == [(-1)**(m-1-i) for i in range(m)];checks+=1
            L=spectral_lebesgue(q,ks)
            assert L<=product(q,m);checks+=1
            if m>=2:
                assert (L==product(q,m)) == all(ks[i+1]==ks[i]+1 for i in range(m-1));checks+=1
                assert L>1;checks+=1
            for n in range(ks[-1]+1,ks[-1]+4):
                assert sum(abs(eval_weight(q,ks,i,n)) for i in range(m))<L if m>=2 else True;checks+=1
    for N in range(1,9):
        for j in range(N+1):
            assert abs(weight(q,tuple(range(N+1)),j))==proj_error(q,N,j);checks+=1
print('GEOMETRIC_SPECTRAL_EXTRAPOLATION_EXACT_OK',checks)
