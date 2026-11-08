"""Direct finite-field checks for the exact three-erasure Alltop-frame theorem.

Requires Python 3.10+ and NumPy. Execute: python CHECK.py
This is supplementary finite verification, not a proof for arbitrary primes.
"""
import itertools
import math
import cmath

import numpy as np


def primitive(p, x):
    return cmath.exp(2j * math.pi * (x % p) / p)


def character(p, n):
    return 1 if pow(n % p, (p - 1) // 2, p) == 1 else -1


def expected(p):
    angle = 0 if p % 4 == 1 else math.pi / (6 * p)
    return 1 + 2 * math.cos(angle) / math.sqrt(p)


def run():
    triples_checked = 0
    phases_checked = 0
    primes = (5, 7, 11, 13, 17, 19)
    for p in primes:
        g = np.array([primitive(p, j ** 3) for j in range(p)]) / math.sqrt(p)
        vectors = np.array([
            [primitive(p, b * t) * g[(t - a) % p] for t in range(p)]
            for a in range(p) for b in range(p)
        ], dtype=complex)
        gram = vectors.conj() @ vectors.T
        assert np.allclose(gram, gram.conj().T, atol=2e-12)
        assert np.allclose(vectors.conj().T @ vectors, p * np.eye(p), atol=2e-12)
        assert np.allclose(np.diag(gram), np.ones(p * p), atol=2e-12)
        top = -1
        if p <= 11:
            for inds in itertools.combinations(range(p * p), 3):
                eigen = np.linalg.eigvalsh(gram[np.ix_(inds, inds)])
                top = max(top, float(eigen[-1]))
                triples_checked += 1
            assert abs(top - expected(p)) < 1e-10, (p, top, expected(p))
        eps = 1 if p % 4 == 1 else 1j
        for a0, a1, a2 in itertools.combinations(range(p), 3):
            slope = [(-3 * a) % p for a in (a0, a1, a2)]
            P = (slope[1] - slope[0]) * (slope[2] - slope[1]) * (slope[0] - slope[2]) % p
            for b0, b1, b2 in ((0, 0, 0), (0, 1, 2), (1, 2, 3), (p - 1, 0, 0)):
                beta = [((3 * a * a) + b) % p for a, b in zip((a0, a1, a2), (b0, b1, b2))]
                R = (beta[0] * (slope[1] - slope[2])
                    + beta[1] * (slope[2] - slope[0])
                    + beta[2] * (slope[0] - slope[1])) % p
                rho = eps ** 3 * character(p, P) * primitive(p, R * R * pow(4 * P, -1, p))
                inds = [a * p + b for a, b in zip((a0, a1, a2), (b0, b1, b2))]
                direct = gram[inds[0], inds[1]] * gram[inds[1], inds[2]] * gram[inds[2], inds[0]] * p ** 1.5
                assert abs(direct - rho) < 1e-10, (p, inds, direct, rho)
                phases_checked += 1
        # Construct an attaining configuration, independently of exhaustive search.
        u = next(u for u in range(2, p) if character(p, u * (1 - u)) == 1)
        aa = (0, (-pow(3, -1, p)) % p, (-u * pow(3, -1, p)) % p)
        ss = (0, 1, u)
        P = u * (1 - u) % p
        Rtarget = 0 if p % 4 == 1 else next(r for r in range(p) if r * r % p == P)
        betas = (Rtarget * pow(1 - u, -1, p) % p, 0, 0)
        bs = tuple((betas[j] - 3 * aa[j] ** 2) % p for j in range(3))
        chosen = [aa[j] * p + bs[j] for j in range(3)]
        attained = np.linalg.eigvalsh(gram[np.ix_(chosen, chosen)])[-1]
        assert abs(attained - expected(p)) < 1e-10, (p, attained, expected(p))
        print(f"p={p} exact_bound={p-expected(p):.12f} attaining_erasures={list(zip(aa,bs))}")
    print(f"CHECK_OK primes={len(primes)} exhaustive_erasure_triples={triples_checked} direct_holonomies={phases_checked}")

if __name__ == '__main__':
    run()
