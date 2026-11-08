"""Independent labelled-state verification of complete-bipartite GH dynamics.

Run: python3 verify_direct.py
"""
from itertools import product
from collections import Counter


def onto(k, n):
    if k == 1:
        return 1
    if k == 2:
        return 2 ** n - 2
    if k == 3:
        return 3 ** n - 3 * 2 ** n + 3
    raise ValueError(k)


# (time, eventual period): coefficient by (left support cardinality,
# right support cardinality), independent of the shore sizes.
COEFF = {
    (0, 1): {(1, 1): 1},
    (0, 3): {(3, 3): 1},
    (0, 4): {(2, 2): 2},
    (1, 1): {(1, 1): 3, (1, 2): 2, (2, 1): 2, (2, 2): 1},
    (1, 4): {(2, 2): 2, (2, 3): 1, (3, 2): 1},
    (2, 1): {(1, 1): 3, (1, 2): 3, (1, 3): 1,
             (2, 1): 3, (2, 2): 1, (3, 1): 1},
    (2, 4): {(2, 2): 2, (2, 3): 1, (3, 2): 1},
    (3, 1): {(1, 1): 2, (1, 2): 2, (1, 3): 1,
             (2, 1): 2, (2, 2): 1, (3, 1): 1},
    (3, 4): {(2, 3): 1, (3, 2): 1},
    (4, 1): {(1, 2): 2, (1, 3): 1, (2, 1): 2, (3, 1): 1},
}


def step(xs, m):
    la = 1 in xs[:m]
    rb = 1 in xs[m:]
    return tuple((v + 1) % 3 if v else (1 if rb else 0) for v in xs[:m]) + tuple(
        (v + 1) % 3 if v else (1 if la else 0) for v in xs[m:])


def entry(x, m):
    hist = {}
    states = []
    while x not in hist:
        hist[x] = len(states)
        states.append(x)
        x = step(x, m)
        if len(states) > 8:
            raise AssertionError('Unpredicted long orbit')
    return (hist[x], len(states) - hist[x])


def expected(m, n):
    return {k: sum(c * onto(a, m) * onto(b, n)
                   for (a, b), c in terms.items())
            for k, terms in COEFF.items()}


def main():
    tested = 0
    labelled = 0
    for m in range(1, 9):
        for n in range(1, 9-m):
            hist = Counter(entry(x, m) for x in product(range(3), repeat=m+n))
            target = {k: v for k,v in expected(m,n).items() if v > 0}
            assert dict(hist) == target, (m,n,hist,target)
            assert sum(hist.values()) == 3 ** (m+n)
            tested += 1
            labelled += 3 ** (m+n)
    print('DIRECT_OK', 'pairs', tested, 'configurations', labelled)
    print('K_3_3', expected(3, 3))

if __name__ == '__main__':
    main()
