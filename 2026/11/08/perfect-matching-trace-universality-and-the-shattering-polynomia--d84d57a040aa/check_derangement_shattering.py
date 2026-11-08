#!/usr/bin/env python3
"""Independent finite tests for derangement-graph VC traces and rook formulas.
Uses direct permutation enumeration, not the one-factorization proof.
Run: python3 check_derangement_shattering.py
"""
import itertools
import math
import random


def rook_formula(n, k):
    return sum((-1)**j * math.comb(n,j) * math.comb(n-j,k-j)**2 * math.factorial(k-j)
               for j in range(k+1))


def rook_dynamic(n):
    # Independent direct dynamic program: one row at a time, skip or place a rook.
    states = {0: 1}
    for i in range(n):
        nxt = {}
        for mask,cnt in states.items():
            nxt[mask] = nxt.get(mask,0)+cnt
            for j in range(n):
                if i != j and not(mask >> j & 1):
                    mm = mask | (1<<j)
                    nxt[mm] = nxt.get(mm,0)+cnt
        states=nxt
    ans=[0]*(n+1)
    for mask, count in states.items():
        ans[mask.bit_count()] += count
    return ans


def derangement_masks(n, edge_index):
    masks=[]
    for p in itertools.permutations(range(n)):
        if any(i==p[i] for i in range(n)):
            continue
        mask=0
        for i in range(n):
            mask |= 1<<edge_index[(i,p[i])]
        masks.append(mask)
    return masks


def is_matching(indices, edges):
    return len({edges[i][0] for i in indices})==len(indices) and len({edges[i][1] for i in indices})==len(indices)


def test_support(n, indices, edges, permutations):
    S=sum(1<<i for i in indices)
    traces={S & p for p in permutations}
    shattered=len(traces)==(1<<len(indices))
    assert shattered == (len(indices)<=n-2 and is_matching(indices,edges)), (n,indices,shattered)
    if len(indices)<=n-2:
        allowed={sum(1<<i for i in T) for k in range(len(indices)+1)
                 for T in itertools.combinations(indices,k) if is_matching(T,edges)}
        assert traces==allowed, (n,indices,'local trace universality')
    return shattered


def main():
    tested=0
    for n in range(2,10):
        via_dp=rook_dynamic(n)
        via_ie=[rook_formula(n,k) for k in range(n+1)]
        assert via_dp==via_ie,(n,via_dp,via_ie)
        if n>6:
            continue
        edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
        edge_index={e:i for i,e in enumerate(edges)}
        permutations=derangement_masks(n,edge_index)
        actual=[0]*(n+1)
        max_all= n if n<=5 else 5
        for k in range(max_all+1):
            for ids in itertools.combinations(range(len(edges)),k):
                actual[k] += test_support(n,ids,edges,permutations)
                tested += 1
        assert actual[:min(n-2,max_all)+1]==via_ie[:min(n-2,max_all)+1], (n,actual,via_ie)
        assert all(actual[k]==0 for k in range(n-1,max_all+1)), (n,actual)
        print('n=%d derangements=%d counts=%s supports=%d' %
              (n,len(permutations),actual,sum(math.comb(len(edges),k) for k in range(max_all+1))))
    rng=random.Random(20261102)
    for n in (6,7,8):
        edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
        edge_index={e:i for i,e in enumerate(edges)}
        permutations=derangement_masks(n,edge_index)
        for k in range(1,n+1):
            for _ in range(40 if n<8 else 20):
                ids=tuple(sorted(rng.sample(range(len(edges)),k)))
                test_support(n,ids,edges,permutations)
                tested+=1
    print('ALL_DERANGEMENT_SHATTERING_CHECKS_PASS',tested,'support_tests',
          '9_rook_polynomials','exhaustive_n_le_5_and_n6_le_5','sampled_n6_to_n8')

if __name__=='__main__':
    main()
