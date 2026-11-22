#!/usr/bin/env python3
"""Exact modular Burnside enumeration for index-six permutation-polynomial QM classes.

Requires Python 3 standard library only. The definitions follow the root-value
model and fixed-point congruences in Fan, arXiv:2611.16944, Theorems 2.3 and 4.2.
"""
from itertools import permutations, product
from math import gcd, isqrt

PERMS = [(0,) + z for z in permutations((1, 2, 3, 4, 5))]
DIVISORS = ((1, 1), (2, -1), (3, -1), (6, 1))

# Six interpolation samples plus one extra independent control, per residue.
PRIME_S = {
    1: (1, 13, 25, 37, 61, 73, 121),
    2: (2, 26, 38, 62, 110, 122, 146),
    3: (3, 27, 51, 63, 87, 123, 135),
    4: (16, 40, 52, 76, 100, 112, 172),
    5: (5, 17, 77, 101, 125, 137, 161),
    6: (6, 18, 30, 66, 90, 102, 126),
    7: (7, 55, 91, 103, 115, 151, 175),
    8: (32, 56, 68, 128, 188, 200, 248),
    9: (21, 33, 45, 81, 105, 153, 165),
    10: (10, 46, 58, 70, 118, 142, 166),
    11: (11, 23, 35, 47, 83, 95, 107),
    12: (12, 72, 96, 156, 168, 192, 216),
}

def prime(n):
    if n < 2: return False
    return all(n % d for d in range(2, isqrt(n) + 1))

def cycles(perm):
    seen = set()
    out = []
    for x in range(len(perm)):
        if x not in seen:
            orbit = []
            v = x
            while v not in seen:
                seen.add(v)
                orbit.append(v)
                v = perm[v]
            out.append(orbit)
    return out

def nu(s, exponents, k, t, delta, d, c):
    m = 6 // d
    if k * (1 + c*s) % d:
        return 0
    if any((exponents[(j+m)%6] - exponents[j] - s*c*m) % 6
           for j in range(6)):
        return 0
    kt = k*(1+c*s) % 6
    rho = [(exponents[j]-c*s*j) % 6 for j in range(m)]
    perm = [(t+delta*j) % m for j in range(m)]
    b = []
    for j in range(m):
        numerator = s*kt*j-rho[j]+rho[perm[j]]-rho[t % m]
        assert numerator % 6 == 0
        b.append(numerator // 6)
    cs = cycles(perm)
    if not any(all((len(C)*y-sum(b[j] for j in C)) % s == 0
                   for C in cs) for y in range(s)):
        return 0
    return s**(len(cs)-1)*gcd(s, *(len(C) for C in cs))

def count_classes(s):
    group = [(k,t,(1+k*s)%6) for k in range(6) for t in range(6)
             if gcd(1+k*s,6)==1]
    fixed_sum = 0
    for sigma in PERMS:
        exponents = [(sigma[j]-j)%6 for j in range(6)]
        for k,t,delta in group:
            alpha = [(t+delta*j)%6 for j in range(6)]
            if any((sigma[alpha[j]]-sigma[t]-sigma[j])%6 for j in range(6)):
                continue
            for d, mobius in DIVISORS:
                fixed_sum += mobius * sum(
                    nu(s,exponents,k,t,delta,d,c) for c in range(d))
    assert fixed_sum % len(group) == 0
    return fixed_sum // len(group)

def predicted(s):
    if s%3:
        if s%2:
            num, den = 60*s**5+8*s*s-3*s+1,6
        elif s%4:
            num, den = 60*s**5+16*s*s-3*s+2,12
        else:
            num, den = s*(20*s**4+16*s-1),4
    elif s%2:
        num, den = 120*s**5-8*s*s+27*s-9,18
    elif s%4:
        num, den = 120*s**5-16*s*s+27*s-18,36
    else:
        num, den = s*(40*s**4+9),12
    assert num%den == 0
    return num//den

def brute_orbits(s):
    # Independent orbit-closure check, feasible for s=1,2,3.
    group = [(k,t,(1+k*s)%6) for k in range(6) for t in range(6)
             if gcd(1+k*s,6)==1]
    universe = set()
    for sigma in PERMS:
        e = [(sigma[j]-j)%6 for j in range(6)]
        for xs in product(range(s),repeat=5):
            U = (0,) + tuple(e[j]+6*xs[j-1] for j in range(1,6))
            # Exclude coefficient supports in a single residue class mod 2 or 3.
            if any(all((U[(j+6//d)%6]-U[j]-c*(6//d)*s)%(6*s)==0
                       for j in range(6))
                   for d in (2,3) for c in range(d)):
                continue
            universe.add(U)
    count = 0
    while universe:
        U = next(iter(universe))
        orbit = {tuple((k*j*s + U[(t+delta*j)%6]-U[t])%(6*s)
                       for j in range(6)) for k,t,delta in group}
        assert orbit <= universe
        universe.difference_update(orbit)
        count += 1
    return count

def main():
    for residue, samples in PRIME_S.items():
        assert len(samples)==7 and len(set(samples))==7
        for j,s in enumerate(samples):
            assert s % 12 == residue % 12
            assert prime(6*s+1)  # exact trial division of each interpolation field size
            got=count_classes(s)
            assert got==predicted(s), (residue,j,s,got,predicted(s))
        print('residue',residue,'six prime checks plus control pass')
    for s in (1,2,3):
        assert brute_orbits(s)==count_classes(s)
    print('INDEX6_SHARP_QUASIPERIOD_OK 72_prime_interpolations 12_extra_prime_controls 3_direct_orbit_checks')

if __name__=='__main__':main()
