"""Independent finite checks for EF1 on vertex-weighted stars.

Run: python3 verify.py
Only finite instances are checked. The general mathematical claims require the written proof.
"""
from itertools import product, combinations
from math import factorial
from random import Random


def ef1_connected_allocation(weights, assignment, n):
    """Direct definition; vertex 0 is the center of the star."""
    k = len(weights) - 1
    groups = [set() for _ in range(n)]
    for v, agent in enumerate(assignment):
        groups[agent].add(v)
    if any(not x for x in groups):
        return False
    if any(0 not in x and len(x) > 1 for x in groups):
        return False
    for i in range(n):
        left = sum(weights[v] for v in groups[i])
        for j in range(n):
            if i == j:
                continue
            if not any(left >= sum(weights[v] for v in groups[j] if v != g)
                       for g in groups[j]):
                return False
    return True


def predicted_feasible(weights, n):
    k = len(weights) - 1
    assert 1 <= n <= k + 1
    if n == 1:
        return True
    leaves = sorted(weights[1:])
    c = k - n + 1
    hub_bundle = [weights[0]] + leaves[:c]
    return sum(hub_bundle) - max(hub_bundle) <= leaves[c]


def exhaustive_count(weights, n):
    return sum(ef1_connected_allocation(weights, mapping, n)
               for mapping in product(range(n), repeat=len(weights)))


def weights_for_pattern(bits):
    """bits[c-2] is feasibility at c centered leaves, c=2,...,k-1."""
    leaves = [2, 3]
    for allowed in bits:
        leaves.append(sum(leaves) if allowed else leaves[-1] + 1)
    # For k leaves the target bitstring length is k-2; append final leaf.
    center = sum(leaves) + 1
    return [center] + leaves


def test():
    count = 0
    checked_profiles = 0
    rng = Random(21843)
    for k in range(1, 6):
        cases = [[rng.randint(0, 18) for _ in range(k + 1)] for _ in range(16)]
        for weights in cases:
            checked_profiles += 1
            for n in range(1, k + 2):
                actual = exhaustive_count(weights, n) > 0
                expected = predicted_feasible(weights, n)
                assert actual == expected, (k, n, weights, actual, expected)
                count += 1

    words = 0
    comparisons = 0
    for k in range(3, 11):
        for bits in product((False, True), repeat=k - 2):
            weights = weights_for_pattern(bits)
            assert len(weights) == k + 1
            assert all(weights[i] < weights[i+1] for i in range(1, k))
            assert weights[0] > sum(weights[1:])
            assert predicted_feasible(weights, 1)
            assert predicted_feasible(weights, k)
            assert predicted_feasible(weights, k + 1)
            for c in range(2, k):
                n = k - c + 1
                expected = bits[c - 2]
                assert predicted_feasible(weights, n) == expected
                # Count all candidate center-leaf sets via direct EF1 definition.
                feasible_sets = 0
                for inds in combinations(range(1, k + 1), c):
                    center_bundle = set(inds) | {0}
                    singles = [i for i in range(1, k + 1) if i not in center_bundle]
                    assignment = [0] * (k + 1)
                    for label, vertex in enumerate(singles, start=1):
                        assignment[vertex] = label
                    if ef1_connected_allocation(weights, assignment, n):
                        feasible_sets += 1
                assert feasible_sets == int(expected), (k, bits, c, feasible_sets)
                comparisons += 1
            words += 1

    example = [19, 2, 3, 4, 9]
    assert [exhaustive_count(example, n) for n in range(1, 6)] == [1, 2, 0, 24, 120]
    print('VERIFIED: direct labeled-partition EF1 tests:', count)
    print('VERIFIED: sampled nonnegative common-weight profiles:', checked_profiles)
    print('VERIFIED: arbitrary-pattern words:', words)
    print('VERIFIED: direct candidate-center-subset checks:', comparisons)
    print('VERIFIED: 5-vertex witness labeled counts: [1, 2, 0, 24, 120]')

if __name__ == '__main__':
    test()
