"""Independent finite checks of the forest formula and exchange-distance theorem.
Run with Python 3 standard library: python check_enumerator.py.
"""
from itertools import combinations
from collections import Counter, deque
from math import comb


def edge_list(n):
    return list(combinations(range(n), 2))


def forest_poly(n):
    edges = edge_list(n)
    counts = Counter()
    for bits in range(1 << len(edges)):
        adj = [[] for _ in range(n)]
        for j, (u, v) in enumerate(edges):
            if bits & (1 << j):
                adj[u].append(v)
                adj[v].append(u)
        # Component-edge identity: a graph is a forest iff #edges = n - #components.
        seen = set()
        components = 0
        for u in range(n):
            if u in seen:
                continue
            components += 1
            stack = [u]
            seen.add(u)
            while stack:
                for v in adj[stack.pop()]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
        if bits.bit_count() == n - components:
            counts[bits.bit_count()] += 1
    return counts


def polynomial_by_forests(n):
    ne = comb(n, 2)
    result = Counter()
    for r in range(n + 1):
        inside = comb(r, 2)
        outside = ne - inside
        for edge_count, frequency in forest_poly(r).items():
            for extra in range(outside + 1):
                degree = n-r + inside-edge_count + extra
                result[degree] += comb(n, r) * frequency * comb(outside, extra)
    return result


def brute_power_poly(n):
    edges = edge_list(n)
    order = n + len(edges)
    neighborhood = [set() for _ in range(order)]
    for i, (u, v) in enumerate(edges, n):
        neighborhood[u].add(i)
        neighborhood[v].add(i)
        neighborhood[i].update((u, v))
    outcome = Counter()
    for selected in range(1 << order):
        active = {v for v in range(order) if selected & (1 << v)}
        current = active | set().union(*(neighborhood[v] for v in active)) if active else set()
        while True:
            add = set()
            for v in current:
                missing = neighborhood[v] - current
                if len(missing) == 1:
                    add.update(missing)
            if not add - current:
                break
            current |= add
        if len(current) == order:
            outcome[selected.bit_count()] += 1
    return outcome


def optimum_sets(n):
    edges = edge_list(n)
    eid = {e: n+i for i, e in enumerate(edges)}
    all_originals = set(range(n))
    result = []
    for omitted in combinations(range(n), 2):
        result.append(frozenset(all_originals - set(omitted)))
    for omitted in combinations(range(n), 3):
        for edge in combinations(omitted, 2):
            result.append(frozenset((all_originals - set(omitted)) | {eid[edge]}))
    return result


def check_exchange(n):
    solutions = optimum_sets(n)
    k = n - 2
    count_A = comb(n, 2)
    assert len(solutions) == n*(n-1)**2//2
    neighbors = [set() for _ in solutions]
    for i in range(len(solutions)):
        for j in range(i+1, len(solutions)):
            if len(solutions[i] & solutions[j]) == k-1:
                neighbors[i].add(j)
                neighbors[j].add(i)
    count_edges = sum(map(len, neighbors))//2
    assert count_edges == n*(n-1)*(n-2)*(n+7)//4
    assert all(len(neighbors[i])==5*(n-2) for i in range(count_A))
    assert all(len(neighbors[i])==n+2 for i in range(count_A, len(solutions)))
    eccentricities=[]
    for i, s in enumerate(solutions):
        dist={i:0}
        todo=deque([i])
        while todo:
            current=todo.popleft()
            for j in neighbors[current]:
                if j not in dist:
                    dist[j]=dist[current]+1
                    todo.append(j)
        assert len(dist)==len(solutions)
        for j, d in dist.items():
            assert d == k-len(s & solutions[j]), (n,i,j,d)
        eccentricities.append(max(dist.values()))
    counts=Counter(eccentricities)
    if n>=6:
        assert counts=={3:count_A,4:len(solutions)-count_A}
    elif n==5:
        assert counts=={3:len(solutions)}
    elif n==4:
        assert counts=={2:len(solutions)}
    else:
        assert counts=={1:len(solutions)}
    print('exchange n=',n,'vertices=',len(solutions),'edges=',count_edges,
          'eccentricity_distribution=',dict(sorted(counts.items())), 'PASS')


if __name__=='__main__':
    for n in range(3,6):
        via_forests = polynomial_by_forests(n)
        direct = brute_power_poly(n)
        assert direct == via_forests, (n,direct,via_forests)
        print('polynomial n=',n,'=',dict(sorted(direct.items())),'PASS')
    for n in range(3,10):
        check_exchange(n)
    print('ALL CHECKS PASSED')
