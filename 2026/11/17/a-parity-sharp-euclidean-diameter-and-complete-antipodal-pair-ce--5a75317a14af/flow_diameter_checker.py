"""Independent exhaustive and randomized checks for complete-ordered-DAG unit-flow diameters."""
from itertools import combinations
from math import comb
from random import Random


def path_edge_mask(N, interior_mask):
    nodes = [0] + [i + 1 for i in range(N - 2) if (interior_mask >> i) & 1] + [N - 1]
    bits = 0
    for a, b in zip(nodes, nodes[1:]):
        # Unique index for every directed arc a -> b, with a < b.
        index = a * (2 * N - a - 1) // 2 + (b - a - 1)
        bits |= 1 << index
    return bits


def predicted(N):
    squared_diameter = N + (N - 3) // 2
    k = N // 2
    number_of_unordered_pairs = (k - 1) * 2 ** (k - 1) if N % 2 == 0 else 2 ** (k - 1)
    return squared_diameter, number_of_unordered_pairs


def predicted_pair_support(N, a, b):
    # A direct independent derivation of the equality condition.
    m = N - 2
    full = (1 << m) - 1
    common = a & b
    if (a | b) != full:
        return False
    if common & 1 or common & (1 << (m - 1)):
        return False
    if common & (common << 1):
        return False
    return common.bit_count() == (N - 3) // 2


def exhaustive(N):
    paths = [path_edge_mask(N, s) for s in range(1 << (N - 2))]
    observed_max = -1
    observed_count = 0
    condition_count = 0
    for a in range(len(paths)):
        for b in range(a + 1, len(paths)):
            value = (paths[a] ^ paths[b]).bit_count()
            if value > observed_max:
                observed_max = value
                observed_count = 1
            elif value == observed_max:
                observed_count += 1
            if predicted_pair_support(N, a, b):
                condition_count += 1
                assert value == predicted(N)[0]
    expected_max, expected_count = predicted(N)
    assert (observed_max, observed_count, condition_count) == (
        expected_max, expected_count, expected_count), (N, observed_max, observed_count, condition_count)
    return len(paths) * (len(paths) - 1) // 2


def randomized():
    rng = Random(20261111)
    checks = 0
    for N in (17, 29, 51, 100, 155, 200):
        bound = predicted(N)[0]
        for _ in range(800):
            a = rng.getrandbits(N - 2)
            b = rng.getrandbits(N - 2)
            distance = (path_edge_mask(N, a) ^ path_edge_mask(N, b)).bit_count()
            assert distance <= bound
            if predicted_pair_support(N, a, b):
                assert distance == bound
            checks += 1
    return checks


if __name__ == "__main__":
    pairs = sum(exhaustive(N) for N in range(3, 14))
    random_checks = randomized()
    print(f"ORDERED_FLOW_DIAMETER_PASS N=3..13 exhaustive_pairs={pairs} random_large_pairs={random_checks}")
