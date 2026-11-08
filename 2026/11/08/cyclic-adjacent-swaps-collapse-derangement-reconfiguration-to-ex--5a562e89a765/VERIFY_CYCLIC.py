"""Exhaustive derangement reconfiguration checker, using cyclic adjacent swaps."""
import itertools,collections

def check(n):
    states=[p for p in itertools.permutations(range(1,n+1)) if all(p[i-1]!=i for i in range(1,n+1))]
    idx={p:i for i,p in enumerate(states)}
    adj=[[] for _ in states]
    winding=[]
    for i,p in enumerate(states):
        k=sum(p[j]>j+1 for j in range(n))
        winding.append(k)
        for j in range(n):
            h=(j+1)%n
            z=list(p);z[j],z[h]=z[h],z[j];z=tuple(z)
            if z in idx: adj[i].append(idx[z])
    visited=set(); comps=[]
    for i in range(len(states)):
        if i in visited:continue
        C={i};todo=[i];visited.add(i)
        while todo:
            v=todo.pop()
            for w in adj[v]:
                assert winding[v]==winding[w]
                if w not in visited:visited.add(w);C.add(w);todo.append(w)
        assert len(set(winding[u] for u in C))==1
        comps.append(C)
    sectors=collections.defaultdict(list)
    for i,p in enumerate(states):
        L=tuple(v for v in range(2,n) if p.index(v)+1<v)
        sectors[L].append(i)
    assert len(sectors)==2**(n-2)
    for L,ids in sectors.items():
        allowed=set(ids); reached={ids[0]};todo=[ids[0]]
        while todo:
            v=todo.pop();p=states[v]
            for j in range(n-1):
                z=list(p);z[j],z[j+1]=z[j+1],z[j];w=idx.get(tuple(z))
                if w is not None and w in allowed and w not in reached:
                    reached.add(w);todo.append(w)
        assert reached==allowed, (n,L)
    assert len(comps)==n-1
    assert sorted(len(x) for x in comps)==sorted(sum(z==k for z in winding) for k in range(1,n))
    assert len(set(winding[next(iter(C))] for C in comps))==n-1
    assert sum(len(x) for x in comps)==len(states)
    if n>=3: assert sum(not x for x in adj)==2
    print(f'PYTHON_CYCLIC_PASS n={n} states={len(states)} components={len(comps)} size_by_excedance='+str([sum(z==k for z in winding) for k in range(1,n)]))

if __name__=='__main__':
    for n in range(3,9):check(n)
    print('PYTHON_EXHAUSTIVE_PASS')
