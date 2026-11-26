"""Exact finite cross-check for a prime-support theorem on Euler/Dedekind composition.

The universal inequality is proved mathematically; this program tests only bounded integers.
No external packages required. Run: python verify_sandor_support.py
"""


def smallest_prime_factors(bound):
    spf = list(range(bound + 1))
    for p in range(2, int(bound**0.5) + 1):
        if spf[p] == p:
            for j in range(p * p, bound + 1, p):
                if spf[j] == j:
                    spf[j] = p
    return spf


def phi_sieve(bound):
    phi = list(range(bound + 1))
    for p in range(2, bound + 1):
        if phi[p] == p:
            for j in range(p, bound + 1, p):
                phi[j] -= phi[j] // p
    return phi


def check(bound=300000):
    spf = smallest_prime_factors(bound)
    psi = [0] * (bound + 1)
    omega = [0] * (bound + 1)
    psi[1] = 1
    for n in range(2, bound + 1):
        p = spf[n]
        m = n // p
        same = m > 1 and m % p == 0
        psi[n] = psi[m] * (p if same else p + 1)
        omega[n] = omega[m] + (0 if same else 1)
    phi = phi_sieve(max(psi))
    equalities = []
    positives = []
    qualified = 0
    for n in range(3, bound + 1):
        f = phi[psi[n]]
        if omega[n] <= 5:
            qualified += 1
            assert f * 385 <= 384 * n, (n, f)
            if f * 385 == 384 * n:
                equalities.append(n)
                m = n
                for p in (2, 3):
                    while m % p == 0:
                        m //= p
                assert m == 5 * 7 * 11 and n % (2 * 3) == 0, n
        if f > n:
            positives.append(n)
            assert omega[n] >= 6, n
    expected = []
    for a in range(1, 30):
        for b in range(1, 30):
            n = (2**a) * (3**b) * 385
            if n <= bound:
                expected.append(n)
    assert sorted(equalities) == sorted(expected), (equalities, expected)
    assert phi[psi[2]] == 2
    assert psi[2310] == 6912 and phi[psi[2310]] == 2304
    assert psi[39270] == 124416 and phi[psi[39270]] == 41472
    assert positives and positives[0] == 39270, positives[:5]
    print('VERIFY_OK', 'range=3..' + str(bound), 'omega_le5_checked=' + str(qualified),
          'sharp_equalities=' + repr(equalities), 'first_positive=' + str(positives[0]),
          'positive_count=' + str(len(positives)), 'exception=2')


if __name__ == '__main__':
    check()
