#!/usr/bin/env python3
"""Exact cyclotomic certificate for quartic chirp ambiguity on prime-square cycles.

No floating-point comparisons are used. For a primitive p^2-th root z,
P(z)=0 exactly when each coefficient subsequence in exponents
r, r+p, ..., r+(p-1)p is constant (0 <= r < p).
"""
from collections import Counter


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))


def observed_nonzero(p, a, b):
    N = p * p
    residues = Counter(((x+a)**4-x**4-b*x) % N for x in range(N))
    return any(len({residues[r+p*j] for j in range(p)}) != 1 for r in range(p))


def predicted_nonzero(p, a, b):
    N = p * p
    if a == 0:
        return b == 0
    if a % p:
        disc = (3 * a * (b-a**3)) % p
        return disc == 0 or pow(disc, (p-1)//2, p) == 1
    if b % p:
        return False
    return not (p % 3 == 2 and b == 0)


def main():
    for p in (5,7,11,13):
        assert is_prime(p)
        N = p*p
        observed = 0
        unit = socle = zero = 0
        zero_autocorr = True
        for a in range(N):
            for b in range(N):
                exact = observed_nonzero(p,a,b)
                pred = predicted_nonzero(p,a,b)
                assert exact == pred, (p,a,b,exact,pred)
                if b == 0 and a != 0 and exact:
                    zero_autocorr = False
                observed += int(exact)
                if exact:
                    if a % p: unit += 1
                    elif a: socle += 1
                    else: zero += 1
        expected = 1 + p*p*(p*p-1)//2 + (p-1)*(p-int(p%3 == 2))
        assert observed == expected
        assert zero_autocorr == (p % 3 == 2)
        assert unit == p*p*(p*p-1)//2 and zero == 1
        assert socle == (p-1)*(p-int(p%3 == 2))
        print('p=%d N=%d support=%d unit=%d nonunit=%d zero-shift=%d cazac=%s' %
              (p,N,observed,unit,socle,zero,zero_autocorr), flush=True)
    print('QUARTIC_PRIME_SQUARE_EXACT_CYCLOTOMIC_PASS')

if __name__ == '__main__':
    main()
