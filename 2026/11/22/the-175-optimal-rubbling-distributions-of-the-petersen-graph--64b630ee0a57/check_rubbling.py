"""Exhaustive dynamic-programming certificate for four-pebble rubbling on KG(5,2).

Run: python3 check_rubbling.py
No nonstandard packages are required.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, permutations

pairs = tuple(combinations(range(5), 2))
position = {p: i for i, p in enumerate(pairs)}
neighbors = tuple(
    tuple(j for j, q in enumerate(pairs) if not (set(p) & set(q)))
    for p in pairs
)


def distributions(vertices, pebbles, prefix=()):
    """All vectors of nonnegative integers with specified coordinate sum."""
    if vertices == 1:
        yield prefix + (pebbles,)
    else:
        for x in range(pebbles + 1):
            yield from distributions(vertices - 1, pebbles - x, prefix + (x,))


@lru_cache(maxsize=None)
def reachable(state, allow_strict=True):
    """Exact union of vertices reached along all legal decreasing move sequences."""
    mask = sum(1 << i for i, count in enumerate(state) if count > 0)
    for target in range(10):
        for a, b in combinations_with_replacement(neighbors[target], 2):
            if not allow_strict and a != b:
                continue
            if state[a] < 1 or state[b] < 1 + (a == b):
                continue
            successor = list(state)
            successor[a] -= 1
            successor[b] -= 1
            successor[target] += 1
            mask |= reachable(tuple(successor), allow_strict)
    return mask


def profile(state):
    return ''.join(map(str, sorted((a for a in state if a), reverse=True)))


def support_shape(state):
    support = [i for i, a in enumerate(state) if a]
    if len(support) != 4:
        return '-'
    deg = [0] * 4
    for i, j in combinations(range(4), 2):
        if support[j] in neighbors[support[i]]:
            deg[i] += 1
            deg[j] += 1
    deg.sort()
    signature = (sum(deg) // 2, tuple(deg))
    return {
        (0, (0, 0, 0, 0)): '4K1',
        (1, (0, 0, 1, 1)): 'K2+2K1',
        (2, (1, 1, 1, 1)): '2K2',
        (2, (0, 1, 1, 2)): 'P3+K1',
        (3, (1, 1, 1, 3)): 'K1,3',
        (3, (1, 1, 2, 2)): 'P4'
    }[signature]


def label_perm(perm):
    return tuple(position[tuple(sorted((perm[a], perm[b])))] for a, b in pairs)


def move_under_perm(state, induced):
    new = [0] * 10
    for i, j in enumerate(induced):
        new[j] = state[i]
    return tuple(new)


def main():
    universe = 1023
    before = tuple(state for size in range(4) for state in distributions(10, size))
    assert len(before) == 286
    assert not any(reachable(s) == universe for s in before)

    all_four = set(distributions(10, 4))
    assert len(all_four) == 715
    rubbling = Counter()
    pebbling = Counter()
    shapes_good, shapes_bad = Counter(), Counter()
    triple_condition_count = 0
    for s in all_four:
        ok = reachable(s) == universe
        if ok:
            rubbling[profile(s)] += 1
        if reachable(s, False) == universe:
            pebbling[profile(s)] += 1
        if profile(s) == '1111':
            (shapes_good if ok else shapes_bad)[support_shape(s)] += 1
        if profile(s) == '211' and ok:
            double = pairs[s.index(2)]
            single = [pairs[i] for i in range(10) if s[i] == 1]
            assert len(set(double) | set(single[0]) | set(single[1])) == 3
            assert set(double) != set(single[0]) and set(double) != set(single[1])
            triple_condition_count += 1
    assert rubbling == {'4': 10, '22': 45, '211': 30, '1111': 90}
    assert pebbling == {'4': 10}
    assert shapes_good == {'4K1': 5, 'K2+2K1': 60, '2K2': 15, 'K1,3': 10}
    assert shapes_bad == {'P3+K1': 60, 'P4': 60}
    assert triple_condition_count == 30

    automorphisms = [label_perm(p) for p in permutations(range(5))]
    orbits = []
    unseen = all_four.copy()
    while unseen:
        rep = min(unseen)
        orbit = {move_under_perm(rep, p) for p in automorphisms}
        assert orbit <= unseen
        unseen -= orbit
        success = reachable(rep) == universe
        assert all((reachable(q) == universe) == success for q in orbit)
        orbits.append((profile(rep), len(orbit), success, rep, support_shape(rep)))
    assert len(orbits) == 17
    assert sum(n for _, n, ok, _, _ in orbits if ok) == 175
    assert sum(ok for _, _, ok, _, _ in orbits) == 8
    print('before_four 286 successful 0')
    print('four_pebbles 715 rubbling_success 175 pebbling_success 10')
    print('rubbling_by_partition', dict(sorted(rubbling.items())))
    print('four_single_success', dict(sorted(shapes_good.items())))
    print('four_single_failure', dict(sorted(shapes_bad.items())))
    print('symmetry_orbits 17 successful_orbits 8')
    for row in sorted(orbits):
        print('orbit', *row)
    print('PASS')


if __name__ == '__main__':
    main()
