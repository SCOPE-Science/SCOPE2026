#!/usr/bin/env python3
"""Independent finite permutation enumeration of a record--interior-peak covariance law.

Run: python3 verify.py
All comparisons use exact rational arithmetic.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def predicted(j, i):
    if i == j-1:
        return Fraction(2-j, 3*(j*j-1))
    if i == j:
        return Fraction(2*j-1, 3*j*(j+1))
    if i == j+1:
        return -Fraction(1, 3*(j+1))
    return Fraction(0)


def check(n):
    record = [0]*n
    peak = [0]*n
    mixed = [[0]*n for _ in range(n)]
    total_r=total_p=total_rr=total_pp=total_rp=0
    for pi in permutations(range(1,n+1)):
        high = 0
        a = []
        for v in pi:
            high = max(high,v)
            a.append(int(v == high))
        b = [0]*n
        for j in range(1,n-1):
            b[j] = int(pi[j-1]<pi[j]>pi[j+1])
        r=sum(a); p=sum(b)
        total_r+=r; total_p+=p; total_rr+=r*r; total_pp+=p*p; total_rp+=r*p
        for i in range(n):
            record[i]+=a[i]
            if a[i]:
                for j in range(1,n-1):
                    mixed[i][j]+=b[j]
        for j in range(1,n-1):
            peak[j]+=b[j]
    N=factorial(n)
    checks=0
    for i in range(n):
        for j in range(1,n-1):
            actual=Fraction(mixed[i][j],N)-Fraction(record[i]*peak[j],N*N)
            expected=predicted(j+1,i+1)
            assert actual == expected,(n,i,j,actual,expected)
            checks+=1
    covariance=Fraction(total_rp,N)-Fraction(total_r*total_p,N*N)
    expected=Fraction((n-2)*(n+1),12*n*(n-1))
    assert covariance == expected,(n,covariance,expected)
    checks+=1
    vr=Fraction(total_rr,N)-Fraction(total_r*total_r,N*N)
    hr=sum((Fraction(1,k) for k in range(1,n+1)),Fraction(0))
    hr2=sum((Fraction(1,k*k) for k in range(1,n+1)),Fraction(0))
    assert vr == hr-hr2
    checks+=1
    vp=Fraction(total_pp,N)-Fraction(total_p*total_p,N*N)
    if n>=4:
        assert vp==Fraction(2*(n+1),45)
        checks+=1
    print(f'n={n}: {N} permutations; {checks} exact assertions; covariance={covariance}; peak_variance={vp}')
    return N,checks

if __name__ == '__main__':
    N=C=0
    for n in range(3,9):
        a,b=check(n)
        N+=a;C+=b
    print(f'PASS total {N} permutations; {C} exact assertions')
