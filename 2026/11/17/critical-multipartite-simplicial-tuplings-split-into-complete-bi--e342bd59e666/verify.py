"""Finite independent verification of simplicial tupling for multipartite joins.

Run: python verify.py
Only uses the standard library. All reported cases are finite tests.
"""
from itertools import combinations, product
from collections import deque
from math import comb, prod


def inspect(sizes):
    q = len(sizes)
    assert q % 2 == 0
    r = q // 2
    base_vertices = tuple((i, a) for i, n in enumerate(sizes) for a in range(n))
    # Generate all r-element subsets; discard those violating facehood in X.
    vertices = tuple(t for t in combinations(base_vertices, r)
                     if len(set(i for i, _ in t)) == r)
    index = {t: k for k, t in enumerate(vertices)}
    adjacent = [set() for _ in vertices]
    # Enumerate Y's edges from the defining union-face condition, not a component formula.
    for k, x in enumerate(vertices):
        sx = set(x)
        for l in range(k + 1, len(vertices)):
            y = vertices[l]
            u = sx | set(y)
            if len(u) == 2*r and len(set(i for i, _ in u)) == 2*r:
                adjacent[k].add(l)
                adjacent[l].add(k)
    seen = set()
    actual = []
    for start in range(len(vertices)):
        if start in seen:
            continue
        seen.add(start)
        queue = deque([start]); group = []
        while queue:
            i = queue.popleft(); group.append(i)
            for j in adjacent[i]:
                if j not in seen:
                    seen.add(j); queue.append(j)
        actual.append(group)
    counts = []
    # Verify each component's complete-bipartite structure without using the claimed pairing formula.
    for group in actual:
        supports = {tuple(sorted(i for i, _ in vertices[v])) for v in group}
        assert len(supports) == 2
        a, b = sorted(supports)
        assert set(a).isdisjoint(b) and len(a)==len(b)==r
        left = [v for v in group if tuple(sorted(i for i, _ in vertices[v])) == a]
        right = [v for v in group if tuple(sorted(i for i, _ in vertices[v])) == b]
        assert all(adjacent[v] == set(right) for v in left)
        assert all(adjacent[v] == set(left) for v in right)
        counts.append((frozenset((frozenset(a),frozenset(b))),len(left),len(right)))
    predicted = {}
    for support in combinations(range(q),r):
        comp = tuple(i for i in range(q) if i not in support)
        key = frozenset((frozenset(support),frozenset(comp)))
        predicted[key] = tuple(sorted((prod(sizes[i] for i in support),
                                       prod(sizes[i] for i in comp))))
    assert len(actual) == comb(q,r)//2 == len(predicted)
    assert {k:tuple(sorted((a,b))) for k,a,b in counts} == predicted
    edges = sum(len(x) for x in adjacent)//2
    actual_rank = edges-len(vertices)+len(actual)
    expected_rank = sum((a-1)*(b-1) for _,a,b in counts)
    from_sum = (comb(q,r)//2)*(prod(sizes)+1)-sum(
        prod(sizes[i] for i in s) for s in combinations(range(q),r))
    assert actual_rank == expected_rank == from_sum
    return len(vertices),edges,len(actual),actual_rank


def main():
    cases = [(2,2),(2,3),(2,2,2,2),(1,2,3,2),
             (2,2,2,2,2,2),(2,1,3,2,2,1),
             (2,2,2,2,2,2,2,2)]
    for sizes in cases:
        v,e,c,b=inspect(sizes)
        print('sizes={} : V={}, E={}, components={}, rankH1={} : PASS'.format(sizes,v,e,c,b))
    print('All {} independent face-enumeration/component/rank checks PASS'.format(len(cases)))


if __name__=='__main__': main()
