#!/usr/bin/env python3
"""Exact proper-interval-graph refinability census (standard library only)."""
from collections import Counter, defaultdict
from math import comb

def proper_orders(n):
    """Nondecreasing right-neighbor endpoints, connected straight orders."""
    def visit(i, previous, endpoints):
        if i == n:
            yield tuple(endpoints)
            return
        lower = max(previous, i + (i + 1 < n))
        for right in range(lower, n):
            yield from visit(i + 1, right, endpoints + [right])
    if n == 1:
        yield (0,)
    else:
        yield from visit(0, 0, [])

def graph(endpoints):
    n = len(endpoints)
    out = [0] * n
    for i in range(n):
        for j in range(i + 1, endpoints[i] + 1):
            out[i] |= 1 << j
            out[j] |= 1 << i
    return tuple(out)

def mirror(a):
    n = len(a)
    return tuple(sum((1 << j) for j in range(n)
                     if a[n - i - 1] & (1 << (n - j - 1)))
                 for i in range(n))

def colors(a):
    n = len(a)
    c = (0,) * n
    for _ in range(n + 1):
        patterns = [(c[i], tuple(sorted(c[j] for j in range(n)
                      if a[i] & (1 << j)))) for i in range(n)]
        dictionary = {p: j for j, p in enumerate(sorted(set(patterns)))}
        new_c = tuple(dictionary[p] for p in patterns)
        if new_c == c:
            return c
        c = new_c
    raise AssertionError('color refinement did not stabilize')

def orbit_partition(a):
    """Exact orbit partition by enumeration of ALL adjacency-preserving bijections."""
    n = len(a)
    degrees = [r.bit_count() for r in a]
    options = [tuple(j for j in range(n) if degrees[j] == degrees[i])
               for i in range(n)]
    parent = list(range(n))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def join(i,j):
        parent[find(i)] = find(j)
    mapping = [-1]*n
    def recurse(used, k):
        if k == n:
            for i,j in enumerate(mapping):
                join(i,j)
            return
        # fixed source order by increasing number of same-degree candidates
        i = order[k]
        for j in options[i]:
            if used & (1 << j):
                continue
            if all(bool(a[i] & (1 << h)) == bool(a[j] & (1 << mapping[h]))
                   for h in order[:k]):
                mapping[i] = j
                recurse(used | (1 << j), k + 1)
                mapping[i] = -1
    order = sorted(range(n), key=lambda i:(len(options[i]), i))
    recurse(0,0)
    return tuple(find(i) for i in range(n))

def same_partition(x, y):
    return all((x[i] == x[j]) == (y[i] == y[j])
               for i in range(len(x)) for j in range(i + 1,len(x)))

def canonical_key(r):
    a = graph(r)
    b = mirror(a)
    # The only other straight-order representation is the reversal;
    # right endpoint of each vertex can be read directly from its row.
    n = len(r)
    reflected = tuple(max((j for j in range(i + 1,n) if b[i] & (1 << j)),
                          default=i) for i in range(n))
    assert graph(reflected) == b
    return min(r, reflected)

def joint_wl_class_count(adjacencies):
    """Shared color alphabet on the disjoint union; one graph per signature."""
    if not adjacencies:
        return 0
    n = len(adjacencies[0])
    c = [[0] * n for a in adjacencies]
    for step in range(n + 1):
        types = []
        for g, a in enumerate(adjacencies):
            types.extend((c[g][i], tuple(sorted(c[g][j] for j in range(n)
                if a[i] & (1 << j)))) for i in range(n))
        palette = {t: k for k,t in enumerate(sorted(set(types)))}
        new_c = [[palette[t] for t in types[g*n:(g+1)*n]]
                 for g in range(len(adjacencies))]
        if new_c == c:
            break
        c = new_c
    return len({tuple(sorted(row)) for row in c})

def main():
    sums = []
    total_bad = []
    for n in range(1,9):
        reps = {}
        num_orders = 0
        for r in proper_orders(n):
            num_orders += 1
            key = canonical_key(r)
            reps.setdefault(key, graph(key))
        # Saitoh et al., Theorem 1; n=1 also follows by convention.
        if n >= 2:
            expected = (comb(2*(n-1),n-1)//n + comb(n-1,(n-1)//2))//2
            assert len(reps) == expected, (n,len(reps),expected)
        bad = []
        for r,a in reps.items():
            c = colors(a)
            orbits = orbit_partition(a)
            if not same_partition(c,orbits):
                bad.append((r,a,c,orbits))
        wl_classes = joint_wl_class_count(list(reps.values()))
        assert wl_classes == len(reps)
        sums.append((n, num_orders, len(reps), len(bad), wl_classes))
        total_bad.extend((n,*v) for v in bad)
    print('n ordered_representations isomorphism_types nonrefinable_types joint_wl_classes')
    for row in sums: print(*row)
    assert [(n,b) for n,_,_,b,_ in sums] == [(n,0) for n in range(1,8)] + [(8,1)]
    n,r,a,c,o=total_bad[0]
    print('unique_exception_right_endpoints', r)
    print('unique_exception_adjacency_masks',a)
    print('unique_exception_colors',c)
    print('unique_exception_orbits',o)
    # Check degree-2 vertices form a matching and degree-3 vertices have no edge.
    dc=defaultdict(list)
    for i,row in enumerate(a):dc[row.bit_count()].append(i)
    assert {k:len(v) for k,v in dc.items()} == {2:6,3:2}
    for i in dc[2]:
        assert sum((a[i] & (1<<j))!=0 for j in dc[2]) == 1
        assert sum((a[i] & (1<<j))!=0 for j in dc[3]) == 1
    for i in dc[3]:
        assert sum((a[i] & (1<<j))!=0 for j in dc[2]) == 3
    assert not (a[dc[3][0]] & (1<<dc[3][1]))
    # Graph must have two triangles, one at each end, and a 3-edge bridge path.
    triangles = [tuple((i,j,k)) for i in range(n) for j in range(i+1,n)
                 for k in range(j+1,n) if (a[i] & (1<<j)) and
                 (a[i] & (1<<k)) and (a[j] & (1<<k))]
    assert len(triangles) == 2
    assert set(triangles[0]).isdisjoint(triangles[1])
    assert sorted(Counter(c).values()) == [2,6]
    print('unique_exception_triangles',triangles)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
