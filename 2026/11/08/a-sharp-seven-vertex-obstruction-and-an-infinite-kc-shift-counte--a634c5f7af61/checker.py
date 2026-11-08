"""Exact reproducibility checks for greedy matching on trees (stdlib only)."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product, permutations
from math import factorial


def expectation(edges):
    edges = tuple(sorted(tuple(sorted(e)) for e in edges))
    conflicts = [sum(1 << j for j, f in enumerate(edges)
                     if e[0] in f or e[1] in f) for e in edges]
    @lru_cache(None)
    def f(mask):
        if mask == 0:
            return Fraction(0)
        return 1 + sum((f(mask & ~conflicts[i]) for i in range(len(edges))
                        if mask & (1 << i)), Fraction(0)) / mask.bit_count()
    return f((1 << len(edges)) - 1)


def all_labeled_trees(n):
    """All n^(n-2) labeled trees, by the Prüfer bijection."""
    for word in product(range(n), repeat=n - 2):
        deg = [1] * n
        for v in word:
            deg[v] += 1
        edges = []
        for v in word:
            leaf = next(i for i in range(n) if deg[i] == 1)
            edges.append(tuple(sorted((leaf, v))))
            deg[leaf] -= 1
            deg[v] -= 1
        rem = [i for i in range(n) if deg[i] == 1]
        edges.append(tuple(rem))
        yield tuple(sorted(edges))


def kc_shifts(edges, n):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    old = set(edges)
    for x in range(n):
        if len(adj[x]) < 2:
            continue
        for y in range(n):
            if y == x or len(adj[y]) < 2:
                continue
            parent = {x: -1}
            queue = [x]
            for v in queue:
                for w in adj[v]:
                    if w not in parent:
                        parent[w] = v
                        queue.append(w)
            path = [y]
            while path[-1] != x:
                path.append(parent[path[-1]])
            path.reverse()
            if len(path) < 2 or any(len(adj[z]) != 2 for z in path[1:-1]):
                continue
            move = [z for z in adj[x] if z != path[1]]
            new = old.copy()
            for z in move:
                new.remove(tuple(sorted((x, z))))
                new.add(tuple(sorted((y, z))))
            yield x, y, tuple(sorted(new))


def brute_mean(edges):
    """Independent full order enumeration, only for small graphs."""
    result = 0
    for order in permutations(edges):
        used = set()
        size = 0
        for a, b in order:
            if a not in used and b not in used:
                used.update((a, b))
                size += 1
        result += size
    return Fraction(result, factorial(len(edges)))


@lru_cache(None)
def p(n):
    if n <= 1:
        return Fraction(0)
    return 1 + Fraction(2, n-1) * sum((p(j) for j in range(n-1)), Fraction(0))


@lru_cache(None)
def spider(arms):
    arms = tuple(sorted(arms))
    if arms[0] == 0:
        return p(sum(arms)+1)
    den = sum(arms)
    num = Fraction(0)
    for z, a in enumerate(arms):
        oth = tuple(arms[i] for i in range(3) if i != z)
        num += p(a-1)+p(oth[0])+p(oth[1])
        for j in range(2, a+1):
            num += p(a-j)+spider(tuple(sorted(oth+(j-2,))))
    return 1+num/den


def main():
    census = []
    for n in range(4, 7):
        totals = Counter()
        for edges in all_labeled_trees(n):
            totals['trees'] += 1
            a = expectation(edges)
            for x, y, shifted in kc_shifts(edges, n):
                delta = expectation(shifted)-a
                totals['kc_comparisons'] += 1
                totals['positive' if delta > 0 else 'negative' if delta < 0 else 'zero'] += 1
                assert delta <= 0, (n, edges, x, y, shifted, delta)
        assert totals['trees'] == n**(n-2)
        census.append((n, dict(totals)))
    for n, counts in census:
        print('PROVED_EXHAUSTIVE', n, counts)

    for L in range(2, 12):
        n = L + 5
        original = tuple((j, j+1) for j in range(n-1))
        shifted = next(H for x, y, H in kc_shifts(original, n) if x == 2 and y == 4)
        d = spider((2, 2, L))-p(n)
        assert d > 0
        assert expectation(shifted)-expectation(original) == d
        b = p(L+3)-2*p(L+2)+2*p(L)-p(L-1)
        closed = Fraction(2*(-2)**(L-2)*(L*L+3*L-2),
                          factorial(L-2)*(L-1)*L*(L+1)*(L+2))
        assert b == closed
        if L == 2:
            assert expectation(shifted) == Fraction(3)
            assert expectation(original) == Fraction(26, 9)
            assert brute_mean(shifted) == Fraction(3)
            assert brute_mean(original) == Fraction(26, 9)
        if L == 3:
            assert brute_mean(shifted) == expectation(shifted)
            assert brute_mean(original) == expectation(original)
    print('VERIFIED 10 exact spider/path identities, 4 independent permutation expectations')
    print('WITNESS P7=26/9, S(2,2,2)=3; all checks passed')

if __name__ == '__main__':
    main()
