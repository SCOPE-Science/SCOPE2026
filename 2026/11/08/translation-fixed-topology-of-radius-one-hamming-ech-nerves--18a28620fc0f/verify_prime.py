"""Independently enumerate translation-subgroup geometric fixed-point nerves.

Usage: python verify_prime.py
Pure Python 3; no nonstandard dependencies.
"""
from itertools import product


def add(a, b, q):
    return tuple((x+y) % q for x, y in zip(a, b))


def mul(t, a, q):
    return tuple((t*x) % q for x in a)


def subspaces(vertices, q):
    z = tuple(0 for _ in vertices[0])
    seen = {frozenset([z])}
    queue = [frozenset([z])]
    for space in queue:
        for v in vertices:
            if v in space:
                continue
            extension = frozenset(add(u, mul(t, v, q), q)
                                  for u in space for t in range(q))
            if extension not in seen:
                seen.add(extension)
                queue.append(extension)
    return queue


def analyze(n, q):
    verts = list(product(range(q), repeat=n))
    sub = subspaces(verts, q)
    checked = 0
    for V in sub:
        if len(V) == 1:
            continue
        cosets = set(frozenset(add(x, u, q) for u in V) for x in verts)
        contained = set()
        max_per_ball = 0
        for c in verts:
            ball = {c}
            for i in range(n):
                for t in range(1, q):
                    y = list(c)
                    y[i] = (y[i] + t) % q
                    ball.add(tuple(y))
            full_orbits = [O for O in cosets if O <= ball]
            contained.update(full_orbits)
            max_per_ball = max(max_per_ball, len(full_orbits))
        if len(V) == q:
            w = next(v for v in V if any(v))
            good = (sum(bool(x) for x in w) in (1, 2)) if q == 2 else (sum(bool(x) for x in w) == 1)
        else:
            good = False
        expected = q ** (n-1) if good else 0
        assert len(contained) == expected, (q,n,sorted(V),len(contained),expected)
        assert max_per_ball <= 1, (q,n,sorted(V),max_per_ball)
        checked += 1
    return len(sub), checked


def main():
    total = 0
    for q,nmax in [(2,5), (3,3), (5,2)]:
        for n in range(1,nmax+1):
            all_sub, checked = analyze(n,q)
            print('q=%d n=%d subspaces=%d nontrivial=%d PASS' % (q,n,all_sub,checked))
            total += checked
    print('ALL_VERIFY_OK nontrivial_subgroups=%d' % total)


if __name__ == '__main__':
    main()
