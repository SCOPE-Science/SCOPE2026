"""Finite verification of parabolic-idempotent commutation in type-A 0-Hecke monoids.

Uses only the Python standard library. Run: python check_hecke.py
"""
from itertools import permutations


def demazure(w, v):
    """Demazure product from a bubble-sort reduced expression for v."""
    n = len(v)
    tmp = list(v)
    word = []
    for expected in range(1, n + 1):
        pos = tmp.index(expected)
        while pos > expected - 1:
            tmp[pos], tmp[pos - 1] = tmp[pos - 1], tmp[pos]
            word.append(pos - 1)
            pos -= 1
    assert tmp == list(range(1, n + 1))
    acc = list(w)
    for i in reversed(word):
        if acc[i] < acc[i + 1]:
            acc[i], acc[i + 1] = acc[i + 1], acc[i]
    return tuple(acc)


def parabolic_longest(n, mask):
    vals = list(range(1, n + 1))
    i = 0
    while i < n - 1:
        if not mask & (1 << i):
            i += 1
            continue
        j = i
        while j < n - 1 and mask & (1 << j):
            j += 1
        vals[i:j + 1] = reversed(vals[i:j + 1])
        i = j + 1
    return tuple(vals)


def allowed(j, k, m):
    union = j | k
    i = 0
    while i < m:
        if not union & (1 << i):
            i += 1
            continue
        t = i
        while t < m and union & (1 << t):
            t += 1
        c = ((1 << (t - i)) - 1) << i
        if (j & c) != c and (k & c) != c:
            return False
        i = t
    return True


def coefficient_row(m):
    # [z^k] F_m(z), F_m=(1+3z)F_(m-1)-2z^2 F_(m-2).
    prevprev = [1]
    if m == 0:
        return prevprev
    prev = [1, 3]
    if m == 1:
        return prev
    for _ in range(2, m + 1):
        cur = [0] * (len(prev) + 1)
        for i, a in enumerate(prev):
            cur[i] += a
            cur[i + 1] += 3 * a
        for i, a in enumerate(prevprev):
            cur[i + 2] -= 2 * a
        assert all(v >= 0 for v in cur)
        prevprev, prev = prev, cur
    return prev


def test():
    total_tested = 0
    observed = []
    for n in range(1, 9):
        m = n - 1
        masks = list(range(1 << m))
        longest = {mask: parabolic_longest(n, mask) for mask in masks}
        idem = set()
        for w in permutations(range(1, n + 1)):
            total_tested += 1
            if demazure(w, w) == w:
                idem.add(w)
        assert idem == set(longest.values()), (n, 'idempotent classification')
        counts = [0] * (m + 1)
        for j in masks:
            for k in masks:
                xy = demazure(longest[j], longest[k])
                yx = demazure(longest[k], longest[j])
                actual = xy == yx
                expected = allowed(j, k, m)
                assert actual == expected, (n, j, k, xy, yx)
                if actual:
                    counts[(j | k).bit_count()] += 1
        assert counts == coefficient_row(m), (n, counts, coefficient_row(m))
        observed.append(sum(counts))
    assert observed == [1, 4, 14, 48, 164, 560, 1912, 6528]
    print('ALL_TYPE_A_HECKE_IDEMPOTENT_CHECKS_PASSED', total_tested, observed)


if __name__ == '__main__':
    test()
