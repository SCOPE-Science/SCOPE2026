"""Independent rank-three type computation for unlabelled full branching trees.

The routine is an exact set-valued Ehrenfeucht--Fraisse recursion: it records
atomic diagrams, not sampled game traces. This is a finite corroboration only.
"""

from itertools import combinations


def complete_tree(b, h):
    neighbors = [set()]
    frontier = [0]
    for _ in range(h):
        following = []
        for parent in frontier:
            for _ in range(b):
                child = len(neighbors)
                neighbors.append({parent})
                neighbors[parent].add(child)
                following.append(child)
        frontier = following
    return neighbors


def rank_three_type(neighbors):
    n = len(neighbors)
    point_types = set()
    for x in range(n):
        # The response y=x is recorded by these attainable third-move patterns.
        diagonal = (bool(neighbors[x]), n - 1 > len(neighbors[x]))
        pair_types = set()
        for y in range(n):
            if x == y:
                continue
            patterns = 0
            for z in range(n):
                if z == x or z == y:
                    continue
                patterns |= 1 << (2 * (z in neighbors[x]) + (z in neighbors[y]))
            pair_types.add((y in neighbors[x], patterns))
        point_types.add((diagonal, frozenset(pair_types)))
    return frozenset(point_types)


def dominant_pair(neighbors):
    n = len(neighbors)
    return any(
        all(z == x or z == y or z in neighbors[x] or z in neighbors[y]
            for z in range(n))
        for x in range(n) for y in range(n)
    )


def run_checks():
    representatives = [(2, 0), (2, 1), (3, 1), (2, 2), (3, 2), (2, 3)]
    signatures = [rank_three_type(complete_tree(b, h)) for b, h in representatives]
    assert len(set(signatures)) == 6
    assert [len(complete_tree(b, h)) for b, h in representatives] == [1, 3, 4, 7, 13, 15]
    assert dominant_pair(complete_tree(2, 2))
    assert not dominant_pair(complete_tree(3, 2))
    assert not dominant_pair(complete_tree(2, 3))
    print('SIX_DISTINCT_REPRESENTATIVES_OK')
    for b, h in representatives:
        print('representative', b, h, 'nodes', len(complete_tree(b, h)))
    stable = signatures[-1]
    for b in (2, 3, 4, 5):
        for h in (3, 4, 5):
            n = len(complete_tree(b, h))
            if n > 390:
                continue
            assert rank_three_type(complete_tree(b, h)) == stable
            print('stable', b, h, 'nodes', n, 'OK')
    for b in range(2, 7):
        if b <= 5:
            assert rank_three_type(complete_tree(b, 1)) == signatures[1 if b == 2 else 2]
        assert rank_three_type(complete_tree(b, 2)) == signatures[3 if b == 2 else 4]
    print('FINITE_EF_RECURSION_OK')


if __name__ == '__main__':
    run_checks()
