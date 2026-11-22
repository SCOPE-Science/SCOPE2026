#!/usr/bin/env python3
"""Exact finite checks of Kummer-phase carry-profiles; standard library only."""
from fractions import Fraction as Q
from math import gcd


def carry(d, j, x):
    return d * x.numerator // x.denominator - j * x.numerator // x.denominator - (d - j) * x.numerator // x.denominator


def cells(d, js):
    frequencies = sorted(set([Q(0), Q(1)] + [Q(k, v) for j in js for v in (d, j, d-j) for k in range(1, v)]))
    for u, v in zip(frequencies, frequencies[1:]):
        x = (u + v) / 2
        yield v-u, x


def check(d):
    s = 0
    m = d
    while m % 2 == 0:
        s += 1
        m //= 2
    assert s >= 1
    center = d // 2
    J = [j for j in range(1, d) if j % (2 ** s) == 0]
    total_by_profile = {}
    center1_by_profile = {}
    for mass, x in cells(d, [center] + J):
        profile = tuple(carry(d, j, x) for j in J)
        total_by_profile[profile] = total_by_profile.get(profile, Q(0)) + mass
        if carry(d, center, x):
            center1_by_profile[profile] = center1_by_profile.get(profile, Q(0)) + mass
    for profile, mass in total_by_profile.items():
        assert center1_by_profile.get(profile,Q(0))*2==mass, (d,profile)
    assert sum(total_by_profile.values(), Q(0)) == 1
    checks=0
    for j in range(1,d):
        b = d//gcd(d,j)
        a = j//gcd(d,j)
        covariance = Q(0) if b%2 else Q(1,4*a*(b-a))
        joint={(0,0):Q(0),(0,1):Q(0),(1,0):Q(0),(1,1):Q(0)}
        for mass,x in cells(d,[center,j]):
            key=(carry(d,center,x),carry(d,j,x))
            assert key in joint
            joint[key]+=mass
        for e in [0,1]:
            for f in [0,1]:
                expected=Q(1,4)+(1 if e==f else -1)*covariance
                assert joint[e,f]==expected, (d,j,e,f,joint,expected)
                checks+=1
    return checks,len(total_by_profile)


def main():
    total=0
    profiles=0
    for d in range(2,102,2):
        n,k=check(d)
        total+=n
        profiles+=k
    print(f'PASS: {total} exact two-by-two joint-probability checks over 50 even denominators (2..100).')
    print(f'PASS: {profiles} exact nonempty vector-profile conditional-independence checks.')
    print('All rational discontinuity cells checked, not a sample of points.')

if __name__=='__main__':
    main()
