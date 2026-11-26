from fractions import Fraction


def r(n):
    if n == 0 or n == 1:
        return Fraction(1, 1)
    return Fraction(15, (2*n - 1) * (2*n + 1) * (2*n + 3))


def S(n):
    if n == 0:
        return Fraction(9, 4)
    return Fraction(15, 4 * (2*n - 1) * (2*n + 1))


def h(n):
    if n == 0:
        return Fraction(1, 1)
    return Fraction(5, 3 * (2*n - 1) * (2*n + 1))


def p(n):
    if n == 0:
        return Fraction(1, 1)
    if n == 1:
        return Fraction(1, 2)
    return Fraction(2*n + 3, 4*n)


def q(n):
    if n == 0:
        return Fraction(0, 1)
    if n == 1:
        return Fraction(1, 2)
    return Fraction(2*n - 3, 4*n)


def p_tilde(n):
    return p(n) * h(n + 1) / h(n)


def q_tilde(n):
    return q(n) * h(n - 1) / h(n)


def pi(n):
    if n == 1:
        return Fraction(1, 1)
    return Fraction(6*n, 5 * (2*n - 1) * (2*n + 1))


# The model has p_0=1, p_1=q_1=1/2, and for n>=2,
# p_n=(2n+3)/(4n), q_n=(2n-3)/(4n).
# Its hitting-probability and transformed-chain formulas are exact.
for n in range(2, 1001):
    assert r(n) == r(n-1) * q(n) / p(n)
    assert S(n) == r(n) + S(n+1)
    assert h(n) == S(n) / S(0)
    assert p(n) * h(n+1) + q(n) * h(n-1) == h(n)
    assert p_tilde(n) == Fraction(2*n - 1, 4*n)
    assert q_tilde(n) == Fraction(2*n + 1, 4*n)
    assert p_tilde(n) + q_tilde(n) == 1
    assert p_tilde(n) - q_tilde(n) == Fraction(-1, 2*n)

for n in range(2, 1000):
    assert pi(n+1) == pi(n) * p_tilde(n) / q_tilde(n+1)

assert h(1) == Fraction(5, 9)
assert p_tilde(1) == Fraction(1, 10)
assert q_tilde(1) == Fraction(9, 10)
assert pi(2) == Fraction(4, 25)

print("PASS: exact rational hitting-probability, h-transform, and invariant-weight identities checked for n=2..1000.")
print("The infinite divergence and general asymptotic theorem are established by the written proof, not by finite computation.")
