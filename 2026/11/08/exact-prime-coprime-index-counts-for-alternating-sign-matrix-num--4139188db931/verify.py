#!/usr/bin/env python3
"""Exact finite checks for the prime-coprime alternating-sign-matrix index count.

Only Python's standard library is needed; uses the factorial-product valuation
increment independently of the digit-tree enumeration theorem.
"""


def factorial_valuation(n, p):
    z = 0
    while n:
        n //= p
        z += n
    return z


def predicted_count(p, r):
    if p % 3 == 1:
        b = (2*p + 1)//3
        return b**r
    b = (2*p - 1)//3
    return b**r + 2 * (b**r - 1)//(b-1)


def check_prime(p, exponent):
    limit = p**exponent
    v = 0
    nonzero = 0
    thresholds = {p**r: r for r in range(exponent+1)}
    observed = {0: 1}
    for n in range(limit):
        assert v >= 0, (p, n, v)
        if v == 0:
            nonzero += 1
        if n+1 in thresholds:
            r = thresholds[n+1]
            observed[r] = nonzero
            assert nonzero == predicted_count(p,r), (p, r, nonzero, predicted_count(p,r))
        step = (factorial_valuation(3*n+1,p) + factorial_valuation(n,p)
                - factorial_valuation(2*n+1,p) - factorial_valuation(2*n,p))
        v += step
    assert all(observed[r] == predicted_count(p, r) for r in range(exponent+1))
    # Endpoints of forbidden middle at every level must remain admissible.
    for r in range(1,exponent+1):
        m = p**r
        L = (m+1)//3
        for a in (L,m-L):
            for j in range(1, r+1):
                t = p**j; Lj = (t+1)//3
                s = a%t
                assert s <= Lj or s >= t-Lj, (p,r,a,j,s)
    return limit, observed




def check_layer_identity():
    """Reconstruct every nonnegative triangular layer from floor increments."""
    tested = 0
    for p in (5,7,11,13,17):
        for a in (1,2,3):
            m = p**a
            L = (m+1)//3
            h = 0
            for n in range(m):
                expected = max(0, min(n-L, m-L-n))
                assert h == expected, (p,a,n,h,expected)
                delta = ((3*n+1)//m + n//m
                         - (2*n+1)//m - (2*n)//m)
                h += delta
                tested += 1
            assert h == 0, (p,a,h)
    return tested

def main():
    trials = [(5,6),(7,5),(11,4),(13,4),(17,3),(19,3),
              (23,3),(29,3),(31,3),(37,2),(41,2),(43,2),(47,2)]
    tested = 0
    for p, exponent in trials:
        total, counts = check_prime(p,exponent)
        tested += total
        print(f"p={p} r=1..{exponent} counts="+
              ",".join(str(counts[r]) for r in range(1,exponent+1)))
    layer_cases = check_layer_identity()
    print(f"VERIFY_OK primes={len(trials)} individual_indices={tested} triangular_layer_checks={layer_cases} factorial_valuation_comparisons=PASS endpoint_prefixes=PASS")


if __name__ == '__main__':
    main()
