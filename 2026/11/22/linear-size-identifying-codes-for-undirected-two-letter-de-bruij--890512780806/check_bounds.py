"""Independent finite checks for identifying codes on undirected length-two de Bruijn graphs.
Run with Python 3: python check_bounds.py
"""
from itertools import combinations

TEMPLATES = {
    3: ((0, 1), (0, 2), (1, 0), (2, 0)),
    4: ((0, 0), (1, 2), (1, 3), (2, 1), (3, 1)),
    5: ((0, 1), (0, 2), (1, 3), (2, 4), (3, 0), (4, 1)),
}


def balls(q):
    words = tuple((a, b) for a in range(q) for b in range(q))
    # The graph is undirected: ab adjacent to bc and ca for all c.
    return words, tuple(
        frozenset([(a, b)] + [(b, c) for c in range(q)] + [(c, a) for c in range(q)])
        for a, b in words
    )


def signatures(q, code):
    words, neighborhoods = balls(q)
    code = frozenset(code)
    return tuple(frozenset(code & neighborhood) for neighborhood in neighborhoods)


def identifies(q, code):
    signatures_ = signatures(q, code)
    return all(signatures_) and len(set(signatures_)) == q*q


def construction(q):
    assert q >= 3
    k, remainder = divmod(q, 3)
    blocks = ([3]*k if remainder == 0 else [remainder+3] + [3]*(k-1))
    offset = 0
    selected = []
    for size in blocks:
        selected.extend((a + offset, b + offset) for a, b in TEMPLATES[size])
        offset += size
    assert offset == q
    return tuple(selected)


def finite_exclusion(q):
    words, neighborhoods = balls(q)
    # Only test subsets of size q: monotonicity excludes every smaller size.
    masks = []
    for neighborhood in neighborhoods:
        mask = sum(1 << i for i, w in enumerate(words) if w in neighborhood)
        masks.append(mask)
    tests = 0
    for indices in combinations(range(q*q), q):
        tests += 1
        mask = sum(1 << i for i in indices)
        traces = [mask & ball for ball in masks]
        if all(traces) and len(set(traces)) == q*q:
            raise AssertionError('Unexpected identifying code of size q: ' + str(indices))
    return tests


if __name__ == '__main__':
    for q in (3, 4, 5):
        assert identifies(q, TEMPLATES[q]), q
        print('template', q, 'OK', len(TEMPLATES[q]))
        trials = finite_exclusion(q)
        print('size-q exclusion', q, 'PASS', trials)
    for q in range(3, 101):
        code = construction(q)
        assert len(code) == q + q//3
        assert identifies(q, code)
    print('constructed identifying codes q=3,...,100 PASS')
    for size in (3, 4, 5):
        rows = []
        for sig in signatures(size, TEMPLATES[size]):
            mask = sum(1 << i for i, edge in enumerate(TEMPLATES[size]) if edge in sig)
            rows.append(mask)
        print('signature-masks', size, rows)
