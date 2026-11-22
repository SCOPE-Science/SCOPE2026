"""Finite exhaustive checks for the maximal-commutative Brandt formula.

Run: python CHECK.py
Uses only the Python standard library.  These checks are finite
corroboration; the unrestricted assertions have a mathematical proof.
"""
import itertools
from collections import Counter


def group(kind):
    if kind == 'C1':
        return [0], lambda a, b: 0
    if kind == 'C2':
        return list(range(2)), lambda a, b: (a+b) % 2
    if kind == 'C3':
        return list(range(3)), lambda a, b: (a+b) % 3
    if kind == 'S3':
        g = list(itertools.permutations(range(3)))
        return g, lambda a, b: tuple(a[b[i]] for i in range(3))
    raise ValueError(kind)


def maximal_abelian_subgroups(g, multiply):
    sub = []
    for mask in range(1, 1 << len(g)):
        h = frozenset(g[i] for i in range(len(g)) if mask & (1 << i))
        if all(multiply(x, y) == multiply(y, x) and
               multiply(x, y) in h for x in h for y in h):
            sub.append(h)
    return [h for h in sub if not any(h < k for k in sub)]


def product(x, y, multiply):
    i, g, j = x
    k, h, ell = y
    return (i, multiply(g, h), ell) if j == k else None


def maximal_cliques(vertices, neighbor):
    """Bron--Kerbosch enumeration with pivot; output uses vertex indices."""
    def rec(R, P, X):
        if not P and not X:
            yield frozenset(R)
            return
        union = P | X
        pivot = max(union, key=lambda u: len(P & neighbor[u])) if union else None
        choices = sorted(P - (neighbor[pivot] if pivot is not None else set()))
        for v in choices:
            yield from rec(R | {v}, P & neighbor[v], X & neighbor[v])
            P.remove(v)
            X.add(v)
    return set(rec(set(), set(range(len(vertices))), set()))


def predicted(n, g, abelian):
    output = set()
    colors = [('D', i) for i in range(len(abelian))] + [('A', 0), ('B', 0)]
    for pattern in itertools.product(colors, repeat=n):
        a = [i for i, (c, _) in enumerate(pattern) if c == 'A']
        b = [i for i, (c, _) in enumerate(pattern) if c == 'B']
        if bool(a) != bool(b):
            continue
        rows = set()
        for i, (c, j) in enumerate(pattern):
            if c == 'D':
                rows.update((i, h, i) for h in abelian[j])
        rows.update((i, h, j) for i in a for j in b for h in g)
        output.add(frozenset(rows))
    return output


def verify(n, kind):
    g, multiply = group(kind)
    abelian = maximal_abelian_subgroups(g, multiply)
    vertices = [(i, h, j) for i in range(n) for j in range(n) for h in g]
    neighbors = {i:set() for i in range(len(vertices))}
    for i in range(len(vertices)):
        for j in range(i+1,len(vertices)):
            if product(vertices[i],vertices[j],multiply) == product(vertices[j],vertices[i],multiply):
                neighbors[i].add(j)
                neighbors[j].add(i)
    cliques = maximal_cliques(vertices, neighbors)
    actual = {frozenset(vertices[i] for i in c) for c in cliques}
    supposed = predicted(n, g, abelian)
    M = len(abelian)
    total = (M+2)**n - 2*(M+1)**n + 2*M**n
    assert actual == supposed and len(actual) == total, (kind,n)
    for subset in actual:
        for x in subset:
            for y in subset:
                p = product(x, y, multiply)
                assert p is None or p in subset, (kind,n,x,y,p)
    size_spectrum = dict(sorted(Counter(1+len(x) for x in actual).items()))
    print('PASS',kind,'n',n,'M',M,'maximal',total,'sizes',size_spectrum)


if __name__ == '__main__':
    for kind, n in [('C1',1),('C1',2),('C1',3),('C1',4),
                    ('C2',2),('C2',3),('C3',2),('C3',3),
                    ('S3',2),('S3',3)]:
        verify(n, kind)
    print('VERIFY_OK')
