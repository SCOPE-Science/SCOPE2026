"""Finite consistency checks for bounded-difference-support pattern bounds.

The infinite theorem is proved symbolically in RESULT.md; these finite
checks test the incidence inequality and the independent dyadic witness.
"""
from collections import Counter
from itertools import combinations


def difference_capacity(support):
    differences = Counter(b - a for a, b in combinations(sorted(support), 2))
    return max(differences.values(), default=0)


def spectrum(support, sample, max_shift=90):
    return {sum(s + n in support for s in sample) for n in range(max_shift)}


def inequality_holds(k, observed, g):
    r = max(0, len(observed) - 2)
    if not r:
        return True
    return 2 * k * ((2 * g + 1) * r + 3 - 2 * g) >= r * (r + 3) ** 2


cases = 0
for support in (
    {2**j for j in range(13)},
    {3**j for j in range(9)},
    {1, 2, 3, 5, 8, 13},
    {0, 2, 5, 9, 14},
):
    g = difference_capacity(support)
    for k in range(1, 7):
        for sample in combinations(range(12), k):
            observed = spectrum(support, sample)
            assert inequality_holds(k, observed, g), (support, sample, observed)
            cases += 1
print('finite_profile_tests=', cases)

powers = {2**j for j in range(20)}
assert difference_capacity(powers) == 1
S = (0, 2, 4, 6, 8, 16)
counts = [sum(n+s in powers for s in S) for n in range(5)]
assert counts == [4, 1, 3, 0, 2], counts
# If six distinct counts occurred with k=6 and g=1, r=4 would imply 6>=98/13.
assert not inequality_holds(6, set(range(6)), 1)
print('dyadic_six_pattern=', S, 'shift_counts=', counts)
print('exact_dyadic_complexity_at_6=5 (lower witness + universal upper bound)')
print('VERIFY_OK')
