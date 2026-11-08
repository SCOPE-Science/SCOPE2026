#!/usr/bin/env python3
"""Exact finite checks for a positive integer quadratic map."""

def T(n):
    return n // 2 if n % 2 == 0 else n * (n + 5) // 2


def is_power_two(n):
    return n > 0 and (n & (n - 1)) == 0


def odd_part(n):
    while n % 2 == 0:
        n //= 2
    return n


def next_odd(y):
    assert y > 0 and y % 2 == 1
    z = T(y)
    while z % 2 == 0:
        z //= 2
    return z


def predicted(u):
    return u == 1 or is_power_two(u + 5)


def fast_count(X):
    total = 1 + X.bit_length() - 1  # powers of two times the exceptional odd state 1
    m = 3
    while (1 << m) - 5 <= X:
        u = (1 << m) - 5
        total += (X // u).bit_length()
        m += 1
    return total


def brute_count(X):
    return sum(predicted(odd_part(n)) for n in range(1, X + 1))


def check():
    checks = 0
    for y in range(1, 48000, 2):
        j = 0
        k = y + 5
        while k % 2 == 0:
            j += 1
            k //= 2
        assert j >= 1 and k % 2 == 1
        assert next_odd(y) == k * y
        checks += 1
    print(f"ODD_STEP_OK count={checks}")

    hits = []
    for j in range(1, 13):
        for k in range(3, 2002, 2):
            y = (1 << j) * k - 5
            if y <= 0:
                continue
            target = k * y
            if is_power_two(target + 5):
                m = (target + 5).bit_length() - 1
                hits.append((j, k, m, y, target))
    assert hits == [(1, 3, 3, 1, 3)], hits
    print("TERMINAL_ENTRY_OK j=1..12 odd_k=3..2001 unique=(1,3,3,1,3)")

    for m in range(3, 21):
        y = (1 << m) - 5
        x = y
        for i in range(1, m + 1):
            x = T(x)
            if i < m:
                assert x != y
        assert x == y
    assert T(1) == 3
    print("PERIOD_OK m=3..20 plus_unique_tail=1_to_3")

    for X in (1, 2, 10, 100, 1000, 10000):
        assert fast_count(X) == brute_count(X), X
    print("COUNT_OK X=1,2,10,100,1000,10000")
    print("VERIFY_OK exact_arithmetic=true finite_checks_only=true")


if __name__ == "__main__":
    check()
