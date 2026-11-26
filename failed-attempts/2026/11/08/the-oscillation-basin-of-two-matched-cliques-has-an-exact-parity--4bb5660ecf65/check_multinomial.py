#!/usr/bin/env python3
"""Independent exact type-enumeration check of paired-clique majority periodic counts."""
from math import comb, factorial


def state(n, a, b, c, d):
    # Columns: (+,+)^a, (+,-)^b, (-,+)^c, (-,-)^d.
    top = [1] * (a + b) + [-1] * (c + d)
    bot = [1] * a + [-1] * b + [1] * c + [-1] * d
    return (top, bot)


def advance(z):
    x, y = z
    sx, sy = sum(x), sum(y)
    def sign_preserving(field, old):
        return (1 if field > 0 else (-1 if field < 0 else old))
    return ([sign_preserving(sx - x[i] + y[i], x[i]) for i in range(len(x))],
            [sign_preserving(sy - y[i] + x[i], y[i]) for i in range(len(y))])


def run():
    examined = 0
    for n in range(2, 41):
        fix = two = eventual_two = tail_one = 0
        fact = factorial(n)
        for a in range(n + 1):
            for b in range(n - a + 1):
                for c in range(n - a - b + 1):
                    d = n - a - b - c
                    x = state(n, a, b, c, d)
                    y = advance(x)
                    z = advance(y)
                    weight = fact // (factorial(a) * factorial(b) * factorial(c) * factorial(d))
                    if x == y:
                        fix += weight
                    elif x == z:
                        two += weight
                        eventual_two += weight
                    else:
                        w = advance(z)
                        if y == w and y != z and x != z:
                            tail_one += weight
                            eventual_two += weight
                        else:
                            r = advance(w)
                            assert z == r or w == r, (n, a, b, c, d, 'long unexpected orbit')
                    examined += 1
        if n % 2:
            ef, et = 4, (n + 3) * comb(n, (n - 1) // 2)
        else:
            z = comb(n, n // 2)
            ef, et = 4 + z, z * (z - 1)
        expected_tail = 0 if n % 2 == 0 else 2 * n * (n - 1) * comb(n - 2, (n - 3) // 2)
        assert (fix, two, tail_one, eventual_two) == (ef, et, expected_tail, et + expected_tail), (n, fix, two, tail_one, eventual_two, ef, et, expected_tail)
        if n in (2, 3, 4, 5, 6, 7, 8, 9, 25, 40):
            print(f'n={n}: fixed={fix}, primitive_two={two}, tail_one={tail_one}, eventual_two={eventual_two} OK')
    print(f'PASS; {examined} weighted four-type cases checked for n=2..40')

if __name__ == '__main__':
    run()
