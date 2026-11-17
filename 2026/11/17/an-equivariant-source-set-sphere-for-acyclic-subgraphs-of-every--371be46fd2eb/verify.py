#!/usr/bin/env python3
"""Finite checks of the head-set map for acyclic-edge complexes.

All examples are small enough for exhaustive face and orbit enumeration.
"""
from itertools import combinations, permutations


def cyclic(n,k): return tuple((i+k)%n for i in range(n))
def reflect(n,k): return tuple((k-i)%n for i in range(n))
def compose(a,b): return tuple(a[b[i]] for i in range(len(a)))
def group_generated(n,gens):
    group={tuple(range(n))};stack=list(group)
    while stack:
        x=stack.pop()
        for y in gens:
            z=compose(x,y)
            if z not in group: group.add(z);stack.append(z)
    return sorted(group)

def is_dag(n,es):
    deg=[0]*n; adj=[[] for _ in range(n)]
    for a,b in es: adj[a].append(b);deg[b]+=1
    q=[i for i,d in enumerate(deg) if d==0];seen=0
    for x in q:
        seen+=1
        for y in adj[x]:
            deg[y]-=1
            if deg[y]==0:q.append(y)
    return seen==n

def orbits(elements,G,action):
    out=[];todo=set(elements)
    while todo:
        x=min(todo)
        o={action(g,x) for g in G}
        assert o<=todo
        todo-=o;out.append(frozenset(o))
    return out

def rank_mod2(rows):
    b={}
    for x in rows:
        while x:
            i=x.bit_length()-1
            if i in b:x^=b[i]
            else:b[i]=x;break
    return len(b)

def mod2_betti(faces,maxdim):
    bydim=[[] for _ in range(maxdim+1)]
    for F in faces:
        if F:bydim[len(F)-1].append(tuple(sorted(F)))
    ranks=[]
    for d in range(1,maxdim+1):
        idx={F:i for i,F in enumerate(bydim[d-1])}
        col=[]
        for F in bydim[d]:
            mask=0
            for i in range(len(F)):
                mask^=1<<idx[F[:i]+F[i+1:]]
            col.append(mask)
        ranks.append(rank_mod2(col))
    betti=[]
    for d in range(maxdim+1):
        dim=len(bydim[d]);lower=ranks[d-1] if d else 0;upper=ranks[d] if d<maxdim else 0
        betti.append(dim-lower-upper)
    return betti

def trial(name,n,edges,gens):
    edges=sorted(set(edges))
    assert all(a!=b for a,b in edges)
    G=group_generated(n,gens)
    assert all({(g[a],g[b]) for a,b in edges}==set(edges) for g in G)
    # Verify directed strong connectivity by reachability.
    for u in range(n):
        seen={u};q=[u]
        for a in q:
            for x,y in edges:
                if x==a and y not in seen:seen.add(y);q.append(y)
        assert len(seen)==n
    edgeorbits=orbits(edges,G,lambda g,e:(g[e[0]],g[e[1]]))
    v_orbits=orbits(range(n),G,lambda g,i:g[i])
    m=len(edgeorbits)
    if m>17: return ('SKIP',name,m)
    faces=[]
    for k in range(1<<m):
        e=set().union(*(edgeorbits[j] for j in range(m) if (k>>j)&1))
        if is_dag(n,e):faces.append(tuple(i for i in range(m) if (k>>i)&1))
    betti=mod2_betti(faces,m)
    t=len(v_orbits)
    if t==1:assert len(faces)==1 and sum(betti)==0,(name,betti)
    else:
        assert ((betti[0]==2 and sum(betti)==2) if t==2 else (betti[0]==1 and betti[t-2]==1 and sum(betti)==2)),(name,t,betti)
    # For every proper invariant nonempty head set T, check canonical invariant cone.
    vset=set(range(n))
    invT=[set().union(*(v_orbits[j] for j in range(t) if k>>j&1)) for k in range(1,2**t-1)]
    for T in invT:
        S=vset-T
        outgoing={(a,b) for a,b in edges if a in S and b in T}
        assert outgoing
        assert all({(g[a],g[b]) for a,b in outgoing}==outgoing for g in G)
        for k in range(1<<m):
            e=set().union(*(edgeorbits[j] for j in range(m) if k>>j&1))
            if e and all(b in T for a,b in e) and is_dag(n,e):
                assert is_dag(n,e|outgoing)
    return (name,n,len(G),len(v_orbits),m,len(faces)-1,[ (i,v) for i,v in enumerate(betti) if v])

if __name__=='__main__':
    cases=[]
    for n in range(3,8):
        e={(i,(i+1)%n) for i in range(n)}
        cases.extend([trial('directed_cycle_%s_rotation_%s'%(n,k),n,e,[cyclic(n,k)]) for k in range(n)])
    for n in range(3,6):
        e={(i,j) for i in range(n) for j in range(n) if i!=j}
        cases.append(trial('complete_bidirected_%s_full'%n,n,e,[tuple((i+1)%n for i in range(n)),tuple([1,0]+list(range(2,n)))]))
        for k in range(1,n):
            cases.append(trial('complete_bidirected_%s_rotation_%s'%(n,k),n,e,[cyclic(n,k)]))
    for n in (4,5,6):
        e={(i,(i+1)%n) for i in range(n)}|{((i+1)%n,i) for i in range(n)}
        cases.append(trial('double_cycle_%s_dihedral'%n,n,e,[cyclic(n,1),reflect(n,0)]))
        for k in range(n):
            cases.append(trial('double_cycle_%s_reflection_%s'%(n,k),n,e,[reflect(n,k)]))
    for r in cases:
        if r[0]=='SKIP':print('OMITTED',r)
        else:print('CHECKED',r)
    print('ACYCLIC_DIGRAPH_EQUIVARIANT_HEAD_MAP_CHECKS_PASS')
