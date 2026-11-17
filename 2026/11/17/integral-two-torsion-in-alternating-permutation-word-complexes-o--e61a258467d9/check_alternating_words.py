#!/usr/bin/env python3
"""Exact standard-library integer-chain checks for alternating permutation complexes.

A word is an ordered tuple of distinct letters. The even permutations are top
cells, and every nonempty subsequence of one is a cell. The signed boundary
of a word deletes its i-th letter with coefficient (-1)**i.

Unit-pivot row/column elimination uses unimodular integer operations; when
no unit remains, the residual entries are divided by two only after their
divisibility is checked. Subsequent unit elimination proves the invariant
factors of the original matrix are 1 and 2, with stated multiplicities.
"""
from itertools import permutations, combinations

def even(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p))) % 2 == 0

def cells(n):
    tops = [p for p in permutations(range(n)) if even(p)]
    levels = {k: sorted({u for p in tops for u in combinations(p, k)}) for k in range(1, n+1)}
    assert levels[n] == tops
    return levels

def boundary(levels, k):
    """Return matrix for C_{k-1} -> C_{k-2}, where k is word length."""
    col = levels[k]
    row = levels[k-1]
    lookup = {w: i for i, w in enumerate(row)}
    m = [[0]*len(col) for _ in row]
    for j, w in enumerate(col):
        for h in range(k):
            m[lookup[w[:h]+w[h+1:]]][j] += (-1)**h
    return m

def verify_chain(left, right):
    """Verify product of consecutive boundary matrices is zero exactly."""
    # left: a x b, right: b x c
    assert len(left[0]) == len(right)
    for j in range(len(right[0])):
        out = [0]*len(left)
        for i, row in enumerate(right):
            v = row[j]
            if v:
                for a, ll in enumerate(left):
                    out[a] += ll[i]*v
        assert not any(out)

def rank_mod(matrix, p):
    a = [[x%p for x in row] for row in matrix]
    if not a: return 0
    rows,cols = len(a),len(a[0]); rank=0
    for j in range(cols):
        pivot = next((i for i in range(rank,rows) if a[i][j]),None)
        if pivot is None: continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][j],-1,p)
        for h in range(j,cols): a[rank][h]=(a[rank][h]*inv)%p
        for i in range(rank+1,rows):
            factor=a[i][j]
            if factor:
                for h in range(j,cols):a[i][h]=(a[i][h]-factor*a[rank][h])%p
        rank+=1
        if rank==rows: break
    return rank

def unit_pivot_block(a,start):
    """Apply only integer unimodular row/column operations on trailing block."""
    rows,cols = len(a),len(a[0])
    end = start
    for k in range(start,cols):
        loc = next(((i,j) for i in range(k,rows) for j in range(k,cols)
                    if abs(a[i][j]) == 1),None)
        if loc is None:break
        i,j = loc
        a[i],a[k] = a[k],a[i]
        for row in a: row[j],row[k] = row[k],row[j]
        unit=a[k][k]
        assert abs(unit)==1
        for h in range(k+1,rows):
            factor=a[h][k]//unit
            if factor:
                for l in range(k,cols):a[h][l]-=factor*a[k][l]
        end=k+1
    return end

def elementary_divisors_top(m):
    a=[row[:] for row in m]
    rows,cols=len(a),len(a[0]); first=unit_pivot_block(a,0)
    residual=[a[i][j] for i in range(first,rows) for j in range(first,cols)]
    assert all(v%2==0 for v in residual), 'residual has an odd nonunit'
    for i in range(first,rows):
        for j in range(first,cols):a[i][j]//=2
    last=unit_pivot_block(a,first)
    assert last==cols, 'divided residual lacks full unit rank'
    assert all(a[i][j]==0 for i in range(last,rows) for j in range(last,cols))
    return first,last-first

def main():
    expected={
      3: {'counts':[3,6,3], 'ranks':[2,3], 'invariants':(3,0),'free':1,'torsion':0},
      4: {'counts':[4,12,24,12], 'ranks':[3,9,12], 'invariants':(11,1),'free':3,'torsion':1},
      5: {'counts':[5,20,60,120,60], 'ranks':[4,16,44,60], 'invariants':(56,4),'free':16,'torsion':4},
    }
    for n,e in expected.items():
        levels=cells(n)
        counts=[len(levels[k]) for k in range(1,n+1)]
        assert counts == e['counts'],(n,counts)
        boundaries={k:boundary(levels,k) for k in range(2,n+1)}
        for k in range(3,n+1):verify_chain(boundaries[k-1],boundaries[k])
        ranks=[rank_mod(boundaries[k],101) for k in range(2,n+1)]
        assert ranks==e['ranks'],(n,ranks)
        # Independently check prime-field ranks and the universal coefficient jump.
        top=boundaries[n]
        profile=elementary_divisors_top(top)
        assert profile==e['invariants'],(n,profile)
        assert rank_mod(top,2)==profile[0]
        assert rank_mod(top,3)==sum(profile)
        assert rank_mod(top,101)==sum(profile)
        for k in range(2,n):
            assert rank_mod(boundaries[k],2)==ranks[k-2]
            assert rank_mod(boundaries[k],3)==ranks[k-2]
        free=counts[-2]-ranks[-1]-(ranks[-2] if len(ranks)>1 else 1)
        assert free==e['free'],(n,free)
        assert profile[1]==e['torsion']
        print(f'n={n} counts={counts} ranks={ranks} top_Smith_1={profile[0]} top_Smith_2={profile[1]} H_{n-2}=Z^{free}+(Z/2)^{profile[1]} PASS')
    print('ALTERNATING_PERMUTATION_INTEGRAL_HOMOLOGY_PASS')
if __name__ == '__main__':main()
