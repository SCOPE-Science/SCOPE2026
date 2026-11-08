"""Exact finite checks for the Euclidean diameter of Pitman--Stanley polytopes.

Python 3, standard library only. These checks support, but do not replace,
the dimension-free mathematical arguments in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
import random


def vertices(capacities):
    """All vertices for strictly increasing rational prefix capacities."""
    n = len(capacities)
    result = []
    for subset in range(1 << n):
        point = [Fraction(0) for _ in range(n)]
        prev = Fraction(0)
        for i in range(n):
            if subset & (1 << i):
                point[i] = capacities[i] - prev
                prev = capacities[i]
        result.append(tuple(point))
    assert len(result) == len(set(result)) == 2 ** n
    for x in result:
        assert all(a >= 0 for a in x)
        assert all(sum(x[:i+1]) <= capacities[i] for i in range(n))
    return result


def sqdist(x, y):
    return sum((a - b) ** 2 for a, b in zip(x, y))


def verify_general(capacities):
    n = len(capacities)
    X = vertices(capacities)
    best = -1
    pairs = []
    for x, y in combinations(X, 2):
        d = sqdist(x, y)
        if d > best:
            best = d
            pairs = [(x, y)]
        elif d == best:
            pairs.append((x, y))
    a, b = capacities[-2:]
    expected = a * a + b * b
    assert best == expected, (capacities, best, expected)
    assert len(pairs) == 1, (capacities, pairs)
    u = tuple([Fraction(0)]*(n-2)+[a,Fraction(0)])
    v = tuple([Fraction(0)]*(n-1)+[b])
    assert frozenset(pairs[0]) == frozenset((u, v))


def verify_uniform(n):
    X = vertices(tuple(map(Fraction, range(1, n+1))))
    classes = {}
    for x, y in combinations(X, 2):
        d = int(sqdist(x, y))
        classes.setdefault(d, []).append((x, y))
    ds = sorted(classes, reverse=True)
    assert ds[0] == n*n+(n-1)**2
    assert len(classes[ds[0]]) == 1
    assert ds[1] == n*n+(n-2)**2+1
    assert len(classes[ds[1]]) == (1 if n == 3 else 2)
    assert ds[0]-ds[1] == 2*(n-2)
    e_n = tuple(map(Fraction, [0]*(n-1)+[n]))
    e_n1 = tuple(map(Fraction, [0]*(n-2)+[n-1,0]))
    assert frozenset(classes[ds[0]][0]) == frozenset((e_n, e_n1))
    top_seconds = [tuple(map(Fraction,[1]+[0]*(n-3)+[n-2,0])),
                   tuple(map(Fraction,[0]*(n-3)+[n-2,1,0]))]
    observed = {frozenset(pair) for pair in classes[ds[1]]}
    assert observed == {frozenset((e_n,y)) for y in top_seconds}


def run():
    random.seed(318170)
    count = 0
    for n in range(2, 8):
        for _ in range(12):
            increments = [Fraction(random.randrange(1,30),random.randrange(1,15))
                          for _ in range(n)]
            capacities = tuple(sum(increments[:i+1]) for i in range(n))
            verify_general(capacities)
            count += 1
    for n in range(3, 11):
        verify_uniform(n)
    print('PITMAN_STANLEY_DIAMETER_TWO_TOP_LEVELS_CHECKS_PASSED',count,8)

if __name__ == '__main__':
    run()
