from collections import deque
from functools import lru_cache

def flip_graph(n,twist):
    # twist 0: two disjoint rings; twist 1: cross-connect ends
    assert n>=4
    ed=set()
    def norm(a,b):return tuple(sorted((a,b)))
    for i in range(n):ed.add((i,i+n))
    for i in range(n):
        j=(i+1)%n
        if i<n-1:
            for row in (0,n):ed.add(norm(i+row,j+row))
        else:
            for row in (0,n):ed.add(norm(i+row,j+row+(n if twist and row==0 else (-n if twist and row==n else 0))))
    assert len(ed)==3*n
    nbr=[set() for _ in range(2*n)]
    for a,b in ed:nbr[a].add(b);nbr[b].add(a)
    assert all(len(x)==3 for x in nbr)
    @lru_cache(None)
    def rec(mask):
        if not mask:return (frozenset(),)
        i=(mask&-mask).bit_length()-1
        arr=[]
        for j in nbr[i]:
            if mask>>j&1:
                for rest in rec(mask^(1<<i)^(1<<j)):
                    arr.append(rest|frozenset((norm(i,j),)))
        return tuple(arr)
    states=rec((1<<(2*n))-1)
    faces=[]
    for i in range(n):
        j=(i+1)%n
        if i<n-1: vs=[i,j,n+j,n+i]
        else:vs=[i,n+j,j,n+i] if twist else [i,j,n+j,n+i]
        f=frozenset(norm(vs[k],vs[(k+1)%4]) for k in range(4))
        assert len(f)==4 and f<=ed
        faces.append(f)
    G=[set() for _ in states];idx={s:k for k,s in enumerate(states)}
    for k,s in enumerate(states):
        for f in faces:
            if len(s&f)==2:
                t=(s-f)|(f-s)
                if t in idx:G[k].add(idx[t])
    assert all(k in G[v] for k,ns in enumerate(G) for v in ns)
    comp=[];seen=set()
    for k in range(len(states)):
        if k in seen:continue
        todo=[k];seen.add(k);cc=set([k])
        while todo:
            a=todo.pop()
            for b in G[a]:
                if b not in seen:seen.add(b);cc.add(b);todo.append(b)
        comp.append(cc)
    return states,G,comp,ed,faces


def lucas_graph(n):
    I=[m for m in range(1<<n) if all(not ((m>>i)&1 and (m>>((i+1)%n))&1) for i in range(n))]
    S=set(I)
    E={frozenset((m,m^(1<<i))) for m in I for i in range(n) if m^(1<<i) in S}
    return len(I),len(E)

for twist in (0,1):
 for n in range(5,15):
    ss,GG,comps,ed,faces=flip_graph(n,twist)
    lc,le=lucas_graph(n)
    cc=sorted(map(len,comps),reverse=True)
    assert cc==[lc]+([1,1] if n%2==twist else []),(n,twist,cc,lc)
    assert sum(map(len,GG))//2==le,(n,twist)
    # Independently reconstruct every nonexceptional matching from an independent set.
    spoke={tuple(sorted((i,i+n))) for i in range(n)}
    independent=[m for m in range(1<<n) if all(not ((m>>i)&1 and (m>>((i+1)%n))&1) for i in range(n))]
    midx={M:k for k,M in enumerate(ss)}
    rep={}
    for m in independent:
        covering=set()
        horizontal=set()
        for i in range(n):
            if m>>i&1:
                j=(i+1)%n
                assert i not in covering and j not in covering
                covering.update((i,j))
                horizontal.update(faces[i]-spoke)
        match=frozenset(horizontal | {tuple(sorted((i,i+n))) for i in range(n) if i not in covering})
        assert match in midx,(n,twist,m)
        rep[m]=midx[match]
    assert len(set(rep.values()))==len(rep)
    # The full induced adjacency relation is exactly one bit toggle.
    for m,k in rep.items():
        expected={rep[m^(1<<i)] for i in range(n) if m^(1<<i) in rep}
        assert GG[k]==expected,(twist,n,m)
    remaining=set(range(len(ss)))-set(rep.values())
    assert len(remaining)==(2 if n%2==twist else 0)
    assert all(not GG[k] for k in remaining)
    # A geodesic deletes I\J bits and then inserts J\I bits.
    for a in independent:
        for b in independent:
            changes=(a^b).bit_count()
            assert changes<=2*(n//2)
    print(f"EXACT_CUBE_MATCH twist={twist} n={n} states={len(ss)} moving={lc} frozen={len(remaining)} moves={le}")
print("BINARY_MODEL_PASS")
