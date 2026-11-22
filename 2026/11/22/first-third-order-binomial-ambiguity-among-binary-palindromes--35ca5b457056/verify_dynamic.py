#!/usr/bin/env python3
"""Independent increment-by-letter subsequence DP for the exact cut-off."""
from itertools import product
from collections import Counter,defaultdict

def signature(word):
    # Dictionaries store integer numbers of all subsequences of each length.
    current={'':1}
    for c in word:
        next_counts=dict(current)
        for s,v in current.items():
            if len(s)<3: next_counts[s+c]=next_counts.get(s+c,0)+v
        current=next_counts
    return tuple(current.get(''.join(x),0) for k in (1,2,3) for x in product('01',repeat=k))

def check():
    expected=[2,2,4,4,8,8,16,16,32,32,64,64,128,122]
    allpairs=[]
    for n in range(1,15):
        h=(n+1)//2
        fibers=defaultdict(list)
        for u in product('01',repeat=h):
            half=''.join(u)
            w=half+ (half[::-1] if n%2==0 else half[:-1][::-1])
            fibers[signature(w)].append(w)
        assert len(fibers)==expected[n-1],(n,len(fibers))
        assert max(map(len,fibers.values()))==(2 if n==14 else 1)
        print(n,len(fibers))
        if n==14:
            allpairs=sorted(sorted(x) for x in fibers.values() if len(x)==2)
            assert len(allpairs)==6
            assert sorted(Counter(map(len,fibers.values())).items())==[(1,116),(2,6)]
    print('pairs',allpairs)
if __name__=='__main__':check()
