#!/usr/bin/env python3
"""Reproducible finite checks for exact repeated-subsequence length of binary run powers."""
from itertools import product


def predicted(a, b, k, e):
    assert min(a, b, k) >= 1 and e >= 2
    return e * max((k // e) * (a + b), (k * a) // e, (k * b) // e)


def is_subsequence(pattern, source):
    j = 0
    for x in source:
        if j < len(pattern) and x == pattern[j]:
            j += 1
    return j == len(pattern)


def exhaustive(a, b, k, e):
    source = ('0' * a + '1' * b) * k
    for m in range(len(source) // e, 0, -1):
        for chars in product('01', repeat=m):
            root = ''.join(chars)
            if is_subsequence(root * e, source):
                return e * m
    return 0


def longest_common_subsequence(a, b):
    old = [0] * (len(b) + 1)
    for x in a:
        new = [0] * (len(b) + 1)
        for j, y in enumerate(b, 1):
            new[j] = old[j-1] + 1 if x == y else max(old[j], new[j-1])
        old = new
    return old[-1]


def partition_square(source):
    return 2 * max(longest_common_subsequence(source[:p], source[p:]) for p in range(1, len(source)))


def cyclic_ceiling_cost(u, a, b):
    if len(set(u)) < 2:
        return None
    runs = []
    for c in u:
        if runs and runs[-1][0] == c:
            runs[-1][1] += 1
        else:
            runs.append([c, 1])
    if runs[0][0] == runs[-1][0]:
        runs[0][1] += runs[-1][1]
        runs.pop()
    return (sum((v+a-1)//a for c,v in runs if c=='0'),
            sum((v+b-1)//b for c,v in runs if c=='1'))


def main():
    tests = 0
    full_root_probes = 0
    cost_checks = 0
    partition_checks = 0
    for a in range(1, 5):
        for b in range(1, 5):
            for k in range(1, 6):
                source = ('0' * a + '1' * b) * k
                for e in range(2, 5):
                    if len(source) > 27:
                        continue
                    actual = exhaustive(a,b,k,e)
                    assert actual == predicted(a,b,k,e), (a,b,k,e,actual,predicted(a,b,k,e))
                    tests += 1
                    full_root_probes += sum(2**m for m in range(1, len(source)//e + 1))
                    if e == 2:
                        part = partition_square(source)
                        assert part == actual, (a,b,k,e,part,actual)
                        partition_checks += 1
                # Check the key cyclic-ceiling necessary condition independently for all roots of bounded length.
                for e in range(2, 5):
                    if len(source) > 24: continue
                    for m in range(1, min(9, len(source)//e) + 1):
                        for chars in product('01', repeat=m):
                            u = ''.join(chars)
                            cost = cyclic_ceiling_cost(u,a,b)
                            if cost is not None and is_subsequence(u*e, source):
                                assert e*max(cost) <= k, (a,b,k,e,u,cost)
                            cost_checks += 1
    # Independent long inputs: partition-based calculation avoids exponential root enumeration.
    for a,b,k in [(10,1,3),(1,10,3),(7,5,5),(11,3,3),(9,2,7),(2,9,7),(6,6,6)]:
        source=('0'*a+'1'*b)*k
        assert partition_square(source)==predicted(a,b,k,2)
        partition_checks += 1
    print('VERIFY_OK', 'exhaustive_parameter_sets',tests,
          'root_candidate_upper_bound',full_root_probes,
          'cyclic_cost_probes',cost_checks,
          'independent_partition_square_cases',partition_checks)

if __name__=='__main__': main()
