#!/usr/bin/env python3
"""Exact finite checks for the stated derangement ternary residue theorem."""
from math import factorial


def square_count(k):
    s = [1, 2]
    for i in range(2, max(k + 1, 2)):
        s.append(3 ** (i - 1) + s[i - 2])
    return s[k]


def expected(k):
    if k == 1:
        return 3
    return 2 * 3 ** (k - 1) + 2 * square_count(k - 2) - 3 ** max(k - 5, 0)


def finite_derivatives(x, q, count):
    val = deriv = second = 0
    p, dp, d2p = 1, 0, 0
    for j in range(count):
        sign = -1 if j & 1 else 1
        val = (val + sign * p) % q
        deriv = (deriv + sign * dp) % q
        second = (second + sign * d2p) % q
        d2p = (d2p * (x - j) + 2 * dp) % q
        dp = (dp * (x - j) + p) % q
        p = p * (x - j) % q
    return val, deriv, second


def main():
    found = []
    for k in range(1, 9):
        q = 3 ** k
        values = set()
        even, odd = set(), set()
        d = 1
        for n in range(2 * q):
            values.add(d)
            (even if n % 2 == 0 else odd).add(d)
            d = ((n + 1) * d + (-1 if (n + 1) % 2 else 1)) % q
        assert d == 1, (k, "period-end")
        assert len(values) == expected(k), (k, len(values), expected(k))
        assert len(values) == len(even | odd)
        if k >= 2:
            critical = 1
            for j in range(1, k):
                modulus = 3 ** (j + 1)
                candidate = [critical + a * 3 ** j for a in range(3)
                             if finite_derivatives(critical + a * 3 ** j, modulus, 6 * k + 40)[1] == 0]
                assert len(candidate) == 1
                critical = candidate[0]
            fv = finite_derivatives(critical, q, 6 * k + 40)[0]
            square_modulus = q // 9
            squares = {(a * a) % square_modulus for a in range(square_modulus)}
            structural = {a for a in range(q) if a % 3 != 0}
            structural.update((fv + 9 * s) % q for s in squares)
            structural.update((-fv - 9 * s) % q for s in squares)
            assert structural == values, (k, "square-translate image")
        # The 3-adic interpolation agrees with the signed sequence on integer indices.
        for n in range(min(q, 10)):
            interpolated = finite_derivatives(n, q, 6 * k + 20)[0]
            recurrence = 1
            for i in range(1, n + 1):
                recurrence = (i * recurrence + (-1 if i & 1 else 1)) % q
            assert interpolated == (recurrence if n % 2 == 0 else -recurrence) % q
        found.append(len(values))
    q = 3 ** 8
    length = 6 * 8 + 40
    f0, fp0, fpp0 = finite_derivatives(0, q, length)
    f1, fp1, fpp1 = finite_derivatives(1, q, length)
    assert f0 == 1 and f1 == 0
    assert fp0 % 3 == 2
    assert fp1 % 27 == 9
    assert fpp0 % 3 == 0
    assert fpp1 % 3 == 2
    c = 1
    for j in range(1, 8):
        modulus = 3 ** (j + 1)
        choices = [c + digit * 3 ** j for digit in range(3)
                   if finite_derivatives(c + digit * 3 ** j, modulus, length)[1] == 0]
        assert len(choices) == 1, (j, choices)
        c = choices[0]
    assert c % 9 == 1 and (c - 1) // 9 % 3 == 1
    fc = finite_derivatives(c, q, length)[0]
    assert fc % 81 == 0 and (fc // 81) % 3 == 2
    print("VERIFY_OK powers=1..8 residue_counts=" + ",".join(map(str, found)) +
          " derivative_certificates=PASS critical_value=PASS")


if __name__ == "__main__":
    main()
