"""Bounded checks for the literal-stay sign formula (standard library only)."""
from fractions import Fraction
from itertools import combinations, product
from math import exp, sqrt


def inversions(bits):
    ones = result = 0
    for bit in bits:
        if bit:
            ones += 1
        else:
            result += ones
    return result


def exact_mean(n, stay):
    total = Fraction(0)
    for bits in product((0, 1), repeat=n):
        switches = sum(x != y for x, y in zip(bits, bits[1:]))
        mass = (1 - stay)**switches * stay**(n - 1 - switches) / 2
        total += mass * (-1)**inversions(bits)
    return total


def transfer(n, p):
    q = 1 - p
    x, y, z, w = Fraction(1, 2), 0, 0, Fraction(1, 2)
    for _ in range(n - 1):
        x, y, z, w = p*x + q*z, -p*y - q*w, q*y + p*w, q*x + p*z
    return x + y + z + w


def odd_words(n, number_of_switches):
    count = 0
    for locations in combinations(range(1, n), number_of_switches):
        boundaries = (0,) + locations + (n,)
        for start in (0, 1):
            bits = []
            for run, (a, b) in enumerate(zip(boundaries, boundaries[1:])):
                bits.extend([(start+run) % 2] * (b-a))
            count += inversions(bits) % 2
    return count


def main():
    for p in map(Fraction, ('0', '1/4', '1/2', '2/3', '7/8', '1')):
        values = [None] + [exact_mean(n, p) for n in range(1, 12)]
        assert values[1:5] == [1, p, 1 - 2*(1-p)**2, 2*p**3-4*p**2+4*p-1]
        for n in range(1, 12):
            assert values[n] == transfer(n, p)
        for n in range(1, 8):
            assert values[n+4] == 2*p*p*values[n+2] - (2*p-1)**2*values[n]
    for n in range(2, 31):
        m = n // 2
        assert not odd_words(n, 0)
        assert odd_words(n, 1) == (0 if n % 2 else m)
        if n % 2:
            assert odd_words(n, 2) == m*(m+1)
    max_error = 0.0
    for xi in (0.5, 2.0):
        a, b = 1 - 1/sqrt(2), 1 + 1/sqrt(2)
        for n in (2000, 2001, 8000, 8001, 32000, 32001):
            weight = 0.5 + (1 if n % 2 else 0.5)/sqrt(2)
            expected = weight*exp(-a*xi) + (1-weight)*exp(-b*xi)
            max_error = max(max_error, abs(transfer(n, 1-xi/n) - expected))
    assert max_error < 0.001
    print('PASS: 66 direct exact means, 42 recurrence checks, and rare switches through n=30')
    print(f'PASS: growing-profile grid; maximum absolute difference {max_error:.3g}')


if __name__ == '__main__':
    main()
