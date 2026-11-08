#!/usr/bin/env python3
"""Exact arithmetic checks for four branch m-ary partition congruences."""
from math import gcd, comb


def coefficient_triple(m, a, b):
    A = m**6
    B_num = -m**4*((m-1)*(2*m+1)+2*a+2*b*m)
    assert B_num % 2 == 0
    B = B_num // 2
    C_num = m**3*(2*m**3+6*m*m*b-3*m*m+6*m*a-2*m+12*a*b-6*a-6*b+3)
    assert C_num % 12 == 0
    C = C_num // 12
    return A,B,C


def closed_gcd(m,a,b):
    base = m**3 // (4 if m%2 == 0 else 1)
    exceptional = (m%9==6 and a==b) or (m%9==3 and a!=b)
    return base*(3 if exceptional else 1)


def polynomial_value(m,a,b,n):
    A,B,C=coefficient_triple(m,a,b)
    return A*comb(n+2,3)+B*comb(n+1,2)+C*n


def partition_numbers(m, max_n):
    d = [0]*(max_n+1)
    d[0] = 1
    p=1
    while p<=max_n:
        for j in range(p,max_n+1):
            d[j] += d[j-p]
        p*=m
    return d


def main():
    for m in range(2,2001):
        for a in (0,1):
            for b in (0,1):
                A,B,C=coefficient_triple(m,a,b)
                g=gcd(gcd(A,B),C)
                assert g==closed_gcd(m,a,b), (m,a,b,g,closed_gcd(m,a,b))
                f=[polynomial_value(m,a,b,n) for n in (1,2,3)]
                assert gcd(gcd(f[0],f[1]),f[2]) == g
    print('FORMULA_CHECK_OK: 7,996 base-branch cases (m=2..2000)')
    trials=0
    for m in range(2,19):
        top=3*m**4-m
        d=partition_numbers(m,top)
        for a in (0,1):
            for b in (0,1):
                seq=[d[m**4*n-m-a*m*m-b*m**3] for n in (1,2,3)]
                assert gcd(gcd(seq[0],seq[1]),seq[2])==closed_gcd(m,a,b), (m,a,b,seq)
                trials+=1
        # Independent truncated recurrence via coin-change, excluding m^4 and higher.
        r=[0]*(3*m**4+1)
        r[0]=1
        for p in (1,m,m*m,m**3):
            for x in range(p,len(r)):
                r[x]+=r[x-p]
        for a in (0,1):
            for b in (0,1):
                for n in (1,2,3):
                    idx=m**4*n-m-a*m*m-b*m**3
                    assert r[idx]==polynomial_value(m,a,b,n), (m,a,b,n,idx,r[idx],polynomial_value(m,a,b,n))
    print(f'PARTITION_CHECK_OK: {trials} base-branch tests and {3*trials} exact coefficient comparisons (m=2..18)')
    for m in (2,3,4,6,12,15,21,24):
        print('SAMPLE',m,[closed_gcd(m,a,b) for a,b in ((0,0),(0,1),(1,0),(1,1))])

if __name__ == '__main__':
    main()
