"""Reproduce commuting-pair counts for Boolean translation inverse monoids.
Standard-library only. The exhaustive checks cover elementary abelian groups of
orders 2, 4 and 8, and direct multiplication for order 4.
"""
from collections import Counter


def rank_binary(rows):
    basis = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = row
                break
            row ^= basis[pivot]
    return len(basis)


def fixed_label_count(n, a, b):
    # G=(C_2)^k with bitwise XOR as addition. For fixed subset S,
    # the commuting conditions are homogeneous linear equations in T.
    total = 0
    for S in range(1 << n):
        rows = []
        for x in range(n):
            row = 0
            if (S >> (x ^ b)) & 1:
                row ^= 1 << x
            if (S >> x) & 1:
                row ^= 1 << (x ^ a)
            rows.append(row)
        total += 1 << (n - rank_binary(rows))
    return total


def reference_formula(n):
    if n == 2:
        return 4**n + 3 * (n - 1) * 10**(n//2)
    return 4**n + 3 * (n - 1) * 10**(n//2) + (n - 1) * (n - 2) * 58**(n//4)


def direct_commutes(n, a, S, b, T):
    # In the semidirect product (S,a)(T,b)=(S intersect (a+T),a+b).
    first = 0
    second = 0
    for x in range(n):
        if ((S >> x) & 1) and ((T >> (x ^ a)) & 1):
            first |= 1 << x
        if ((T >> x) & 1) and ((S >> (x ^ b)) & 1):
            second |= 1 << x
    return first == second


def quotient_multiply(n, element1, element2):
    if element1 is None or element2 is None:
        return None
    a, S = element1
    b, T = element2
    intersection = sum(1 << x for x in range(n)
                       if ((S >> x) & 1) and ((T >> (x ^ a)) & 1))
    if intersection == 0:
        return None
    return (a ^ b, intersection)


def verify_quotient_direct(n):
    elements = [None] + [(a, S) for a in range(n)
                         for S in range(1, 1<<n)]
    count = sum(quotient_multiply(n, u, v) == quotient_multiply(n, v, u)
                for u in elements for v in elements)
    return count


def check(n):
    raw = sum(fixed_label_count(n, a, b) for a in range(n) for b in range(n))
    target = reference_formula(n)
    assert raw == target, (n, raw, target)
    quotient = raw - 2*n*(n-1)*2**n + (n-1)**2
    size = 1 + n*(2**n-1)
    assert quotient >= 4**n and quotient <= size**2
    print(f'order {n}: full={raw}, quotient={quotient}, monoid_size={size} -> PASS')
    if n <= 4:
        direct = sum(direct_commutes(n, a, S, b, T)
                     for a in range(n) for S in range(1<<n)
                     for b in range(n) for T in range(1<<n))
        assert direct == raw
        print(f'order {n}: direct multiplication full={direct} -> PASS')
        quotient_direct = verify_quotient_direct(n)
        assert quotient_direct == quotient
        print(f'order {n}: direct quotient={quotient_direct} -> PASS')


def check_rank_table():
    counts = Counter()
    a,b,n = 1,2,4
    for S in range(1<<n):
        rows=[]
        for x in range(n):
            row=0
            if (S>>(x^b))&1:row^=1<<x
            if (S>>x)&1:row^=1<<(x^a)
            rows.append(row)
        counts[(S.bit_count(),rank_binary(rows))]+=1
    expected = {(0,0):1,(1,2):4,(2,2):4,(2,4):2,(3,4):4,(4,2):1}
    assert counts == expected, (counts,expected)
    assert sum(c*(2**(4-r)) for (_,r),c in counts.items()) == 58
    print('four-point independent-shift rank table: PASS')


if __name__ == '__main__':
    check_rank_table()
    for n in [2,4,8]:
        check(n)
    print('ALL CHECKS PASSED')
