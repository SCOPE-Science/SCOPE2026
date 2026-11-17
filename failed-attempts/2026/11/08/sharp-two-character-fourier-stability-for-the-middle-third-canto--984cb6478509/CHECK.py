"""Reproducibility checks for the sharp two-character Cantor Gram theorem.

The universal assertion is proved analytically in RESULT.md; this program
checks the finite residue mechanism, elementary certificate margins, and
independently calculated Fourier and Gram values. Python 3 standard library.
"""
import cmath
import math

count = 0
pi = math.pi

def check(b):
    global count
    assert b
    count += 1


def fourier_mod(n, depth=34):
    p = 1.0
    for j in range(1, depth + 1):
        p *= abs(math.cos(2 * pi * ((n % 3**j) / 3**j)))
    return p

C = fourier_mod(1, 44)
check(1/3 < C < 3/8)
check(7/16 * 3/4 < 1/3)
check(0.5 + 2*pi/27 < 3/4)
check(0.5 + pi/27 < 2/3)
check(0.5 * math.cos(2*pi/9) < 7/16)
check(0.5 * math.cos(pi/9) < 1/2)
check(0.5 * math.cos(4*pi/9) < 1/3)

# Enumerate all possible survivors of the finite-product threshold.
survivors = {}
for k in range(2, 16):
    modulus = 3 ** k
    expected = {1, modulus - 1, (modulus - 1)//2, (modulus + 1)//2}
    if k == 2:
        candidates = [n for n in range(1, modulus) if n % 3]
        previous = {n for n in candidates if fourier_mod(n, k) > C}
    else:
        candidates = {(n + j * (modulus//3)) for n in previous for j in range(3)}
        previous = {n for n in candidates if fourier_mod(n, k) > C}
    check(previous == expected)
    survivors[k] = tuple(sorted(previous))

# Independent calculation of the full infinite-product approximants.
for n in range(1, 15001):
    v = fourier_mod(n, 32)
    check(v <= C + 1e-11)
    m = n
    while m % 3 == 0:
        m //= 3
    if m == 1:
        check(abs(v - C) < 1e-11)
    else:
        check(v < C - 1e-7)

# Gram matrices from direct numerical quadrature on finite Cantor point clouds.
# Take Fourier values via independent finite digit expansion (not cos product).
for gap in [1, 2, 3, 4, 5, 7, 9, 10, 12, 13, 27, 39, 81]:
    vals = [0.0]
    for j in range(1, 13):
        delta = 2 / 3**j
        vals = [z for x in vals for z in (x, x+delta)]
    avg = sum(cmath.exp(2j * pi * gap * x) for x in vals) / len(vals)
    value = abs(avg)
    check(abs(value - fourier_mod(gap, 12)) < 3e-11)
    eig_min, eig_max = 1 - value, 1 + value
    check(eig_min > 0 and eig_max >= eig_min)
    check(eig_min >= 1 - C - 1e-6)
    check(eig_max <= 1 + C + 1e-6)

print(f'PASS: {count} checked assertions; C={C:.15f}, A={1-C:.15f}, ratio={(1+C)/(1-C):.15f}')
