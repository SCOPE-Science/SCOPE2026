#!/usr/bin/env python3
"""Finite checks for cyclic diagonal fixed sets of complete-graph Hom complexes.

Uses independent subset enumeration of invariant Hom cells and GF(2) homology
of the predicted fixed simplicial complexes. No external dependencies.
"""
from itertools import combinations
from math import prod

def integer_partitions(n, low=1):
    if n == 0:
        yield ()
    for x in range(low, n+1):
        for rem in integer_partitions(n-x, x):
            yield (x,)+rem

def cycle_permutation(lengths):
    pi = []
    cycles = []
    for L in lengths:
        start = len(pi)
        C = tuple(range(start, start+L))
        cycles.append(C)
        pi += [start+(j+1)%L for j in range(L)]
    return pi, cycles

def rotate_mask(mask, pi):
    out = 0
    for a,b in enumerate(pi):
        if mask & (1 << a): out |= 1 << b
    return out

def observed_supports(n,m,pi):
    """Source-0 supports of cells fixed setwise under (m-cycle,pi)."""
    out = set()
    for a in range(1,1<<n):
        x=a
        translated=[]
        for k in range(m):
            translated.append(x)
            x=rotate_mask(x,pi)
        if x != a: continue
        union=0
        for y in translated:
            if union & y:
                break
            union |= y
        else: out.add(a)
    return out

def expected_supports(m, cycles):
    choices=[]
    for cyc in cycles:
        if len(cyc)%m: continue
        opts=[]
        for r in range(m):
            opts.append(sum(1<<cyc[j] for j in range(r,len(cyc),m)))
        choices.append(opts)
    out={0}
    for opts in choices:
        out |= {x|v for x in tuple(out) for v in opts}
    return out-{0}, choices

def rank_mod2(columns):
    pivots={}
    for v in columns:
        while v:
            p=v.bit_length()-1
            if p in pivots: v ^= pivots[p]
            else:
                pivots[p]=v
                break
    return len(pivots)

def reduced_betti_join(m,q):
    if q==0: return {-1:1}
    verts=tuple(range(m*q))
    faces={-1:[()]}
    for s in range(1,q+1):
        faces[s-1]=[c for c in combinations(verts,s)
                     if len({v//m for v in c})==s]
    ranks={}
    for dim in range(q):
        rows={f:i for i,f in enumerate(faces[dim-1])}
        cols=[]
        for f in faces[dim]:
            vec=0
            for j in range(len(f)):
                vec ^= 1<<rows[f[:j]+f[j+1:]]
            cols.append(vec)
        ranks[dim]=rank_mod2(cols)
    return {dim: len(faces[dim])-ranks[dim]-ranks.get(dim+1,0)
            for dim in range(-1,q) if len(faces[dim])-ranks.get(dim,0)-ranks.get(dim+1,0)}

def test():
    checked=0; cells=0; nonempty=0; examples=[]
    for n in range(2,11):
        for part in integer_partitions(n):
            pi,cycles=cycle_permutation(part)
            for m in range(2,min(5,n)+1):
                obs=observed_supports(n,m,pi)
                exp,opts=expected_supports(m,cycles)
                assert obs==exp, ('cell discrepancy',m,n,part,sorted(obs^exp))
                q=len(opts)
                assert len(obs)==(m+1)**q-1
                cells+=len(obs)
                checked+=1
                nonempty+=bool(q)
                if q>=2 and len(examples)<20:
                    examples.append((m,n,part,q))
    for m in (2,3,4):
        for q in (1,2,3):
            betti=reduced_betti_join(m,q)
            assert betti=={q-1:(m-1)**q},(m,q,betti)
    assert reduced_betti_join(3,0)=={-1:1}
    # Explicit mixed-length examples test the divisibility filter.
    for m,part,q in ((3,(3,6,2),2),(4,(4,8,1),2),(3,(4,5),0),(2,(2,2,2),3)):
        pi,cycles=cycle_permutation(part)
        obs=observed_supports(sum(part),m,pi)
        expected,_=expected_supports(m,cycles)
        assert obs==expected
        assert len(obs)==(m+1)**q-1
    print('partitions_and_source_lengths_checked=',checked)
    print('observed_invariant_cells_checked=',cells)
    print('nonempty_fixed_cases=',nonempty)
    print('gf2_joins_checked=',9)
    print('sample_cases=',examples[:8])
    print('DIAGONAL_HOM_CYCLIC_FIXED_JOIN_CHECKS_PASS')
if __name__=='__main__': test()
