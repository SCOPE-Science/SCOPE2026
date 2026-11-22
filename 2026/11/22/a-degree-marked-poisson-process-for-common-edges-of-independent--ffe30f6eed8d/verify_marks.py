"""Exact finite checks for degree-marked common-edge laws in uniform Cayley trees.

All comparisons use rational arithmetic and complete labelled-tree enumerations
at stated small orders; the infinite-size limit is proved analytically.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def tree_from_prufer(word, n):
    deg = [1] * n
    for j in word:
        deg[j] += 1
    d = deg.copy()
    edges = set()
    for j in word:
        i = next(i for i in range(n) if d[i] == 1)
        edges.add((min(i, j), max(i, j)))
        d[i] -= 1
        d[j] -= 1
    i, j = [i for i in range(n) if d[i] == 1]
    edges.add((i, j))
    return edges, deg


def predicted_degree_mark_law(n, k):
    """Conditional joint law for degrees at k disjoint forced edges.

    The k prescribed edges are (0,1), (2,3), ... .  Each contracted
    edge contributes one fair endpoint incidence; the remaining quotient
    Prufer letters independently select its endpoints with chance 1/n
    each, or any outside singleton with total chance (n-2k)/n.
    """
    choices = tuple(range(2 * k)) + ('outside',)
    weight = {c: Fraction(1, n) for c in range(2 * k)}
    weight['outside'] = Fraction(n - 2 * k, n)
    out = Counter()
    for mandatory in product((0, 1), repeat=k):
        base = [0] * (2 * k)
        for i, b in enumerate(mandatory):
            base[2 * i + b] += 1
        for word in product(choices, repeat=n - k - 2):
            p = Fraction(1, 2**k)
            vals = base.copy()
            for j in word:
                p *= weight[j]
                if j != 'outside':
                    vals[j] += 1
            out[tuple(v + 1 for v in vals)] += p
    return out


def validate_degree_marks(n, k):
    edges = tuple((2*i, 2*i+1) for i in range(k))
    observed = Counter()
    count = 0
    for word in product(range(n), repeat=n-2):
        e, deg = tree_from_prufer(word, n)
        if all(edge in e for edge in edges):
            count += 1
            observed[tuple(deg[j] for j in range(2*k))] += 1
    assert Fraction(count, n**(n-2)) == Fraction(2, n)**k
    theory = predicted_degree_mark_law(n, k)
    assert set(observed) == {c for c in theory if theory[c]}
    assert sum(theory.values(), Fraction(0)) == 1
    for marker, probability in theory.items():
        assert Fraction(observed[marker], count) == probability, (n, k, marker)
    if k == 1:
        ex = sum(Fraction(z[0]) * p for z,p in theory.items())
        ey = sum(Fraction(z[1]) * p for z,p in theory.items())
        exy = sum(Fraction(z[0]*z[1]) * p for z,p in theory.items())
        assert exy-ex*ey == -Fraction(1,4)-Fraction(n-3,n*n)
    return count, len(observed)


def validate_pair_tree_overlap(n):
    trees = [tree_from_prufer(w, n) for w in product(range(n), repeat=n-2)]
    shared = same = opposite = 0
    for e1, d1 in trees:
        for e2, d2 in trees:
            overlap = e1 & e2
            shared += len(overlap)
            for u, v in overlap:
                m1 = 'L' if d1[u] == 1 else ('R' if d1[v] == 1 else '0')
                m2 = 'L' if d2[u] == 1 else ('R' if d2[v] == 1 else '0')
                if m1 == m2 and m1 != '0':
                    same += 1
                if m1 != m2 and m1 != '0' and m2 != '0':
                    opposite += 1
    denominator = len(trees)**2
    assert Fraction(shared, denominator) == Fraction(2*(n-1), n)
    expected = Fraction(n-1, n) * Fraction(n-1, n)**(2*(n-3))
    assert Fraction(same, denominator) == expected
    assert Fraction(opposite, denominator) == expected
    return len(trees), expected


def run():
    total = 0
    for n in (3, 4, 5):
        trees, exp = validate_pair_tree_overlap(n)
        print('Two-tree exhaustive', n, 'trees', trees, 'same/opposite means', exp)
        total += 3
    for n,k in ((3,1), (4,1), (4,2), (5,1), (5,2), (6,1), (6,2), (6,3)):
        count, cells = validate_degree_marks(n, k)
        print('Forced matching exhaustive', n, k, 'conditional trees', count, 'degree cells', cells)
        total += cells + 2 + (1 if k == 1 else 0)
    print('PASS', total, 'exact rational constraints across exhaustive checks')

if __name__ == '__main__':
    run()
