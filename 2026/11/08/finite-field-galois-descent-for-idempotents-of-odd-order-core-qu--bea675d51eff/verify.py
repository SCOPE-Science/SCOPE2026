"""Independent direct multiplication checks for finite-field core-quandle idempotents.

Run with Python 3: python3 verify.py. No third-party dependencies.
"""
import itertools
from collections import Counter
from math import gcd


def multiplicative_order(a, m):
    value = a % m
    j = 1
    while value != 1:
        value = (value * a) % m
        j += 1
        if j > m:
            raise AssertionError("order computation did not terminate")
    return j


def predicted_cyclic(n, q):
    assert n % 2 == 1 and gcd(n, q) == 1
    total = 2
    factors = []
    for m in range(3, n + 1, 2):
        if n % m:
            continue
        d = multiplicative_order(2, m)
        minus_one_in_doubling = any(pow(2, j, m) == m - 1 for j in range(d))
        E = 2 ** (d // 2) + 1 if minus_one_in_doubling else 2**d - 1
        H = {sgn * pow(2, j, m) % m for j in range(d) for sgn in (1, -1)}
        L = {sgn * pow(2, j, m) * pow(q, i, m) % m
             for j in range(d) for sgn in (1, -1) for i in range(m)}
        t = next(i for i in range(1, m + 1) if pow(q, i, m) in H)
        b_options = {sgn * 2**j for j in range(d) for sgn in (1, -1)
                     if sgn * pow(2, j, m) % m == pow(q, t, m)}
        g_values = {gcd(E, q**t - b) for b in b_options}
        assert len(g_values) == 1
        g = next(iter(g_values))
        N_m = sum(1 for j in range(n) if n // gcd(n, j) == m)
        assert N_m % len(L) == 0
        count = N_m // len(L)
        total *= (1 + g) ** count
        factors.append((m, len(H), len(L), t, E, g, count))
    return total, factors


def finite_field(q):
    if q in (2, 3, 5, 7, 11):
        return [[a*b % q for b in range(q)] for a in range(q)], lambda a, b: (a+b) % q
    if q in (4, 8):
        modulus = {4: 0b111, 8: 0b1011}[q]
        top = q
        def multiply(a, b):
            result = 0
            while b:
                if b & 1:
                    result ^= a
                b >>= 1
                a <<= 1
                if a & top:
                    a ^= modulus
            return result
        return [[multiply(a, b) for b in range(q)] for a in range(q)], lambda a, b: a ^ b
    raise ValueError("unsupported test field")


def brute_cyclic(n, q):
    multiplication, addition = finite_field(q)
    counts = Counter()
    for coefficients in itertools.product(range(q), repeat=n):
        square = [0] * n
        aug = 0
        for i, a in enumerate(coefficients):
            aug = addition(aug, a)
            if a:
                for j, b in enumerate(coefficients):
                    if b:
                        k = (2*j - i) % n
                        square[k] = addition(square[k], multiplication[a][b])
        if tuple(square) == coefficients:
            counts[aug] += 1
    return counts


def elementary_ternary_group_test():
    # In characteristic 2, the core operation on F_3^2 is commutative:
    # all cross terms in a square cancel and every one of 2^9 elements is idempotent.
    group = [(i, j) for i in range(3) for j in range(3)]
    for coefficients in itertools.product(range(2), repeat=9):
        square = {(i, j): 0 for i, j in group}
        for idx, x in enumerate(group):
            for jdx, y in enumerate(group):
                square[((2*y[0]-x[0]) % 3, (2*y[1]-x[1]) % 3)] ^= (coefficients[idx] & coefficients[jdx])
        assert tuple(square[x] for x in group) == coefficients
    print("DIRECT_OK A=C3xC3 q=2 idempotents=512")


def run():
    cases = [(3,2),(3,4),(3,5),(3,7),(3,8),
             (5,2),(5,3),(5,4),(5,7),
             (7,2),(7,3),(7,4),(7,5),
             (9,2),(11,2),(11,3),(15,2)]
    for n, q in cases:
        predicted, factors = predicted_cyclic(n, q)
        actual = brute_cyclic(n, q)
        assert sum(actual.values()) == predicted, (n, q, actual, predicted, factors)
        assert actual == {0: predicted//2, 1: predicted//2}, (n, q, actual)
        print(f"DIRECT_OK n={n} q={q} total={predicted} augmentation={dict(actual)}")
    elementary_ternary_group_test()
    assert predicted_cyclic(17,2)[0] == 648
    assert predicted_cyclic(17,3)[0] == 36
    print("ARITHMETIC_OK n=17 q=2 total=648 q=3 total=36")
    print("VERIFY_OK")


if __name__ == "__main__":
    run()
