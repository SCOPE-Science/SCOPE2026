"""Finite certificate for three-distinct-cubic-residue sums over small fields.

Requires Python 3 standard library only. This program constructs every prime-power
field of order q < 169 for which q == 1 (mod 3). For each field it checks the
chosen multiplication has no nonzero zero divisors, enumerates the full cubic
residue subgroup, and enumerates every 3-element subset and its sum.

This is the finite part of a proof; the large-field analytic argument is in the
accompanying mathematical statement.
"""

from itertools import combinations
from collections import Counter

BINARY_MODULI = {4: 0b111, 16: 0b10011, 64: 0b1000011}
QUADRATIC_NONRESIDUES = {25: 2, 49: 3, 121: 2}
EXPECTED_MISSING = {4: 4, 7: 7, 13: 9, 16: 6,
                    19: 6, 25: 1, 31: 1, 43: 1}


def prime(n):
    return n >= 2 and all(n % d != 0 for d in range(2, int(n ** .5) + 1))


def prime_power(n):
    for p in range(2, n + 1):
        if not prime(p):
            continue
        k, exponent = n, 0
        while k % p == 0:
            k //= p
            exponent += 1
        if k == 1:
            return p, exponent
    return None


class Field:
    def __init__(self, q, p, exponent):
        self.q, self.p, self.exponent = q, p, exponent
        if exponent == 1:
            self.add = lambda a, b: (a + b) % p
            self.mul = lambda a, b: (a * b) % p
        elif p == 2:
            assert q in BINARY_MODULI
            modulus = BINARY_MODULI[q]
            def mult(a, b):
                product = 0
                while b:
                    if b & 1:
                        product ^= a
                    a <<= 1
                    if a & q:
                        a ^= modulus
                    b >>= 1
                return product
            self.add = lambda a, b: a ^ b
            self.mul = mult
        else:
            assert exponent == 2 and q in QUADRATIC_NONRESIDUES
            d = QUADRATIC_NONRESIDUES[q]
            assert pow(d, (p - 1) // 2, p) == p - 1
            self.add = lambda a, b: ((a % p + b % p) % p) + p * ((a // p + b // p) % p)
            self.mul = lambda a, b: (((a % p)*(b % p) + d*(a // p)*(b // p)) % p) + p * (((a % p)*(b // p) + (a // p)*(b % p)) % p)

    def power(self, a, exponent):
        product = 1
        while exponent:
            if exponent & 1:
                product = self.mul(product, a)
            a = self.mul(a, a)
            exponent //= 2
        return product


def check_field_and_sums(q, p, exponent):
    field = Field(q, p, exponent)
    add, mul = field.add, field.mul
    # Every nonzero element satisfies a^(q-1)=1, verifying that the
    # explicit quotient algebra is a field, not merely a ring with q labels.
    assert all(field.power(x, q-1) == 1 for x in range(1, q))
    assert all(0 <= mul(a,b) < q for a,b in ((a,b) for a in range(q) for b in range(q)))
    H = sorted({field.power(x, 3) for x in range(1, q)})
    assert len(H) == (q - 1) // 3
    counts = [0] * q
    for a,b,c in combinations(H,3):
        counts[add(add(a,b),c)] += 1
    assert sum(counts) == len(H)*(len(H)-1)*(len(H)-2)//6
    absent = [b for b, count in enumerate(counts) if count == 0]
    expected_count = EXPECTED_MISSING.get(q, 0)
    assert len(absent) == expected_count, (q, len(absent), expected_count)
    return len(H), len(absent), min(counts), max(counts), 0 in absent


def main():
    checked = 0
    triples = 0
    fields = []
    for q in range(4, 169):
        if q % 3 != 1:
            continue
        pe = prime_power(q)
        if pe is None:
            continue
        p, exponent = pe
        h, missing, low, high, zero_missing = check_field_and_sums(q, p, exponent)
        checked += 1
        triples += h*(h-1)*(h-2)//6
        fields.append(q)
        print(f"q={q:3d} characteristic={p:3d} degree={exponent} |H|={h:2d} missing={missing:2d} zero_missing={zero_missing} fibers=[{low},{high}]")
    assert fields == [4, 7, 13, 16, 19, 25, 31, 37, 43, 49, 61, 64, 67, 73, 79, 97, 103, 109, 121, 127, 139, 151, 157, 163]
    assert checked == 24
    assert all(EXPECTED_MISSING.get(q, 0) == 0 for q in fields if q >= 49)
    print(f"VERIFY_OK fields={checked} distinct_triples={triples} threshold=49 exceptional_covering_field=37")


if __name__ == '__main__':
    main()
