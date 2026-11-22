from itertools import combinations
from collections import Counter

def criterion(edges,p):
    nbr=[set() for _ in range(p)]
    for a,b in edges: nbr[a].add(b)
    high=[nbr[a] for a in range(p) if len(nbr[a])>=2]
    if not high:return True
    common=set.intersection(*high)
    return all(len(N-common)<=1 for N in high)

def brute(edges,p,q):
    edges=list(edges)
    n=len(edges)
    # enumerate all subteam U; check independence rectangle and complement dependence
    for mask in range(1<<n):
        U=[edges[i] for i in range(n) if mask>>i&1]
        V=[edges[i] for i in range(n) if not(mask>>i&1)]
        a={x for x,y in U};b={y for x,y in U}
        if len(U)!=len(a)*len(b):continue
        rows={}
        if all(rows.setdefault(x,y)==y for x,y in V):return True
    return False

def minimal(m,p,q):
    edges={(a,b) for a in range(p) for b in range(q) if m>>(a*q+b)&1}
    return not criterion(edges,p) and all(criterion(edges-{e},p) for e in edges)

def classification(edges):
    rows={a for a,b in edges}; cols={b for a,b in edges}
    ns={a:{b for aa,b in edges if aa==a} for a in rows}
    if len(edges)==4 and len(rows)==2 and len(cols)==4 and all(len(n)==2 for n in ns.values()):return 4
    if len(edges)==6 and len(rows)==3 and len(cols)==3 and all(len(n)==2 for n in ns.values()) and all(sum(b in n for n in ns.values())==2 for b in cols):return 6
    return 0

for p,q in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,3),(4,4)]:
    want={4:0,6:0};bad=[];n=0
    for mask in range(1<<(p*q)):
        n+=1
        edges={(a,b) for a in range(p) for b in range(q) if mask>>(a*q+b)&1}
        if p*q<=10 and criterion(edges,p)!=brute(edges,p,q):raise AssertionError(('sem',p,q,mask))
        if minimal(mask,p,q):
            typ=classification(edges)
            if typ==0:bad.append(mask)
            else:want[typ]+=1
    expected={4:__import__('math').comb(p,2)*(__import__('math').comb(q,2) if q>=2 else 0)*(__import__('math').comb(q-2,2) if q>=4 else 0),6:6*(__import__('math').comb(p,3) if p>=3 else 0)*(__import__('math').comb(q,3) if q>=3 else 0)}
    print('CHECK',p,q,'teams',n,'observed',want,'expected',expected,'unclassified',len(bad),flush=True)
    assert not bad and want==expected
# all enumerations verified

# A satisfying full rectangle contains a falsifying cycle.
full={(a,b) for a in range(3) for b in range(3)}
cycle={(0,0),(0,1),(1,1),(1,2),(2,0),(2,2)}
assert criterion(full,3) and brute(full,3,3)
assert not criterion(cycle,3) and not brute(cycle,3,3)
assert cycle <= full
print('ALL_OK',flush=True)
