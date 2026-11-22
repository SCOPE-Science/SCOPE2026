#!/usr/bin/env python3
"""Exact finite checks for size-marked block-minimum statistics of uniform set partitions.

Run: python3 check.py
Standard library only.  This checks exact identities, not asymptotic convergence.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb


def bell_numbers(n):
    b=[1]
    for k in range(n):
        b.append(sum(comb(k,j)*b[j] for j in range(k+1)))
    return b


def partitions(n):
    if n == 0:
        yield ()
        return
    def rec(word, high):
        if len(word) == n:
            blocks=[[] for _ in range(high+1)]
            for i, c in enumerate(word,1):
                blocks[c].append(i)
            yield tuple(tuple(x) for x in blocks)
            return
        for j in range(high+2):
            yield from rec(word+[j], max(high,j))
    yield from rec([0],0)


def actual_count(partition,r,lo,hi):
    return sum(len(b)==r and lo<=b[0]<=hi for b in partition)


def exact_mean(n,r,lo,hi,B):
    if r>n: return Fraction(0)
    cnt=comb(n-lo+1,r)-comb(n-hi,r)
    return Fraction(cnt*B[n-r],B[n])


def all_allowed_blocks(n,r,lo,hi):
    return [frozenset(t) for t in combinations(range(1,n+1),r) if lo<=t[0]<=hi]


def exact_product(n,r,A,s,C,B, factorial=False):
    left=all_allowed_blocks(n,r,*A)
    right=all_allowed_blocks(n,s,*C)
    cnt=sum(not (a & b) for a in left for b in right) if r+s<=n else 0
    disjoint=Fraction(cnt*B[n-r-s],B[n]) if r+s<=n else Fraction(0)
    diagonal=Fraction(len(set(left)&set(right))*B[n-r],B[n]) if r==s and not factorial else Fraction(0)
    return disjoint+diagonal


def main():
    checks=0
    B=bell_numbers(9)
    assert B[:9]==[1,1,2,5,15,52,203,877,4140]
    checks+=1
    for n in range(2,9):
        P=list(partitions(n))
        assert len(P)==B[n]
        checks+=1
        ranges=sorted(set([(1,n),(1,max(1,n//2)),(max(1,n-2),n)]))
        sample={}
        for r in range(1,min(3,n)+1):
            for A in ranges:
                v=[actual_count(p,r,*A) for p in P]
                sample[(r,A)]=v
                actual=Fraction(sum(v),B[n])
                wanted=exact_mean(n,r,*A,B)
                assert actual==wanted,(n,r,A,actual,wanted)
                checks+=1
        for r in range(1,min(3,n)+1):
            for s in range(1,min(3,n)+1):
                for A,C in product(ranges,repeat=2):
                    X=sample[(r,A)]
                    Y=sample[(s,C)]
                    factorial=r==s and A==C
                    num=sum(x*y-(x if factorial else 0) for x,y in zip(X,Y))
                    actual=Fraction(num,B[n])
                    wanted=exact_product(n,r,A,s,C,B,factorial)
                    assert actual==wanted, (n,r,A,s,C,actual,wanted)
                    checks+=1
    print(f'PASS: {checks} exact identities and partition-count checks, n=2..8')
    print('Finite checks do not certify point-process or extremal asymptotics.')


if __name__=='__main__':
    main()
