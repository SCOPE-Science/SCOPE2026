"""Independent finite checks for balanced parity-restricted Boolean layers.
Usage: python3 check.py
No external libraries required.
"""
from itertools import combinations
from functools import lru_cache

def layer(a,b):
    n=a+b;m=n//2
    out=[]
    for s in combinations(range(n),m):
        if sum(x<a for x in s)%2==0:
            out.append(sum(1<<x for x in s))
    return out

def vc(C,n):
    v=0
    for k in range(1,n+1):
        yes=False
        for supp in combinations(range(n),k):
            mask=sum(1<<x for x in supp)
            if len({c&mask for c in C})==(1<<k):
                yes=True;break
        if not yes:break
        v=k
    return v

def ldim(C,n):
    f=[sum(1<<j for j,c in enumerate(C) if c>>i&1) for i in range(n)]
    whole=(1<<len(C))-1
    @lru_cache(None)
    def rec(s):
        if s.bit_count()<2: return 0
        best=0
        for t in f:
            v=s&t; w=s^v
            if not v or not w: continue
            if min(v.bit_count(),w.bit_count()) < (1<<best):continue
            best=max(best,1+min(rec(v),rec(w)))
        return best
    return rec(whole),rec.cache_info().currsize

for n in (4,6,8,10):
    m=n//2
    for a in range(1,n,2):
        b=n-a;C=layer(a,b)
        v=vc(C,n); l,states=ldim(C,n)
        expected_v=m-1
        expected_l=m if a>=3 and b>=3 else m-1
        assert (v,l)==(expected_v,expected_l),(a,b,v,l,expected_v,expected_l)
        print(f'a={a:2d} b={b:2d} r={m:2d} |C|={len(C):4d} VC={v} Ldim={l} states={states}')
print('PASS finite exhaustive checks')
