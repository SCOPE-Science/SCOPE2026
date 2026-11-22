#!/usr/bin/env python3
"""Direct finite-field checks for a two-parabola additive-energy theorem.

No third-party dependencies.  Finite fields are represented by polynomial residues.
These finite checks supplement, but do not replace, the all-field proof.
"""
from collections import Counter
from itertools import product


def field(p, poly):
    # poly is lower coefficients of monic irreducible polynomial of degree n
    n = len(poly)
    q = p ** n
    powers = [p ** i for i in range(n)]
    digits = [tuple((j // powers[i]) % p for i in range(n)) for j in range(q)]
    codes = {x: i for i, x in enumerate(digits)}

    def add(a, b):
        return codes[tuple((x + y) % p for x, y in zip(digits[a], digits[b]))]

    def mul(a, b):
        z = [0] * (2 * n - 1)
        for i, x in enumerate(digits[a]):
            for j, y in enumerate(digits[b]):
                z[i + j] = (z[i + j] + x * y) % p
        for i in range(2 * n - 2, n - 1, -1):
            t = z[i]
            for j, c in enumerate(poly):
                z[i - n + j] = (z[i - n + j] - t * c) % p
        return codes[tuple(z[:n])]

    zero, one = 0, 1
    two = add(one, one)
    negone = codes[tuple((-x) % p for x in digits[one])]
    return q, add, mul, zero, one, two, negone


def run(p, poly):
    q, add, mul, zero, one, two, negone = field(p, poly)
    neg = lambda a: mul(negone, a)
    sub = lambda a, b: add(a, neg(b))
    square = lambda a: mul(a, a)
    def power(x, n):
        y = one
        while n:
            if n & 1:
                y = mul(y, x)
            x = mul(x, x)
            n >>= 1
        return y
    def chi(a):
        if a == zero:
            return 0
        v = power(a, (q-1)//2)
        assert v in (one, negone)
        return 1 if v == one else -1

    values = {}
    pair_counts = Counter()
    for la in range(q):
        if la in (zero, one):
            continue
        s = {(x, square(x)) for x in range(q)}
        s.update((x, mul(la, square(x))) for x in range(q))
        assert len(s) == 2*q-1
        r = Counter()
        for x, y in s:
            for u, v in s:
                r[(add(x, u), add(y, v))] += 1
        direct = sum(v*v for v in r.values())
        a = chi(sub(mul(two, la), one))
        b = chi(mul(la, sub(two, la)))
        opposite = int(la == negone)
        predicted = 22*q*q-54*q+33-4*(q-1)*(a+b-opposite)
        assert direct == predicted, (p, poly, la, direct, predicted)
        values[la] = direct
        if a != 0 and b != 0:
            pair_counts[(a,b)] += 1

    if p != 3:
        inv2 = next(x for x in range(q) if mul(two,x) == one)
        excluded = {zero, one, inv2, two}
        T = sum(chi(mul(mul(sub(mul(two,x),one),x),sub(two,x))) for x in range(q))
        R = chi(negone) + 1 + chi(add(one,two))
        for aa,bb in product((-1,1), repeat=2):
            pred_count = (q-4-(aa+bb)*R+aa*bb*(T-1))//4
            assert 4*pred_count == q-4-(aa+bb)*R+aa*bb*(T-1)
            observed = sum(1 for x in values if x not in excluded and
                           chi(sub(mul(two,x),one)) == aa and
                           chi(mul(x,sub(two,x))) == bb)
            assert observed == pred_count, (q, aa, bb, observed, pred_count)
        if q >= 31:
            base = 22*q*q-54*q+33
            assert min(values.values()) == base-8*(q-1)
            expect_max = base+(12 if chi(neg(mul(add(one,two),one))) == -1 else 8)*(q-1)
            assert max(values.values()) == expect_max
            if chi(neg(add(one,two))) == -1:
                assert [la for la,v in values.items() if v == expect_max] == [negone]
    elif q >= 27:
        base = 22*q*q-54*q+33
        assert min(values.values()) == base-8*(q-1)
        assert max(values.values()) == base+8*(q-1)
    return q-2


def main():
    total = 0
    for p in (3,5,7,11,13,17,19,23,29,31):
        n = run(p, (0,)) # x + 0
        total += n
        print('prime', p, 'parameters', n)
    for p, poly in ((3,(1,0)), (5,(2,0)), (3,(1,2,0)), (7,(1,0))):
        # x^2+1 irreducible over 3,7; x^2+2 over 5; x^3+2x+1 over 3
        n = run(p, poly)
        total += n
        print('extension',p,len(poly),'parameters',n)
    print('DIRECT_ENERGY_CHECK_OK',total)

if __name__ == '__main__': main()
