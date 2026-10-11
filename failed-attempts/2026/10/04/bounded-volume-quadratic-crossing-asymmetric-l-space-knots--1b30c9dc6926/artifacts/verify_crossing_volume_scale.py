#!/usr/bin/env python3
"""Arithmetic regression for the exact crossing formula and density scale.

The topological inputs are proved in the cited literature. This script only
checks the algebraic identities used in the packaged theorem.
"""
pairs = 0
for m in range(3, 103):
    b = m + 2
    for n in range(1, 101):
        word_length = (m+1)*((m+2)*n+2) + (m+1) + 4
        two_g = (m*m + 3*m + 2)*n + 2*m + 6
        lower = two_g + b - 1
        closed = (m+1)*(m+2)*n + 3*m + 7
        bform = b*(b-1)*n + 3*b + 1
        assert word_length == lower == closed == bform
        if n == 1:
            assert bform == (b+1)**2
        pairs += 1

print(
    "VERIFY_OK "
    f"pairs={pairs} "
    "crossing_identity=true "
    "n1_square_identity=true"
)
