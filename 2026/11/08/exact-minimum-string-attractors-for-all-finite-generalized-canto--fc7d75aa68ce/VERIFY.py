#!/usr/bin/env python3
"""Finite independent checks for exact Cantor-word string-attractor theorem.
No external packages. Diagnostics supplement a mathematical proof, not replace it.
"""
from collections import defaultdict

def cantor(base, depth):
    word = '1'
    for _ in range(depth):
        word = ''.join('1'+'0'*(base-2)+'1' if x == '1' else '0'*base for x in word)
    return word

def candidate(base, depth):
    if depth == 1:
        return {0, base-2}
    power = base ** (depth - 1)
    out = {power-1, (base-1)*power-1}
    out.update((base-1)*power + base**i - 1 for i in range(1, depth-1))
    return out

def test(base, depth):
    word = cantor(base, depth)
    n = len(word)
    selected = candidate(base,depth)
    assert len(selected)==max(2,depth) and min(selected)>=0 and max(selected)<n
    # Exact factor-occurrence union: an attractor must intersect at least one occurrence.
    factors = defaultdict(int)
    for lo in range(n):
        v=0
        for hi in range(lo,n):
            v |= (1 << hi)
            s=word[lo:hi+1]
            if s not in factors: factors[s]=v
            else: factors[s] |= v
    target=sum(1 << p for p in selected)
    missing=[s for s,positions in factors.items() if not (positions&target)]
    assert not missing, (base,depth,missing[:3])
    # Disjoint all-occurrence supports for the lower-bound witness factors.
    if depth==1: witnesses=['0','1']
    elif depth==2: witnesses=['1','0'*((base-2)*base)]
    else:
        h=(base-2)*base**(depth-2)+1
        witnesses=['1'+'0'*h,'0'*h+'1']
        witnesses+=['1'+'0'*((base-2)*base**r)+'1' for r in range(1,depth-1)]
    assert len(witnesses)==max(2,depth)
    occupied=0
    for w in witnesses:
        support=factors.get(w,0)
        assert support, (base,depth,w)
        assert not (occupied & support),(base,depth,w)
        occupied |=support
    return n,len(factors),len(selected),len(witnesses)

if __name__=='__main__':
    cases=[(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),
           (4,1),(4,2),(4,3),(4,4),(5,1),(5,2),(5,3),
           (6,1),(6,2),(6,3),(7,1),(7,2),(7,3),(8,1),(8,2),(9,1),(9,2)]
    total=0
    for b,k in cases:
        n,nf,up,low=test(b,k)
        total+=nf
        print(f'PASS b={b} depth={k} length={n} factors={nf} upper={up} lower={low}')
    print(f'VERIFY_OK cases={len(cases)} factors={total}')
