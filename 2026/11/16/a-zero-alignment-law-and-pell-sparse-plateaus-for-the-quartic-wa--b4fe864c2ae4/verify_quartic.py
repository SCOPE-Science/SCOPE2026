#!/usr/bin/env python3
"""Exact-integer checks for the fourth Walsh-layer projection increment."""
from math import comb, isqrt
from fractions import Fraction


def krawtchouk(d, n, s):
    assert abs(s) <= n and (n - s) % 2 == 0
    neg = (n - s) // 2
    pos = n - neg
    return sum((-1)**j * comb(neg, j) * comb(pos, d-j)
               for j in range(max(0, d-pos), min(d, neg)+1))


def quartic(N, s):
    assert (s**4 - (6*N - 8)*s*s + 3*N*(N-2)) % 24 == 0
    return (s**4 - (6*N - 8)*s*s + 3*N*(N-2)) // 24


def exact_projection_norm(d, n):
    total = sum(comb(n, (n+s)//2)*abs(krawtchouk(d, n, s))
                for s in range(-n,n+1,2))
    return Fraction(total, 2**n)


def sign_change_increment(n):
    total=0
    for s in range(-n,n+1,2):
        left, right=quartic(n+1,s-1), quartic(n+1,s+1)
        if left*right<0:
            total += comb(n,(n+s)//2)*min(abs(left),abs(right))
    return Fraction(total, 2**n)


def pell_possible(N):
    D = 6*(2*N-3)**2+10
    z=isqrt(D)
    if z*z!=D: return False
    aa=(6*N-8-z)//2
    bb=(6*N-8+z)//2
    if aa<0 or (6*N-8-z)%2: return False
    a=isqrt(aa);b=isqrt(bb)
    return a*a==aa and b*b==bb and a%2==N%2 and b%2==N%2


def pell_orbit(seed, bound):
    z,m=seed
    while (m+3)//2<=bound:
        yield (m+3)//2,z,m
        z,m=5*z+12*m, 2*z+5*m


for n in range(4,301):
    N=n+1
    for s in range(-N,N+1,2):
        assert krawtchouk(4,N,s)==quartic(N,s)
    delta=exact_projection_norm(4,N)-exact_projection_norm(4,n)
    assert delta==sign_change_increment(n), (n,delta,sign_change_increment(n))
    assert (delta==0)==pell_possible(N), (n,delta)

# Each Pell candidate through 10^100 is checked with exact integer square roots.
bound=10**100
candidate_count=0
plateaus=[]
for seed in ((4,1),(8,3)):
    for N,z,m in pell_orbit(seed,bound):
        if N<5: continue
        candidate_count+=1
        if pell_possible(N):
            plateaus.append(N-1)
assert plateaus == [7], plateaus
assert exact_projection_norm(4,7)==exact_projection_norm(4,8)==Fraction(35,8)
print('QUARTIC_WALSH_INCREMENT_PASS exact_dimensions=4..300 pell_bound=10^100 '
      f'pell_candidates={candidate_count} certified_plateaus={plateaus}')
