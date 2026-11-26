#!/usr/bin/env python3
"""Exact-arithmetic checks for a separated-block digital-weight family."""

def digit_sum(n: int) -> int:
    assert n >= 0
    total = 0
    while n:
        n, d = divmod(n, 10)
        total += d
    return total


def verify() -> None:
    a = 448999
    assert a * a == 201600102001
    assert 2 * a * a == 403200204002
    assert (digit_sum(a), digit_sum(a*a), digit_sum(2*a*a)) == (43, 13, 17)
    assert 2*a*a < 10**12
    for k in range(12, 101):
        t = 10**k
        n = a * (t+1)
        assert n % 10 == 9
        assert n == a*t+a
        assert n*n == (a*a)*t*t + (2*a*a)*t + a*a
        assert digit_sum(n) == 86
        assert digit_sum(n*n) == 43
        assert 86 % 43 == 0 and 43 < 86
    print("PASS: exact seed certificates and 89 finite instances; proof handles all k>=12")

if __name__ == "__main__":
    verify()
