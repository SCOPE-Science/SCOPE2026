#!/usr/bin/env python3
"""Exact, standalone breadth-first nearest-ranking checks for complete bipartite preference domains."""
from collections import Counter, deque
from fractions import Fraction
from itertools import permutations
from math import factorial


def fall(n, k):
    if k < 0 or k > n:
        return 0
    t = 1
    for j in range(k):
        t *= n - j
    return t


def check(a, b):
    n = a + b
    sources = [p for p in permutations(range(n)) if (p[0] < a) != (p[1] < a)]
    seen = {p: 0 for p in sources}
    queue = deque(sources)
    while queue:
        p = queue.popleft()
        for j in range(n - 1):
            q = p[:j] + (p[j+1], p[j]) + p[j+2:]
            if q not in seen:
                seen[q] = seen[p] + 1
                queue.append(q)
    assert len(sources) == 2*a*b*factorial(n-2)
    assert len(seen) == factorial(n)
    counts = Counter(seen.values())
    for p, actual in seen.items():
        t = 1
        while t < n and ((p[t] < a) == (p[0] < a)):
            t += 1
        assert actual == t-1, (a, b, p, actual, t)
    pmf = [Fraction(counts[d], factorial(n)) for d in range(max(a,b))]
    target = [Fraction(b*fall(a,d+1) + a*fall(b,d+1), fall(n,d+2))
              for d in range(max(a,b))]
    assert pmf == target, (a,b,pmf,target)
    observed_mean = sum((d*v for d, v in enumerate(pmf)), Fraction(0))
    target_mean = Fraction(n*n - 3*a*b - 1, a*b + n + 1)
    assert observed_mean == target_mean, (a,b,observed_mean,target_mean)
    target_outer = Fraction(1) - 4*target_mean/Fraction(n*(n-1))
    assert Fraction(0) <= target_outer <= Fraction(1)
    return len(seen)


def main():
    cases = 0
    permutations_checked = 0
    for n in range(3, 9):
        for a in range(1, n//2+1):
            permutations_checked += check(a, n-a)
            cases += 1
    print('PASS', cases, 'shore splits,', permutations_checked,
          'fully enumerated rankings, all distance, probability, mean and outer-diversity checks')


if __name__ == '__main__':
    main()
