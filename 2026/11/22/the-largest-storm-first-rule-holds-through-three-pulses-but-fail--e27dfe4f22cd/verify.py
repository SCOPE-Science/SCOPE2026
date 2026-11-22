"""Exact rational supplementary checks for finite three-storm ordering."""
from fractions import Fraction as F
from itertools import permutations, combinations_with_replacement


def runoff(order, q, capacity):
    storage = F(0)
    total = F(0)
    for amount in order:
        before_spill = q * storage + amount
        total += max(F(0), before_spill - capacity)
        storage = min(capacity, before_spill)
    return total


def state(order, q, capacity):
    storage = F(0)
    total = F(0)
    states = []
    for amount in order:
        before_spill = q * storage + amount
        total += max(F(0), before_spill - capacity)
        storage = min(capacity, before_spill)
        states.append(storage)
    return total, states


def check():
    count = 0
    # Exact, not floating-point, exhaustive checks on this bounded parameter grid.
    for q in (F(1,5), F(1,4), F(1,3), F(1,2), F(2,3), F(3,4), F(4,5)):
        for capacity in (F(1,2), F(1), F(3,2), F(2), F(3), F(4), F(5)):
            for triple in combinations_with_replacement((F(0), F(1,4), F(1,2), F(1), F(3,2), F(2), F(3), F(4)), 3):
                lo, md, hi = triple
                values = [runoff(p, q, capacity) for p in set(permutations(triple))]
                best_with_hi_first = min(runoff(p, q, capacity) for p in set(permutations(triple)) if p[0] == hi)
                assert best_with_hi_first == min(values), (triple, q, capacity)
                count += 1
                assert runoff((hi, md, lo), q, capacity) <= runoff((lo, md, hi), q, capacity)
                count += 1
                assert runoff((hi, lo, md), q, capacity) <= runoff((lo, hi, md), q, capacity)
                count += 1
    four = (F(1), F(11), F(12), F(13))
    q = F(1,4); capacity = F(14)
    values = {p: runoff(p, q, capacity) for p in permutations(four)}
    assert min(values.values()) == F(1,8)
    assert [p for p in values if values[p] == F(1,8)] == [(F(12),F(11),F(1),F(13))]
    assert min(v for p, v in values.items() if p[0] == F(13)) == F(1,4)
    count += 3
    mass_bal = 0
    for p in permutations(four):
        R, S = state(p, q, capacity)
        assert R == sum(p) - (1-q)*sum(S[:-1]) - S[-1]
        mass_bal += 1
    count += mass_bal
    print(f"PASS: {count} exact rational assertions; four-pulse optimum 1/8 vs largest-first 1/4")

if __name__ == '__main__':
    check()
