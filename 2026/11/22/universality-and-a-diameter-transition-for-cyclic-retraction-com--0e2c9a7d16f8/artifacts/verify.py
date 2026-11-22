"""Exact finite checks for cyclic-retraction commuting graph universal formulas."""
from itertools import product
from collections import deque, Counter
from math import factorial, prod

def canonical_lines(p,d):
    return [v for v in product(range(p), repeat=d) if any(v) and v[next(i for i,a in enumerate(v) if a)]==1]

def dot(a,b,p): return sum(x*y for x,y in zip(a,b))%p

def projections(p,d):
    return [(u,l) for u in canonical_lines(p,d) for l in product(range(p),repeat=d) if dot(u,l,p)==1]

def verify_graph(p,d,c=0):
    base=projections(p,d)
    verts=[(u,l,z) for u,l in base for z in range(p**c)]
    N=len(verts)
    expected=(p**c)*(p**(d-1))*(p**d-1)//(p-1)
    assert N==expected,(N,expected)
    adj=[set() for _ in verts]
    for i,(u,l,z) in enumerate(verts):
        for j in range(i):
            v,m,t=verts[j]
            if dot(l,v,p)==0 and dot(m,u,p)==0:
                adj[i].add(j);adj[j].add(i)
    deg=(p**c)*(p**(d-2))*(p**(d-1)-1)//(p-1)
    assert all(len(a)==deg for a in adj)
    discovered=set(); comps=[];diam=0
    for i in range(N):
        if i in discovered: continue
        ds={i:0};queue=deque([i])
        while queue:
            x=queue.popleft()
            for y in adj[x]:
                if y not in ds:ds[y]=ds[x]+1;queue.append(y)
        discovered.update(ds);comps.append(len(ds));diam=max(diam,max(ds.values()))
    if d==2:
        assert sorted(comps)==[2*p**c]*(p*(p+1)//2)
        assert diam==(2 if p**c>1 else 1)
    if d==3: assert comps==[N] and diam==3
    if d>=4: assert comps==[N] and diam==2
    # number of edges = number of cliques of size two from formula
    pairs=N*deg//2
    formula2= (p**(2*c+2*(d-2))*(p**d-1)*(p**d-p))//(2*(p-1)**2)
    assert pairs==formula2
    print(f'CHECK p={p} d={d} c={c}: N={N} regular_degree={deg} edges={pairs} components={len(comps)} diameter={diam} PASS')

if __name__=='__main__':
    for p,d,c in [(3,2,1),(2,2,0),(2,3,0),(3,3,0),(2,4,0)]:verify_graph(p,d,c)
    print('CYCLIC_RETRACTION_GRAPH_VERIFIED')
