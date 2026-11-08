#!/usr/bin/env python3
"""Finite consistency checks for the quadratic odd-branch n(n+3)/2.

The all-integer classification rests on the proof, not on these finite tests.
"""

def is_power2(n):
    return n > 0 and n & (n - 1) == 0


def step(n):
    return n // 2 if n % 2 == 0 else n * (n + 3) // 2


def odd_part(n):
    assert n > 0
    return n >> ((n & -n).bit_length() - 1)


def next_odd(q):
    assert q > 0 and q % 2 == 1
    value = step(q)
    while value % 2 == 0:
        value //= 2
    return value


def terminal(q):
    return is_power2(q + 3)


def bounded_count(x):
    total = 0
    m = 2
    while (1 << m) - 3 <= x:
        q = (1 << m) - 3
        while q <= x:
            total += 1
            q *= 2
        m += 1
    return total


def check():
    for q in range(1, 100001, 2):
        z = q + 3
        j = (z & -z).bit_length() - 1
        k = z >> j
        assert next_odd(q) == q * k
        assert (k == 1) == terminal(q)
        if k > 1:
            assert next_odd(q) > q
    for j in range(1, 16):
        for k in range(3, 502, 2):
            q = (1 << j) * k - 3
            assert q > 0
            assert not terminal(q * k)
    for m in range(2, 18):
        q = (1 << m) - 3
        x = q
        seen = []
        for _ in range(m):
            seen.append(x)
            x = step(x)
        assert x == q
        assert len(set(seen)) == m
        assert set(seen) == {q * (1 << i) for i in range(m)}
    for n in range(1, 2001):
        q = odd_part(n)
        pred = terminal(q)
        x = n
        seen = set()
        for _ in range(120):
            if x in seen:
                assert pred
                break
            seen.add(x)
            if x > 10**125:
                assert not pred
                break
            x = step(x)
        else:
            raise AssertionError(f'unresolved test orbit n={n}')
    for x in (100, 1000, 10000):
        brute = sum(terminal(odd_part(n)) for n in range(1, x+1))
        assert brute == bounded_count(x)
    print('VERIFY_OK odd_transition_100000=yes terminal_arrivals_tested=15x250')
    print('VERIFY_OK exact_cycles_m=2..17 direct_start_n=1..2000')
    print('VERIFY_OK bounded_counts_X=100,1000,10000')
    print('PROOF_STATUS infinite_classification_derived_algebraically_not_from_finite_tests')


if __name__ == '__main__':
    check()
