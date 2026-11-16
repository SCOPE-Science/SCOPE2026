"""Independent Boolean Möbius-transform and monomial-to-Walsh verification.
Run: python3 verify_mobius.py (standard library only)."""
from math import gcd


def indicator(mask, n, k):
    forbidden = (1 << k) - 1
    return int(all(((mask >> j) & forbidden) != forbidden for j in range(n-k+1)))


def coefficients_from_mobius(n, k):
    coeff = [indicator(x, n, k) for x in range(1 << n)]
    for bit in range(n):
        for mask in range(1 << n):
            if mask >> bit & 1:
                coeff[mask] -= coeff[mask ^ (1 << bit)]
    return coeff


def predicted_coefficient(mask, n, k):
    product = 1
    i = 0
    while i < n:
        if not (mask >> i & 1):
            i += 1
            continue
        j = i
        while j < n and (mask >> j & 1):
            j += 1
        r = (j-i) % (k+1)
        if r == k:
            product = -product
        elif r != 0:
            return 0
        i = j
    return product


def main():
    cases = 0
    exact_characters = 0
    for k in range(2, 8):
        for n in range(0, 12):
            coefficients = coefficients_from_mobius(n, k)
            assert all(c == predicted_coefficient(m, n, k)
                       for m, c in enumerate(coefficients)), (n, k, 'coefficients')
            d = max(m.bit_count() for m,c in enumerate(coefficients) if c)
            r = n % (k + 1)
            expected_degree = n if r in (0, k) else n-r
            assert d == expected_degree, (n, k, d, expected_degree)
            if n <= 9:
                for freq in range(1 << n):
                    direct = sum((-1)**((freq & x).bit_count()) * indicator(x,n,k)
                                 for x in range(1 << n))
                    formula = (-1)**freq.bit_count() * sum(
                        c * (1 << (n - mask.bit_count()))
                        for mask, c in enumerate(coefficients)
                        if c and (mask & freq) == freq)
                    assert formula == direct, (n, k, freq, formula, direct)
                    exact_characters += 1
            cases += 1
    print('MOBIUS_RUN_CLASSIFICATION_PASS', cases, exact_characters)


if __name__ == '__main__':
    main()
