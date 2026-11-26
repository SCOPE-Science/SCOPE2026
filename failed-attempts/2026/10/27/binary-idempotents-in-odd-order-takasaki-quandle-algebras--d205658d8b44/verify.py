#!/usr/bin/env python3
"""Exact independent finite checks for binary odd-order Takasaki quandle idempotents.

Run: python3 verify_binary_takasaki.py
"""

def gf2_divmod(a, b):
    assert b > 0
    q = 0
    while a and a.bit_length() >= b.bit_length():
        k = a.bit_length() - b.bit_length()
        q ^= 1 << k
        a ^= b << k
    return q, a


def factors_xn_plus_1(n):
    assert n >= 1 and n % 2 == 1
    rem = (1 << n) | 1
    factors = []
    for d in range(1, n + 1):
        for body in range(1, 1 << d, 2):
            p = (1 << d) | body
            while rem != 1:
                q, r = gf2_divmod(rem, p)
                if r:
                    break
                factors.append(p)
                rem = q
        if rem == 1:
            break
    assert rem == 1 and len(factors) == len(set(factors))
    return factors


def reciprocal(p):
    d = p.bit_length() - 1
    return sum(((p >> i) & 1) << (d - i) for i in range(d + 1))


def formula_cyclic(n):
    fs = factors_xn_plus_1(n)
    unseen = set(fs)
    total = 1
    while unseen:
        f = unseen.pop()
        d = f.bit_length() - 1
        g = reciprocal(f)
        assert g in fs
        if f == g:
            if d == 1:
                total *= 2
            else:
                assert d % 2 == 0
                total *= (1 << (d // 2)) + 2
        else:
            assert g in unseen
            unseen.remove(g)
            total *= 1 << d
    return total


def count_direct(elements, operation):
    n = len(elements)
    table = [[operation(i, j) for j in range(n)] for i in range(n)]
    count = 0
    for mask in range(1 << n):
        nonzero = [i for i in range(n) if mask >> i & 1]
        product = 0
        for i in nonzero:
            for j in nonzero:
                product ^= 1 << table[i][j]
        count += product == mask
    return count


def run():
    for n in (1, 3, 5, 7, 9, 11, 13, 15):
        actual = count_direct(list(range(n)), lambda i, j: (2 * j - i) % n)
        predicted = formula_cyclic(n)
        assert actual == predicted, (n, actual, predicted)
        print('cyclic', n, 'idempotents', actual)
    # For exponent-three groups, the quandle product is commutative,
    # hence every binary linear combination is idempotent.
    a = [(i, j) for i in range(3) for j in range(3)]
    index = {v: i for i, v in enumerate(a)}
    actual = count_direct(a, lambda i, j: index[tuple((2 * a[j][k] - a[i][k]) % 3 for k in range(2))])
    assert actual == 2 * 4**4 == 512
    print('C3xC3', 'idempotents', actual)
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
