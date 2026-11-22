#!/usr/bin/env python3
"""Exact independently implemented finite-field census for five consecutive quadratic characters.
Run: python3 verify.py
Standard-library only; finite enumeration, not a substitute for the Weil-bound argument.
"""
from math import isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def prime_power_cases(limit=1697):
    cases = []
    for p in range(5, isqrt(limit) + 1):
        if not prime(p):
            continue
        q, degree = p * p, 2
        while q < limit:
            cases.append((q, p, degree))
            degree += 1
            q *= p
    return sorted(cases)


def nonsquare(p):
    squares = {x * x % p for x in range(1, p)}
    return next(a for a in range(2, p) if a not in squares)


def cubic_coefficients(p):
    # x^3 + A*x+B is irreducible exactly when it has no root in F_p.
    for A in range(p):
        for B in range(1, p):
            if all((t**3 + A*t + B) % p for t in range(p)):
                return A, B
    raise AssertionError('irreducible cubic not found')


class Field:
    def __init__(self, p, degree):
        self.p, self.degree, self.q = p, degree, p**degree
        if degree == 2:
            # T^2 - c
            self.mod = [(-nonsquare(p)) % p, 0]
        elif degree == 3:
            a, b = cubic_coefficients(p)
            # T^3 + aT + b
            self.mod = [b, a, 0]
        elif degree == 4 and p == 5:
            # T^4+2 is irreducible over F_5. If it had a factor of degree <=2,
            # T^4=3 would have a solution in F_25. But 3 has order 4 in
            # F_25^*, whereas all fourth powers have order dividing 6.
            self.mod = [2,0,0,0]
        else:
            raise ValueError('Only degrees 2, 3 and (5,4) fall below the analytic cutoff')

    def mul(self, x, y):
        p, d = self.p, self.degree
        a = []
        b = []
        for _ in range(d):
            a.append(x % p); x //= p
            b.append(y % p); y //= p
        c = [0] * (2 * d - 1)
        for i in range(d):
            for j in range(d):
                c[i + j] += a[i] * b[j]
        for k in range(2 * d - 2, d - 1, -1):
            for j in range(d):
                c[k - d + j] -= c[k] * self.mod[j]
        return sum((c[i] % p) * p**i for i in range(d))

    def power(self, x, n):
        z = 1
        while n:
            if n & 1:
                z = self.mul(z, x)
            x = self.mul(x, x)
            n >>= 1
        return z

    def plus_base(self, x, j):
        return x - x % self.p + (x % self.p + j) % self.p


def census(field):
    p, q = field.p, field.q
    # Method A: all nonzero quadratic residues are explicit squares.
    square_set = {field.mul(x, x) for x in range(1, q)}
    assert len(square_set) == (q - 1) // 2
    # Method B: Euler's criterion for every nonzero field element.
    for x in range(1, q):
        power = field.power(x, (q - 1) // 2)
        assert power in (1, p - 1), (p, q, x, power)
        assert (x in square_set) == (power == 1), (p, q, x)
    counts = [0] * 32
    for x in range(q):
        code = 0
        for j in range(5):
            y = field.plus_base(x, j)
            if not y:
                break
            if y in square_set:
                code |= (1 << j)
        else:
            counts[code] += 1
    assert sum(counts) == q - 5
    if field.degree == 2:
        # Method C: chi_{p^2}(a+bT)=chi_p(a^2-c*b^2).
        c = -field.mod[0] % p
        leg_squares = {t * t % p for t in range(1, p)}
        for x in range(1, q):
            a, b = x % p, x // p
            norm = (a*a - c*b*b) % p
            assert norm != 0
            assert (x in square_set) == (norm in leg_squares)
    return counts


def main():
    cases = prime_power_cases()
    assert [(q,p,e) for q,p,e in cases] == [
        (25,5,2),(49,7,2),(121,11,2),(125,5,3),(169,13,2),
        (289,17,2),(343,7,3),(361,19,2),(529,23,2),
        (625,5,4),(841,29,2),(961,31,2),(1331,11,3),
        (1369,37,2),(1681,41,2)]
    observed = {}
    for q, p, e in cases:
        field = Field(p, e)
        counts = census(field)
        absent = [code for code, c in enumerate(counts) if c == 0]
        observed[q] = absent
        print('order=%4d characteristic=%2d degree=%d missing=%s min_count=%d' %
              (q, p, e, absent, min(counts)))
    expected = {
        25: [0,1,2,4,7,8,11,13,14,15,16,19,21,22,23,25,26,27,28,29,30,31],
        49: [0,2,8,11,13,15,17,22,23,26,27,29,30],
        121: [0,27],
        125: [0,5,7,9,10,14,18,19,20,25,28,31],
        169: [4],
    }
    assert {q: v for q, v in observed.items() if v} == expected
    print('PASS: all fifteen nonprime fields of characteristic at least 5 below 1697 checked,')
    print('with three independent quadratic-character checks where applicable.')


if __name__ == '__main__':
    main()
