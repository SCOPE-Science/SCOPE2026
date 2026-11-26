"""Test all exact point-line flags of two ordered Pascal sextuples."""
from collections import Counter
from itertools import combinations, permutations
from math import gcd


def cross(a, b):
    return tuple(a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3]
                 for i in range(3))


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def norm(v):
    d = gcd(*v)
    assert d
    if next(z for z in v if z) < 0:
        d = -d
    return tuple(z//d for z in v)


def canonical_cycle(h):
    j = h.index(0)
    h = h[j:] + h[:j]
    return min(h, h[:1]+h[:0:-1])


WORDS = [(0,)+p for p in permutations(range(1, 6)) if p[0]<p[-1]]
INDEX = {h:i for i, h in enumerate(WORDS)}


def orbit(base):
    labels = [tuple(ord(c)-65 for c in h) for h in base]
    return {tuple(sorted(INDEX[canonical_cycle(tuple(g[i] for i in h))]
                         for h in labels)) for g in permutations(range(6))}


# Baralic-Spasojevic, arXiv:1209.4795, Propositions 3.2 and 3.3.
S = orbit(('ABEDCF', 'ADEFCB', 'AFEBCD'))
K = orbit(('ABFDCE', 'AEFBDC', 'ABDFEC'))
assert len(S)==20 and len(K)==60 and not S&K


def flags(T):
    assert len(set(T))==6
    def pascal(h):
        def side(i):
            a, b = T[h[i]], T[h[(i+1)%6]]
            return a*b, -a-b, 1
        P = [cross(side(i), side(i+3)) for i in range(3)]
        L = norm(cross(P[0],P[1]))
        assert dot(P[2],L)==0
        return L
    lines = list(map(pascal, WORDS))
    assert len(set(lines))==60
    marked = {}
    for i, j, k in S|K:
        point = norm(cross(lines[i],lines[j]))
        assert point not in marked
        marked[point] = tuple(l for l,L in enumerate(lines) if dot(point,L)==0)
        assert {i,j,k} <= set(marked[point])
    assert len(marked)==80
    edges = {e for members in marked.values() for e in combinations(members,2)}
    return Counter(map(len,marked.values())),len(edges)


assert flags((0,1,3,9,27,81)) == ({3:80},240)
assert flags((0,65,195,585,1755,9)) == ({3:79,4:1},243)
print('EXACT_RATIONAL_PASCAL_GEOMETRY_VERIFIED_OK')
