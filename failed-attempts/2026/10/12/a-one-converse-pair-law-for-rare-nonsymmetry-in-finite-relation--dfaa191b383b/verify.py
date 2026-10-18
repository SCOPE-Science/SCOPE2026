from fractions import Fraction
from math import factorial

assertions = 0

def check(cond, msg=""):
    global assertions
    assertions += 1
    if not cond:
        raise AssertionError(msg)

def Q6(n, s):
    # Six times Q(n,s), kept integral.
    return (n - 1) * ((n - 1) ** 2 + 3 * s - 1)

def P(n, s):
    assert 1 <= s <= n and (n - s) % 2 == 0
    k = (n - s) // 2
    return factorial(s - 1) * factorial(k) * (2 ** k)

def R(n, k):
    assert 0 <= k <= (n - 1) // 2
    return Fraction(
        factorial(n - 1),
        factorial(n - 2 * k - 1) * factorial(k) * (2 ** k),
    ) * Fraction(1, 2 ** (k * (n - 1)))

for n in range(5, 251):
    maxk = (n - 1) // 2
    check(P(n, n) == factorial(n - 1), (n, "P0"))
    for k in range(maxk + 1):
        s = n - 2 * k
        check((Q6(n, s) - Q6(n, n)) == -6 * k * (n - 1), (n, k, "Qdiff"))
        check(P(n, s) == factorial(n - 2 * k - 1) * factorial(k) * 2 ** k, (n, k, "P"))
        direct = Fraction(P(n, n), P(n, s)) * Fraction(1, 2 ** (k * (n - 1)))
        check(R(n, k) == direct, (n, k, "Rdirect"))
    check(R(n, 0) == 1, (n, "R0"))
    check(R(n, 1) == Fraction((n - 1) * (n - 2), 2 ** n), (n, "R1"))
    for k in range(maxk):
        ratio = R(n, k + 1) / R(n, k)
        expected = Fraction((n - 2 * k - 1) * (n - 2 * k - 2), (k + 1) * (2 ** n))
        check(ratio == expected, (n, k, "ratio"))
        if k >= 1:
            check(ratio <= Fraction(n * n, 2 ** (n + 1)), (n, k, "ratio_bound"))

for n in range(8, 251):
    maxk = (n - 1) // 2
    rho = Fraction(n * n, 2 ** (n + 1))
    if rho < 1 and maxk >= 2:
        tail = sum((R(n, k) for k in range(2, maxk + 1)), Fraction(0, 1))
        bound = R(n, 1) * rho / (1 - rho)
        check(tail <= bound, (n, "tail"))

print(f"VERIFY_OK {assertions} exact assertions")
