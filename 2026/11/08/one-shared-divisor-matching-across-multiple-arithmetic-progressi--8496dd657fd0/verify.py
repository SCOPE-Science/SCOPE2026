#!/usr/bin/env python3
"""Exact finite checks of a two-progression divisor matching theorem."""
from itertools import permutations, product
from math import gcd
from fractions import Fraction

D = (1, 5, 7, 35)
# All four-symbol forbidden-prime masks, no assumption of arithmetic progression.
for masks in product(range(4), repeat=4):
    A = sum(bool(m & 1) for m in masks)
    B = sum(bool(m & 2) for m in masks)
    AB = sum(bool(m) for m in masks)
    C = sum(m == 3 for m in masks)
    criterion = A <= 2 and B <= 2 and AB <= 3 and C <= 1
    brute = any(all(not (m & dm) for m, dm in zip(masks, perm))
                for perm in permutations((0, 1, 2, 3)))
    assert criterion == brute, (masks, criterion, brute)
print('HALL_ALL_PATTERNS_OK 256')

for prime in (5, 7, 11):
    counts = {}
    for a in range(prime):
        for b in range(prime):
            if a == b == 0: continue
            z = sum(1 << t for t in range(4) if (a+b*t) % prime == 0)
            counts[z] = counts.get(z, 0)+1
    assert counts.get(0) == (prime-1)*(prime-3)
    assert all(counts.get(1 << t) == prime-1 for t in range(4))
    assert sum(counts.values()) == prime*prime-1
    assert len(counts) == 5
print('LOCAL_PRIMITIVE_RESIDUES_OK 5 7 11')

# Independent enumeration of every primitive residue pair mod 35 and every
# ordered pair of progressions; this computes the density, not sampling.
mod = 35
pairs = []
for a in range(mod):
    for b in range(mod):
        if gcd(a,b,mod)!=1: continue
        P = sum(1 << t for t in range(4) if (a+b*t)%5==0)
        Q = sum(1 << t for t in range(4) if (a+b*t)%7==0)
        pairs.append((P,Q))
assert len(pairs) == (5*5-1)*(7*7-1)
fail = 0
for p1,q1 in pairs:
    for p2,q2 in pairs:
        U = p1 | p2
        V = q1 | q2
        fail += int(U.bit_count() == 2 and V.bit_count() == 2
                    and (U & V).bit_count() != 1)
all_cases = len(pairs)**2
assert fail == all_cases//48, (fail,all_cases)
assert Fraction(fail, all_cases) == Fraction(48, (5+1)**2 * (7+1)**2)
print('CRT_ALL_PRIMITIVE_QUADRUPLES_OK', all_cases, 'fail', fail,
      'success_density', 1-Fraction(fail,all_cases))

# Two constructive failure mechanisms; every progression individually primitive.
for A,B in (((35,1),(34,1)), ((5,1),(4,1))):
    assert all(gcd(a,b)==1 for a,b in (A,B))
    masks = [((1 if (A[0]+A[1]*t)*(B[0]+B[1]*t)%5==0 else 0) |
              (2 if (A[0]+A[1]*t)*(B[0]+B[1]*t)%7==0 else 0))
             for t in range(4)]
    assert not any(all(not(m&dm) for m,dm in zip(masks,perm))
                   for perm in permutations((0,1,2,3)))
    assert all(any(all(gcd(x,d)==1 for x,d in zip(
                   (a+b*t for t in range(4)),perm))
                   for perm in permutations(D)) for a,b in (A,B))
print('INDEPENDENT_PRIMITIVE_BUT_NO_COMMON_MATCHING_OK')

from math import comb

def closed_density(p,q,k):
    def W2(r):
        return Fraction((r-1)**k - 2*(r-2)**k + (r-3)**k, (r+1)**k)
    def U(r):
        return Fraction(6*(r-1)**k - 8*(r-2)**k + 3*(r-3)**k, (r+1)**k)
    return U(p)*U(q) - 12*W2(p)*W2(q)

def local_dp(r,k):
    from collections import defaultdict
    weights=defaultdict(int)
    for a in range(r):
        for b in range(r):
            if a==b==0:continue
            mask=sum(1<<t for t in range(4) if (a+b*t)%r==0)
            weights[mask]+=1
    out={0:1}
    for _ in range(k):
        new=defaultdict(int)
        for mask,num in out.items():
            for root,weight in weights.items():
                new[mask|root] += num*weight
        out=new
    assert sum(out.values())==(r*r-1)**k
    return out

for p,q in ((5,7),(5,11),(7,11)):
    for k in range(1,8):
        d_p=local_dp(p,k)
        d_q=local_dp(q,k)
        good=0
        for maskp, wp in d_p.items():
            for maskq, wq in d_q.items():
                if (maskp.bit_count() <= 2 and maskq.bit_count() <= 2
                  and (maskp|maskq).bit_count() <= 3
                  and (maskp&maskq).bit_count() <=1):
                    good += wp*wq
        density=Fraction(good,(p*p-1)**k*(q*q-1)**k)
        assert density == closed_density(p,q,k),(p,q,k,density,closed_density(p,q,k))
print('ALL_ORDER_DENSITY_DP_OK p,q=(5,7),(5,11),(7,11); k=1..7')
for k in range(1,5):
    print('EXACT_DENSITY_5_7',k,closed_density(5,7,k))

print('VERIFY_OK exact_integer_and_rational=yes full_256_and_1327104_cases=yes')
