#!/usr/bin/env python3
"""Independent finite-state verification of three-site path adsorption.

Python standard library only. Numerical simulations are optional diagnostics;
mathematical asymptotics are established in the accompanying proof.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import sqrt
import random


def reduced(a, b):
    @lru_cache(None)
    def solve(a, b):
        if a == 0 or b == 0 or a + b < 3:
            return {a + b: Fraction(1)}
        out = defaultdict(Fraction)
        den = a + b - 2
        if b >= 2:
            for r, p in solve(a - 1, b - 2).items():
                out[r] += Fraction(b - 1, den) * p
        if a >= 2:
            for r, p in solve(a - 2, b - 1).items():
                out[r] += Fraction(a - 1, den) * p
        return dict(out)
    return solve(a, b)


def labelled(a, b):
    vertices_a = tuple(range(a))
    vertices_b = tuple(range(a, a + b))
    paths = []
    for i, j in combinations(vertices_a, 2):
        for k in vertices_b:
            paths.append((1 << i) | (1 << j) | (1 << k))
    for i, j in combinations(vertices_b, 2):
        for k in vertices_a:
            paths.append((1 << i) | (1 << j) | (1 << k))
    @lru_cache(None)
    def solve(occupied):
        available = [p for p in paths if p & occupied == 0]
        if not available:
            return {a + b - occupied.bit_count(): Fraction(1)}
        out = defaultdict(Fraction)
        for p in available:
            for r, prob in solve(occupied | p).items():
                out[r] += prob / len(available)
        return dict(out)
    return solve(0), len(paths), solve.cache_info().currsize


def check_all():
    cases = 0
    for a in range(1, 5):
        for b in range(1, 5):
            p, edge_count, states = labelled(a, b)
            q = reduced(a, b)
            assert p == q, (a, b, p, q)
            assert sum(p.values()) == 1
            assert edge_count == a * b * (a + b - 2) // 2
            cases += 1
    print('labeled versus reduced finite-state distribution: PASS', cases, 'cases')

    identities = 0
    for a in range(1, 100):
        for b in range(1, 100):
            if a+b < 4: continue
            den = a + b - 2
            plus = Fraction(b-1, den)
            minus = Fraction(a-1, den)
            d = a - b
            assert plus + minus == 1
            assert plus*(d+1)+minus*(d-1) == Fraction(d*(a+b-3), a+b-2)
            variance = plus*(1 + Fraction(d,den))**2 + minus*(-1+Fraction(d,den))**2
            assert variance == 1 - Fraction(d*d,den*den)
            identities += 1
    print('drift and variance identities: PASS', identities, 'states')

    rng = random.Random(157491)
    trials = 3000
    for n, mu_shift in [(512, 0), (2048, 0), (2048, 90)]:
        s0 = 2*n+mu_shift
        end=[]
        for _ in range(trials):
            a=n+mu_shift
            b=n
            while a>0 and b>0 and a+b>=3:
                if rng.random() < (b-1)/(a+b-2):
                    a-=1;b-=2
                else:
                    a-=2;b-=1
            end.append((a+b)/s0**.25)
        avg=sum(end)/trials
        print('diagnostic', 'a',n+mu_shift,'b',n,'scaled survivor mean',round(avg,5),'(not a proof)')
    print('ALL FINITE CHECKS PASS')


if __name__ == '__main__':
    check_all()
