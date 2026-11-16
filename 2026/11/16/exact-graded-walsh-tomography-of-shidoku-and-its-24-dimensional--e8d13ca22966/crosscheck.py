#!/usr/bin/env python3
"""Independent Shidoku enumeration and binary-monomial rank check.

Uses 12 normalized grids and all 24 symbol relabelings, rather than filtering
all ordered row-permutation quadruples. Computes incidence ranks via bitsets.
"""
from itertools import permutations,combinations
from collections import Counter

def normalized_grids():
    first=(0,1,2,3)
    ps=list(permutations(range(4)))
    out=[]
    for second in ps:
        if set(second[:2]) & {0,1} or set(second[2:]) & {2,3}:continue
        for third in ps:
            if any(third[c] in {first[c],second[c]} for c in range(4)):continue
            for fourth in ps:
                if any(fourth[c] in {first[c],second[c],third[c]} for c in range(4)):
                    continue
                if set(third[:2]) & set(fourth[:2]):continue
                if set(third[2:]) & set(fourth[2:]):continue
                out.append(first+second+third+fourth)
    return out

def main():
    norm=normalized_grids()
    assert len(norm)==12
    boards=sorted({tuple(perm[x] for x in g)
                 for perm in permutations(range(4)) for g in norm})
    assert len(boards)==288
    colbits=[]
    bases=[]
    for d in range(5):
        for sub in combinations(range(64),d):
            bits=0
            for i,g in enumerate(boards):
                if all(g[j//4]==j%4 for j in sub):bits|=1<<i
            while bits:
                h=bits.bit_length()-1
                if h not in colbits:
                    colbits.append(h);bases.append(bits);break
                bits ^= bases[colbits.index(h)]
            if len(bases)==288:break
        print('degree',d,'binary incidence rank',len(bases))
        assert len(bases)==(1,25,150,264,288)[d]
    clues=Counter()
    for g in boards:
        for sub in combinations(range(16),4):
            clues[tuple(4*j+g[j] for j in sub)]+=1
    assert sum(v==1 for v in clues.values())==25728
    assert all(any(clues[tuple(4*j+g[j] for j in sub)]==1
                   for sub in combinations(range(16),4)) for g in boards)
    print('PASS: independent enumeration and four-clue witnesses')
if __name__=='__main__':main()
