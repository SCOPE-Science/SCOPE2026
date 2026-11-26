#!/usr/bin/env python3
"""Finite independent tests for the length-two free-semigroup morphism formulas."""
from itertools import product, combinations, permutations
from math import factorial

def all_masks(n):
    for m in range(1<<n): yield set(i for i in range(n) if (m>>i)&1)

def rpres(W,n):
    # Direct examination of all potential factor bases for the words of length <= 2.
    # Letter members of W must themselves be in any basis.
    W=set(W)
    for A in all_masks(n):
        if any(len(w)==1 and w[0] not in A for w in W):continue
        need={w for w in W if len(w)==2 and not(w[0] in A and w[1] in A)}
        if len(A)+len(need)<n: return False
    return True

def eligible_graph(W,n):
    if len(set(W))!=n:return False
    for A in all_masks(n):
        if sum(u in A and v in A for (u,v) in W)>len(A):return False
    return True

def proposed_irreducible(W,n):
    if not eligible_graph(W,n):return False
    return all(sum(u in A and v in A for u,v in W)<len(A)
               for A in all_masks(n) if 0<len(A)<n)

def all_reducible(n):
    """Enumerate complete finite factor pairs once; keep length-two outputs."""
    words=[(i,) for i in range(n)]+list(product(range(n),repeat=2))
    perms=set(permutations([(i,) for i in range(n)]))
    red=set()
    for left in product(words,repeat=n):
        if left in perms:continue
        # Only right-generator words giving an output of exact length two.
        right_options=[(i,) for i in range(n) if len(left[i])==2]
        right_options += [(i,j) for i in range(n) for j in range(n)
                          if len(left[i])==1 and len(left[j])==1]
        for right in product(right_options,repeat=n):
            if right in perms:continue
            result=tuple(tuple(y for t in w for y in left[t]) for w in right)
            red.add(result)
    return red

def verify_small():
    for n in (2,3):
        edges=list(product(range(n), repeat=2)); rp=0; irr=0
        reducible=all_reducible(n)
        for W in product(edges,repeat=n):
            pr=rpres(W,n)
            gr=eligible_graph(W,n)
            assert pr==gr,(n,W,'rpres')
            if not pr:continue
            rp+=1
            pred=proposed_irreducible(W,n)
            genuine=(W not in reducible)
            assert pred==genuine,(n,W,'irreducibility')
            irr+=pred
        expected=(2 if n==2 else 2**(n-1)*factorial(n)*factorial(n-1))
        assert irr==expected
        print('independent factor check:',n,'rank_preserving',rp,'irreducible',irr)

def verify_graph_larger():
    for n in (4,5):
        edges=list(product(range(n),repeat=2))
        rp=0;irr=0
        for W in combinations(edges,n):
            if not eligible_graph(W,n):continue
            rp+=1
            if proposed_irreducible(W,n):irr+=1
        expect=2**(n-1)*factorial(n-1)
        assert irr==expect,(n,irr,expect)
        print('all distinct edge sets:',n,'pseudoforests',rp,'single spanning cycles',irr)
if __name__=='__main__':
    verify_small();verify_graph_larger();print('VERIFY_OK')

def connected_edge_sets(k):
    """Independent combinatorial enumeration by cycle length and rooted forests."""
    from math import comb
    total=0
    for ell in range(1,k+1):
        core=1 if ell<=2 else 2**(ell-1)*factorial(ell-1)
        rooted=1 if ell==k else ell*k**(k-ell-1)
        total += comb(k,ell)*core*rooted*2**(k-ell)
    return total

def forest_counts(N=12):
    from math import comb
    p=[1]
    for n in range(1,N+1):
        p.append(sum(comb(n-1,k-1)*connected_edge_sets(k)*p[n-k]
                     for k in range(1,n+1)))
    assert p[2:9]==[6,72,1274,29610,850692,29086624,1153013052], p[2:9]
    for n in (2,3,4,5):
        b=2 if n==2 else 2**(n-1)*factorial(n)*factorial(n-1)
        a=factorial(n)*p[n]
        assert a>b>0
    print('unicyclic-forest recurrence:',p[2:9])

if __name__=='__main__':
    forest_counts()
