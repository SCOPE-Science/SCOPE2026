"""Independent numerical consistency checks for a sine-forced skew-product threshold.

Run with `python check_threshold.py` (Python standard library only).
The proof of the dimension-uniform results is mathematical, not computational.
"""
import math

PI = math.pi
M = 2 / PI
V = 0.5 - M * M
TAU = 4 / (3 * PI) - 3 * M / 2 + 2 * M ** 3
c1_moment = V / (2 * M * M)
c2_moment = 3 * V ** 2 / (4 * M ** 4) - TAU / (3 * M ** 3)
c1_closed = PI * PI / 16 - 0.5
c2_closed = 3 * PI ** 4 / 256 - 17 * PI ** 2 / 144 + 1 / 12
assert abs(c1_moment - c1_closed) < 1e-13
assert abs(c2_moment - c2_closed) < 1e-13
assert c1_closed > 0 and c2_closed > 0

# The integrated Fourier series has only odd terms, with 1/n^3 coefficients.
ODD_N = 50001
odd_sum = sum(1 / n ** 3 for n in range(1, ODD_N + 1, 2))
zeta3 = sum(1 / n ** 3 for n in range(1, 120000))
assert abs(odd_sum - 7 * zeta3 / 8) < 3e-10
K2_series = 4 * math.exp(-8 * odd_sum / (PI * PI))

# Direct deterministic midpoint quadrature (no random seeds or external data).
def integral_2d(n):
    s = [math.sin(PI * (j + .5) / n) for j in range(n)]
    total = 0.
    for a in s:
        for b in s:
            total += math.log((a + b) / 2)
    return total / (n * n)

values = [integral_2d(n) for n in (64, 128, 256, 512)]
assert abs(math.exp(-values[-1]) - K2_series) < 3e-5
assert all(abs(values[j + 1] + math.log(K2_series)) < abs(values[j] + math.log(K2_series)) for j in range(3))
assert 1.70 < K2_series < 1.71
assert 2 > K2_series > PI/2

# The asymptotic expression predicts a strict improvement over its 1/d truncation.
for d in (50, 100, 250, 1000):
    a1 = math.log(PI / 2) + c1_closed / d
    a2 = a1 + c2_closed / (d*d)
    assert a2 > a1

print('PASS: moments, dimension coefficients, odd Fourier sum, and 2D quadrature')
print('K2 ~', format(K2_series, '.12f'))
print('c1 ~', format(c1_closed, '.12f'), 'c2 ~', format(c2_closed, '.12f'))
