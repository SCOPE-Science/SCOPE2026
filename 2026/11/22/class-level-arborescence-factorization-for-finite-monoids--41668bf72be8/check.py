"""Reproduce finite computations for the Green-class divisibility arborescence theorem.
Uses only Python's standard library; no data files are required.
"""
from itertools import product, permutations
from collections import Counter
from fractions import Fraction
from math import factorial, comb

def determinant(M):
    """Exact determinant by rational elimination, independent of tree factorization."""
    A = [[Fraction(x) for x in row] for row in M]
    n=len(A); ans=Fraction(1)
    for k in range(n):
        j=next((i for i in range(k,n) if A[i][k]),None)
        if j is None: return 0
        if j!=k:
            A[k],A[j]=A[j],A[k]; ans=-ans
        q=A[k][k]; ans *= q
        for i in range(k+1,n):
            if A[i][k]:
                t=A[i][k]/q
                for h in range(k+1,n): A[i][h]-=t*A[k][h]
                A[i][k]=0
    assert ans.denominator==1
    return int(ans)

def graph_from_poset(weights, relations, internal=None, external=None):
    """Blocks indexed by 0..m-1; relations are strict, transitively closed comparisons."""
    m=len(weights)
    vertices=[(j,i) for j,w in enumerate(weights) for i in range(w)]
    if internal is None: internal=[1]*m
    if external is None: external={key:1 for key in relations}
    adj=[[0]*len(vertices) for _ in vertices]
    for a,(j,i) in enumerate(vertices):
        for b,(k,l) in enumerate(vertices):
            if a!=b:
                adj[a][b]=internal[j] if j==k else external.get((j,k),0) if (j,k) in relations else 0
    return vertices,adj

def arborescence_det(adj,root):
    n=len(adj)
    L=[[(-adj[i][j] if i!=j else sum(adj[i])) for j in range(n)] for i in range(n)]
    return determinant([[L[i][j] for j in range(n) if j!=root] for i in range(n) if i!=root])

def enumerate_arborescences(adj,root):
    n=len(adj); others=[x for x in range(n) if x!=root]
    opts=[[(v,adj[i][v]) for v in range(n) if adj[i][v]>0] for i in others]
    total=0; by_exit=Counter()
    for choices in product(*opts):
        parents=dict(zip(others,(t for t,w in choices)))
        if any(not reaches_root(parents,i,root,n) for i in others): continue
        weight=1
        for dest,w in choices: weight*=w
        total+=weight
        by_exit[tuple(choices)] +=weight
    return total

def reaches_root(parents,x,root,n):
    for _ in range(n):
        if x==root: return True
        x=parents[x]
    return False

def factor(weights,relations,internal=None,external=None,top=None):
    m=len(weights)
    if internal is None:internal=[1]*m
    if external is None:external={key:1 for key in relations}
    tops=[i for i in range(m) if not any(i==j for j,k in relations)]
    if top is None:
        assert len(tops)==1
        top=tops[0]
    u=weights[top]
    z=(u**(u-2) * internal[top]**(u-1)) if u>=2 else 1
    for j,w in enumerate(weights):
        if j==top:continue
        U=sum(weights[k]*external[j,k] for k in range(m) if (j,k) in relations)
        z *= U*(w*internal[j]+U)**(w-1)
    return z

def closure_relations(m,covers):
    rel=set(covers)
    while 1:
        old=set(rel)
        rel.update((a,d) for a,b in old for c,d in old if b==c)
        if old==rel:break
    assert not any(a==b for a,b in rel)
    return rel

def checks():
    tests=[([1],set()),([2],set()),([3],set()),([1,1,1],{(0,1),(1,2),(0,2)}),
        ([1,1,1],{(0,2),(1,2)}),([2,2],{(0,1)}),
        ([2,1,2],{(0,2),(1,2)}),([1,2,2],{(0,1),(1,2),(0,2)}),
        ([2,1,1,2],{(0,1),(0,2),(0,3),(1,3),(2,3)})]
    for weights,rel in tests:
        v,adj=graph_from_poset(weights,rel)
        root=next(i for i,(j,k) in enumerate(v) if j==len(weights)-1)
        d=arborescence_det(adj,root)
        f=factor(weights,rel)
        assert d==f,(weights,d,f)
        if len(v)<=7: assert enumerate_arborescences(adj,root)==f
        internal=[2+i for i in range(len(weights))]
        external={p:2+p[0]+2*p[1] for p in rel}
        v,adj=graph_from_poset(weights,rel,internal,external)
        d=arborescence_det(adj,root); f=factor(weights,rel,internal,external)
        assert d==f,(weights,'weighted',d,f)
        if len(v)<=7: assert enumerate_arborescences(adj,root)==f
    # Produce full monoids with composition and derive Green J classes directly.
    def monoid_test(maps):
        n=len(maps[0]); idx={f:i for i,f in enumerate(maps)}
        def compose(f,g):return tuple(-1 if v<0 else f[v] for v in g)
        N=len(maps)
        assert all(compose(f,g) in idx for f in maps for g in maps)
        e=tuple(range(n)); root=idx[e]
        prod=[[idx[compose(f,g)] for g in maps] for f in maps]
        ideals=[]
        for a in range(N):
            s={a}
            s.update(prod[x][a] for x in range(N))
            s.update(prod[a][x] for x in range(N))
            s.update(prod[prod[x][a]][y] for x in range(N) for y in range(N))
            ideals.append(frozenset(s))
        adj=[[int(i!=j and ideals[i]<=ideals[j]) for j in range(N)] for i in range(N)]
        blocks=sorted(set(ideals),key=lambda q:(len(q),sorted(q)))
        weights=[sum(z==q for z in ideals) for q in blocks]
        relations={(i,j) for i,p in enumerate(blocks) for j,q in enumerate(blocks) if p<q}
        assert blocks[-1]==frozenset(range(N))
        d=arborescence_det(adj,root)
        f=factor(weights,relations)
        assert d==f,(N,d,f)
        if N<=7:assert enumerate_arborescences(adj,root)==f
        return N,weights,f
    t2=monoid_test(list(product(range(2),repeat=2)))
    # Partial bijections on two points.
    partial=[]
    for a in product((-1,0,1),repeat=2):
        nonzero=[x for x in a if x>=0]
        if len(nonzero)==len(set(nonzero)):partial.append(a)
    i2=monoid_test(partial)
    assert t2==(4,[2,2],8),t2
    assert i2==(7,[1,4,2],2592),i2
    # Boolean lattice of subsets, where multiplication is intersection.
    bool2=[i for i in range(4)]
    ideals=[frozenset(i&j for j in bool2) for i in bool2]
    adj=[[int(i!=j and ideals[i]<=ideals[j]) for j in bool2] for i in bool2]
    assert arborescence_det(adj,3)==3
    # Exact exit-count distribution in the T2 lower J-class: 4 with one exit and 4 with two.
    v,adj=graph_from_poset([2,2],{(0,1)})
    root=v.index((1,0)); by=Counter()
    opts=[[(dest,wt) for dest,wt in enumerate(adj[i]) if wt] for i in range(4) if i!=root]
    inds=[i for i in range(4) if i!=root]
    for cs in product(*opts):
        P=dict(zip(inds,(k for k,wt in cs)))
        if all(reaches_root(P,i,root,4) for i in inds):
            by[sum(P[i]>=2 for i in (0,1))]+=1
    assert by=={1:4,2:4},by
    print('GREEN_DIVISIBILITY_ARBORESCENCES_OK')
    print('tested_posets',len(tests),'T2',t2,'I2',i2,'B2',3,'T2_exit_profile',dict(by))

if __name__=='__main__':checks()
