#!/usr/bin/env python3
"""Independent small-model and all-depth checks for one-letter modal agendas on rings.
Run with: python3 verify.py
"""
from itertools import combinations


def closed_walk_masks(n):
    # Direct graph adjacency propagation, not the closed-form arithmetic progression.
    mask = 1
    out = []
    for _ in range(n - 1):
        mask = sum(1 << j for j in range(n) if
                   any((mask >> z) & 1 for z in ((j-1) % n, (j+1) % n)))
        out.append(mask)
    return out


def predicted(n):
    ans = set()
    if n % 2 == 0:
        return ans
    r = (n - 1) // 2
    for a in range(1, r):
        e = 2 * a
        for b in range(r):
            o = 2 * b + 1
            if a + b < r - 1:
                continue
            for k in range(1, n):
                if (k % 2 == 0 and k > e) or (k % 2 == 1 and k > o):
                    ans.add((min(e, o), max(e, o), k))
    return ans


def coverage_triplets(n):
    masks = closed_walk_masks(n)
    ans = set()
    for i, j in combinations(range(1,n), 2):
        a, b = masks[i-1], masks[j-1]
        for k in range(1,n):
            target = masks[k-1]
            if target & ~(a|b) == 0 and target & ~a != 0 and target & ~b != 0:
                ans.add((i,j,k))
    return ans


def valuation_triplets(n):
    # Independently check actual Kripke semantics over all 2^n valuations.
    # Every signed formula is represented by the set of valuations satisfying it.
    masks = closed_walk_masks(n)
    all_val = (1 << (1 << n)) - 1
    pos = [0] * (n-1)
    for v in range(1 << n):
        bit = 1 << v
        for j, requirement in enumerate(masks):
            if (v & requirement) == requirement:
                pos[j] |= bit
    neg = [all_val ^ s for s in pos]
    out = set()
    for i,j in combinations(range(1,n), 2):
        for k in range(1,n):
            first, second, third = pos[i-1], pos[j-1], neg[k-1]
            if not (first & second & third) and (first & second) and (first & third) and (second & third):
                out.add((i,j,k))
    # Any minimal triple with another sign configuration would invalidate the claim.
    literals = [(sign, k, pos[k-1] if sign else neg[k-1])
                for k in range(1,n) for sign in (False, True)]
    for a,b,c in combinations(literals, 3):
        va,vb,vc = a[2], b[2], c[2]
        if not (va & vb & vc) and (va & vb) and (va & vc) and (vb & vc):
            signature = (a[0],b[0],c[0])
            assert signature.count(True) == 2 and signature.count(False) == 1, (n,a,b,c)
            pp = sorted([x[1] for x in (a,b,c) if x[0]])
            nn = [x[1] for x in (a,b,c) if not x[0]][0]
            assert (pp[0],pp[1],nn) in out
    return out


def main():
    direct = 0
    semantic = 0
    for n in range(3,62):
        want = predicted(n)
        observed = coverage_triplets(n)
        assert observed == want, ('walk-support mismatch',n,observed ^ want)
        if n % 2:
            r = (n-1)//2
            expected_count = r*(r-1)*(2*r+5)//6
            assert len(want) == expected_count, ('count',n)
            if r >= 2:
                assert min(max(*trip) for trip in want) == r+1, ('depth',n)
        else:
            assert not want, ('even cycle',n)
        direct += 1
        if n <= 15:
            brute = valuation_triplets(n)
            assert brute == want, ('semantic mismatch',n,brute ^ want)
            semantic += 1
    print(f'VERIFY_OK walk_orders={direct} exhaustive_valuations_orders={semantic}')

if __name__=='__main__':
    main()
