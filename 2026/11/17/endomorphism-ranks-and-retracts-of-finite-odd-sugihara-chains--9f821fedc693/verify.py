#!/usr/bin/env python3
from itertools import product, combinations
from math import comb
from collections import Counter

checks = 0

def ok(cond, msg='assertion failed'):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def elems(m):
    return list(range(-m, m+1))

def neg(a):
    return -a

def meet(a,b):
    return min(a,b)

def join(a,b):
    return max(a,b)

def mul(a,b):
    aa, bb = abs(a), abs(b)
    if bb < aa:
        return a
    if aa < bb:
        return b
    return min(a,b)

def imp(a,b):
    if a <= b:
        return max(-a,b)
    return min(-a,b)

def preserves(m,n,h):
    # h is dict source index -> target index
    if h[0] != 0:
        return False
    for a in elems(m):
        if h[neg(a)] != neg(h[a]):
            return False
    for a in elems(m):
        for b in elems(m):
            if h[meet(a,b)] != meet(h[a],h[b]): return False
            if h[join(a,b)] != join(h[a],h[b]): return False
            if h[mul(a,b)] != mul(h[a],h[b]): return False
            if h[imp(a,b)] != imp(h[a],h[b]): return False
    return True

def characterized_maps(m,n):
    # choose r target positive levels, collapse an initial block of positives to 0
    out=[]
    for r in range(0,min(m,n)+1):
        for A in combinations(range(1,n+1),r):
            c=[0]*(m-r)+list(A)
            h={0:0}
            for i,v in enumerate(c,1):
                h[i]=v
                h[-i]=-v
            out.append(h)
    return out

def key(m,h):
    return tuple(h[i] for i in elems(m))

def rank(h):
    return len(set(h.values()))

def compose(m,f,g):
    # g o f, both selfmaps of S_{2m+1}
    return {i:g[f[i]] for i in elems(m)}

# Full exhaustive check among every involution-preserving, identity-preserving set map.
# A map is determined by arbitrary images of positive levels; negatives follow by involution.
exhaustive_candidates=0
exhaustive_homs=0
for m in range(1,5):
    for n in range(1,5):
        actual=[]
        for vals in product(range(-n,n+1), repeat=m):
            exhaustive_candidates += 1
            h={0:0}
            for i,v in enumerate(vals,1):
                h[i]=v
                h[-i]=-v
            if preserves(m,n,h):
                actual.append(h)
        predicted=characterized_maps(m,n)
        A={key(m,h) for h in actual}
        P={key(m,h) for h in predicted}
        ok(A==P, f'classification mismatch m={m}, n={n}')
        expected=sum(comb(n,r) for r in range(0,min(m,n)+1))
        ok(len(A)==expected, f'hom count mismatch m={m}, n={n}')
        actual_ranks=Counter(rank(h) for h in actual)
        predicted_ranks=Counter({2*r+1:comb(n,r) for r in range(0,min(m,n)+1)})
        ok(actual_ranks==predicted_ranks, f'rank profile mismatch m={m}, n={n}')
        exhaustive_homs += len(A)

# Constructed-map operation-by-operation checks and formulas farther out.
constructed=0
for m in range(1,9):
    for n in range(1,9):
        hs=characterized_maps(m,n)
        expected=sum(comb(n,r) for r in range(0,min(m,n)+1))
        ok(len(hs)==expected)
        for h in hs:
            constructed += 1
            ok(preserves(m,n,h), f'constructed map fails m={m}, n={n}')
        # injective and surjective exact counts
        inj=sum(1 for h in hs if len(set(h.values()))==2*m+1)
        sur=sum(1 for h in hs if set(h.values())==set(elems(n)))
        ok(inj==(comb(n,m) if m<=n else 0), f'injective count m={m}, n={n}')
        ok(sur==(1 if m>=n else 0), f'surjective count m={m}, n={n}')

# Endomorphism rank polynomial, idempotents, subalgebra images, and retracts.
for m in range(1,13):
    hs=characterized_maps(m,m)
    ok(len(hs)==2**m, f'end count m={m}')
    ranks=Counter(rank(h) for h in hs)
    ok(ranks==Counter({2*r+1:comb(m,r) for r in range(m+1)}), f'end rank m={m}')
    idems=[]
    images=set()
    for h in hs:
        images.add(tuple(sorted(set(h.values()))))
        hh=compose(m,h,h)
        if key(m,hh)==key(m,h):
            idems.append(h)
    ok(len(images)==2**m, f'image count m={m}')
    ok(len(idems)==m+1, f'idempotent count m={m}')
    idem_ranks=sorted(rank(h) for h in idems)
    ok(idem_ranks==list(range(1,2*m+2,2)), f'idempotent ranks m={m}')
    # Idempotent images are exactly the outer symmetric subchains.
    expected_images=[]
    for r in range(m+1):
        S={0}
        for j in range(m-r+1,m+1):
            S.update({-j,j})
        expected_images.append(tuple(sorted(S)))
    got=sorted(tuple(sorted(set(h.values()))) for h in idems)
    ok(sorted(expected_images)==got, f'retract images m={m}')

print('VERIFY_OK', checks, 'exact assertions;',
      exhaustive_candidates, 'involution-preserving candidate maps exhaustively tested;',
      exhaustive_homs, 'actual homomorphisms through m,n<=4;',
      constructed, 'classified homomorphisms operation-checked through m,n<=8')
