#!/usr/bin/env python3
"""Exact finite checks for short circular Bernoulli run-count covariance."""
from fractions import Fraction

CASES = 0
for n in range(7, 14):
    for R in range(2, min(4, (n - 3) // 2) + 1):
        for p in (Fraction(1, 4), Fraction(2, 5), Fraction(4, 5)):
            q = 1 - p
            a = [q * q * p ** r for r in range(1, R + 1)]
            means = [Fraction(0) for _ in range(R)]
            mixed = [[Fraction(0) for _ in range(R)] for _ in range(R)]
            for mask in range(1 << n):
                ones = mask.bit_count()
                weight = p ** ones * q ** (n - ones)
                counts = [0] * R
                if ones != n:
                    for k in range(n):
                        if (mask >> ((k - 1) % n)) & 1:
                            continue
                        if not ((mask >> k) & 1):
                            continue
                        length = 0
                        while (mask >> ((k + length) % n)) & 1:
                            length += 1
                        if 1 <= length <= R:
                            counts[length - 1] += 1
                for j in range(R):
                    means[j] += weight * counts[j]
                    for k in range(R):
                        mixed[j][k] += weight * counts[j] * counts[k]
            for j in range(R):
                assert means[j] == n * a[j]
                CASES += 1
                for k in range(R):
                    actual = mixed[j][k] - means[j] * means[k]
                    expected = n * (a[j] if j == k else 0) + n * a[j] * a[k] * (2 / q - j - k - 5)
                    assert actual == expected, (n, R, p, j, k)
                    # Divide by n*a_j*a_k: rationalized H-I.
                    residual = actual / (n * a[j] * a[k]) - (1 / a[j] if j == k else 0)
                    assert residual == 2 / q - j - k - 5
                    CASES += 2
            A = sum(a)
            B = sum((j + 1) * aj for j, aj in enumerate(a))
            C = sum((j + 1) ** 2 * aj for j, aj in enumerate(a))
            delta = A * C - B * B
            assert delta > 0
            tau = (2 / q - 3) * A - 2 * B
            assert tau * tau + 4 * delta > 0
            CASES += 2
print(f"PASS: {CASES} exact arithmetic assertions (plus complete word enumerations)")
