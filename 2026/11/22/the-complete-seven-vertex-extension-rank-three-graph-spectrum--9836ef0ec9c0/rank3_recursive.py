"""Second check of rank-three census directly from the recursive extension game.
No third-party packages; graph6 cases are supplied alongside this script.
"""
from functools import lru_cache
from collections import Counter
from pathlib import Path

def decode_graph6(s):
    n=ord(s[0])-63
    if n>62:raise ValueError('Only small graph6 supported')
    bits=[]
    for c in s[1:]:
        q=ord(c)-63
        bits.extend(((q>>i)&1) for i in (5,4,3,2,1,0))
    need=n*(n-1)//2
    if len(bits)<need:raise ValueError('Short graph6')
    a=[0]*n;k=0
    # standard graph6 upper-triangle column order: (0,1),(0,2),(1,2),(0,3),...
    for j in range(1,n):
        for i in range(j):
            if bits[k]:a[i]|=1<<j; a[j]|=1<<i
            k+=1
    return a

def rank3_direct(adj):
    n=len(adj)
    @lru_cache(None)
    def R(S,r):
        if r==0:return True
        vs=[v for v in range(n) if S>>v&1]
        rem=[v for v in range(n) if not(S>>v&1)]
        for pat in range(1<<len(vs)):
            viable=False
            for v in rem:
                if all(((adj[v]>>u)&1)==((pat>>i)&1) for i,u in enumerate(vs)) and R(S|(1<<v),r-1):
                    viable=True;break
            if not viable:return False
        return True
    return R(0,3)

if __name__=='__main__':
    p=Path(__file__).with_name('atlas_le7.g6')
    x=[s.strip() for s in p.read_text().splitlines()]
    assert len(x)==1253
    hist=Counter(); maxn=0
    for s in x:
        a=decode_graph6(s)
        if rank3_direct(a):
            assert len(a)==7
            hist[sum(r.bit_count() for r in a)//2]+=1
    goal={6:1,7:10,8:31,9:61,10:83,11:83,12:61,13:31,14:10,15:1}
    assert dict(hist)==goal, (hist,goal)
    print('DIRECT_RECURSION_OK 1253 graph-atlas representatives; rank3 classes=372; edge histogram='+str(sorted(hist.items())))
