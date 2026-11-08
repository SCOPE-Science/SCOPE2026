"""Standalone exact integer checks for Rudin--Shapiro extremal window locations.

Run: python3 verify.py
Only finite cases are verified computationally; the accompanying proof covers all k.
"""
from itertools import product


def rs(i):
    return -1 if (i & (i >> 1)).bit_count() % 2 else 1


def formula(k):
    if k % 2 == 0:
        h = k // 2
        L = 4**h
        H = 3 * 2**h - 2
        return H, (5 * 4**h + 1) // 3, (35 * 4**h + 1) // 3
    h = (k - 1) // 2
    L = 2 * 4**h
    H = 2**(h + 2) - 2
    return H, (10 * L + 1) // 3, (16 * L + 1) // 3


def check(k):
    L = 1 << k
    max_expected, imax, imin = formula(k)
    # k even: imin = (35*L+1)/3? For L=4 expect (140+1)/3 =47.
    # k odd: imin = (16*L+1)/3? L=8 -> 129/3=43.
    assert imax >= 0 and imin >= 0
    m = 13 * L + 1
    signs = [rs(i) for i in range(m)]
    sums = [0]
    for a in signs:
        sums.append(sums[-1] + a)
    windows = [sums[i+L] - sums[i] for i in range(12*L+1)]
    hpos = max(windows)
    hneg = min(windows)
    gotpos = windows.index(hpos)
    gotneg = windows.index(hneg)
    assert (hpos, hneg) == (max_expected, -max_expected), (k, hpos, hneg, max_expected)
    assert gotpos == imax, (k, 'positive start', gotpos, imax)
    assert gotneg == imin, (k, 'negative start', gotneg, imin)
    return L, hpos, gotpos, gotneg


def recursive_checks():
    P, Q = [1], [1]
    u, v = 1, 1
    for k in range(0, 17):
        assert len(P) == len(Q) == 1 << k
        assert all(P[i] == rs(i) for i in range(len(P)))
        assert all(Q[i] == rs(i) * (-1 if k and i >= 1 << (k-1) else 1)
                   for i in range(len(Q)))
        p, q = sum(P), sum(Q)
        ap = [0]; bp = [0]
        for a, b in zip(P, Q):
            ap.append(ap[-1] + a)
            bp.append(bp[-1] + b)
        assert min(ap) == min(bp) == 0
        assert ap.index(max(ap)) == u
        assert bp.index(max(bp)) == v
        if k % 2 == 0:
            t = 1 << (k // 2)
            assert (p, q, max(ap), max(bp)) == (t, t, 2*t-1, t)
        else:
            t = 1 << ((k+1)//2)
            assert (p, q, max(ap), max(bp)) == (t, 0, t, t-1)
        if k < 16:
            P, Q = P + Q, P + [-v for v in Q]
            u, v = (1 << k) + v, u


def main():
    recursive_checks()
    for k in range(2, 17):
        L, H, imax, imin = check(k)
        print(f'k={k:2d} length={L:5d} extreme={H:4d} first_positive={imax:6d} first_negative={imin:6d}')
    print('PASS: recursive prefix-extremum certificates and 15 complete finite scans')


if __name__ == '__main__':
    main()
