"""Finite exact checks for coefficient identities in bilateral weighted shifts.

All infinite-dimensional assertions in the accompanying result are proved analytically.
This script checks finite rational identities only; it is not an infinite proof.
"""
from fractions import Fraction

CHECKS = 0

def equal(actual, expected, description):
    global CHECKS
    if actual != expected:
        raise AssertionError((description, actual, expected))
    CHECKS += 1


def weights(j):
    if j <= 0:
        return Fraction(1)
    # Positive, bounded, nonmonotone across several adjacent levels.
    return Fraction(1, 2 ** (j // 2 + (j % 4 == 0) * 2))


def W(k):
    if k <= 1:
        return Fraction(1)
    v = Fraction(1)
    for j in range(1, k):
        v *= weights(j)
    return v


def forward(x):
    y = {}
    for j, v in x.items():
        y[j + 1] = v * weights(j)
    return y


def backward(x):
    y = {}
    for j, v in x.items():
        y[j - 1] = v / weights(j - 1)
    return y


for j in range(-12, 29):
    x = {j: Fraction(j + 13, 17)}
    for n in range(0, 9):
        f = x.copy()
        b = x.copy()
        for _ in range(n):
            f = forward(f)
            b = backward(b)
        prod_forward = Fraction(1)
        prod_back = Fraction(1)
        for i in range(j, j + n):
            prod_forward *= weights(i)
        for i in range(j - n, j):
            prod_back *= weights(i)
        equal(f.get(j + n, Fraction(0)), x[j] * prod_forward, 'forward product')
        equal(b.get(j - n, Fraction(0)), x[j] / prod_back, 'backward product')
        if j >= 1:
            equal(b.get(j - n, Fraction(0)),
                  x[j] * W(max(j - n, 1)) / W(j),
                  'analytic-core predecessor identity')
        else:
            equal(b.get(j - n, Fraction(0)), x[j], 'constant left half-line')
        equal(forward(b).get(j - n + 1, Fraction(0)),
              b[j-n] * weights(j-n), 'shift evaluation')

# Exact partition of coordinate products and the first n-th orbit entries.
for k in range(1, 45):
    v = Fraction(1)
    for j in range(1, k):
        v *= weights(j)
    equal(W(k), v, 'cumulative product')
    for n in range(0, min(k + 3, 15)):
        denom = Fraction(1)
        for j in range(k - n, k):
            denom *= weights(j)
        equal(denom, W(k) / W(max(k-n,1)), 'positive predecessor product')

# Two explicit separated damping profiles: log_2 of positive products.
def slow_log2_W(k):
    return -k*(k-1)//2

def fast_log2_W(k):
    return -(k-1)*k*(2*k-1)//6

for k in range(1, 121):
    equal(slow_log2_W(k), -sum(range(1,k)), 'linear decay product exponent')
    equal(fast_log2_W(k), -sum(j*j for j in range(1,k)), 'quadratic decay product exponent')
    equal(fast_log2_W(k) <= slow_log2_W(k), True, 'core embedding ratio')
    if k >= 40:
        equal(fast_log2_W(k) - (-k*k) < -3*k, True,
              'witness cannot have exponential ratio in fast profile')

print(f'PASS {CHECKS} exact rational/integer identities; no numerical tolerance')
