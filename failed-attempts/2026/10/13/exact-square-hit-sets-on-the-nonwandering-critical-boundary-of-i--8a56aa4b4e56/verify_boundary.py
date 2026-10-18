#!/usr/bin/env python3
from fractions import Fraction
from math import isqrt


def is_square_int(n):
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def is_square_fraction(q):
    return q >= 0 and is_square_int(q.numerator) and is_square_int(q.denominator)


def fval(a, b, c, x):
    return a*x*x + b*x + c


def irreducible_over_q(a, b, c):
    d = b*b - 4*a*c
    return d < 0 or not is_square_int(d)


def predicted(a, b, kappa, k):
    if kappa == 0:
        return Fraction(-b, 2*a)
    if kappa == -4:
        if k % 2:
            return Fraction(-(b+2), 2*a)
        return Fraction(-b, 2*a)
    if kappa == -8:
        if k == 1:
            return Fraction(-(b+4), 2*a)
        return Fraction(4-b, 2*a)
    raise ValueError(kappa)


def expected_square(a, b, kappa, k):
    return is_square_fraction(predicted(a, b, kappa, k))


def main():
    cases = 0
    iterates = 0
    square_checks = 0
    patterns = {0:set(), -4:set(), -8:set()}
    for kappa in (0, -4, -8):
        for a in range(-20, 21):
            if a == 0:
                continue
            for b in range(-50, 51):
                num = kappa + b*b - 2*b
                den = 4*a
                if num % den:
                    continue
                c = num // den
                assert 4*a*c - b*b + 2*b == kappa
                gamma = Fraction(-b, 2*a)
                x = gamma
                cases += 1
                for k in range(1, 11):
                    x = fval(a, b, c, x)
                    p = predicted(a, b, kappa, k)
                    assert x == p, (a, b, c, kappa, k, x, p)
                    assert is_square_fraction(x) == expected_square(a, b, kappa, k)
                    iterates += 1
                    square_checks += 1
                if irreducible_over_q(a, b, c):
                    if kappa == 0:
                        pat = "all" if expected_square(a,b,kappa,1) else "empty"
                    elif kappa == -4:
                        o = expected_square(a,b,kappa,1)
                        e = expected_square(a,b,kappa,2)
                        pat = ("odd" if o else "") + ("even" if e else "") or "empty"
                    else:
                        one = expected_square(a,b,kappa,1)
                        tail = expected_square(a,b,kappa,2)
                        pat = ("one" if one else "") + ("tail" if tail else "") or "empty"
                    patterns[kappa].add(pat)
    assert cases > 100
    assert patterns[0] == {"empty","all"}
    assert patterns[-4] == {"empty","odd","even"}
    assert patterns[-8] == {"empty","one","tail"}
    print(f"VERIFY_OK boundary_cases={cases} iterates={iterates} square_checks={square_checks} k_max=10 irreducible_patterns=OK")


if __name__ == '__main__':
    main()
