"""Independent set-based power propagation and Johnson-edge reconstruction."""
from itertools import combinations
from collections import Counter, deque

def make(n):
    G={v:set() for v in range(n)}
    for a,b in combinations(range(n),2):
        e=('edge',a,b)
        G[e]={a,b}
        G[a].add(e); G[b].add(e)
    return G

def power(G,chosen):
    active=set(chosen)
    for v in chosen:active.update(G[v])
    while True:
        new=set(active)
        for v in active:
            remain=G[v]-active
            if len(remain)==1:new.update(remain)
        if len(new)==len(active):return active==set(G)
        active=new

def family(n):
    groups={}; labels=set(range(n))
    for a,b in combinations(range(n),2):
        groups[('A',a,b)]=frozenset(labels-{a,b})
    for a,b,c in combinations(range(n),3):
        for u,v in ((a,b),(a,c),(b,c)):
            groups[('B',a,b,c,u,v)]=frozenset((labels-{a,b,c})|{('edge',u,v)})
    return groups

def eccentricity(R,start):
    dst={start:0};pending=deque([start])
    while pending:
        x=pending.popleft()
        for y in R[x]:
            if y not in dst:dst[y]=dst[x]+1;pending.append(y)
    assert len(dst)==len(R)
    return max(dst.values())

def analyze(n):
    G=make(n); F=family(n)
    if n<=6:
        found=[]
        for k in range(n-1):
            found=[frozenset(t) for t in combinations(G,k) if power(G,t)]
            if found:break
        assert k==n-2
        assert set(found)==set(F.values()),(n,len(found),len(F))
    R={x:set() for x in F}
    pairs=list(F.items())
    for i,(u,S) in enumerate(pairs):
        for v,T in pairs[i+1:]:
            if len(S-T)==1 and len(T-S)==1:
                x=next(iter(S-T)); y=next(iter(T-S))
                if y in G[x]:R[u].add(v);R[v].add(u)
    # Reconstruct each Johnson edge from its two A endpoint states.
    A=[frozenset(pair) for pair in combinations(range(n),2)]
    J={frozenset((a,b)) for a,b in combinations(A,2) if len(a&b)==1}
    midpoint_counts=Counter()
    for name,S in F.items():
        if name[0]=='A':assert len(R[name])==2*(n-2)
        else:
            nb=list(R[name]);assert len(nb)==2,(n,name,nb)
            assert all(x[0]=='A' for x in nb)
            U=frozenset(nb[0][1:]);V=frozenset(nb[1][1:])
            e=frozenset((U,V))
            assert e in J
            midpoint_counts[e]+=1
    assert len(midpoint_counts)==len(J) and set(midpoint_counts.values())=={1}
    assert len(R)==n*(n-1)*(n-1)//2
    assert sum(map(len,R.values()))//2==n*(n-1)*(n-2)
    if n<=10:
        ecc=Counter(eccentricity(R,x) for x in R)
        assert max(ecc)==min(n,6)
        print('n',n,'counts',len(R),sum(map(len,R.values()))//2,'ecc',dict(sorted(ecc.items())))
    else:print('n',n,'bijective Johnson edge subdivisions verified')

if __name__=='__main__':
    for n in list(range(3,11))+[12,16]:analyze(n)
