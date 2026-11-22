"""Independent exact-arithmetic check of mixed hard-core occupation cumulants.

Run with Python >=3.9: python verify_cumulants.py
No external packages are required. Finite tests supplement the analytic proof.
"""
from fractions import Fraction
from itertools import combinations
from math import factorial


def set_partitions(items):
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for p in set_partitions(rest):
        yield ((first,),) + p
        for j in range(len(p)):
            yield p[:j] + ((first,) + p[j],) + p[j + 1:]


def direct_cumulant(m, n, r, z):
    # All occupied sets are subsets entirely of one side; the empty set appears once.
    samples = [(0, Fraction(1))]
    for shore in (list(range(m)), list(range(m, m+n))):
        for k in range(1, len(shore)+1):
            for inds in combinations(shore, k):
                mask = sum(1 << j for j in inds)
                samples.append((mask, z**k))
    ztotal = sum(w for _, w in samples)
    ids = list(range(r)) + [m]
    cache = {}
    def moment(block):
        mask = sum(1 << ids[j] for j in block)
        if mask not in cache:
            cache[mask] = sum(w for occ, w in samples if occ & mask == mask)/ztotal
        return cache[mask]
    answer = Fraction(0)
    for part in set_partitions(tuple(range(r+1))):
        term = Fraction((-1)**(len(part)-1)*factorial(len(part)-1))
        for block in part:
            term *= moment(block)
        answer += term
    return answer


def stirling(r, k):
    row = [0] * (r+1)
    row[0] = 1
    for i in range(1, r+1):
        nxt = [0] * (r+1)
        for j in range(1, i+1):
            nxt[j] = row[j-1] + j*row[j]
        row = nxt
    return row[k]


def analytic_cumulant(m, n, r, z):
    x = 1+z
    Z = x**m + x**n - 1
    a, b, p = x**m/Z, x**n/Z, z/x
    return b*p**(r+1)*sum((-a)**k * factorial(k)*stirling(r,k) for k in range(1,r+1))


def main():
    checked = 0
    for m in range(2,7):
        for n in range(1,8):
            for r in range(2,min(m,5)+1):
                for z in (Fraction(1,5), Fraction(2,3), Fraction(1), Fraction(3)):
                    lhs = direct_cumulant(m,n,r,z)
                    rhs = analytic_cumulant(m,n,r,z)
                    assert lhs == rhs, (m,n,r,z,lhs,rhs)
                    checked += 1
    print('MIXED_CUMULANTS_EXACT:', checked)
    # Independent irrational-root sign tests for K_{3,2} at rational fugacities.
    m,n,r = 3,2,3
    signs = []
    for z in (Fraction(1,10),Fraction(1),Fraction(4)):
        v = direct_cumulant(m,n,r,z)
        signs.append(1 if v>0 else -1 if v<0 else 0)
    assert signs == [-1,1,-1], signs
    print('K_3_2_REENTRANT_SIGNS:', signs)

if __name__=='__main__': main()
