"""Independent finite-field orbit BFS and Tutte support-count checks."""
from itertools import product,combinations
from collections import Counter

def rank_of_support(n,edges,S):
    par=list(range(n))
    def find(u):
        while par[u]!=u:
            par[u]=par[par[u]];u=par[u]
        return u
    for j in S:
        u,v=edges[j]; par[find(u)]=find(v)
    return n-len(set(find(i) for i in range(n)))

def expected(n,edges,q):
    out=Counter()
    for bits in product([0,1],repeat=len(edges)):
        S=[i for i,b in enumerate(bits) if b]
        r=rank_of_support(n,edges,S)
        out[(q*(q-1))**r]+=q**(n-r)*(q-1)**(len(S)-r)
    return out

def orbit_bfs(n,edges,q):
    m=len(edges)
    dim=n+m
    U=set(product(range(q),repeat=dim))
    sizes=Counter()
    gens=[]
    for e,(u,v) in enumerate(edges):
        if u==v:continue
        def shear(x,e=e,u=u,v=v):
            y=list(x);w=x[n+e];y[u]=(y[u]-w)%q;y[v]=(y[v]+w)%q;return tuple(y)
        gens.append(shear)
    # for q=3, one element t=2 generates the entire nonzero scalar group
    for v in range(n):
        def scale(x,v=v):
            y=list(x)
            for j,(u,w) in enumerate(edges):
                if u==v and w!=v:y[n+j]=(y[n+j]*2)%q
                if w==v and u!=v:y[n+j]=(y[n+j]*pow(2,-1,q))%q
            return tuple(y)
        if q==3:gens.append(scale)
    while U:
        x=next(iter(U));orb={x};todo=[x]
        while todo:
            y=todo.pop()
            for fn in gens:
                z=fn(y)
                if z not in orb:
                    orb.add(z);todo.append(z)
        U.difference_update(orb);sizes[len(orb)]+=1
    return sizes

CASES=[('edge',2,[(0,1)]),('parallel',2,[(0,1),(0,1)]),('opposing',2,[(0,1),(1,0)]),('loop',2,[(0,0)]),('chain',3,[(0,1),(1,2)]),('triangle',3,[(0,1),(1,2),(2,0)]),('cycle-with-loop',3,[(0,1),(1,2),(2,0),(2,2)]),('empty',3,[])]
for q in (2,3):
  for name,n,edges in CASES:
    if q==3 and len(edges)>3:continue
    got=orbit_bfs(n,edges,q);want=expected(n,edges,q)
    assert got==want,(q,name,got,want)
    print('PASS',q,name,'orbit-size histogram',dict(sorted(got.items())))
print('ALL_COADJOINT_ORBIT_CHECKS_PASS')
