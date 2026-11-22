"""Independent composition-level checks for commuting partial translations.

The finite checks are illustrations. The all-n assertion uses the separate
combinatorial proof given in RESULT.md; testing is not that proof.
"""
from itertools import product
from math import comb


def elements(n):
    # Each transformation is (left shift, bitset of its nonempty domain).
    ans = [(0, mask) for mask in range(1 << n)]
    for k in range(1, n):
        for selector in range(1, 1 << (n-k)):
            ans.append((k, selector << k))
    return ans


def compose(a, b, n):
    k, s = a
    l, t = b
    mask = 0
    for x in range(n):
        if (s >> x) & 1 and x >= k and (t >> (x-k)) & 1:
            mask |= 1 << x
    if not mask:
        return (0, 0)
    return (k+l, mask)


def commuting(a, b, n):
    return compose(a,b,n) == compose(b,a,n)


def exact_one_shift_formula(n):
    return 4 * 3**n - (2*n+4) * 2**n


def direct_counts(n):
    els = elements(n)
    count = 0
    one_shift = 0
    crossing_ranks = [0] * (n + 1)
    e_e = 0
    for a in els:
        for b in els:
            if commuting(a,b,n):
                count += 1
                if (a[0] == 0) and (b[0] == 0):
                    e_e += 1
                if (a[0] == 0) != (b[0] == 0):
                    one_shift += 1
                    shifted = a if a[0] else b
                    crossing_ranks[shifted[1].bit_count()] += 1
    return len(els), count, e_e, one_shift, crossing_ranks


def spin_count(n, d):
    total = 0
    for subset in range(1 << n):
        equals = sum(((subset >> x) & 1) == ((subset >> (x-d)) & 1)
                     for x in range(d, n))
        total += (1 << equals)
    return total


def main():
    for n in range(1, 9):
        length, comm, ee, one, ranks = direct_counts(n)
        assert length == 2**(n+1)-n-1, (n,length)
        assert ee == 4**n, (n,ee)
        assert one == exact_one_shift_formula(n), (n,one)
        for d in range(1,n):
            assert spin_count(n,d) == 2**d * 3**(n-d)
        assert comm >= ee + one
        assert all(ranks[r] == (2**(n-r+1)*comb(n,r+1) if 1 <= r < n else 0) for r in range(n+1)), (n,ranks)
        print(n, length, comm, ee, one)
    print('ORDER_DECREASING_PARTIAL_ISOMETRY_COMMUTING_OK')

if __name__ == '__main__':
    main()
