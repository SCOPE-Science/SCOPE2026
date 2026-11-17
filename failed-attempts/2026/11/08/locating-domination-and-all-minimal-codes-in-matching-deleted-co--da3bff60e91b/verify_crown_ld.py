"""Exhaustive finite checks for locating-dominating sets of K_(n,n) minus a matching.

Standard-library-only usage: python3 verify_crown_ld.py
The theorem for all n is proved separately; this script checks finite orders.
"""
from collections import Counter
from math import comb


def predicted_all(n):
    p = Counter()
    for j in range(n + 1):
        p[n + j] += comb(n, j) * 2 ** (n - j)
    for j in range(n):
        p[n - 1 + j] += n * comb(n - 1, j) * 2 ** (n - 1 - j)
    p[n - 1] -= 2 * n * n
    p[n] -= 2 * n
    return {j: a for j, a in p.items() if a}


def predicted_minimal(n):
    if n == 4:
        return {4: 56}
    return {n-1: n * (2 ** (n - 1) - 2 * n), n: 2 + 2*n*(n-1)}


def theoretical_criterion(n, mask):
    base = (1 << n) - 1
    ia = mask & base
    jb = (mask >> n) & base
    a = ia.bit_count()
    b = jb.bit_count()
    if a >= 2 and b >= 2:
        return (ia | jb).bit_count() >= n - 1
    if b == 0:
        return a == n
    if a == 0:
        return b == n
    if b == 1:
        return a >= n - 1 and bool(jb & ia)
    if a == 1:
        return b >= n - 1 and bool(ia & jb)
    return False


def theoretical_minimal(n, mask):
    base = (1 << n) - 1
    ia = mask & base
    jb = (mask >> n) & base
    a, b = ia.bit_count(), jb.bit_count()
    if (a == n and b == 0) or (a == 0 and b == n):
        return True
    if a == n-1 and b == 1 and (ia & jb):
        return True
    if b == n-1 and a == 1 and (ia & jb):
        return True
    if n == 4:
        return a == 2 and b == 2 and (ia | jb).bit_count() >= 3
    return a >= 2 and b >= 2 and not (ia & jb) and (ia | jb).bit_count() == n-1


def brute(n):
    full = (1 << (2*n)) - 1
    neighbors = [0] * (2*n)
    for i in range(n):
        for j in range(n):
            if i != j:
                neighbors[i] |= 1 << (n+j)
                neighbors[n+j] |= 1 << i
    accepted = bytearray(full + 1)
    all_counts = Counter()
    for mask in range(full + 1):
        missing = full ^ mask
        signatures = set()
        valid = True
        while missing:
            bit = missing & -missing
            missing ^= bit
            v = bit.bit_length() - 1
            sig = neighbors[v] & mask
            if not sig or sig in signatures:
                valid = False
                break
            signatures.add(sig)
        assert valid == theoretical_criterion(n, mask), (n, mask, 'characterization')
        if valid:
            accepted[mask] = 1
            all_counts[mask.bit_count()] += 1
    min_counts = Counter()
    for mask in range(full + 1):
        if not accepted[mask]:
            continue
        selected = mask
        is_min = True
        while selected:
            bit = selected & -selected
            selected ^= bit
            if accepted[mask ^ bit]:
                is_min = False
                break
        assert is_min == theoretical_minimal(n,mask), (n,mask,'minimal characterization')
        if is_min:
            min_counts[mask.bit_count()] += 1
    assert dict(all_counts) == predicted_all(n), (n,all_counts,predicted_all(n))
    assert dict(min_counts) == predicted_minimal(n), (n,min_counts,predicted_minimal(n))
    return (full+1, sum(all_counts.values()), sum(min_counts.values()))


if __name__ == '__main__':
    total = [0, 0, 0]
    for order in range(4,10):
        stats = brute(order)
        total = [a+b for a,b in zip(total, stats)]
        print(f'n={order}: candidate_subsets={stats[0]}, locating_dominating={stats[1]}, inclusion_minimal={stats[2]}')
    print('VERIFY_OK orders=4..9 subsets=%d LD_sets=%d minimal=%d characterization=PASS minimal_families=PASS both_polynomials=PASS' % tuple(total))
