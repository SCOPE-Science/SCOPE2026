"""Independent brute-force cross-check for n<=7 via itertools + pattern test."""
import bisect, itertools
from collections import Counter
from math import comb
def Cat(n): return comb(2*n,n)//(n+1)
def Nar(n,k): return comb(n,k)*comb(n,k-1)//n if 1<=k<=n else 0
def avoids231(p):
    for i,j,k in itertools.combinations(range(len(p)),3):
        a,b,c=p[i],p[j],p[k]
        r={v:i+1 for i,v in enumerate(sorted([a,b,c]))}
        if (r[a],r[b],r[c])==(2,3,1): return False
    return True
def lis(p):
    piles=[]
    for x in p:
        i=bisect.bisect_left(piles,x)
        if i==len(piles): piles.append(x)
        else: piles[i]=x
    return len(piles)
def des(p): return sum(1 for i in range(len(p)-1) if p[i]>p[i+1])
for n in range(1,8):
    avt=[p for p in itertools.permutations(range(1,n+1)) if avoids231(p)]
    assert len(avt)==Cat(n), (n,len(avt),Cat(n))
    dl=Counter(lis(p) for p in avt)
    dd=Counter(des(p)+1 for p in avt)
    nar={k:Nar(n,k) for k in range(1,n+1)}
    assert dict(dl)==nar, (n,dict(dl),nar)
    assert dict(dd)==nar, (n,dict(dd))
    print(f"n={n}: C={Cat(n)} LIS-dist={dict(sorted(dl.items()))} == Narayana OK; descents+1 OK")
print("ALL SMALL-N BRUTE-FORCE CHECKS PASS")
