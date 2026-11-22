#!/usr/bin/env python3
"""Independent exact run enumerator and two-marker formula checks."""
from itertools import combinations
from fractions import Fraction
from random import Random
from collections import Counter


def enumerate_runs(w):
    n = len(w)
    result = []
    for left in range(n):
        for right in range(left + 2, n + 1):
            t = w[left:right]
            for p in range(1, len(t)//2 + 1):
                if t[p:] != t[:-p]:
                    continue
                if left > 0 and w[left-1] == w[left-1+p]:
                    break
                if right < n and w[right] == w[right-p]:
                    break
                result.append((left,right,p))
                break
    return result


def predicted(a,b,c):
    if b == 0:
        return Fraction((a if a>=2 else 0)+(c if c>=2 else 0)+2)
    unary = sum(g if g>=2 else 0 for g in (a,b,c))
    p=b+1
    L=p+1+min(a,b)+min(c,b)
    return Fraction(unary) + (Fraction(L,p) if L>=2*p else 0)


def independent_exponent(w):
    return sum((Fraction(r-l,p) for l,r,p in enumerate_runs(w)), Fraction(0))

count=0
for n in range(2,26):
    vals=[]
    for i,j in combinations(range(n),2):
        a,b,c=i,j-i-1,n-1-j
        w='0'*a+'1'+'0'*b+'1'+'0'*c
        measured=independent_exponent(w)
        expect=predicted(a,b,c)
        assert measured==expect,(n,a,b,c,measured,expect,enumerate_runs(w))
        vals.append((measured,a,b,c))
        count+=1
    if n>=8:
        P=(n+1)//3
        bound=Fraction(n+1)-Fraction(1,P)
        maxima=[(a,b,c) for x,a,b,c in vals if x==bound]
        R=n-3*P+1
        target=[(P-1+i,P-1,P-1+R-i) for i in range(R+1)]
        assert set(maxima)==set(target),(n,maxima,target)
        assert max(x for x,_,_,_ in vals)==bound
    elif n>=4:
        assert max(x for x,_,_,_ in vals)==n
print(f'Exact independent interval-run checks: {count} binary words, all lengths 2..25; all verified.')

rng=Random(1731)
random_checks=0
for rep in range(1000):
    a,b,c=(rng.randrange(0,36) for _ in range(3))
    w='0'*a+'1'+'0'*b+'1'+'0'*c
    if len(w)>75:continue
    assert independent_exponent(w)==predicted(a,b,c)
    random_checks+=1
print(f'{random_checks} seeded random gap trials with length at most 75 passed.')

for n in (60,120,240,480,960):
    counts=Counter()
    total=0
    centered=[]
    for i,j in combinations(range(n),2):
        a,b,c=i,j-i-1,n-1-j
        y=predicted(a,b,c)-n
        counts['negative_two'] += int(y==-2)
        counts['near_positive_one'] += int(y>Fraction(9,10))
        centered.append(float(y))
        total+=1
    print(f'n={n}: P(Y=-2)={counts["negative_two"]/total:.6f}; P(Y>0.9)={counts["near_positive_one"]/total:.6f}; E[Y]={sum(centered)/total:.6f}')
print('Target weak-limit law: atoms 1/4 at -2, 1/3 at 1, and density 6/(2+y)^3 for 0<y<1.')
