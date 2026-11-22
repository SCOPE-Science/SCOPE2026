#!/usr/bin/env python3
"""Independent finite checks of a seven-adic Delannoy-character correlation theorem.

Usage: python3 verify_delannoy7.py
Python standard library only. Finite checks supplement, but do not replace, the proof.
"""
from math import comb

P = 7
W = (1, -1, -1, 0, -1, -1, 1)


def delannoy(n):
    return sum(comb(n, j)**2 * 2**j for j in range(n + 1))


def digit_character(n):
    out = 1
    while n:
        out *= W[n % 7]
        n //= 7
    return out


def direct_character(n):
    v = delannoy(n) % 7
    return 0 if v == 0 else (1 if pow(v, 3, 7) == 1 else -1)


def transition(d):
    t = [[0, 0], [0, 0]]
    for c in range(2):
        for a in range(7):
            t[c][(a + d + c) // 7] += W[a] * W[(a + d + c) % 7]
    return t


T = [transition(d) for d in range(7)]
EXPECTED = [
    [[6, 0], [0, 1]],
    [[0, 1], [-1, -2]],
    [[-1, -2], [2, -1]],
    [[2, -1], [-1, 2]],
    [[-1, 2], [-2, -1]],
    [[-2, -1], [1, 0]],
    [[1, 0], [0, 6]],
]


def rowtimes(v, matrix):
    return [sum(v[c] * matrix[c][end] for c in range(2)) for end in range(2)]


def digits(h):
    z = []
    while h:
        z.append(h % 7)
        h //= 7
    return z


def carry_vector(h):
    assert h >= 1
    v = [1, 0]
    ds = digits(h)
    for d in ds:
        v = rowtimes(v, T[d])
    return v, len(ds)


def exact_sum_formula(r, h):
    v, k = carry_vector(h)
    assert r >= k
    return v[0] * 6**(r-k) - v[1]


def limit_num_den(h):
    v, k = carry_vector(h)
    return v[0], 6**k


def main():
    checks = 0
    assert T == EXPECTED
    checks += 7*4
    for n in range(100):
        assert digit_character(n) == direct_character(n), n
        checks += 1
    for d in range(7):
        assert max(sum(abs(T[d][i][j]) for i in range(2)) for j in range(2)) <= 6
        checks += 1
    for d in range(1, 7):
        first = rowtimes([1,0],T[d])
        assert max(abs(x) for x in first) <= 2
        checks += 1
    for r, max_h in [(1, 6), (2, 47), (3, 120), (4, 130)]:
        F = [digit_character(n) for n in range(7**r + max_h)]
        for h in range(1, max_h+1):
            if 7**r <= h:
                continue
            direct = sum(F[n]*F[n+h] for n in range(7**r))
            predicted = exact_sum_formula(r, h)
            assert predicted == direct, (r, h, predicted, direct)
            checks += 1
    for h in range(1,7**5):
        a, den = limit_num_den(h)
        assert abs(3*a) <= den, h
        expected = ((3 if a>0 else 5)*7**(len(digits(h))-1)) if a and abs(3*a)==den else None
        # Equality need not have the nonzero digit in the top place: strip powers of seven.
        if a and abs(3*a) == den:
            x=h
            while x%7 == 0: x//=7
            assert x == (3 if a>0 else 5), (h,a,den)
        else:
            x=h
            while x%7 == 0: x//=7
            assert x not in (3,5), (h,a,den)
        checks += 1
    for j in range(6):
        for d, sign in ((3,1), (5,-1)):
            a,den=limit_num_den(d*7**j)
            assert 3*a==sign*den
            checks += 1
    print(f"PASS: {checks} exact finite assertions")
    print("Transition matrix, residue seed, direct coefficients, all-shift finite-block identity, and sharp extremizers checked.")

if __name__ == '__main__':
    main()
