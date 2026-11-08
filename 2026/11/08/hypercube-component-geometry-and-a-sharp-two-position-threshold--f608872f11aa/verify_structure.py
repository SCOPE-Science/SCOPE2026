"""Independent exhaustive and constructive checks of derangement-swap claims."""
from collections import Counter, deque
from itertools import permutations, product


def signature(p):
    pos = [0] * (len(p) + 1)
    for j, x in enumerate(p, 1):
        pos[x] = j
    return tuple(pos[i] < i for i in range(2, len(p)))


def legal(q):
    return all(q[j] != j + 1 for j in range(len(q)))


def neighbors(q, radius):
    n = len(q)
    for i in range(n):
        for j in range(i + 1, min(n, i + radius + 1)):
            r = list(q)
            r[i], r[j] = r[j], r[i]
            if legal(r):
                yield tuple(r)


def structural_check(n):
    states = [p for p in permutations(range(1, n + 1)) if legal(p)]
    state_set = set(states)
    by_sign = {}
    for p in states:
        by_sign.setdefault(signature(p), set()).add(p)
    assert len(by_sign) == 2 ** (n - 2)
    isolated = []
    for sign, fiber in by_sign.items():
        seed = next(iter(fiber))
        reached = {seed}
        queue = deque([seed])
        while queue:
            p = queue.popleft()
            ns = set(neighbors(p, 1))
            if not ns:
                isolated.append(p)
            for q in ns:
                assert q in state_set and signature(q) == sign
                if q not in reached:
                    reached.add(q)
                    queue.append(q)
        assert reached == fiber, (n, sign, len(fiber), len(reached))
    assert set(isolated) == {tuple([n] + list(range(1, n))), tuple(list(range(2, n+1)) + [1])}
    quotient = set()
    for p in states:
        sp = signature(p)
        for q in neighbors(p, 2):
            sq = signature(q)
            if sp != sq:
                assert sum(a != b for a, b in zip(sp, sq)) == 1
                quotient.add(tuple(sorted((sp, sq))))
    expect = (n-2) * 2 ** (n-3)
    if n >= 4:
        assert len(quotient) == expect, (n, len(quotient), expect)
    else:
        assert len(quotient) == 0
    print('n=%d configurations=%d components=%d quotient_edges=%d isolated=%d' %
          (n, len(states), len(by_sign), len(quotient), len(isolated)), flush=True)


def constructive_flip(n, sign, value):
    left = [v for v in range(2, n) if sign[v-2]] + [n]
    right = [1] + [v for v in range(2, n) if not sign[v-2]]
    a = left + right
    assert signature(a) == sign and legal(a) and sign[value-2]
    j = a.index(value) + 1
    while j < value - 1:
        a[j-1], a[j] = a[j], a[j-1]
        assert legal(a)
        j += 1
    assert j == value - 1
    if a[value] == value - 1:
        a[value-1], a[value] = a[value], a[value-1]
        assert legal(a)
    a[value-2], a[value] = a[value], a[value-2]
    assert legal(a)
    target = tuple(False if k == value-2 else sign[k] for k in range(n-2))
    assert signature(a) == target


def distance_check():
    a = (3, 1, 2, 5, 6, 4)
    b = (3, 6, 2, 5, 1, 4)
    q = deque([a]); d = {a: 0}
    while q:
        p = q.popleft()
        for r in neighbors(p, 1):
            if r not in d:
                d[r] = d[p] + 1; q.append(r)
    assert d[b] == 7
    def kendall(x, y):
        pos = {v: i for i, v in enumerate(y)}
        ranks = [pos[v] for v in x]
        return sum(ranks[i] > ranks[j] for i in range(len(x)) for j in range(i+1, len(x)))
    assert kendall(a, b) == 5
    route = [3,2,3,4,3,2,3]
    p = list(a)
    for i in route:
        p[i-1], p[i] = p[i], p[i-1]
        assert legal(p)
    assert tuple(p) == b
    print('distance_witness n=6 restricted=7 ordinary=5 steps=7')


if __name__ == '__main__':
    for n in range(3, 9):
        structural_check(n)
    for n in range(4, 15):
        for bits in product((False, True), repeat=n-2):
            for i in range(2, n):
                if bits[i-2]:
                    constructive_flip(n, bits, i)
        print('constructive_all_patterns n=%d PASS' % n, flush=True)
    distance_check()
    print('PYTHON_INDEPENDENT_PASS')
