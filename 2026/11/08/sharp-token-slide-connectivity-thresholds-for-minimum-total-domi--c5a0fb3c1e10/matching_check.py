"""Standalone matching-state and local-move verification, without graph domination tests."""
from itertools import combinations, permutations
from math import comb, factorial
from collections import Counter


def generate(m, n):
    return [frozenset(zip(rs, cs)) for rs in combinations(range(m), 3)
            for cs0 in combinations(range(n), 3) for cs in permutations(cs0)]


def neighbors(s, m, n):
    used_rows = {r for r, c in s}
    used_cols = {c for r, c in s}
    for (r, c) in s:
        for nr in range(m):
            if nr in used_rows:
                continue
            for nc in range(n):
                if nc not in used_cols:
                    yield frozenset((s - {(r, c)}) | {(nr, nc)})


def component_profile(m, n):
    states = generate(m, n)
    ids = {s: i for i, s in enumerate(states)}
    assert len(ids) == 6*comb(m, 3)*comb(n, 3)
    seen = set()
    sizes = []
    all_edges = 0
    for i, s in enumerate(states):
        nei = list(neighbors(s, m, n))
        assert len(nei) == len(set(nei)) == 3*(m-3)*(n-3)
        for t in nei:
            assert t in ids
            assert s in set(neighbors(t, m, n))
        all_edges += len(nei)
        if i in seen:
            continue
        q = [i]
        seen.add(i)
        for j in q:
            for t in neighbors(states[j], m, n):
                jj = ids[t]
                if jj not in seen:
                    seen.add(jj)
                    q.append(jj)
        sizes.append(len(q))
    assert all_edges % 2 == 0
    return len(states), all_edges // 2, Counter(sizes)


def apply_template(sequence, goal):
    s = frozenset(((0,0),(1,1),(2,2)))
    for old, new in sequence:
        assert old in s and new not in s
        assert old[0] != new[0] and old[1] != new[1]
        s = frozenset((s - {old}) | {new})
        assert len(s) == len({r for r,c in s}) == len({c for r,c in s}) == 3
    assert s == frozenset(goal), (s, goal)
    return len(sequence)

if __name__ == '__main__':
    templates = {
        'swap_two_selected': ([((1,1),(3,3)), ((0,0),(1,4)), ((1,4),(0,1)), ((3,3),(1,0))], [(0,1),(1,0),(2,2)]),
        'replace_selected_row': ([((0,0),(3,3)), ((3,3),(0,4)), ((0,4),(3,0))], [(3,0),(1,1),(2,2)]),
        'replace_selected_column': ([((0,0),(3,4)), ((3,4),(0,3))], [(0,3),(1,1),(2,2)])
    }
    for label, (sequence, goal) in templates.items():
        print('template',label,apply_template(sequence,goal))
    for m, n in [(3,3), (3,5), (4,4), (4,5), (4,7), (5,5), (5,6), (6,6), (7,7)]:
        count, edges, components = component_profile(m,n)
        expected_count = factorial(m)//(6*factorial(m-3))*factorial(n)//factorial(n-3)
        expected_edges = count * 3*(m-3)*(n-3)//2
        assert (count,edges) == (expected_count,expected_edges)
        if min(m,n) == 3: assert components == Counter({1:count})
        elif m == n == 4: assert components == Counter({4:24})
        else: assert components == Counter({count:1})
        print('matching',m,n,count,edges,sorted(components.items()))
    print('MATCHING_CHECK_PASS')
