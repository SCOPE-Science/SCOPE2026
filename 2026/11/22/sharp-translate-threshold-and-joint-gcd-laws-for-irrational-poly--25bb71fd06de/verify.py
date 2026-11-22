"""Exact finite checks supporting the polynomial-translate GCD law.

The infinite-density and tail statements are established analytically, not by this script.
"""
from collections import Counter
from math import gcd, isqrt


def primes_up_to(n):
    arr = [True] * (n + 1)
    if n >= 0: arr[0] = False
    if n >= 1: arr[1] = False
    for k in range(2, isqrt(n) + 1):
        if arr[k]:
            for j in range(k*k, n + 1, k): arr[j] = False
    return [i for i, v in enumerate(arr) if v]


def vp(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def local_pair(p, a, b):
    if a == b:
        return (1 - 2 / p**2 + 1 / p**3) / p**(3*a)
    return (1 - 1 / p) * (1 - 1 / p**2) / p**(a+b+max(a,b))


def predicted_pair(a, b, primes):
    x = 1.0
    for p in primes: x *= local_pair(p, vp(a,p), vp(b,p))
    return x


def exact_floor_sqrt2_power(n, d):
    assert n >= 0
    return isqrt(2 * n**(2*d))


def empirical(N, d, shifts):
    hist = Counter()
    for n in range(1, N + 1):
        hist[tuple(gcd(n, exact_floor_sqrt2_power(n + h, d)) for h in shifts)] += 1
    return hist


def check_finite_crt():
    # Count independent residues (N,M1,M2) modulo q for q=8,9,16.
    for q in [4, 8, 9, 16]:
        for a, b in [(1,1), (2,1), (2,2), (4,2)]:
            if a > q or b > q: continue
            actual = sum(1 for n in range(q) for m1 in range(q) for m2 in range(q)
                         if gcd(q, n) % a == 0 and gcd(q, n) % b == 0
                         and m1 % a == 0 and m2 % b == 0)
            # For q divisible by a and b, exact residue frequency is q^3/(lcm(a,b)*a*b).
            if q % a == 0 and q % b == 0:
                expected = q**3 // ((a*b // gcd(a,b)) * a * b)
                assert actual == expected, (q,a,b,actual,expected)


def check_local_weights():
    # Directly count p-adic exact valuation profiles in independent residues mod p^K.
    for p, K in [(2,5), (3,4)]:
        q = p**K
        for a, b in [(0,0), (0,1), (1,0), (1,1), (2,0), (2,2)]:
            if max(a,b) >= K: continue
            count = 0
            for n in range(q):
                v = vp(n,p) if n else K
                for m1 in range(q):
                    if min(v, vp(m1,p) if m1 else K) != a: continue
                    for m2 in range(q):
                        if min(v, vp(m2,p) if m2 else K) == b: count += 1
            # For valuations <K the finite and p-adic probabilities coincide.
            e = local_pair(p,a,b)
            assert abs(count/q**3 - e) < 1e-12, (p,K,a,b,count/q**3,e)


def run():
    check_finite_crt()
    check_local_weights()
    primes = primes_up_to(10000)
    N = 120000
    hist = empirical(N,2,(0,1))
    print('quadratic shifts 0,1 N=',N)
    for a,b in [(1,1),(1,2),(2,1),(2,2),(3,1),(3,3)]:
        obs = hist[(a,b)]/N
        pred = predicted_pair(a,b,primes)
        print((a,b), 'observed=',round(obs,6),'Euler_product=',round(pred,6))
        assert abs(obs-pred) < 0.015
    # Cubic case has three independently distributed polynomial translates mod 2.
    h3 = empirical(60000,3,(0,1,2))
    obs = sum(c for a,c in h3.items() if all(z%2==0 for z in a))/60000
    print('cubic three shifted gcds all even, empirical=',obs,'limit=',1/16)
    assert abs(obs-1/16) < 0.01
    # The quadratic three-translate obstruction is exact, not just experimental.
    # f(n)=5 sqrt(2) n^2 has finite second difference S strictly between 0 and 23.
    # Therefore all three floor values cannot simultaneously be 0 mod 23.
    for n in range(1,20001):
        a = [isqrt(50*(n+j)**4) for j in (0,1,2)]
        delta = a[2]-2*a[1]+a[0]
        assert 0 < delta < 23
        assert not all(x%23==0 for x in a)
    print('all exact CRT, valuation, sample-density and finite-difference checks passed')

if __name__ == '__main__': run()
