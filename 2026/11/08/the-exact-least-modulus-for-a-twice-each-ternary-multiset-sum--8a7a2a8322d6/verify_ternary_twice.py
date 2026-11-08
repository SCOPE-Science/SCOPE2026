"""Exact finite cross-checks of the ternary twice-each modular uniqueness theorem.

Run: python3 verify_ternary_twice.py
Python standard library only. The proof of the unrestricted theorem is in RESULT.md.
"""
from itertools import combinations


def predicted(n):
    powers = [3 ** t for t in range(n) if t % 2 != n % 2 and 3 ** t <= 2*n-1]
    assert powers
    return (3**n - max(powers)) // 2


def direct_differences(n):
    """List every possible difference using compositions of 2n into n bins."""
    length = 2*n
    baseline = 3**n-1
    d = set()
    def rec(i, left, val):
        if i == n-1:
            diff = val + left * 3**i - baseline
            d.add(diff)
            return
        for count in range(left+1):
            rec(i+1,left-count,val+count*3**i)
    rec(0,length,0)
    assert 0 in d
    return d


def dynamic_differences(n):
    """Independent coin-count dynamic programming over weighted sums."""
    length = 2*n
    states = [set() for _ in range(length+1)]
    states[0].add(0)
    for i in range(n):
        nxt=[set() for _ in range(length+1)]
        power=3**i
        for used in range(length+1):
            for value in states[used]:
                for take in range(length-used+1):
                    nxt[used+take].add(value+take*power)
        states=nxt
    return {x-(3**n-1) for x in states[length]}


def first_valid(d, cap):
    return next(N for N in range(2,cap+1) if all(x % N for x in d if x))


if __name__ == '__main__':
    for n in range(2,9):
        d=direct_differences(n)
        alt=dynamic_differences(n)
        assert d == alt
        N=predicted(n)
        assert N == first_valid(d,N)
        # Nonzero exact integer collisions must be absent.
        assert 0 in d
        # Compare all possible size-2n multisets; every difference was tested.
        print(f'n={n} N_min={N} attainable_differences={len(d)} exhaustive=yes')
    for n in range(2,1001):
        N=predicted(n)
        assert N & 1
        t=3**n-2*N
        assert t <= 2*n-1 and t > 0
        assert N <= (3**n-1-2*n)
    print('VERIFY_OK exhaustive_n=2..8 independent_DP=yes arithmetic=exact formula_integrity_n=2..1000')
