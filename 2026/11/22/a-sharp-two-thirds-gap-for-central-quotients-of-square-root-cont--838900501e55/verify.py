"""Exact continued-fraction algorithm and finite verification of the central-quotient gap."""
from math import isqrt


def period(d):
    a0 = isqrt(d)
    if d <= 1 or a0 * a0 == d:
        raise ValueError("d must be an integer greater than one and nonsquare")
    m, q, a = 0, 1, a0
    states = []
    while True:
        m = q * a - m
        numerator = d - m * m
        assert numerator % q == 0
        q = numerator // q
        assert q > 0
        a = (a0 + m) // q
        assert a >= 1
        states.append((m, q, a))
        if a == 2 * a0:
            return a0, states


def check():
    checked = 0
    even_periods = 0
    exceptional = []
    for d in range(2, 100001):
        a0 = isqrt(d)
        if d == a0 * a0:
            continue
        a0, states = period(d)
        checked += 1
        ell = len(states)
        assert states[-1] == (a0, 1, 2 * a0)
        if ell % 2 == 0:
            even_periods += 1
            r = ell // 2
            m, q, c = states[r - 1]
            assert m == states[r][0]
            assert 2 * m == q * c
            assert q >= 2
            assert 1 <= c <= a0
            assert c in (a0, a0 - 1) or 3 * c <= 2 * a0
            if c == a0 - 2:
                exceptional.append((d, a0, ell, c))
    assert exceptional == [(15, 3, 2, 1), (20, 4, 2, 2),
                           (21, 4, 6, 2), (39, 6, 2, 4)]
    # This finite loop is a complete exhaustion of the only allowable A values.
    small = []
    for A in range(3, 7):
        for d in range(A*A+1, (A+1)*(A+1)):
            a0, states = period(d)
            assert a0 == A
            if len(states) % 2 == 0 and states[len(states)//2 - 1][2] == A-2:
                small.append(d)
    assert small == [15, 20, 21, 39]
    for t in range(1, 501):
        A = 3*t
        a0, states = period(A*A + 3)
        assert a0 == A and states == [(A, 3, 2*t), (A, 1, 2*A)]
    print(f"PASS: {checked} nonsquares through 100000, {even_periods} even periods")
    print("PASS: complete A=3..6 exceptional census [15, 20, 21, 39]")
    print("PASS: sharp family, t=1..500")

if __name__ == "__main__":
    check()
