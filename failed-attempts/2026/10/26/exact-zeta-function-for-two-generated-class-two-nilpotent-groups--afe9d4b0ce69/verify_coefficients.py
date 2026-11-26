#!/usr/bin/env python3
"""Check the first twenty coefficients of the local zeta factor only."""

def coefficients(nmax):
    c = [0] * (nmax + 1)
    c[0] = 1
    for degree in (1, 2, 3, 3, 4):
        for n in range(degree, nmax + 1):
            c[n] += c[n - degree]
    return c

expected = [1, 1, 2, 4, 6, 8, 13, 17, 23, 31, 40, 50, 65, 79, 97, 119, 143, 169, 203, 237]
actual = coefficients(19)
assert actual == expected, (actual, expected)
print("LOCAL_COEFFICIENTS_OK", actual)
