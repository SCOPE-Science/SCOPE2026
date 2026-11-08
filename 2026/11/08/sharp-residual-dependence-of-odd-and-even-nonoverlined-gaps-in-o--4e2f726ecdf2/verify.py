#!/usr/bin/env python3
"""Finite checks for a two-color nonoverlined-gap theorem in overpartitions.
Symbolic asymptotics and infinite covariance law are mathematical, not computational assertions.
"""
from fractions import Fraction
from math import pi, sqrt
from collections import Counter


def overpartition_numbers(limit):
    # Independent generating-function multiplication, ordinary/overlined choices.
    coeff = [0] * (limit + 1)
    coeff[0] = 1
    for part in range(1, limit + 1):
        for weight in range(part, limit + 1):
            coeff[weight] += coeff[weight - part]
        for weight in range(limit, part - 1, -1):
            coeff[weight] += coeff[weight - part]
    return coeff


def partitions(n, biggest=None):
    if biggest is None: biggest=n
    if n == 0:
        yield ()
    else:
        for first in range(min(biggest,n), 1 - 1, -1):
            for rem in partitions(n-first,first):
                yield (first,) + rem


def direct_survival(n,r,s):
    answer = 0
    for parts in partitions(n):
        distinct = sorted(set(parts))
        for mask in range(1 << len(distinct)):
            overlined = {d for j,d in enumerate(distinct) if mask >> j & 1}
            # Even with an overlined instance, nonoverlined instances may remain.
            available = {d for d in distinct if parts.count(d) > (d in overlined)}
            if all(2*j - 1 in available for j in range(1,r+1)) and all(2*j in available for j in range(1,s+1)):
                answer += 1
    return answer


def count(p,index):
    return p[index] if 0<=index<len(p) else 0


def covariance(p,n):
    total=p[n]
    odd=sum((2*r-1)*count(p,n-r*r) for r in range(1,int(sqrt(n))+3))
    even=sum((2*s-1)*count(p,n-s*(s+1)) for s in range(1,int(sqrt(n))+3))
    both=sum((2*r-1)*(2*s-1)*count(p,n-r*r-s*(s+1))
        for r in range(1,int(sqrt(n))+3) for s in range(1,int(sqrt(n))+3))
    return Fraction(both*total-odd*even,total*total)


def main():
    p=overpartition_numbers(3000)
    tests=0
    for n in range(0,13):
        for r in range(0,4):
            for s in range(0,4):
                expected=count(p,n-r*r-s*(s+1))
                actual=direct_survival(n,r,s)
                assert actual==expected,(n,r,s,actual,expected)
                tests+=1
    print('DIRECT_NONOVERLINED_JOINT_BIJECTION_OK',tests,'independent finite overpartition enumerations')
    checks=0
    for n in range(0,3001):
        for r in (1,2,3,4,5,10):
            A=r*r
            for s in (1,2,3,4,5,10):
                B=s*(s+1)
                assert count(p,n-A-B)*p[n] <= count(p,n-A)*count(p,n-B),(n,r,s)
                checks+=1
    print('FINITE_NEGATIVE_QUADRANT_TESTS_OK',checks)
    for n in (100,400,900,1600,3000):
        cv=float(covariance(p,n))
        print('SQUARED_GAP_COVARIANCE',n,'normalized',format(cv/sqrt(n),'.9f'))
    print('LIMIT_PREDICTION',format(-4/pi**3,'.9f'))
    print('FINITE_CHECKS_ONLY_TRUE; INFINITE_PROOF_SEPARATE_TRUE; INDEPENDENT_AUDIT_FALSE')


if __name__=='__main__': main()
