"""Exact finite verification of the cubic-coset triple-completeness cutoff.

Python 3, standard library only. Two independent assignments of coset labels
(via cube sets and via primitive-root discrete logarithms) are compared.
"""
from math import isqrt
from collections import Counter


def primes_under(limit):
    for p in range(2, limit + 1):
        if all(p % d for d in range(2, isqrt(p) + 1)):
            yield p


def cosets_by_cube(p):
    cubes = {pow(a, 3, p) for a in range(1, p)}
    h = next(a for a in range(2, p) if a not in cubes)
    labels = [-1] * p
    for j in range(3):
        for a in cubes:
            v = a * pow(h, j, p) % p
            if labels[v] != -1:
                assert labels[v] == j
            labels[v] = j
    assert labels[0] == -1 and set(labels[1:]) == {0, 1, 2}
    return labels, h


def prime_divisors(n):
    out = []
    for p in range(2, isqrt(n) + 1):
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
    if n > 1:
        out.append(n)
    return out


def cosets_by_generator(p, h):
    divs = prime_divisors(p - 1)
    g = next(g for g in range(2, p)
             if all(pow(g, (p - 1) // q, p) != 1 for q in divs))
    labels = [-1] * p
    v = 1
    for k in range(p - 1):
        assert labels[v] == -1
        labels[v] = k % 3
        v = v * g % p
    assert v == 1
    assert labels[h] in (1, 2)
    alpha = labels[h]
    return [(x * alpha) % 3 if x != -1 else -1 for x in labels]


def patterns(labels, p):
    return {tuple(labels[n:n + 3]) for n in range(1, p - 2)}


def test():
    all_patterns = {(a, b, c) for a in range(3) for b in range(3) for c in range(3)}
    fails = []
    checked = []
    for p in primes_under(840):
        if p % 3 != 1:
            continue
        ca, h = cosets_by_cube(p)
        cb = cosets_by_generator(p, h)
        assert ca == cb, (p, ca, cb)
        got = patterns(ca, p)
        missing = sorted(all_patterns - got)
        if missing:
            fails.append((p, len(got), missing))
        else:
            checked.append(p)
        if p >= 307:
            assert not missing, (p, missing)
    assert fails[-1][0] == 283
    assert len(checked) > 0
    assert min(x for x in checked if x > 283) == 307
    ca, _ = cosets_by_cube(307)
    witnesses = {}
    for n in range(1, 305):
        witnesses.setdefault(tuple(ca[n:n+3]), n)
    assert len(witnesses) == 27
    print('checked_eligible_primes=', len(checked) + len(fails))
    print('all_27_pass_prime_count=', len(checked))
    print('failing_primes_and_missing_counts=', [(p, len(ms)) for p, _, ms in fails])
    print('last_failure=', fails[-1])
    print('smallest_success_above_last_failure=', 307)
    print('p307_witnesses=', [(k, witnesses[k]) for k in sorted(witnesses)])
    print('weillower_bound_at_841=', 841 - 28 * 841 ** 0.5 - 27)
    assert 841 - 28 * 841 ** 0.5 - 27 > 0
    assert all( p % 3 != 1 for p in range(284, 307) if p in set(primes_under(307)))
    print('VERIFY_OK')


if __name__ == '__main__':
    test()
