"""Finite diagnostic checks for dyadic 2-binomial rigidity of period-doubling factors.

Run with: python3 verify.py
The infinite theorem is proved symbolically in RESULT.md; these checks are not a proof.
"""


def period_doubling(n):
    v = n + 1
    e = 0
    while (v & 1) == 0:
        v >>= 1
        e += 1
    return e & 1


def signature(word):
    weight = sum(word)
    moment = sum(j for j, x in enumerate(word) if x)
    return (weight, moment)


def scattered_pair_counts(word):
    out = {(a, b): 0 for a in (0, 1) for b in (0, 1)}
    for i in range(len(word)):
        for j in range(i + 1, len(word)):
            out[(word[i], word[j])] += 1
    return out


def main():
    windows_checked = 0
    direct_pair_checks = 0
    for k in range(12):
        n = 1 << k
        p = tuple(period_doubling(i) for i in range(7 * n))
        factors = set()
        profiles = {}
        for start in range(2 * n):
            word = p[start:start + n]
            s = signature(word)
            if s in profiles:
                assert profiles[s] == word, (k, start, profiles[s], word)
            else:
                profiles[s] = word
            factors.add(word)
            windows_checked += 1
        target = 2 if k == 0 else 3 * n // 2
        assert len(factors) == len(profiles) == target, (k, len(factors), target)
        assert len({s[0] for s in profiles}) == 2, k
        for start in range(2 * n, 6 * n):
            assert p[start:start + n] in factors, (k, start)
            windows_checked += 1
        if k <= 4:
            for word in factors:
                m, moment = signature(word)
                counts = scattered_pair_counts(word)
                assert counts[(0, 1)] == moment - m * (m - 1) // 2
                assert counts[(1, 0)] == m * (n - m) - counts[(0, 1)]
                assert counts[(0, 0)] == (n - m) * (n - m - 1) // 2
                assert counts[(1, 1)] == m * (m - 1) // 2
                direct_pair_checks += 1
        if k >= 1:
            v = tuple(period_doubling(i) for i in range(n - 1))
            a0, a1 = v + (0,), v + (1,)
            e = (k - 1) & 1
            periodic = a0 if e == 0 else a1
            primitive = a1 if e == 0 else a0
            assert sum(primitive) % 2 == 1
            assert periodic[:n // 2] == periodic[n // 2:]
            if k > 1:
                assert sum(periodic[:n // 2]) % 2 == 1
            assert {word for a in (a0, a1) for word in
                    (a[r:] + a[:r] for r in range(n))} == factors
    assert (1, 0, 0, 0, 1) != (0, 1, 0, 1, 0)
    assert signature((1, 0, 0, 0, 1)) == signature((0, 1, 0, 1, 0))
    p = tuple(period_doubling(i) for i in range(128))
    assert (1, 0, 0, 0, 1) in {p[i:i + 5] for i in range(124)}
    assert (0, 1, 0, 1, 0) in {p[i:i + 5] for i in range(124)}
    print('VERIFY_OK levels=0..11 windows_checked={} pair_checks={} five_factor_collision=confirmed'.format(
        windows_checked, direct_pair_checks))


if __name__ == '__main__':
    main()
