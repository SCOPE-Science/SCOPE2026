"""Reproducible checks of Lucas classification for odd-cube progressions.

All calculations are exact integer arithmetic. Finite checks illustrate but
cannot replace the infinite descent and modular-recursion proof.
"""
from math import isqrt


def LucasU(k, j):
    u0, u1 = 0, 1
    for _ in range(j):
        u0, u1 = u1, k * u1 - u0
    return u0


def direct_sums(n, a):
    s = sum(a + 2 * i for i in range(n))
    c = sum((a + 2 * i) ** 3 for i in range(n))
    return s, c


def structural_quotient(n, a):
    x = a + n - 1
    assert (n * x) > 0
    numerator = x*x + n*n - 1
    return numerator, n*x


def classify(k, t):
    assert k >= 5 and k % 2 == 1 and t >= 1
    j = 3*t + 1
    n = LucasU(k, j)
    a = (k-1)*n - LucasU(k, j-1) + 1
    return n, a


def run():
    cases = 0
    # Independent literal power sums vs exact factored identity.
    for n in range(2, 45):
        for a in range(1, 160, 2):
            s, c = direct_sums(n, a)
            num, den = structural_quotient(n, a)
            assert c * den == num * s*s, (n, a)
            cases += 1
    # Every integer quotient in a bounded rectangular search is explained
    # by the Lucas classification (including the known k=3 boundary).
    brute = []
    for n in range(2, 300):
        for a in range(1, 1000, 2):
            num, den = structural_quotient(n, a)
            if num % den == 0:
                k = num//den
                assert k % 2 == 1 and k >= 3
                if k >= 5:
                    matches = [classify(k, t) for t in range(1, 6)]
                    assert (n, a) in matches, (n, a, k)
                    brute.append((n, a, k))
    # Recurrence, exact power sums and divisor identity for 14 generated pairs.
    generated = 0
    for k in (5, 7, 9, 11, 13, 15, 19):
        for t in (1, 2, 3, 4):
            n, a = classify(k, t)
            assert a > 0 and a % 2 and n > 1 and n % 2
            num, den = structural_quotient(n, a)
            assert num == k * den
            assert n >= k**3 - 2*k
            if t == 1:
                assert n == k**3 - 2*k
                assert a == k**4-k**3-3*k*k+2*k+2
                s, c = direct_sums(n, a)
                assert c == k*s*s
            generated += 1
    # Denominator parity: no even length can have any integral quotient.
    for n in range(2, 300, 2):
        for a in range(1, 200, 2):
            num, den = structural_quotient(n, a)
            assert num % den != 0
    print('PASS exact literal-cube identity cases:', cases)
    print('PASS all bounded integral quotients n<300, a<1000; new k>=5 pairs:', brute)
    print('PASS Lucas generated cases:', generated)
    print('PASS no even-length cases')
    print('EXAMPLE k=5 first:', classify(5, 1), 'k=7 first:', classify(7, 1))

if __name__ == '__main__':
    run()
