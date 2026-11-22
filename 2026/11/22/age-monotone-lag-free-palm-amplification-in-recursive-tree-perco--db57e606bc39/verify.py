"""Reproduce exact labelled-vertex Palm amplification for a percolated recursive tree.

Run: python3 verify.py
Only the Python standard library is needed.
"""
from itertools import product
from fractions import Fraction
from math import factorial


def a(m, p):
    z = Fraction(1)
    for t in range(1, m):
        z *= 1 + p / t
    return z


def b(m, p):
    z = Fraction(1)
    for t in range(1, m):
        z *= 1 + 2 * p / t
    return z


def amplifier(j, p):
    return 2 * b(j-1, p) / (a(j-1, p)*a(j, p))


def expected_member(j, p):
    return p*a(j-1,p)/(j-1)


def exact_pair(j, k, p):
    return expected_member(j,p)*expected_member(k,p)*amplifier(j,p)


def census(n):
    # For every recursion-parent vector and retention subset, store the number
    # of assignments with a given count of retained bonds (polynomial in p).
    z = n-1
    marginal = [[0]*(z+1) for _ in range(n+1)]
    pairs = [[[0]*(z+1) for _ in range(n+1)] for _ in range(n+1)]
    weighted_sum = [[0]*(z+1) for _ in range(n+1)]
    totals = [0]*(z+1)
    for parent in product(*(range(1, j) for j in range(2, n+1))):
        for mask in range(1 << z):
            present=[False]*(n+1)
            present[1]=True
            bits=mask.bit_count()
            for j in range(2,n+1):
                present[j]=bool((mask>>(j-2))&1) and present[parent[j-2]]
            size=sum(present)
            totals[bits]+=1
            for j in range(2,n+1):
                if not present[j]: continue
                marginal[j][bits]+=1
                weighted_sum[j][bits]+=size
                for k in range(j+1,n+1):
                    if present[k]:pairs[j][k][bits]+=1
    assert totals == [factorial(z)*__import__('math').comb(z,s) for s in range(z+1)]
    return marginal,pairs,weighted_sum


def evalpoly(counts,n,p):
    return sum((Fraction(v,factorial(n-1))*p**s*(1-p)**(n-1-s)
                for s,v in enumerate(counts)), Fraction(0))


def check(n,p):
    mar,pairs,weighted_sum=census(n)
    asserts=0
    for j in range(2,n+1):
        assert evalpoly(mar[j],n,p)==expected_member(j,p);asserts+=1
        assert evalpoly(weighted_sum[j],n,p)==expected_member(j,p)*amplifier(j,p)*a(n,p);asserts+=1
        for k in range(j+1,n+1):
            assert evalpoly(pairs[j][k],n,p)==exact_pair(j,k,p);asserts+=1
    for j in range(2,n):
        r=amplifier(j,p)
        assert r>1
        assert amplifier(j+1,p)/r==1+p*(1-p)/((j-1+p)*(j+p))
        asserts+=2
    return asserts


def main():
    nchecks=0
    for n,p in [(4,Fraction(1,3)),(5,Fraction(2,3)),
                (6,Fraction(1,3)),(7,Fraction(1,2)),(8,Fraction(1,2))]:
        nchecks+=check(n,p)
        print('verified',n,'vertices, p=',p)
    print('PASS:',nchecks,'symbolic/rational assertions, exhaustive through n=8')

if __name__=='__main__':main()
