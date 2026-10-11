from fractions import Fraction
from math import factorial

def v2(x):
    assert x > 0
    r = 0
    while x % 2 == 0:
        x //= 2
        r += 1
    return r

def s2(x):
    return x.bit_count()

def deg_lg(n):
    M = n * (n + 1) // 2
    num = factorial(M)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            num *= 2 * (j - i)
    den = 1
    for i in range(1, n + 1):
        den *= factorial(2 * i - 1)
    assert num % den == 0
    return num // den

def deg_spinor(n):
    M = n * (n + 1) // 2
    num = factorial(M)
    for a in range(2, n):
        num *= factorial(a)
    den = 1
    for a in range(2, n + 1):
        den *= factorial(2 * a - 1)
    assert num % den == 0
    return num // den

def shifted_staircase_count(n):
    # General shifted hook product in the equivalent strict-partition form:
    # g^lambda = N!/prod(lambda_i!) * prod_{i<j}(lambda_i-lambda_j)/(lambda_i+lambda_j).
    lam = list(range(n, 0, -1))
    N = sum(lam)
    q = Fraction(factorial(N), 1)
    for a in lam:
        q /= factorial(a)
    for i in range(n):
        for j in range(i + 1, n):
            q *= Fraction(lam[i] - lam[j], lam[i] + lam[j])
    assert q.denominator == 1
    return q.numerator

checks = 0
for n in range(1, 101):
    M = n * (n + 1) // 2
    dl = deg_lg(n)
    ds = deg_spinor(n)
    assert dl == (1 << (n * (n - 1) // 2)) * ds
    odd_l = dl >> v2(dl)
    odd_s = ds >> v2(ds)
    assert odd_l == odd_s
    assert v2(dl) == M - s2(M)
    assert v2(dl) - v2(ds) == n * (n - 1) // 2
    checks += 1

shifted_checks = 0
for n in range(1, 21):
    assert shifted_staircase_count(n) == deg_spinor(n)
    shifted_checks += 1

assert [deg_lg(n) for n in range(1, 6)] == [1, 2, 16, 768, 292864]
assert [deg_spinor(n) for n in range(1, 6)] == [1, 1, 2, 12, 286]

print("VERIFY_OK", checks, shifted_checks)
