#!/usr/bin/env python3
"""Exact finite checks for power domination and TAR connectivity on crown graphs.

Run: python3 verify_crown.py
No nonstandard libraries. Finite checks are evidence, not proofs for arbitrary n.
"""
from collections import Counter
from math import comb


def power_dominates(n, mask):
    """Simulate the standard observation + iterative single-white-neighbor rules."""
    order = 2 * n
    nb = [sum(1 << (n + j) for j in range(n) if j != i)
          for i in range(n)]
    nb += [sum(1 << j for j in range(n) if j != i)
           for i in range(n)]
    observed = mask
    for v in range(order):
        if (mask >> v) & 1:
            observed |= nb[v]
    while True:
        previous = observed
        for v in range(order):
            if (observed >> v) & 1:
                white = nb[v] & ~observed
                if white and (white & (white - 1)) == 0:
                    observed |= white
        if previous == observed:
            return observed == (1 << order) - 1


def criterion(n, mask):
    low = mask & ((1 << n) - 1)
    high = mask >> n
    return (bool(low) and bool(high)) or (
        not high and low.bit_count() >= n - 2
    ) or (not low and high.bit_count() >= n - 2)


def polynomial_coefficients(n):
    """Compute from the closed enumerator without enumerating graph subsets."""
    ans = Counter()
    for i in range(1, n+1):
        for j in range(1, n+1):
            ans[i+j] += comb(n,i)*comb(n,j)
    for j in range(n-2,n+1):
        ans[j] += 2*comb(n,j)
    return ans


def component_sizes(n, admissible, k):
    N = 2*n
    remaining = {mask for mask in admissible if mask.bit_count() <= k}
    sizes = []
    while remaining:
        seed = remaining.pop()
        queue = [seed]
        count = 0
        while queue:
            mask = queue.pop()
            count += 1
            for j in range(N):
                other = mask ^ (1 << j)
                if other in remaining:
                    remaining.remove(other)
                    queue.append(other)
        sizes.append(count)
    return sorted(sizes)


def predicted_components(n,k):
    if n == 4:
        return 28 if k==2 else 1
    if k==2:
        return n*n
    if k==n-2:
        return 1+2*comb(n,2)
    return 1


def main():
    tested = 0
    found = 0
    min_found = 0
    component_checks = 0
    for n in range(4,9):
        P = {}
        for mask in range(1 << (2*n)):
            direct = power_dominates(n,mask)
            assert direct == criterion(n,mask), (n,mask)
            P[mask] = direct
            tested += 1
        accepted = {mask for mask,yes in P.items() if yes}
        found += len(accepted)
        counts = Counter(mask.bit_count() for mask in accepted)
        assert counts == polynomial_coefficients(n), (n,counts,polynomial_coefficients(n))
        minimum = {mask for mask in accepted if all(
            not P[mask^(1<<i)] for i in range(2*n) if (mask>>i)&1)}
        min_counts = Counter(mask.bit_count() for mask in minimum)
        expected_min = Counter({2:n*n})
        expected_min[n-2] += 2*comb(n,2)
        assert min_counts == expected_min, (n,min_counts,expected_min)
        min_found += len(minimum)
        for k in range(2,n+1):
            sizes = component_sizes(n,accepted,k)
            assert len(sizes) == predicted_components(n,k), (n,k,sizes)
            if n >= 5 and k==n-2:
                assert sizes.count(1) == 2*comb(n,2), (n,k,sizes)
                assert len(sizes)==1+2*comb(n,2)
            component_checks += 1
        print('CHECK n=%d powersets=%d PDS=%d minimal=%d TAR_tests=%d' %(
            n,1<<(2*n),len(accepted),len(minimum),n-1))
    print('VERIFY_OK orders=4..8 subsets=%d power_dominating=%d minimal=%d TAR_cases=%d exact_polynomials=PASS exact_components=PASS' % (
        tested,found,min_found,component_checks))


if __name__ == '__main__':
    main()
