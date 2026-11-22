#!/usr/bin/env python3
"""Exact 2- and 3-particle coalescence time verification, no nonstdlib modules.
All state spaces are enumerated in full; no simulation or floating-point arithmetic.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from collections import defaultdict

V=tuple(range(16))
D={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}

def graph(which):
    if which=='rook':
        return tuple(tuple(v for v in V if v!=u and (v//4==u//4 or v%4==u%4)) for u in V)
    if which=='shrikhande':
        return tuple(tuple(v for v in V if (((v//4-u//4)%4, (v%4-u%4)%4) in D)) for u in V)
    raise ValueError(which)

def maps(which):
    if which=='rook':
        p=list(permutations(range(4)))
        return tuple(tuple((a[x//4]*4+b[x%4]) if not swap else (b[x%4]*4+a[x//4]) for x in V)
                     for a in p for b in p for swap in (False,True))
    mats=[]
    for a,b,c,d in product(range(4),repeat=4):
        if {( (a*x+b*y)%4, (c*x+d*y)%4) for x,y in D}==D:
            mats.append((a,b,c,d))
    assert len(mats)==12
    return tuple(tuple(( (a*(x//4)+b*(x%4)+tx)%4 )*4 +
                        ((c*(x//4)+d*(x%4)+ty)%4)
                        for x in V)
                 for a,b,c,d in mats for tx,ty in product(range(4), repeat=2))

def solve(A,b):
    n=len(b); m=[[Q(v) for v in A[i]]+[Q(b[i])] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if m[i][c])
        m[c],m[p]=m[p],m[c]
        k=m[c][c]; m[c]=[v/k for v in m[c]]
        for i in range(n):
            if i!=c and m[i][c]:
                k=m[i][c]
                m[i]=[m[i][j]-k*m[c][j] for j in range(n+1)]
    return [m[i][-1] for i in range(n)]

def adjacency_signature(g,x):
    return sum(b in g[a] for a,b in combinations(x,2))

def orbit_partition(which,g,triples):
    gg=maps(which); n=len(gg)
    assert n==(1152 if which=='rook' else 192)
    assert len(set(gg))==n
    for a in gg:
        assert set(a)==set(V)
        assert all((a[v] in g[a[u]]) for u in V for v in g[u])
    left=set(triples); groups=[]
    while left:
        x=min(left)
        orbit={tuple(sorted(a[v] for v in x)) for a in gg}
        assert orbit<=left
        groups.append(orbit);left-=orbit
    assert len(groups)==(4 if which=='rook' else 8)
    return groups

def refine_partition(g,triples):
    # Independent equitable partition computed solely from transition-count signatures.
    ids={x:adjacency_signature(g,x) for x in triples}
    while True:
        signatures={}
        for x in triples:
            outgoing=defaultdict(int);collisions=[0,0]
            for v in x:
                for u in g[v]:
                    y=tuple(sorted((set(x)-{v})|{u}))
                    if len(y)==2:collisions[int(u in g[next(w for w in y if w!=u)])]+=1
                    else:outgoing[ids[y]]+=1
            signatures[x]=(ids[x],tuple(collisions),tuple(sorted(outgoing.items())))
        sig_ids={sig:i for i,sig in enumerate(sorted(set(signatures.values())))}
        nxt={x:sig_ids[signatures[x]] for x in triples}
        # Check not just label stability but block-equivalence stability.
        if len(set(nxt.values()))==len(set(ids.values())):
            blocks=defaultdict(set)
            for x,i in nxt.items(): blocks[i].add(x)
            return list(blocks.values())
        ids=nxt

def calculate(g,groups):
    pairs=list(combinations(V,2)); triples=list(combinations(V,3))
    ix={x:i for i,grp in enumerate(groups) for x in grp}
    assert len(ix)==len(triples)==560
    def kind(x):return 1 if x[1] in g[x[0]] else 0
    # 2-particle states: nonadjacent=0, adjacent=1.
    reps={0:next(x for x in pairs if kind(x)==0),1:next(x for x in pairs if kind(x)==1)}
    a=[[Q(int(i==j)) for j in (0,1)] for i in (0,1)]; b=[Q(1,2)]*2
    for i,x in reps.items():
        for v in x:
            for u in g[v]:
                y=tuple(sorted((set(x)-{v})|{u}))
                if len(y)==2:a[i][kind(y)]-=Q(1,12)
    p=solve(a,b)
    assert p==[Q(9),Q(15,2)]
    n=len(groups);a=[[Q(int(i==j)) for j in range(n)] for i in range(n)];b=[Q(1,3) for i in range(n)]
    for i,grp in enumerate(groups):
        x=min(grp)
        for v in x:
            for u in g[v]:
                y=tuple(sorted((set(x)-{v})|{u}))
                if len(y)==3:a[i][ix[y]]-=Q(1,18)
                else:b[i]+=p[kind(y)]/18
    times=solve(a,b)
    for x in triples:
        rhs=Q(1,3)
        for v in x:
            for u in g[v]:
                y=tuple(sorted((set(x)-{v})|{u}))
                rhs+=(times[ix[y]] if len(y)==3 else p[kind(y)])/18
        assert rhs==times[ix[x]], (x,rhs,times[ix[x]])
    triangle=[times[ix[x]] for x in triples if adjacency_signature(g,x)==3]
    assert len(triangle)==32 and len(set(triangle))==1
    mean=sum(times[ix[x]] for x in triples)/560
    certificate=[(min(o),len(o),adjacency_signature(g,min(o)),str(times[i])) for i,o in enumerate(groups)]
    return {'pair_nonadjacent':p[0],'pair_adjacent':p[1],'triangle_time':triangle[0],
            'uniform_triple_mean':mean,'groups':certificate}

def check():
    data={}
    for name in ('rook','shrikhande'):
        g=graph(name)
        assert all(len(n)==6 for n in g)
        assert sum(adjacency_signature(g,t)==3 for t in combinations(V,3))==32
        assert {(len(set(g[a])&set(g[b])),b in g[a]) for a,b in combinations(V,2)}=={(2,True),(2,False)}
        t=list(combinations(V,3))
        o1=orbit_partition(name,g,t)
        o2=refine_partition(g,t)
        v1=calculate(g,o1); v2=calculate(g,o2)
        assert {tuple(sorted(o)) for o in o1}=={tuple(sorted(o)) for o in o2}
        assert all(v1[k]==v2[k] for k in ('pair_nonadjacent','pair_adjacent','triangle_time','uniform_triple_mean'))
        data[name]=v1
        print(name,'group count',len(o1),'triangle',v1['triangle_time'],'uniform',v1['uniform_triple_mean'])
        for z in v1['groups']: print('  orbit:',z)
    assert data['rook']['triangle_time']==Q(143,14)
    assert data['shrikhande']['triangle_time']==Q(1145,112)
    assert data['shrikhande']['triangle_time']-data['rook']['triangle_time']==Q(1,112)
    assert data['rook']['uniform_triple_mean']==data['shrikhande']['uniform_triple_mean']==Q(2203,196)
    print('PASS exact orbit and equitable refinement, 560-state backward equations per graph')
if __name__=='__main__':check()
