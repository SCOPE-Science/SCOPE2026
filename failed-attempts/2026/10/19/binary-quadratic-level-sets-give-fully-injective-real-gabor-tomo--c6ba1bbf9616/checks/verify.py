"""Exact finite checks for real Gabor tomography from binary quadratic level sets.

Run: python3 checks/verify.py. Standard-library only. This is corroboration for
small dimensions; the proof of the general theorem is mathematical.
"""
from collections import Counter


def parity(z):
    return z.bit_count() & 1


def model(m, anisotropic, level):
    n = 2 * m
    N = 1 << n
    mask = (1 << m) - 1

    def q(x):
        u = x & mask
        v = x >> m
        return parity(u & v) ^ (anisotropic & (u & 1)) ^ (anisotropic & (v & 1))

    def polar_index(a):
        return ((a & mask) << m) | (a >> m)

    sigma = sum(1 - 2 * q(x) for x in range(N)) // (1 << m)
    assert sigma in (-1, 1)
    rho = (1 - 2 * level) * sigma
    K = N // 2 + rho * (1 << (m - 1))
    L = N // 4 + rho * (1 << (m - 1))
    h = 1 << (m - 1)
    support = tuple(x for x in range(N) if q(x) == level)
    assert len(support) == K

    counts = Counter()
    for a in range(N):
        for b in range(N):
            actual = sum((1 - 2 * parity(b & x)) for x in support if q(x ^ a) == level)
            if a == 0 and b == 0:
                modulus = K
            elif a and b in (0, polar_index(a)):
                modulus = L
            elif not parity(a & b):
                modulus = h
            else:
                modulus = 0
            assert abs(actual) == modulus, (m, anisotropic, level, a, b, actual, modulus)
            counts[modulus] += 1

    # Count the symmetric nonzero Weyl coefficients, and the predicted spectrum.
    rank = sum(1 for a in range(N) for b in range(N)
               if (a == b == 0) or
               (a != 0 and b in (0, polar_index(a)) and L > 0) or
               (not parity(a & b) and b not in (0, polar_index(a)) and a != 0) or
               (a == 0 and b != 0))
    assert rank == (N * (N + 1) // 2 if L else N)
    assert sum(counts.values()) == N * N
    assert counts[0] == N * (N - 1) // 2 + (0 if L else 2 * (N - 1))

    if m == 2 and rho == -1:
        # In this case the exact second-moment identity is
        # 36 * sum_P tr(XP) P = 64 X + 32 tr(X) I
        # for all real symmetric 16-by-16 matrices X. Check on its basis
        # E_ii and E_ij+E_ji using integer arithmetic only.
        assert (N, K, L, h) == (16, 6, 2, 2)
        orbit = []
        for a in range(N):
            for b in range(N):
                w = tuple((1 - 2 * parity(b & x)) if q(x ^ a) == level else 0
                          for x in range(N))
                orbit.append(w)
        for i in range(N):
            for j in range(i, N):
                target = [[0] * N for _ in range(N)]
                for w in orbit:
                    scalar = w[i] * w[i] if i == j else 2 * w[i] * w[j]
                    if not scalar:
                        continue
                    active = [k for k in range(N) if w[k]]
                    for k in active:
                        for ell in active:
                            target[k][ell] += scalar * w[k] * w[ell]
                for k in range(N):
                    for ell in range(N):
                        expected = (64 if (k, ell) == (i, j) else 0)
                        if i != j and (k, ell) == (j, i):
                            expected += 64
                        if i == j and k == ell:
                            expected += 32
                        assert target[k][ell] == expected, (i, j, k, ell, target[k][ell], expected)

    print("CHECK_OK", m, anisotropic, level, sigma, rho, N, K, L, h, sorted(counts.items()))


if __name__ == "__main__":
    for mm in (1, 2, 3):
        for aa in (0, 1):
            for ee in (0, 1):
                model(mm, aa, ee)
    print("VERIFY_OK")
