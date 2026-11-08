#!/usr/bin/env python3
"""Standalone finite checks for sparse binary fair-allocation theorem.
All goods are labeled and represented by the tuple of agents approving them.
No external files or nonstandard modules are needed.
"""
from itertools import combinations, product
from fractions import Fraction
import random


def max_equal_utility(supports, n, d):
    assert n >= 3 and d >= 2
    assert all(1 <= len(z) <= 2 and len(set(z)) == len(z) for z in supports)
    assert all(sum(i in z for z in supports) == d for i in range(n))
    all_agents = range(n)
    counts = []
    for mask in range(1, 1 << n):
        z = {i for i in all_agents if (mask >> i) & 1}
        neighbors = sum(bool(z.intersection(s)) for s in supports)
        counts.append(neighbors // len(z))
    return min(counts)


def make_allocation(supports, n, t):
    """Maximal matching between goods and t copies of each agent."""
    slots = [(i, k) for i in range(n) for k in range(t)]
    approved_slots = [[idx for idx, (i, _) in enumerate(slots) if i in s]
                      for s in supports]
    matched_good = [-1] * len(slots)
    def augment(g, seen):
        for slot in approved_slots[g]:
            if slot in seen:
                continue
            seen.add(slot)
            if matched_good[slot] == -1 or augment(matched_good[slot], seen):
                matched_good[slot] = g
                return True
        return False
    for g in range(len(supports)):
        augment(g, set())
    assert all(g >= 0 for g in matched_good), 'Hall witness violated'
    owner = [-1] * len(supports)
    for slot, g in enumerate(matched_good):
        owner[g] = slots[slot][0]
    for g, support in enumerate(supports):
        if owner[g] == -1:
            owner[g] = next(i for i in range(n) if i not in support)
    return owner


def check_ef1_eq(supports, n, t, owner):
    assert len(supports) == len(owner)
    utility = [sum(owner[g] == i and i in s for g, s in enumerate(supports))
               for i in range(n)]
    assert utility == [t] * n, (utility, t)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            vi_j = sum(owner[g] == j and i in s for g, s in enumerate(supports))
            assert vi_j <= t + 1, (i, j, vi_j, t)
            if vi_j > t:
                assert any(owner[g] == j and i in s for g, s in enumerate(supports))
    return True


def instances(n, d):
    types = [tuple(z) for size in (1, 2) for z in combinations(range(n), size)]
    remain = [d] * n
    def generate(k, tup):
        if k == len(types):
            if all(x == 0 for x in remain):
                yield tuple(g for g, mult in zip(types, tup) for _ in range(mult))
            return
        z = types[k]
        for ct in range(min(remain[i] for i in z) + 1):
            for i in z:
                remain[i] -= ct
            yield from generate(k + 1, tup + (ct,))
            for i in z:
                remain[i] += ct
    yield from generate(0, ())


def density_formula(supports, n, d):
    e = [z for z in supports if len(z) == 2]
    lam = 0
    for mask in range(1, 1 << n):
        z = {i for i in range(n) if (mask >> i) & 1}
        ct = sum(set(g).issubset(z) for g in e)
        lam = max(lam, (ct + len(z) - 1) // len(z))
    return d - lam


def brute_max_equitable(supports, n):
    best = -1
    for assign in product(range(n), repeat=len(supports)):
        util = [sum(assign[g] == i and i in s for g, s in enumerate(supports))
                for i in range(n)]
        if len(set(util)) == 1:
            best = max(best, util[0])
    return best


def run():
    count = 0
    tight = 0
    for n, d in [(3, 2), (3, 3), (3, 4), (4, 2), (4, 3)]:
        h = d // 2
        bound = Fraction(n*d-2*(d-h)+1, n*h)
        max_found = Fraction(0)
        for supports in instances(n, d):
            t = max_equal_utility(supports, n, d)
            assert h <= t <= d
            assert t == density_formula(supports, n, d)
            lam = d - t
            if lam == 0:
                assert len(supports) == n*d
            else:
                assert len(supports) <= n*d-(2*lam-1)
            owners = make_allocation(supports, n, t)
            check_ef1_eq(supports, n, t, owners)
            ratio = Fraction(len(supports), n*t)
            assert ratio <= bound, (n,d,supports,ratio,bound)
            max_found = max(max_found, ratio)
            count += 1
        assert max_found == bound, (n,d,max_found,bound)
        tight += 1
        print(f'all multiplicity types n={n}, D={d}: sharp maximum ratio {max_found}')
    for n,d in [(3,2),(3,3),(3,4),(4,2)]:
        e = 2*(d-d//2)-1
        z = [(0,1)] * e
        for i in (0,1):
            z += [(i,)]*(d-e)
        for i in range(2,n):
            z += [(i,)]*d
        assert max_equal_utility(z,n,d)==d//2
        assert Fraction(len(z),n*(d//2)) == Fraction(n*d-e,n*(d//2))
    for n,d in [(3,2),(3,3),(3,4),(4,2),(4,3),(5,5)]:
        for lam in range(1,(d+1)//2+1):
            shared = 2*lam-1
            supports = [(0,1)]*shared
            for i in (0,1):
                supports += [(i,)]*(d-shared)
            for i in range(2,n):
                supports += [(i,)]*d
            assert density_formula(supports,n,d)==d-lam
            assert len(supports)==n*d-(2*lam-1)
    rng=random.Random(73114)
    trials=0
    for n,d in [(3,2),(3,3),(4,2)]:
        pool = list(instances(n,d))
        for supports in rng.sample(pool,min(len(pool),20)):
            assert max_equal_utility(supports,n,d) == brute_max_equitable(supports,n)
            trials+=1
    print(f'PASS: {count} normalized sparse instances, {tight} sharp cases, {trials} full allocation enumerations.')

if __name__ == '__main__':
    run()
