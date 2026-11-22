#!/usr/bin/env python3
"""Finite checks for complete shortest absent subsequence languages of Tribonacci words."""
from functools import lru_cache
from itertools import product

subst={'0':'01','1':'02','2':'0'}
w='0'; lengths={0:1}
for k in range(1,11):
    w=''.join(subst[a] for a in w)
    lengths[k]=len(w)
    if k<4: continue
    n=len(w);r=lengths[k-3]
    expect=3 if k%3==2 else 1
    # All greedy arches must end in the unique 2 of the arch.
    arches=[]; seen=set(); j=0
    for i,c in enumerate(w):
        seen.add(c)
        if len(seen)==3:
            arches.append(w[j:i+1]);j=i+1;seen=set()
    assert len(arches)==r
    assert set(arches)<=set(['0102','0100102','010102'])
    assert arches[-1] in ('0100102','010102')
    assert w[j:]==('010' if k%3==0 else '01' if k%3==1 else '')
    # next[i][c] is the earliest c at or following i, sentinel n if none.
    nxt=[[n,n,n] for _ in range(n+1)]
    for i in range(n-1,-1,-1):
        nxt[i]=nxt[i+1].copy();nxt[i][int(w[i])]=i
    @lru_cache(None)
    def missing(i,h):
        if h==0: return 0
        return sum((3**(h-1) if p==n else missing(p+1,h-1)) for p in nxt[i])
    assert missing(0,r+1)==expect,(k,missing(0,r+1),expect)
    if k<=5:
        absent=[]
        for a in product('012',repeat=r+1):
            j0=0
            for c in a:
                p=nxt[j0][int(c)]
                if p==n:absent.append(''.join(a));break
                j0=p+1
        predicted=['2'*(r+1)] if k%3!=2 else ['2'*r+c for c in '012']
        assert set(absent)==set(predicted),(k,absent,predicted)
    print('rank',k,'length',n,'arches',r,'missing',expect)
print('VERIFY_OK')
