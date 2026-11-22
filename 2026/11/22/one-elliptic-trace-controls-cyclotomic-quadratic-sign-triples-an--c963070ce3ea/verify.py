"""Reproducibility checker for the three-factor cyclotomic sign law.

Standard-library Python 3. The infinite assertion uses the mathematical
character-sum/Hasse argument in RESULT.md, not a finite experiment.
"""
from itertools import product
from math import isqrt
import json

SIGNS = tuple(product((-1, 1), repeat=3))


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def prime_character(p):
    # Two deliberately different implementations: Euler's criterion and squares.
    powers = [0] * p
    squares = [0] * p
    for x in range(1, p):
        powers[x] = 1 if pow(x, (p - 1) // 2, p) == 1 else -1
        squares[x * x % p] = 1
    squares = [0 if x == 0 else (1 if squares[x] else -1) for x in range(p)]
    assert powers == squares, (p, 'character mismatch')
    return powers


def quadratic_extension(p):
    # Integers ap+b encode a+b*theta with theta^2 = D, D a nonsquare in F_p.
    base_ch = prime_character(p)
    D = next(x for x in range(2, p) if base_ch[x] == -1)
    q = p * p
    def add(x, y):
        a, b = divmod(x, p)
        c, d = divmod(y, p)
        return ((a + c) % p) * p + ((b + d) % p)
    def mul(x, y):
        a, b = divmod(x, p)
        c, d = divmod(y, p)
        return ((a*c + D*b*d) % p) * p + ((a*d + b*c) % p)
    square_set = {mul(x, x) for x in range(1, q)}
    char_squares = [0 if x == 0 else (1 if x in square_set else -1)
                    for x in range(q)]
    # Independent norm method: chi_{p^2}(a+b theta) = chi_p(a^2-D*b^2).
    char_norm = []
    for x in range(q):
        a, b = divmod(x, p)
        char_norm.append(base_ch[(a*a - D*b*b) % p])
    assert char_squares == char_norm, (p, 'norm-square character mismatch')
    return q, p, add, mul, char_squares


def prime_field(p):
    def add(x, y):
        return (x + y) % p
    def mul(x, y):
        return (x*y) % p
    return p, 1, add, mul, prime_character(p)


def count_signs(field):
    q, one, add, mul, chi = field
    counts = {s: 0 for s in SIGNS}
    U = 0
    for x in range(q):
        h = add(add(mul(x, x), x), one)
        s = (chi[x], chi[add(x, one)], chi[h])
        U += chi[mul(x, h)]
        if 0 not in s:
            counts[s] += 1
    return U, counts


def formula(q, chi_minus_one, r, U, s):
    a, b, c = s
    if chi_minus_one == 1:
        return ((q - 5 - 6*c - 4*r + 3*c*U) // 8 if a == b == 1
                else (q - 1 - 2*c - c*U) // 8)
    return ((q + 1 - 4*r + 3*c*U) // 8 if (a,b) == (1,-1)
            else (q - 3 - 4*c - c*U) // 8)


def encode(s):
    return ''.join('+' if x == 1 else '-' for x in s)


def verify_case(field, expect_formulas=True):
    q, one, add, mul, chi = field
    U, counts = count_signs(field)
    if expect_formulas:
        # The additive inverse of 1 is the field element -1.
        minus_one = next(x for x in range(q) if add(x, one) == 0)
        delta = chi[minus_one]
        r = 2 if (q - 1) % 3 == 0 else 0
        for s in SIGNS:
            predicted = formula(q, delta, r, U, s)
            assert predicted == counts[s], (q, s, predicted, counts[s])
    return {
        'q': q,
        'trace_sum_U': U,
        'counts': {encode(s): counts[s] for s in SIGNS},
        'missing': [encode(s) for s in SIGNS if counts[s] == 0],
        'min_count': min(counts.values())
    }


def main():
    finite = []
    for p in range(3, 71, 2):
        if is_prime(p):
            finite.append(verify_case(prime_field(p), expect_formulas=(p != 3)))
    for p in (5, 7):
        finite.append(verify_case(quadratic_extension(p)))
    finite.sort(key=lambda x: x['q'])
    exceptions = [x['q'] for x in finite if x['missing'] and x['q'] % 3 != 0]
    assert exceptions == [5,7,11,13,17,19,23,25,29,31,37,49], exceptions
    assert [x['q'] for x in finite if x['q'] >= 53 and x['missing']] == []
    # Additional validation beyond the finite certificate: all prime fields < 500.
    spot_count = 0
    for p in range(71, 500, 2):
        if is_prime(p):
            x = verify_case(prime_field(p))
            assert x['min_count'] > 0
            spot_count += 1
    output = {
        'finite_fields_below_71_char_at_least_5': len(finite) - 1,
        'prime_field_spot_checks_71_to_499': spot_count,
        'exceptions_char_at_least_5': exceptions,
        'cases': finite
    }
    with open('finite_cases.json', 'w', encoding='utf8') as f:
        json.dump(output, f, indent=2, sort_keys=True)
        f.write('\n')
    print('PASS', len(finite), 'finite cases including characteristic 3,',spot_count, 'extra prime-field cases')
    print('exception fields (characteristic >=5):', exceptions)

if __name__ == '__main__':
    main()
