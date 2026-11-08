#!/usr/bin/env python3
"""Exact finite tests for simultaneous primitive-root lifting of x +/- x^{-1}."""


def prime_divisors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive(x, p, k):
    mod = p ** k
    if x % p == 0:
        return False
    order = (p - 1) * p ** (k - 1)
    return all(pow(x, order // q, mod) != 1 for q in prime_divisors(order))


def f(x, eps, m):
    return (x + eps * pow(x, -1, m)) % m


def roots(p, eps, a):
    m = p * p
    t1 = [t for t in range(p) if pow(a + p * t, p - 1, m) == 1]
    t2 = [t for t in range(p) if pow(f(a + p * t, eps, m), p - 1, m) == 1]
    assert len(t1) == len(t2) == 1
    return t1[0], t2[0]


def run():
    primes = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
              53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    local_checks = 0
    seed_checks = 0
    triple_checks = 0
    delta_types = set()
    for p in primes:
        for eps in (1, -1):
            seeds = [a for a in range(1, p)
                     if primitive(a, p, 1) and primitive(f(a, eps, p), p, 1)]
            predicted = 0
            for a in seeds:
                s1, s2 = roots(p, eps, a)
                delta = int(s1 == s2)
                delta_types.add(delta)
                count2 = sum(primitive(a + p * t, p, 2)
                             and primitive(f(a + p * t, eps, p * p), p, 2)
                             for t in range(p))
                assert count2 == p - 2 + delta, (p, eps, a, count2, delta)
                predicted += count2
                seed_checks += 1
            direct = sum(primitive(x, p, 2) and primitive(f(x, eps, p*p), p, 2)
                         for x in range(1, p*p) if x % p)
            assert predicted == direct, (p, eps, predicted, direct)
            local_checks += 1
    for p in (7, 11, 17, 19, 23):
        for eps in (1, -1):
            mod = p ** 3
            for a in range(1, p):
                if not (primitive(a, p, 1) and primitive(f(a, eps, p), p, 1)):
                    continue
                predicted = p * (p - 2 + int(roots(p, eps, a)[0] == roots(p, eps, a)[1]))
                direct = sum(primitive(x, p, 3) and primitive(f(x, eps, mod), p, 3)
                             for x in range(a, mod, p))
                assert predicted == direct, (p, eps, a, predicted, direct)
                triple_checks += 1
    exceptions = {1: {3, 5, 7, 13}, -1: {3, 5, 13, 61}}
    exception_checks = 0
    for p in (3, 5, 7, 13, 61):
        for eps in (1, -1):
            seeds = [a for a in range(1, p)
                     if primitive(a, p, 1) and primitive(f(a, eps, p), p, 1)]
            assert bool(seeds) == (p not in exceptions[eps])
            exception_checks += 1
    assert delta_types == {0, 1}
    print(f"VERIFY_OK local_cases={local_checks} base_seeds={seed_checks} "
          f"prime_cube_fibers={triple_checks} exception_checks={exception_checks} both_overlap_types=PASS")


if __name__ == '__main__':
    run()
