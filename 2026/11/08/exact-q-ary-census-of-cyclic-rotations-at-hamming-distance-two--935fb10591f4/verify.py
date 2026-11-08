"""Direct finite tests of the exact distance-two cyclic-shift multiplicity formulas."""
from itertools import product


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    primes = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            primes += 1
        p += 1
    if n > 1:
        primes += 1
    return (-1) ** primes


def phi(n):
    ans = n
    for p in range(2, n + 1):
        if n % p == 0:
            ans = ans // p * (p - 1)
            while n % p == 0:
                n //= p
        if n == 1:
            break
    return ans


def predicted(n, q):
    proper = divisors(n)[:-1]
    N = {g: n * (q - 1) * q**g if n // g >= 3 else
         (n // 2) * (q - 1) * q**g for g in proper}
    E = {g: sum(mobius(g // d) * N[d] for d in proper if g % d == 0)
         for g in proper}
    numerator = n * (q - 1) * sum(phi(h) * (h - 1) * q**(n // h)
                                   for h in divisors(n) if h > 1)
    assert numerator % 2 == 0
    T = numerator // 2
    rem = T - sum((n // g - 1) * E[g] for g in proper)
    assert rem % 2 == 0
    B = rem // 2
    counts = {0: q**n - sum(E.values()) - B, 2: B}
    for g in proper:
        r = n // g - 1
        counts[r] = counts.get(r, 0) + E[g]
    return {r: val for r, val in counts.items() if val}


def observed(n, q):
    out = {}
    for w in product(range(q), repeat=n):
        k = sum(sum(w[i] != w[(i + d) % n] for i in range(n)) == 2
                for d in range(1, n))
        out[k] = out.get(k, 0) + 1
    return out


def main():
    cases = 0
    for q, stop in ((3, 9), (4, 7), (5, 6)):
        for n in range(2, stop):
            a, b = predicted(n, q), observed(n, q)
            assert a == b, (q, n, a, b)
            cases += 1
    print('PASS: %d exact q-ary exhaustive histograms' % cases)
    print('example q=3 n=6:', predicted(6, 3))


if __name__ == '__main__':
    main()
