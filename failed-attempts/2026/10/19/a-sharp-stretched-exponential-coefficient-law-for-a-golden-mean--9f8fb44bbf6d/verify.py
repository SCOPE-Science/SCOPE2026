#!/usr/bin/env python3
"""Exact short-index checks and numerical diagnostics for a dihedral zeta law.

Only Python standard-library modules are used. Finite tests do not prove the
asymptotic statement; that proof is analytical in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import exp, pi, sqrt


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def cyclic_words(n):
    for word in product((0, 1), repeat=n):
        if all(word[j] * word[(j + 1) % n] == 0 for j in range(n)):
            yield word


def reflection_count(word_list, n, j):
    return sum(all(w[i] == w[(j - i) % n] for i in range(n)) for w in word_list)


def recurrence_r(n):
    # P(z) R(z) = z + 2z^2 + z^3 + z^4.
    r = [0] * (n + 1)
    numer = {1: 1, 2: 2, 3: 1, 4: 1}
    for k in range(1, n + 1):
        r[k] = numer.get(k, 0)
        if k >= 2:
            r[k] += r[k - 2]
        if k >= 4:
            r[k] += r[k - 4]
    return r


def independent_exact_coefficients(M):
    # The logarithmic series comes from subgroup fixed-point numbers, not
    # from algebraic expansion of the asserted closed form.
    la = [Fraction(0)] * (M + 1)
    for n in range(1, M + 1):
        # Averaged reflection fixed-point counts.
        la[n] = Fraction(fibonacci(n // 2 + 2))
        if n % 2 == 0:
            m = n // 2
            lucas_m = fibonacci(m - 1) + fibonacci(m + 1)
            la[n] += Fraction(lucas_m, n)
    co = [Fraction(1)] + [Fraction(0)] * M
    for n in range(1, M + 1):
        co[n] = sum(k * la[k] * co[n - k] for k in range(1, n + 1)) / n
    return la, co


def check():
    n_bru = 13
    comparisons = 0
    for n in range(1, n_bru + 1):
        words = list(cyclic_words(n))
        lucas = fibonacci(n - 1) + fibonacci(n + 1)
        assert len(words) == lucas, (n, len(words), lucas)
        for j in range(n):
            observed = reflection_count(words, n, j)
            if n % 2:
                predicted = fibonacci((n + 3) // 2)
            else:
                m = n // 2
                predicted = fibonacci(m + 3) if j % 2 == 0 else fibonacci(m)
            assert observed == predicted, (n, j, observed, predicted)
            comparisons += 1

    M = 35
    rec = recurrence_r(M)
    for n in range(1, M + 1):
        assert rec[n] == fibonacci(n // 2 + 2)
    loga, coeffs = independent_exact_coefficients(M)
    for n in range(1, M + 1):
        assert loga[n] == Fraction(rec[n]) + (
            Fraction(fibonacci(n // 2 - 1) + fibonacci(n // 2 + 1), n)
            if n % 2 == 0 else Fraction(0)
        )
    assert coeffs[0:6] == [
        Fraction(1), Fraction(1), Fraction(3), Fraction(14, 3),
        Fraction(61, 6), Fraction(163, 10)
    ], coeffs[:6]

    phi = (1 + sqrt(5)) / 2
    rho = phi ** -0.5
    u = rho * rho
    p = 2 * u + 4 * u * u
    N = lambda z: z + 2*z*z + z**3 + z**4
    dN = lambda z: 1 + 4*z + 3*z*z + 4*z**3
    A = N(rho) / p
    Am = N(-rho) / p
    B = -rho * dN(rho) / p + N(rho) * (u + 6*u*u) / (p*p)
    C = exp(B + A / 2) / (2 * sqrt(pi * p))
    assert 0 < Am < A
    assert abs(A - 1.04563122925493147) < 2e-14
    assert abs(C - 0.08988631850254084) < 2e-14

    # Coefficients are computed from an independent periodic+reflection
    # logarithm. Radius-normalize to suppress exponential growth.
    M2 = 1200
    fib = [0, 1]
    for _ in range(M2 // 2 + 4):
        fib.append(fib[-1] + fib[-2])
    alpha = [0.0] * (M2 + 1)
    for n in range(1, M2 + 1):
        value = fib[n // 2 + 2]
        if n % 2 == 0:
            k = n // 2
            value += (fib[k-1] + fib[k+1]) / n
        alpha[n] = value * rho**n
    coeff = [1.0] + [0.0]*M2
    for n in range(1, M2 + 1):
        coeff[n] = sum(k * alpha[k] * coeff[n-k] for k in range(1,n+1)) / n
    ratios = {}
    for n in (100, 200, 400, 800, 1200):
        approximate = C * exp(2*sqrt(A*n)) / sqrt(n)
        ratios[n] = coeff[n] / approximate
    assert ratios[1200] < 1.03 and ratios[1200] > 1.0
    assert all(abs(ratios[b]-1) < abs(ratios[a]-1)
               for a, b in zip((100, 200, 400, 800), (200, 400, 800, 1200)))
    print('VERIFY_OK: 91 exact reflection checks; 35 rational generating checks;')
    print('first coefficients:', ', '.join(str(x) for x in coeffs[:6]))
    print('A=', format(A,'.14f'), 'C=',format(C,'.14f'), 'Aminus=',format(Am,'.14f'))
    print('scaled coefficient/asymptotic ratios:',
          ', '.join(f'{n}:{ratios[n]:.6f}' for n in ratios))
    return True


if __name__ == '__main__':
    check()
