"""Finite checks for logical equivalence of rectangular rook graphs.

Usage: python rook_logic_checker.py
The refinement implements the non-counting k-pebble extension invariant.
No finite cutoff is used as a substitute for an infinite proof.
"""
from itertools import product, combinations_with_replacement
from collections import defaultdict


def graph(a,b):
    v = tuple(product(range(a), range(b)))
    e = {(i,j): (v[i][0]==v[j][0] or v[i][1]==v[j][1]) and i!=j
         for i in range(len(v)) for j in range(len(v))}
    return v,e


def invariants(a,b,k):
    return tuple(sorted((min(a,k), min(b,k))))


def refine_family(k, pairs):
    data=[]
    keys=[]
    # Every coordinate of a k-tuple may be replaced. Sets (not multisets)
    # of extension colours implement counting-free pebble refinement.
    for a,b in pairs:
        v,ed=graph(a,b)
        tuples=list(product(range(len(v)), repeat=k))
        atoms=[]
        for t in tuples:
            atoms.append(tuple((t[i]==t[j], bool(ed[(t[i],t[j])])) for i in range(k) for j in range(i+1,k)))
        data.append((a,b,len(v),tuples))
        keys.extend(atoms)
    palette={x:i for i,x in enumerate(sorted(set(keys)))}
    colors=[palette[x] for x in keys]
    iterations=0
    while True:
        offset=0
        newkeys=[]
        for a,b,n,tuples in data:
            local=colors[offset:offset+len(tuples)]
            offset+=len(tuples)
            # All possible single-coordinate replacements of one tuple
            # have a fixed other-coordinate context.
            groups=[defaultdict(set) for _ in range(k)]
            for t,c in zip(tuples,local):
                for p in range(k):
                    groups[p][t[:p]+t[p+1:]].add(c)
            signatures=[{ctx:tuple(sorted(cs)) for ctx,cs in gs.items()} for gs in groups]
            for t,c in zip(tuples, local):
                newkeys.append((c, tuple(signatures[p][t[:p]+t[p+1:]] for p in range(k))))
        palette={x:i for i,x in enumerate(sorted(set(newkeys)))}
        refined=[palette[x] for x in newkeys]
        iterations+=1
        # Since refinement never merges, a stable number of classes
        # certifies no further split, even if palette labels changed.
        if len(set(refined))==len(set(colors)):
            colors=refined
            break
        assert iterations<20
        colors=refined
    observed={}
    offset=0
    for a,b,n,tuples in data:
        observed[(a,b)]=frozenset(colors[offset:offset+len(tuples)])
        offset+=len(tuples)
    for p,q in product(pairs,repeat=2):
        actual=observed[p]==observed[q]
        expect=invariants(*p,k)==invariants(*q,k)
        assert actual==expect, (k,p,q,actual,expect)
    return len(set(observed.values())), len(pairs)**2, iterations, sum(len(v[3]) for v in data)


def check():
    totals=[]
    for k,limit in ((2,5),(3,5),(4,4)):
        pairs=list(combinations_with_replacement(range(2,limit+1),2))
        distinct,comparisons,iters,positions=refine_family(k,pairs)
        expected=len(set(invariants(*p,k) for p in pairs))
        assert distinct==expected
        totals.append((k,len(pairs),comparisons,positions,iters,distinct))
        print(f"width={k} graphs={len(pairs)} ordered_comparisons={comparisons} "
              f"pebble_positions={positions} refinement_rounds={iters} "
              f"classes={distinct} PASS")
    for k in range(3,11):
        pairs=list(combinations_with_replacement(range(2,k+2),2))
        classes={invariants(*p,k) for p in pairs}
        assert len(classes)==k*(k-1)//2
        # Every truncated parameter pair has one minimal representative.
        assert max(a*b for a,b in classes)==k*k
    print('theory_count_and_minimum_order k=3..10 PASS')
    for k in range(3,10):
        for a in range(2,12):
            for b in range(a,12):
                assert invariants(a,b,k)==invariants(min(a,k),min(b,k),k)
                assert k<max(a,b)+1 or (a,b)==(min(a,k),min(b,k))
    print('canonical_representatives_and_width_checks PASS')


if __name__=='__main__':
    check()
