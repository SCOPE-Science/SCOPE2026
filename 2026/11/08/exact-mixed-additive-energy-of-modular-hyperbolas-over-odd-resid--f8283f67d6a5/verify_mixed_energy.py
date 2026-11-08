"""Independent finite checks for exact mixed energy of modular hyperbolas.

Run with Python 3.8+; only standard-library modules are required.
"""
from collections import Counter
from math import gcd
from random import Random


def local_formula(p, k, lam, mu):
    modulus = p ** k
    if gcd(lam * mu, p) != 1:
        raise ValueError("both parameters must be units")
    difference = (lam - mu) % modulus
    valuation = 0
    while valuation < k and difference % p == 0:
        difference //= p
        valuation += 1
    scale = (p - 1) * p ** (2 * k - 2)
    if valuation == 0:
        chi = 1 if pow((lam * mu) % p, (p - 1) // 2, p) == 1 else -1
        return scale * (2 * p - 5 - chi + (k - 1) * (p - 1) * (1 + chi))
    return scale * (3 * p - 7 + 2 * (k - 1) * (p - 1)
                    + (valuation - 1) * (p - 1) + (valuation == k))


def differences(modulus, parameter):
    points = [(x, (parameter * pow(x, -1, modulus)) % modulus)
              for x in range(modulus) if gcd(x, modulus) == 1]
    counts = Counter()
    for x, y in points:
        for u, v in points:
            counts[((x - u) % modulus, (y - v) % modulus)] += 1
    return counts


def direct_energy(modulus, lam, mu):
    a = differences(modulus, lam)
    b = differences(modulus, mu)
    return sum(count * b[key] for key, count in a.items())


def factor_odd(n):
    factors = []
    d = 3
    while d * d <= n:
        if n % d == 0:
            k = 0
            while n % d == 0:
                k += 1
                n //= d
            factors.append((d, k))
        d += 2
    if n > 1:
        factors.append((n, 1))
    return factors


def global_formula(modulus, lam, mu):
    product = 1
    for p, k in factor_odd(modulus):
        product *= local_formula(p, k, lam, mu)
    return product


def singular_direct_count(p, k, epsilon):
    q = p ** k
    els = range(0, q, p)
    return sum(1 for a in els for b in els if (a * b + epsilon) % q == 0)


def singular_formula(p, k, epsilon):
    q = p ** k
    d = epsilon % q
    v = 0
    while v < k and d % p == 0:
        d //= p
        v += 1
    if v == k:
        return (1 + (k - 1) * (p - 1)) * p ** (k - 1)
    if v < 2:
        return 0
    return (v - 1) * (p - 1) * p ** (k - 1)


def main():
    rng = Random(32291)
    cases = [(3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
             (5, 1), (5, 2), (5, 3), (7, 1), (7, 2),
             (11, 1), (11, 2), (13, 1)]
    compared = 0
    for p, k in cases:
        q = p ** k
        units = [a for a in range(q) if a % p]
        trials = [(1, 1), (1, 1 + p), (1, 1 + p ** 2),
                  (1, 1 + p ** 3), (1, 1 + p ** 4), (1, 2)]
        if q <= 27:
            trials += [(x, y) for x in units for y in units]
        else:
            trials += [(rng.choice(units), rng.choice(units)) for _ in range(12)]
        for lam, mu in trials:
            if lam % p == 0 or mu % p == 0:
                continue
            actual = direct_energy(q, lam, mu)
            predicted = local_formula(p, k, lam, mu)
            if actual != predicted:
                raise AssertionError((p, k, lam, mu, actual, predicted))
            compared += 1
    crt_comparisons = 0
    for n in (15, 21, 45, 75, 99, 105, 135):
        for lam, mu in ((1, 1), (1, 2), (2, 7), (4, 8), (11, 17)):
            if gcd(n, lam * mu) != 1:
                continue
            actual = direct_energy(n, lam, mu)
            predicted = global_formula(n, lam, mu)
            if actual != predicted:
                raise AssertionError((n, lam, mu, actual, predicted))
            crt_comparisons += 1
    singular_compared = 0
    for p, k in ((3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
                 (5, 1), (5, 2), (5, 3), (7, 2), (7, 3)):
        q = p ** k
        for epsilon in (0, p, p ** 2, p ** 3, p ** 4, q - p, 2 * p):
            if singular_direct_count(p, k, epsilon) != singular_formula(p, k, epsilon):
                raise AssertionError((p, k, epsilon))
            singular_compared += 1
    print("VERIFY_OK local_parameter_pairs=", compared,
          "crt_comparisons=", crt_comparisons,
          "singular_product_cases=", singular_compared,
          "independent_difference_enumeration=PASS")


if __name__ == "__main__":
    main()
