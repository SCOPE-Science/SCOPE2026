"""Independent direct one-minor enumeration for layered-permutation compositions."""
from itertools import combinations
from collections import defaultdict, Counter

def compositions(n):
    if n == 0: return [()]
    return [(a,)+tail for a in range(1,n+1) for tail in compositions(n-a)]

def minors(c):
    # By standardizing after deleting one entry from each decreasing layer.
    out=set()
    for j,a in enumerate(c):
        if a == 1: out.add(c[:j]+c[j+1:])
        else: out.add(c[:j]+(a-1,)+c[j+1:])
    return out

def predicted_edges(c):
    out=set()
    L=len(c)
    for j in range(L):
        if c[j]!=1: continue
        for t in range(1,(L-j)//1):
            k=j+t+1
            if k > L or any(v!=2 for v in c[j+1:k]): break
            out.add(c[:j]+(2,)*t+(1,)+c[k:])
            if k<L and c[k]==1:
                out.add(c[:j]+(2,)*(t+1)+c[k+1:])
    return out

def component_signature(c):
    gap=[]; heavy=[]; s=0; two=False
    for x in c:
        if x>=3:
            gap.append((s,two));heavy.append(x);s=0;two=False
        else:
            s+=x
            two |= x==2
    gap.append((s,two))
    return tuple(heavy),tuple(gap)

def fib(n):
    a,b=0,1
    for i in range(n):a,b=b,a+b
    return a

for n in range(1,12):
    cs=compositions(n);deck={c:minors(c) for c in cs}
    actual=set()
    for a,b in combinations(cs,2):
        if len(deck[a].intersection(deck[b]))>=2:
            actual.add(frozenset((a,b)))
    predicted={frozenset((a,b)) for a in cs for b in predicted_edges(a)}
    assert actual==predicted,(n,'edge mismatch',len(actual^predicted))
    count=(n-1)*2**(n-4) if n>=4 else (1 if n==3 else 0)
    assert len(actual)==count,(n,len(actual),count)
    # Independently group by declared component invariants then test connectivity.
    groups=defaultdict(set)
    for c in cs:groups[component_signature(c)].add(c)
    adj={c:set() for c in cs}
    for a,b in (tuple(pair) for pair in actual):adj[a].add(b);adj[b].add(a)
    for sig,vs in groups.items():
        heavy,gaps=sig
        assert all(len(adj[v]-vs)==0 for v in vs),(n,'cross-signature edge')
        v0=next(iter(vs));todo=[v0];seen={v0}
        for u in todo:
            for v in adj[u]:
                if v not in seen:seen.add(v);todo.append(v)
        assert seen==vs,(n,sig,'not connected')
        size=1
        for m,has_two in gaps:
            if has_two:size*=fib(m+1)-1
        assert len(vs)==size,(n,sig,len(vs),size)
    iso=sum(not adj[c] for c in cs)
    print('n=%d vertices=%d edges=%d components=%d isolated=%d PASS'%(n,len(cs),len(actual),len(groups),iso))
