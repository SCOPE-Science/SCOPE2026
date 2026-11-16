"""Finite consistency checks for the three-tap cross-STFT support law.

No numerical experiment is used to justify its universal lower bound.
"""
import cmath
import itertools
import math


def stft(p, f, g):
    """Return the support size and the zero counts on the nonzero shift rows."""
    zeta = cmath.exp(-2j * math.pi / p)
    total = 0
    details = {}
    for x in range(p):
        terms = [(t, a * g[(t - x) % p].conjugate())
                 for t, a in enumerate(f) if a and g[(t-x)%p]]
        if not terms:
            continue
        count = 0
        for k in range(p):
            v = sum(c * (zeta ** (k * t)) for t, c in terms)
            if abs(v) < 2e-8:
                count += 1
        assert count <= len(terms) - 1, (p, x, terms, count)
        total += p - count
        details[x] = (len(terms), count)
    return total, details


def vector(p, sites, coeff):
    out = [0j] * p
    for s, c in zip(sites, coeff):
        out[s % p] = complex(c)
    return out


def examples(p):
    s = math.sqrt(2 * math.cos(2 * math.pi / p))
    cases = [
        (0, [1, 1, 1], [1, 1, 1]),
        (1, [1, 1, 1], [1, -1, 2]),
        (2, [1, -1, 1], [1, 1, 1]),
        (3, [1, -math.sqrt(2), 1], [1, math.sqrt(2), 1]),
        (4, [1, -s, 1], [1, s, 1]),
    ]
    for zeros, ff, gg in cases:
        f = vector(p, [0, 1, 2], ff)
        g = vector(p, [0, 1, 2], gg)
        count, detail = stft(p, f, g)
        assert count == 5*p-zeros, (p, zeros, count, detail)
        assert sum(v[1] for v in detail.values()) == zeros
        print('p', p, 'five-row-zero-count', zeros, 'support', count)
    f = vector(p, [0, 1, 2], [1, -1, 1])
    g = vector(p, [0, 1, 3], [1, 1, -1])
    count, detail = stft(p, f, g)
    assert count == 6*p-3, (p, count, detail)
    print('p', p, 'six-row-onset', count)


def is_ap(s, p):
    return {d for d in range(1, p) if any(
        {(a % p), ((a+d) % p), ((a+2*d) % p)} == s for a in s)}


def support_geometry(p):
    triples = [frozenset(s) for s in itertools.combinations(range(p), 3)]
    ap_steps = {s: is_ap(set(s), p) for s in triples}
    pair_count = 0
    h5 = 0
    for F in triples:
        for G in triples:
            h = len({(a-b) % p for a in F for b in G})
            assert h >= 5, (p,F,G,h)
            assert (p+1)*h-9 >= 5*p-4
            if h == 5:
                h5 += 1
                assert ap_steps[F].intersection(ap_steps[G]), (p,F,G)
            else:
                assert (p+1)*h-9 >= 6*p-3
            pair_count += 1
    print('p',p,'support-pair-geometries',pair_count,'five-row-geometries',h5)


if __name__ == '__main__':
    for p in (7, 11, 13, 17, 23, 31):
        examples(p)
    for p in (7, 11, 13):
        support_geometry(p)
    print('THREE_TAP_CROSS_STFT_PASS')
