#!/usr/bin/env python3
"""Independent enumeration of determinant-valuation strata for small finite chain rings.

Run: python3 checks/check_hankel.py
Only Python's standard library is needed. The theorem for unbounded lengths
is established algebraically; these exhaustive checks test its boundary cases.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def convolution(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def predicted(q, length):
    u = Fraction(1, q)
    numerator = convolution(convolution([1-u], [1, -u**3]), [1, 0, -u**5])
    denominator = convolution(convolution([1, -u], [1, 0, -u**3]), [1, 0, 0, -u**5])
    vals = []
    for i in range(length):
        c = numerator[i] if i < len(numerator) else Fraction(0)
        c -= sum(denominator[j] * vals[i-j] for j in range(1, min(i, len(denominator)-1)+1))
        vals.append(c)
    return vals + [1 - sum(vals)]


def determinant(a, b, c, d, e, add, mul, neg):
    # Universal integer-coefficient determinant polynomial, valid in all characteristics.
    x = add(mul(mul(a, c), e), add(mul(mul(b, c), d), mul(mul(b, c), d)))
    x = add(x, neg(mul(a, mul(d, d))))
    x = add(x, neg(mul(mul(b, b), e)))
    return add(x, neg(mul(mul(c, c), c)))


def valuation(v, p, length):
    if v == 0:
        return length
    k = 0
    while v % p == 0:
        k += 1
        v //= p
    return k


def count_mod_prime_power(p, length):
    modulus = p**length
    counts = [0] * (length+1)
    for a,b,c,d,e in product(range(modulus), repeat=5):
        det = (a*c*e + 2*b*c*d - a*d*d - b*b*e - c*c*c) % modulus
        counts[valuation(det, p, length)] += 1
    return [Fraction(x, modulus**5) for x in counts]


def truncated_polynomial_ops(p, length):
    powers = [p**i for i in range(length)]
    def coefficients(x):
        return [(x//powp) % p for powp in powers]
    def add(x,y):
        a,b = coefficients(x),coefficients(y)
        return sum(((a[i]+b[i])%p)*powers[i] for i in range(length))
    def neg(x):
        a=coefficients(x)
        return sum((-a[i]%p)*powers[i] for i in range(length))
    def mul(x,y):
        a,b=coefficients(x),coefficients(y)
        return sum((sum(a[j]*b[i-j] for j in range(i+1))%p)*powers[i] for i in range(length))
    return add, mul, neg


def count_equal_characteristic(p, length):
    modulus=p**length
    add,mul,neg=truncated_polynomial_ops(p,length)
    counts=[0]*(length+1)
    for args in product(range(modulus), repeat=5):
        counts[valuation(determinant(*args,add,mul,neg),p,length)] += 1
    return [Fraction(x,modulus**5) for x in counts]


def count_quaternary_dual_numbers():
    # F4 = F2[z]/(z^2+z+1), R = F4[epsilon]/(epsilon^2).
    mul4=[[0]*4 for _ in range(4)]
    for a in range(4):
        for b in range(4):
            z=0
            for i in range(2):
                for j in range(2):
                    if a&(1<<i) and b&(1<<j): z ^= (1<<(i+j))
            if z&4: z^=7
            mul4[a][b]=z
    ring_mul=[[0]*16 for _ in range(16)]
    for a in range(16):
        for b in range(16):
            a0,a1=a%4,a//4
            b0,b1=b%4,b//4
            ring_mul[a][b]=mul4[a0][b0]+4*(mul4[a0][b1]^mul4[a1][b0])
    # Characteristic two: addition and negation both XOR.
    counts=[0]*3
    for a,b,c,d,e in product(range(16),repeat=5):
        v=(ring_mul[ring_mul[a][c]][e]
           ^ring_mul[a][ring_mul[d][d]]
           ^ring_mul[ring_mul[b][b]][e]
           ^ring_mul[ring_mul[c][c]][c])
        counts[2 if not v else (1 if v%4==0 else 0)] += 1
    return [Fraction(x,16**5) for x in counts]


def check(label,q,length,actual):
    expected=predicted(q,length)
    assert actual==expected, (label,actual,expected)
    print(label, 'PASS', ' '.join(str(x) for x in actual))


def main():
    for p, length in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(5,1)]:
        check(f'Z/{p**length}Z (p={p}, m={length})',p,length,count_mod_prime_power(p,length))
    for p,length in [(2,2),(3,2)]:
        check(f'F_{p}[t]/(t^{length})',p,length,count_equal_characteristic(p,length))
    check('F_4[t]/(t^2)',4,2,count_quaternary_dual_numbers())
    print('ALL 10 exhaustive ring configurations passed.')


if __name__=='__main__':
    main()
