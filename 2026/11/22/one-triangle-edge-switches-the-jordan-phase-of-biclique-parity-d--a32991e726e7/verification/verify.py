"""Finite independent checks for parity dynamics on a biclique with one inner edge.

Run: python3 verification/verify.py
Uses only the Python standard library. An exhaustive finite check does not prove
an all-size statement; the result's proof is algebraic.
"""
from collections import Counter, defaultdict


def neighbor_masks(a, b, defect=True):
    n = a + b
    masks = []
    for i in range(n):
        mask = 0
        if i < a:
            for j in range(a, n):
                mask |= 1 << j
        else:
            for j in range(a):
                mask |= 1 << j
        if defect:
            if i == 0:
                mask |= 1 << 1
            if i == 1:
                mask |= 1 << 0
        masks.append(mask)
    return masks


def step(x, masks):
    ans = 0
    for i, mask in enumerate(masks):
        ans |= ((x & mask).bit_count() & 1) << i
    return ans


def rank_vectors(vectors):
    basis = {}
    for v in vectors:
        while v:
            j = v.bit_length() - 1
            if j in basis:
                v ^= basis[j]
            else:
                basis[j] = v
                break
    return len(basis)


def target_ranks(a, b):
    n = a + b
    if a % 2 and b % 2:
        return (n, 4, 4, 4, 4, 4)
    if not (a % 2) and not (b % 2):
        return (n, 4, 2, 2, 2, 2)
    return (n, 4, 3, 2, 2, 2)


def expected(a, b):
    n = a+b
    if a % 2 and b % 2:
        return {1:2, 2:2, 4:12}, {0:16, 1: (1<<n)-16}, 4
    if not a % 2 and b % 2:
        return {1:4}, {0:4, 1:(1<<(n-2))-4, 2:(1<<(n-2)), 3:(1<<(n-1))}, 2
    if a % 2 and not b % 2:
        return {1:2, 2:2}, {0:4, 1:(1<<(n-2))-4, 2:(1<<(n-2)), 3:(1<<(n-1))}, 2
    return {1:2, 2:2}, {0:4, 1:(1<<(n-2))-4, 2:3*(1<<(n-2))}, 2


def finite_functional_graph(masks):
    size = 1 << len(masks)
    next_state = [step(x, masks) for x in range(size)]
    answer = {}
    cycle_members = {}
    for origin in range(size):
        if origin in answer:
            continue
        trail = []
        position = {}
        y = origin
        while y not in answer and y not in position:
            position[y] = len(trail)
            trail.append(y)
            y = next_state[y]
        if y in position:
            prefix = position[y]
            cyc = frozenset(trail[prefix:])
            period = len(cyc)
            for j, state in enumerate(trail):
                answer[state] = (max(prefix-j, 0), period, cyc)
        else:
            mu, period, cyc = answer[y]
            for j, state in enumerate(trail):
                answer[state] = (mu + len(trail)-j, period, cyc)
    return answer


def main():
    checks = 0
    tested = 0
    for a in range(3, 13):
        for b in range(2, 13):
            n = a+b
            masks = neighbor_masks(a, b)
            vectors = [1<<i for i in range(n)]
            actual = []
            for t in range(6):
                actual.append(rank_vectors(vectors))
                vectors = [step(v, masks) for v in vectors]
            assert tuple(actual) == target_ranks(a, b), (a,b,actual)
            checks += 6
            if n <= 12:
                orbit = finite_functional_graph(masks)
                period_counts, entry_counts = Counter(), Counter()
                basins = defaultdict(int)
                direct_periodic = defaultdict(set)
                for state,(mu,period,cyc) in orbit.items():
                    period_counts[period] += mu==0
                    entry_counts[mu] += 1
                    basins[cyc] += 1
                    if mu == 0:
                        direct_periodic[period].add(state)
                expected_period, expected_entry, stable_dim = expected(a,b)
                assert dict(period_counts) == expected_period, (a,b,period_counts,expected_period)
                assert dict(entry_counts) == expected_entry, (a,b,entry_counts,expected_entry)
                assert sum(len(c) for c in basins) == sum(expected_period.values())
                for cyc,basin_size in basins.items():
                    assert basin_size == len(cyc) * (1 << (n-stable_dim)), (a,b,cyc,basin_size)
                checks += 3 + len(basins)
                tested += 1
    # A contrasting boundary: the unedited graph has no nonzero recurrent
    # state as soon as at least one shore has even cardinality.
    for a,b in [(3,4),(4,3),(4,4),(5,6),(6,5),(5,5)]:
        graph=finite_functional_graph(neighbor_masks(a,b,defect=False))
        periodic={state for state,(entry,period,_) in graph.items() if entry==0}
        assert len(periodic) == (4 if a%2 and b%2 else 1)
        checks += 1
    print('VERIFY_OK parameter_pairs=110 exhaustive_graphs=',tested,'checks=',checks)

if __name__ == '__main__':
    main()
