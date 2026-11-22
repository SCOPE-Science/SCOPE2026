"""Reproducible exact transfer and independent finite-board checks for odd-island strips."""
from collections import defaultdict, deque
from itertools import product
from math import log
import sympy as sp


def transition(state, mask, width):
    labels, parities = state
    old_count = len(parities)
    parent = list(range(old_count + width))

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def join(a, b):
        a, b = root(a), root(b)
        if a != b:
            parent[b] = a

    for r in range(width):
        if mask & (1 << r):
            if labels[r] >= 0:
                join(labels[r], old_count + r)
            if r and mask & (1 << (r - 1)):
                join(old_count + r - 1, old_count + r)

    parity = defaultdict(int)
    for i, p in enumerate(parities):
        parity[root(i)] ^= p
    for r in range(width):
        if mask & (1 << r):
            parity[root(old_count + r)] ^= 1

    active = {root(old_count + r) for r in range(width) if mask & (1 << r)}
    if any(v == 0 for i, v in parity.items() if i not in active):
        return None

    numbering = {}
    new_labels = []
    new_parities = []
    for r in range(width):
        if not mask & (1 << r):
            new_labels.append(-1)
            continue
        x = root(old_count + r)
        if x not in numbering:
            numbering[x] = len(numbering)
            new_parities.append(parity[x])
        new_labels.append(numbering[x])
    return (tuple(new_labels), tuple(new_parities))


def transfer(width):
    empty = ((-1,) * width, ())
    seen = {empty}
    queue = deque([empty])
    transitions = {}
    while queue:
        state = queue.popleft()
        transitions[state] = []
        for mask in range(1 << width):
            next_state = transition(state, mask, width)
            if next_state is not None:
                transitions[state].append((mask, next_state))
                if next_state not in seen:
                    seen.add(next_state)
                    queue.append(next_state)
    states = sorted(seen)
    idx = {state: i for i, state in enumerate(states)}
    matrix = sp.zeros(len(states))
    for state, pairs in transitions.items():
        for mask, after in pairs:
            matrix[idx[state], idx[after]] += 1
    return matrix, idx[empty], states, transitions


def valid_finite(masks, width):
    occupied = {(c, r) for c, mask in enumerate(masks)
                for r in range(width) if mask & (1 << r)}
    while occupied:
        first = occupied.pop()
        stack = [first]
        size = 1
        while stack:
            c, r = stack.pop()
            for v in ((c + 1, r), (c - 1, r), (c, r + 1), (c, r - 1)):
                if v in occupied:
                    occupied.remove(v)
                    stack.append(v)
                    size += 1
        if size % 2 == 0:
            return False
    return True


def locally_admissible(masks, width):
    occupied = {(c, r) for c, mask in enumerate(masks)
                for r in range(width) if mask & (1 << r)}
    length = len(masks)
    while occupied:
        first = occupied.pop()
        stack = [first]
        size = 1
        touches_boundary = False
        while stack:
            c, r = stack.pop()
            touches_boundary |= (c == 0 or c == length - 1)
            for v in ((c + 1, r), (c - 1, r), (c, r + 1), (c, r - 1)):
                if v in occupied:
                    occupied.remove(v)
                    stack.append(v)
                    size += 1
        if size % 2 == 0 and not touches_boundary:
            return False
    return True


def run():
    M, base, states, edges = transfer(3)
    assert len(states) == 19
    assert sum(map(len, edges.values())) == 119
    X = sp.Symbol('X')
    P = X**11-6*X**10-10*X**9+32*X**8-30*X**7-38*X**6+99*X**5-2*X**4-49*X**3+16*X**2+10*X-1
    target = (X-1)**3*(X+1)*(X**4+X**3-3*X-1)*P
    assert sp.expand(M.charpoly(X).as_expr()-target) == 0
    assert sp.count_roots(P, 6, 9) == 1
    assert int((M ** 20)[base, base]) > 6 ** 20
    assert P.subs(X, sp.Rational(688017, 100000)) < 0
    assert P.subs(X, sp.Rational(688018, 100000)) > 0

    # Every state communicates with the empty state via one/two full columns,
    # followed by a zero column; reachability from empty is by construction.
    full = 7
    empty = ((-1, -1, -1), ())
    for state in states:
        assert any(transition(transition(state, full, 3), full if k else 0, 3) == empty
                   for k in (0, 1)) or transition(transition(transition(state, full, 3), full, 3), 0, 3) == empty

    powers = sp.eye(len(states))
    expected = [1, 6, 37, 251, 1692, 11635, 79973, 550440]
    for n, expected_count in enumerate(expected):
        a = (powers * M)[base, base]
        assert int(a) == expected_count, (n, a, expected_count)
        powers = powers * M

    for n in range(1, 6):
        brute = sum(valid_finite(t, 3) for t in product(range(8), repeat=n))
        exact = int((M ** (n+1))[base, base])
        assert brute == exact, (n, brute, exact)
        for block in product(range(8), repeat=n):
            if not locally_admissible(block, 3):
                continue
            left = [(), (7,), (7, 7)] if block[0] else [()]
            right = [(), (7,), (7, 7)] if block[-1] else [()]
            assert any(valid_finite(a + block + b, 3) for a in left for b in right), block

    M2, b2, _, _ = transfer(2)
    P2 = X**5-4*X**4+3*X**3-5*X**2+2*X+1
    assert sp.rem(M2.charpoly(X).as_expr(), P2, X) == 0
    assert sp.count_roots(P2, 3, 4) == 1
    assert P2.subs(X, sp.Rational(349757, 100000)) > 0
    assert sp.Rational(688017, 100000) ** 3 > sp.Rational(349757, 100000) ** 4
    print('PASS: 19-state transfer, 119 transitions, exact characteristic polynomial.')
    print('PASS: independent component enumeration and 4-column padding for n=1..5.')
    print('PASS: finite-board counts n=0..7 and root enclosure.')
    print('lambda3 in (6.88017, 6.88018); entropy per column is log(lambda3).')
    print('2D lower bound log(lambda3)/4 exceeds the two-row log(lambda2)/3 bound.')

if __name__ == '__main__':
    run()
