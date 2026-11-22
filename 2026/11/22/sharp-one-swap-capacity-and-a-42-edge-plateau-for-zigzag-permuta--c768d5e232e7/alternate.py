"""Independent direct inversion-distance check; Python >=3.9, standard library.
Run: python3 alternate.py.
"""
from itertools import permutations
from collections import Counter,defaultdict

def family(n,rise):
    out=[]
    for p in permutations(range(n)):
        if all((p[i]<p[i+1])==(rise if i%2==0 else not rise) for i in range(n-1)):
            out.append(p)
    return out

def kendall(a,b):
    rank=dict((x,i) for i,x in enumerate(b))
    inv=[rank[x] for x in a]
    return sum(inv[i]>inv[j] for i in range(len(inv)) for j in range(i+1,len(inv)))

for n,want in [(2,1),(3,4),(4,10),(5,22),(6,42),(7,42)]:
    U=family(n,True);D=family(n,False)
    assert all(kendall(a,b)>=3 for F in (U,D) for ix,a in enumerate(F) for b in F[ix+1:])
    edges=[(a,b) for a in U for b in D if kendall(a,b)<3]
    assert len(edges)==want,(n,len(edges))
    if n in (6,7):
        degrees=Counter()
        for a,b in edges:
            assert kendall(a,b)==2
            degrees[(0,a)]+=1;degrees[(1,b)]+=1
        assert max(degrees.values())==1
        assert 2*len(U)-len(edges)==(80 if n==6 else 502)
        assert len(edges)==42
    print('n',n,'Euler',len(U),'cross_conflicts',len(edges))
print('ALTERNATE_OK')
