"""Independent numerical and exact-Ramanujan checks of a semiprime Fourier sampler."""
from fractions import Fraction
from math import gcd, isqrt
import numpy as np


def primes_up_to(n):
    return [k for k in range(2, n + 1) if all(k % d for d in range(2, isqrt(k) + 1))]


def spectrum_formula(p, q):
    assert p < q and p in primes_up_to(p) and q in primes_up_to(q)
    k, s = divmod(q, p)
    assert 1 <= s < p
    phi = (p - 1) * (q - 1)
    a = Fraction(q, q - 1)
    U = a - Fraction(p * (k + 1), phi)
    V = a - Fraction(p * k, phi)
    W = a - Fraction(q + p - 2 * s, phi)
    values = [a] * (q - p + 1) + [U] * (s - 1) + [V] * (p - s - 1) + [W]
    assert len(values) == q
    return sorted(values)


def direct_gram(p, q):
    N = p * q
    units = np.array([a for a in range(N) if gcd(a, N) == 1], dtype=np.int64)
    sites = np.arange(q)
    mat = np.exp((2j * np.pi / N) * units[:, None] * sites[None, :]) / np.sqrt(len(units))
    return mat.conj().T @ mat


def arithmetic_gram(p, q):
    phi = (p - 1) * (q - 1)
    result = np.empty((q, q), float)
    for i in range(q):
        for j in range(q):
            d = i-j
            cp = (p-1) if d % p == 0 else -1
            cq = (q-1) if d % q == 0 else -1
            result[i, j] = cp * cq / phi
    return result


def check():
    pairs = [(p, q) for p in primes_up_to(13) for q in primes_up_to(67) if p < q]
    assertions = 0
    for p, q in pairs:
        gram = direct_gram(p, q)
        ag = arithmetic_gram(p, q)
        lam = np.linalg.eigvalsh(gram)
        expected = np.array([float(v) for v in spectrum_formula(p, q)])
        assert np.max(np.abs(gram - ag)) < 2e-12
        assert np.max(np.abs(lam - expected)) < 2e-12
        assert np.min(expected) >= -1e-13
        assertions += 3
        if p == 2:
            assert sum(x == 0 for x in spectrum_formula(p, q)) == 1
            assert np.max(np.abs(gram @ ((-1.) ** np.arange(q)))) < 2e-12
            assertions += 2
        else:
            s = q % p
            lower = Fraction(p - 2, p - 1) + Fraction(max(s - 2, 0), (p - 1) * (q - 1))
            assert spectrum_formula(p, q)[0] == lower
            assert spectrum_formula(p, q)[-1] == Fraction(q, q - 1)
            assertions += 2
    print(f"PASS: {len(pairs)} distinct-prime pairs, {assertions} checked assertions")


if __name__ == "__main__":
    check()
