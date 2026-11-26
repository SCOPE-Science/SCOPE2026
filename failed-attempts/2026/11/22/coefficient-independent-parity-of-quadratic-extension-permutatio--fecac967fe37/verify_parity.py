#!/usr/bin/env python3
"""Finite examples for the parity theorem on quadratic-extension permutation binomials.

This is an exact finite-domain check, not a substitute for the general proof.
Requires only Python 3's standard library.
"""
from math import gcd


def check(q):
    # This checker treats odd prime q. A nonsquare k defines F_{q^2} = F_q[u]/(u^2-k).
    assert all(q % p for p in range(2, int(q ** .5) + 1))
    k = next(k for k in range(2, q) if pow(k, (q-1)//2, q) == q-1)
    def add(x, y):
        return (x % q + y % q) % q + q * ((x // q + y // q) % q)
    def mul(x, y):
        a, b = x % q, x // q
        c, d = y % q, y // q
        return ((a*c + k*b*d) % q) + q * ((a*d + b*c) % q)
    def power(x, exponent):
        z = 1
        while exponent:
            if exponent & 1:
                z = mul(z, x)
            x = mul(x, x)
            exponent //= 2
        return z
    def parity(perm):
        marked = bytearray(len(perm))
        cycles = 0
        for i in range(len(perm)):
            if marked[i]:
                continue
            cycles += 1
            x = i
            while not marked[x]:
                marked[x] = 1
                x = perm[x]
        return (len(perm) - cycles) % 2

    count = [0, 0]
    for d in range(1, q+2):
        if gcd(d, q+1) != 2:
            continue
        for r in range(1, 2*(q+1), 2):
            if gcd(r, q-1) != 1:
                continue
            for a in range(q*q):
                f = [mul(power(x, r), add(power(x, d*(q-1)), a))
                     for x in range(q*q)]
                if len(set(f)) != q*q:
                    continue
                observed = parity(f)
                expected = ((r-1)//2) % 2
                assert observed == expected, (q, d, r, a, observed, expected)
                # Verify the finite-field coefficient lemma used in the proof.
                w = power(a, (q+1)//2)
                assert power(w, q) == w, (q, d, r, a, w)
                count[observed] += 1
    return count


def main():
    total = [0, 0]
    for q in (3, 5, 7, 11, 13):
        counts = check(q)
        assert sum(counts) > 0
        print(f'q={q}: even={counts[0]}, odd={counts[1]}')
        total[0] += counts[0]
        total[1] += counts[1]
    assert total == [707, 544], total
    print(f'PASS: {sum(total)} exact permutation instances; parity and coefficient lemma verified')


if __name__ == '__main__':
    main()
