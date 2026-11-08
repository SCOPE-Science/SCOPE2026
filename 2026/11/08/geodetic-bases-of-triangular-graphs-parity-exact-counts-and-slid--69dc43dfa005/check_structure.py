"""Independent construction and one-edge-exchange census for triangular-graph bases."""
from collections import Counter, deque
from itertools import combinations, permutations
from math import comb, factorial


def all_matchings(vertices):
    vertices = tuple(sorted(vertices))
    if not vertices:
        yield frozenset()
        return
    a = vertices[0]
    for b in vertices[1:]:
        remainder = set(vertices) - {a, b}
        for rest in all_matchings(remainder):
            yield rest | {tuple(sorted((a, b)))}


def bases(n):
    ground = set(range(n))
    if n % 2 == 0:
        return set(all_matchings(ground))
    sets = set()
    for tr in combinations(range(n), 3):
        tr = set(tr)
        triple = frozenset(tuple(sorted(ab)) for ab in combinations(tr, 2))
        for rest in all_matchings(ground - tr):
            sets.add(rest | triple)
    for five in combinations(range(n), 5):
        F = set(five)
        for order in permutations(five):
            if order[0] > order[-1]:
                continue
            path = frozenset(tuple(sorted((order[i], order[i+1]))) for i in range(4))
            for rest in all_matchings(ground - F):
                sets.add(rest | path)
    return sets


def criterion(n, edge_set):
    neigh = [set() for _ in range(n)]
    for a, b in edge_set:
        neigh[a].add(b); neigh[b].add(a)
    return all(neigh) and all(sum(len(neigh[x]) == 1 for x in neigh[v]) < 2 for v in range(n))


def structural_kind(n, s):
    degrees = [0] * n
    for a, b in s: degrees[a] += 1; degrees[b] += 1
    if n % 2 == 0: return 'matching'
    return 'triangle' if any(all(tuple(sorted(pair)) in s for pair in combinations(t, 2)) for t in combinations(range(n), 3)) else 'path'


def test(n):
    B = bases(n)
    assert all(criterion(n, s) for s in B)
    k = n//2 if n % 2 == 0 else (n+3)//2
    assert all(len(s) == k for s in B)
    def match_num(j): return factorial(j) // (2**(j//2) * factorial(j//2))
    tri = comb(n, 3)*match_num(n-3) if n % 2 else 0
    path = 60*comb(n, 5)*match_num(n-5) if n % 2 and n >= 5 else 0
    total = match_num(n) if n % 2 == 0 else tri+path
    assert len(B) == total
    kinds = Counter(structural_kind(n, x) for x in B)
    if n % 2: assert kinds['triangle'] == tri and kinds['path'] == path
    else: assert kinds['matching'] == total
    print(f'n={n} count={len(B)} types={dict(kinds)} structure=PASS')
    if n > 7: return
    sets = list(B)
    ids = {s: i for i, s in enumerate(sets)}
    all_edges = set(combinations(range(n),2))
    jumps = [[] for _ in sets]
    slides = [[] for _ in sets]
    for i, x in enumerate(sets):
        for u in x:
            for v in all_edges - x:
                j = ids.get((x - {u}) | {v})
                if j is not None:
                    jumps[i].append(j)
                    if set(u) & set(v): slides[i].append(j)
    def components(adj):
        unused = set(range(len(adj)))
        comp = []
        while unused:
            root = unused.pop()
            stack = [root]
            for a in stack:
                for b in adj[a]:
                    if b in unused: unused.remove(b); stack.append(b)
            comp.append(len(stack))
        return Counter(comp)
    for adj, mode in [(jumps,'jump'),(slides,'slide')]:
        deg = Counter(len(v) for v in adj)
        if n % 2 == 0:
            assert deg == {0: len(sets)}
            assert components(adj) == {1:len(sets)}
        else:
            expect_t = 6*(n-3)
            expect_p = (4*n-10) if mode == 'jump' else (2*n-2)
            for i, s in enumerate(sets):
                assert len(adj[i]) == (expect_t if structural_kind(n,s)=='triangle' else expect_p)
            assert components(adj) == {len(sets):1}
        print(f'  mode={mode} edges={sum(map(len,adj))//2} degrees={dict(deg)} components={dict(components(adj))} PASS')

if __name__ == '__main__':
    for n in range(3, 10):
        test(n)
    print('STRUCTURAL_CHECK_PASS')
