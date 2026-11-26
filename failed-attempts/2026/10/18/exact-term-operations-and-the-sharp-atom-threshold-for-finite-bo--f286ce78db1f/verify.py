#!/usr/bin/env python3
"""Finite checks for endpoint-test Boolean algebras and their term-function spectra."""
from itertools import combinations, product
from math import comb


def count_formula(k,m):
    n=1 << m
    exponent=sum(r*comb(n,r) for r in range(1,min(n,k)+1))
    return exponent,1 << exponent


def closure_dimension(k,m):
    """Independently find the Boolean algebra of term tables by iterative refinement.

    Coordinates (support, atom-type) represent atomic observations of an
    m-ary operation. This check uses the actual endpoint-test operation.
    """
    types=tuple(range(1 << m))
    pats=[frozenset(p) for r in range(1,min(k,len(types))+1)
          for p in combinations(types,r)]
    coords=[(p,t) for p in pats for t in sorted(p)]
    full=(1 << len(coords))-1
    generators=[]
    for i in range(m):
        generators.append(sum((1 << j) for j, (_,t) in enumerate(coords) if t & (1 << i)))
    groups={p:[j for j,(q,_) in enumerate(coords) if q==p] for p in pats}

    def circ(mask):
        ans=0
        for indices in groups.values():
            vals=[(mask >> j)&1 for j in indices]
            if all(v==0 for v in vals) or all(v==1 for v in vals):
                ans|=sum(1 << j for j in indices)
        return ans

    def atoms(gs):
        partition={}
        for j in range(len(coords)):
            key=tuple((g >> j)&1 for g in gs)
            partition.setdefault(key,0)
            partition[key] |= (1 << j)
        return list(partition.values())

    rounds=[]
    for it in range(12):
        parts=atoms(generators)
        rounds.append(len(parts))
        # All Boolean terms in the current generators are unions of partition blocks.
        new=[]
        for flags in range(1<<len(parts)):
            x=0
            for j,atom in enumerate(parts):
                if flags&(1 << j):
                    x|=atom
            y=circ(x)
            if any(y&block not in (0,block) for block in parts):
                new.append(y)
        if not new:
            return len(coords),len(parts),rounds
        generators.extend(set(new))
    raise AssertionError('refinement failed to stabilize')


def unary_direct(k):
    """Directly close unary operations of a k-atom power-set algebra."""
    carrier=list(range(1<<k))
    top=(1<<k)-1
    circ=lambda v:top if v in (0,top) else 0
    neg=lambda v:v^top
    ops={tuple(carrier)}
    changed=True
    while changed:
        prev=len(ops)
        snapshot=list(ops)
        for a in snapshot:
            ops.add(tuple(neg(v) for v in a))
            ops.add(tuple(circ(v) for v in a))
        snapshot=list(ops)
        for a in snapshot:
            for b in snapshot:
                ops.add(tuple(x&y for x,y in zip(a,b)))
                ops.add(tuple(x|y for x,y in zip(a,b)))
        changed=(len(ops)!=prev)
    return len(ops)


def main():
    for k,m in [(1,1),(1,2),(2,1),(2,2),(3,1)]:
        coordinates,dim,rounds=closure_dimension(k,m)
        exp,_=count_formula(k,m)
        assert dim==coordinates==exp,(k,m,coordinates,dim,exp)
        print('REFINEMENT',k,m,'dimension',dim,'rounds',rounds)
    for k in [1,2,3]:
        found=unary_direct(k)
        exp,_=count_formula(k,1)
        assert found==(1<<exp),(k,found,1<<exp)
        print('DIRECT_UNARY',k,found)
    assert count_formula(2,2)==(16,65536)
    assert count_formula(3,2)[0]==28
    assert count_formula(4,2)[0]==32
    print('ENDPOINT_TEST_TERM_CLONE_VERIFY_OK')
if __name__=='__main__':main()
