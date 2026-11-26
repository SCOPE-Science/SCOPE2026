#!/usr/bin/env python3
"""Direct verification of idempotent-retraction dihedral orbit profiles for cycles.

No mathematical result is assumed: enumerate adjacent-image maps and compare
with predictions from independent path-walk dynamic programming.
"""
from collections import Counter
from itertools import product


def path_walk(k, steps, start):
    ways=[0]*k
    ways[start]=1
    for _ in range(steps):
        nxt=[0]*k
        for x in range(k):
            if x: nxt[x-1]+=ways[x]
            if x+1<k:nxt[x+1]+=ways[x]
        ways=nxt
    return ways


def predicted(n):
    result={n:(1,1,0)}  # element count, n-sized orbits, 2n-sized orbits
    if n%2:
        return result
    for k in range(2,n//2+2):
        L=n-k+1
        W=path_walk(k,L,k-1)[0]
        m=L//2
        if k%2:
            assert L%2==0
            F=path_walk(k,m,k-1)[(k-1)//2]
        else:
            assert L%2==1
            counts=path_walk(k,m,k-1)
            F=counts[k//2-1]+counts[k//2]
        assert 0<=F<=W and (W-F)%2==0,(n,k,W,F)
        result[k]=(n*W,F,(W-F)//2)
    return result


def all_idempotent_endomorphisms(n):
    result=[]
    for a in range(n):
        for moves in product((-1,1),repeat=n-1):
            vals=[a]
            for s in moves:
                vals.append((vals[-1]+s)%n)
            if ((vals[-1]-vals[0])%n) not in (1,n-1):
                continue
            if all(vals[vals[i]]==vals[i] for i in range(n)):
                result.append(tuple(vals))
    return result


def transform(f, sign, shift):
    # automorphism g(x)=sign*x+shift modulo n
    n=len(f)
    inverse_sign=sign
    inverse_shift=(-sign*shift)%n
    return tuple((sign*f[(inverse_sign*i+inverse_shift)%n]+shift)%n for i in range(n))


def test(n):
    maps=all_idempotent_endomorphisms(n)
    remaining=set(maps)
    observed=Counter()
    orbits_total=0
    while remaining:
        f=next(iter(remaining))
        orb={transform(f,sign,shift) for sign in (-1,1) for shift in range(n)}
        assert orb<=set(maps)
        remaining-=orb
        k=len(set(f))
        if k==n:
            assert len(orb)==1
            observed[(k,1)]+=1
        else:
            assert len(orb) in (n,2*n),(n,k,len(orb))
            observed[(k,len(orb))]+=1
        orbits_total+=1
    by_rank=Counter(len(set(f)) for f in maps)
    pred=predicted(n)
    assert {k:v[0] for k,v in pred.items()}==dict(by_rank),(n,by_rank,pred)
    for k,(num,sym,asym) in pred.items():
        if k==n:
            assert observed[(k,1)]==1
        else:
            assert observed[(k,n)]==sym,(n,k,'sym',observed[(k,n)],sym)
            assert observed[(k,2*n)]==asym,(n,k,'asym',observed[(k,2*n)],asym)
    assert orbits_total==sum(s+a for k,(v,s,a) in pred.items() if k!=n)+1
    return len(maps),orbits_total,sorted(observed.items())

if __name__=='__main__':
    total=0
    for n in range(3,15):
        cnt,orbits,profiles=test(n)
        print(f'C{n}: idempotents={cnt}, conjugacy_orbits={orbits}, '+', '.join(f'rank{k},orbit{sz}:{v}' for (k,sz),v in profiles))
        total+=cnt
    print(f'ALL_CYCLE_RETRACTION_DIHEDRAL_ORBIT_CHECKS_PASSED cases=12 elements={total}')
