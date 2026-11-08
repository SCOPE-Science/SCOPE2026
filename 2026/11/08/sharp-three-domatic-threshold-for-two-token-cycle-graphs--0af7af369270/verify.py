#!/usr/bin/env python3
"""Independent finite checks of the explicit domatic construction for F_2(C_n).
Only Python 3 standard library is needed. Scientific claims and proof in RESULT.md.
"""
from itertools import combinations, product
from pathlib import Path


def pairs(n):
    return list(combinations(range(n), 2))


def neighbors(n, p):
    result = set()
    for x in p:
        for y in ((x - 1) % n, (x + 1) % n):
            q = set(p)
            q.remove(x)
            q.add(y)
            if len(q) == 2:
                result.add(tuple(sorted(q)))
    return result


def colors(n):
    out = {p: sum(p) % 3 for p in pairs(n)}
    if n >= 7 and n % 3 == 1:
        out.update({(0, 1): 0, (0, n-2): 0,
                    (0, n-1): 2, (2, n-1): 1})
    elif n >= 8 and n % 3 == 2:
        out.update({(0, n-3): 0, (0, n-2): 2,
                    (1, n-1): 0, (2, n-1): 2})
    return out


def patches(n):
    base = {p: sum(p) % 3 for p in pairs(n)}
    return {p: col for p, col in colors(n).items() if col != base[p]}


def exceptional(n):
    t = {(0, 1), (n-2, n-1)}
    for p in patches(n):
        t.add(p)
        t.update(neighbors(n, p))
    return t


def profile(n, p, c=None):
    if c is None:
        c = colors(n)
    return tuple(sorted(set(c[q] for q in neighbors(n, p) | {p})))


def test_explicit():
    for n in list(range(3, 4)) + list(range(6, 141)):
        c = colors(n)
        assert set(c) == set(pairs(n))
        failures = [(p, profile(n, p, c)) for p in pairs(n) if profile(n, p, c) != (0, 1, 2)]
        assert not failures, (n, failures[:10])
    print('EXPLICIT_3_DOMATIC_OK n=3 and every 6<=n<=140')


def test_boundary():
    cert = Path(__file__).with_name('boundary_certificate.tsv')
    raw = cert.read_text(encoding='utf-8').splitlines()
    expect = ['n\ti\tj\tcolor\tclosed_colors']
    for n in (7, 8, 10, 11):
        c = colors(n)
        for p in sorted(exceptional(n)):
            expect.append(f'{n}\t{p[0]}\t{p[1]}\t{c[p]}\t' + ''.join(map(str, profile(n, p, c))))
    assert raw == expect, 'standalone fixed boundary certificate disagrees with token-graph computation'
    for n, step in ((10, 3), (11, 3), (13, 3), (14, 3)):
        def lift(p):
            return tuple(x + step if x >= n-4 else x for x in p)
        original = exceptional(n)
        mapped = {lift(p) for p in original}
        # Positions are all either 0..3 or n-4..n-1, with no overlap for n>=10.
        assert mapped == exceptional(n + step), (n, mapped ^ exceptional(n + step))
        assert all(profile(n, p) == profile(n+step, lift(p)) for p in original), n
    print('BOUNDARY_CERTIFICATE_AND_MOD3_STABILITY_OK 7 8 10 11; lifts 10->13 11->14 13->16 14->17')


def exhaustive_no_three(n):
    V = pairs(n)
    closed = [tuple([i] + sorted({V.index(q) for q in neighbors(n, p)})) for i, p in enumerate(V)]
    attempts = 0
    for tuplecol in product(range(3), repeat=len(V)):
        attempts += 1
        if all({tuplecol[j] for j in nb} == {0, 1, 2} for nb in closed):
            raise AssertionError(f'unexpected 3-domatic coloring at n={n}: {tuplecol}')
    return attempts


def test_low():
    assert exhaustive_no_three(4) == 3**6
    assert exhaustive_no_three(5) == 3**10
    print('EXHAUSTIVE_NO_3_DOMATIC_OK n=4 (729 assignments), n=5 (59049 assignments)')


if __name__ == '__main__':
    test_explicit()
    test_boundary()
    test_low()
    print('VERIFY_OK')
