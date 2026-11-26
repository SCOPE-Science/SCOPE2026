#!/usr/bin/env python3
"""Finite diagnostics for a chain neighbourhood-operator classification."""
from itertools import product
from math import comb
from random import Random


def all_families(n):
    sets = tuple(frozenset(i for i in range(n) if mask & (1 << i)) for mask in range(1<<n))
    return [tuple(sets[j] for j in range(len(sets)) if family & (1 << j)) for family in range(1 << (1<<n))]

def is_continual(families):
    return all((not families[i]) or bool(families[i+1]) for i in range(len(families)-1))

def modal_upset(n,families,t,kind):
    U=set(range(t,n))
    out=[]
    for w in range(n):
        if kind=='box':
            good=all(any(a<=U for a in families[v]) for v in range(w,n))
        else:
            good=all(all(bool(a&U) for a in families[v]) for v in range(w,n))
        if good:out.append(w)
    return frozenset(out)

def profile(n,families):
    return tuple(tuple(int(w in modal_upset(n,families,t,kind)) for w in range(n) for t in range(n+1)) for kind in ('box','diamond'))

def local_type(n,family):
    if not family:return (-1,n)
    if frozenset() in family:return (n,-1)
    return max(min(a) for a in family),min(max(a) for a in family)

def canonical(n,family):
    b,d=local_type(n,family)
    if b==-1:return ()
    if b==n:return (frozenset(),)
    if b<=d:return (frozenset((b,d)),)
    return (frozenset((b,)),frozenset((d,)))

def predicted_count(n):
    return 1 + comb(2*n,n-1) + sum(comb(n+L-1,L)**2 + comb(n+L-2,L-1)*(comb(n+L-1,L-1)-1) for L in range(1,n+1))

def modal_threshold_profile(n,families):
    bs,ds=[],[]
    for family in families:
        b,d=local_type(n,family)
        bs.append(b); ds.append(d)
    for i in range(n-2,-1,-1):
        bs[i]=min(bs[i],bs[i+1]);ds[i]=min(ds[i],ds[i+1])
    return tuple(bs),tuple(ds)

def direct_formula(n,families,val,formula):
    tag,*args=formula
    if tag=='p':return val[0]
    if tag=='q':return val[1]
    if tag=='bottom':return frozenset()
    if tag=='and':return direct_formula(n,families,val,args[0]) & direct_formula(n,families,val,args[1])
    if tag=='or':return direct_formula(n,families,val,args[0]) | direct_formula(n,families,val,args[1])
    if tag=='imp':
        A=direct_formula(n,families,val,args[0]); B=direct_formula(n,families,val,args[1])
        return frozenset(i for i in range(n) if all(j not in A or j in B for j in range(i,n)))
    if tag in ('box','diamond'):
        A=direct_formula(n,families,val,args[0])
        return frozenset(i for i in range(n) if all((any(a <= A for a in families[j]) if tag=='box' else all(bool(a&A) for a in families[j])) for j in range(i,n)))
    raise Exception('unknown')

rng=Random(60191)
# Raw neighbourhood families, not threshold encodings, are enumerated here.
for n in (1,2):
    fs=all_families(n)
    profiles=set(); framecount=0
    for families in product(fs,repeat=n):
        if not is_continual(families):continue
        framecount+=1
        compressed=tuple(canonical(n,f) for f in families)
        assert is_continual(compressed)
        pr=profile(n,families)
        assert pr==profile(n,compressed)
        profiles.add(pr)
    assert len(profiles)==predicted_count(n),(n,len(profiles),predicted_count(n))
    print('RAW_FAMILIES',n,framecount,len(profiles))

# All allowed raw local b,d types and suffix minima, independently realized by sets.
for n in range(1,5):
    opts=[(),(frozenset(),)]+[(frozenset((b,d)),) if b<=d else (frozenset((b,)),frozenset((d,))) for b,d in product(range(n),repeat=2)]
    seen=set()
    for k in range(n+1):
        for suffix in product(opts[1:],repeat=n-k):
            ff=((),)*k+suffix
            B,D=modal_threshold_profile(n,ff)
            assert tuple(tuple(int(t<=T) for T in arr for t in range(n+1)) for arr in (B,D))==profile(n,ff)
            seen.add((B,D))
    assert len(seen)==predicted_count(n),(n,len(seen),predicted_count(n))
    print('RAW_REPRESENTATIVES',n,len(seen))

# Deep formulas under all upsets of 2 variables in random raw 3- and 4-world models.
for n in (3,4):
    fam=all_families(n)
    for rep in range(300):
        k=rng.randrange(n+1)
        ff=tuple(() if i<k else rng.choice(fam[1:]) for i in range(n))
        cc=tuple(canonical(n,f) for f in ff)
        assert is_continual(cc)
        valuations=tuple(frozenset(range(rng.randrange(n+1),n)) for _ in range(2))
        def formula(depth):
            if depth==0:return (rng.choice(['p','q','bottom']),)
            op=rng.choice(['and','or','imp','box','diamond'])
            return (op,formula(depth-1),formula(depth-1)) if op in ('and','or','imp') else (op,formula(depth-1))
        for rep2 in range(30):
            f=formula(3)
            a=direct_formula(n,ff,valuations,f)
            b=direct_formula(n,cc,valuations,f)
            assert a==b,(n,ff,f,a,b)
    print('NESTED_FORMULAS',n,9000)

# Sharpness: at top world, two singleton neighbourhoods induce b=n-1>d=0.
for n in range(2,9):
    witness=(frozenset((0,)),frozenset((n-1,)))
    assert local_type(n,witness)==(n-1,0)
    candidates=[(),(frozenset(),)]+[(frozenset(mask_i for mask_i in range(n) if mask & (1<<mask_i)),) for mask in range(1,1<<n)]
    assert all(local_type(n,alt)!=(n-1,0) for alt in candidates)
print('EXACT_COUNTS',[predicted_count(n) for n in range(1,11)])
print('ALL_CHECKS_OK')
