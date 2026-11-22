#!/usr/bin/env python3
"""Independent validation of the diagonal-fault collapse theorem for small graphs.
Run: python3 verify.py (standard library only)."""
import itertools, random

def subsets(seq, lo=0):
    for k in range(lo, len(seq)+1):
        yield from itertools.combinations(seq,k)

def graph_faces(n, edges):
    E={frozenset(e) for e in edges}
    F=set()
    def simplex(seq):
        for s in subsets(seq,1): F.add(frozenset(s))
    for i in range(n):
        simplex([i*n+j for j in range(n)])
        simplex([j*n+i for j in range(n)])
    for s in subsets(list(range(n)),1):
        if all(frozenset(e) in E for e in itertools.combinations(s,2)):
            F.add(frozenset(i*n+i for i in s))
    for pair in edges:
        i,j=pair
        for x in (i*n+j,j*n+i):simplex([i*n+i,j*n+j,x])
    return F

def core_faces(n, edges):
    E={frozenset(e) for e in edges}
    K=set()
    for s in subsets(list(range(n)),1):
        if all(frozenset(e) in E for e in itertools.combinations(s,2)):
            K.add(frozenset(i*n+i for i in s))
    for i,j in itertools.combinations(range(n),2):
        if frozenset((i,j)) not in E:
            for x in (i*n+j,j*n+i):
                for t in [(x,), (i*n+i,x), (j*n+j,x)]:
                    K.add(frozenset(t))
    return K

def verify(n, edges):
    F=graph_faces(n,edges)
    orig=len(F)
    def drop(a,b):
        a,b=frozenset(a),frozenset(b)
        assert a in F and b in F and a<b and len(b)==len(a)+1,(n,edges,a,b,'absent')
        assert not any(a<t and t!=b for t in F),(n,edges,a,b,'nonfree')
        F.remove(a);F.remove(b)
    # Every row/column simplex collapses relative to its diagonal-rooted star.
    for kind in ('row','column'):
        for i in range(n):
            d=i*n+i
            O=[(i*n+j if kind=='row' else j*n+i) for j in range(n) if j!=i]
            for k in range(len(O),1,-1):
                for S in itertools.combinations(O,k):drop(S,tuple(S)+(d,))
    for i,j in edges:
        for x in (i*n+j,j*n+i):
            drop((i*n+i,x),(i*n+i,j*n+j,x))
            drop((x,), (j*n+j,x))
    expected=core_faces(n,edges)
    assert F==expected,(n,edges,len(F),len(expected),list(F^expected)[:3])
    # Independently reconstruct all maximal independent cliques for n<=4 by exhaustive subsets.
    if n<=4:
        allg=graph_faces(n,edges)
        E={frozenset(t) for t in edges}
        actual=set()
        for mask in range(1,1<<(n*n)):
            S=[i for i in range(n*n) if mask>>i&1]
            ok=True
            for u,v in itertools.combinations(S,2):
                i,j=divmod(u,n);k,l=divmod(v,n)
                if i!=k and j!=l and not(i==j and k==l and frozenset((i,k)) in E):
                    ok=False;break
            if ok:actual.add(frozenset(S))
        assert actual==allg,(n,edges,'incorrect-face-predicate')
    return orig,len(F), (orig-len(F))//2

def components(n, edges):
    adj=[set() for _ in range(n)]
    for i,j in edges:adj[i].add(j);adj[j].add(i)
    seen=set();c=0
    for i in range(n):
        if i in seen:continue
        c+=1;stack=[i];seen.add(i)
        while stack:
            for v in adj[stack.pop()]-seen:seen.add(v);stack.append(v)
    return c

if __name__=='__main__':
    counts=0; pairs=0
    for n in (2,3,4):
        U=list(itertools.combinations(range(n),2))
        for mask in range(1<<len(U)):
            E=[u for k,u in enumerate(U) if mask>>k&1]
            a,b,k=verify(n,E)
            assert 2*(len(U)-len(E)) - components(n,E)+1>=0
            counts+=1;pairs+=k
    rng=random.Random(3172026)
    for n in (5,6,7):
        U=list(itertools.combinations(range(n),2))
        candidates=[[],U,[(i,(i+1)%n) for i in range(n)],[(i,j) for i,j in U if i%3!=j%3]]
        for _ in range(16):candidates.append([e for e in U if rng.random()<rng.uniform(.1,.9)])
        for E in candidates:
            a,b,k=verify(n,E);counts+=1;pairs+=k
    print('PASS:',counts,'fault-graph instances,',pairs,'explicit elementary free-face collapses; target complexes matched exactly.')
    print('All 74 complete instances n<=4; additional boundary, cycle, multipartite, random examples n=5,6,7.')
