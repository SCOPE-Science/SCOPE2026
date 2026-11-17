"""Exact independent finite checks for minimum facet transversals of cyclic polytopes.

Gale evenness is implemented directly, not via the matching reduction.
Run: python3 verify.py
"""
from itertools import combinations
from math import comb


def facets_gale(n, d):
    vertices = set(range(n))
    ans = []
    for entry in combinations(range(n), d):
        f = set(entry)
        missing = sorted(vertices - f)
        if all(sum(i < x < j for x in entry) % 2 == 0
               for i, j in combinations(missing, 2)):
            ans.append(sum(1 << i for i in entry))
    return ans


def predicted_count(n, k):
    h = n // 2
    r = k - 1
    return (n if n % 2 else 2) * comb(h, r)


def brute(n, k):
    d = 2 * k
    fac = facets_gale(n, d)
    best = n + 1
    solutions = []
    for mask in range(1 << n):
        count = mask.bit_count()
        if count > best:
            continue
        if all(mask & f for f in fac):
            if count < best:
                best, solutions = count, [mask]
            else:
                solutions.append(mask)
    return best, solutions, len(fac)


def classify(n, k, sols):
    h, r = n // 2, k - 1
    # Every optimal complement must contain a maximum independent set of C_n.
    independent = []
    for set_bits in combinations(range(n), h):
        s = set(set_bits)
        if all((i + 1) % n not in s for i in s):
            independent.append(sum(1 << i for i in s))
    predicted = set()
    all_mask = (1 << n) - 1
    for I in independent:
        rem = [i for i in range(n) if not ((I >> i) & 1)]
        for add in combinations(rem, r):
            Y = I | sum(1 << i for i in add)
            predicted.add(all_mask ^ Y)
    assert set(sols) == predicted, (n, k, 'classification mismatch')


def main():
    cases = 0
    tested = 0
    for n in range(3, 14):
        for k in range(1, (n - 1) // 2 + 1):
            if n == 13 and k > 4:
                continue
            best, sols, fcount = brute(n, k)
            assert best == (n + 1) // 2 - k + 1, (n, k, best)
            assert len(sols) == predicted_count(n, k), (n, k, len(sols))
            classify(n, k, sols)
            cases += 1
            tested += fcount
    print('PASS', cases, 'Gale-evenness instances,', tested,
          'directly constructed facet sets; exact minimum size, count, classification.')


if __name__ == '__main__':
    main()
