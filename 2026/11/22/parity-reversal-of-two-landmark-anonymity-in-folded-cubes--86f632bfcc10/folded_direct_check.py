"""Independent binary-word quotient distance check (no coefficient formula)."""
from collections import Counter
from itertools import combinations
from math import comb

def dist(a,b,n):
    d=(a^b).bit_count()
    return min(d,n-d)

def k_direct(n,a,b,verts):
    d=dist(a,b,n)
    profiles=Counter((dist(x,a,n),dist(x,b,n)) for x in verts if x!=a and x!=b)
    assert sum(profiles.values())==len(verts)-2
    return min(profiles.values())

def claim(n,h):
    if h==1: return n-1
    if n==4 and h==2:return 2
    if n%2==0 and h==n//2:return n
    return h

for n in range(4,9):
    verts=list(range(1<<(n-1))) # canonical quotient representative: leading bit 0
    maxima=0; number=0
    for a,b in combinations(verts,2):
        h=dist(a,b,n)
        k=k_direct(n,a,b,verts)
        assert k==claim(n,h),(n,a,b,h,k)
        if k>maxima:maxima,number=k,0
        if k==maxima:number+=1
    expected_pairs = (2**(n-2)*n if n%2 or n==4
                      else 2**(n-3)*comb(n,n//2))
    assert number==expected_pairs,(n,maxima,number,expected_pairs)
    print('EXHAUSTIVE_PAIRS',n,'max',maxima,'count',number)

for n in range(9,15):
    verts=list(range(1<<(n-1)))
    for h in range(1,n//2+1):
        b=(1<<h)-1
        assert k_direct(n,0,b,verts)==claim(n,h)
print('DIRECT_QUOTIENT_CHECK_OK')
