#!/usr/bin/env python3
"""Exact checks for a bilinear zero-product graph classification over prime fields."""
import itertools
from collections import Counter, deque

def dot(a, b, matrix, p):
    return sum(x * matrix[i][j] * y for i, x in enumerate(a) for j, y in enumerate(b)) % p

def graph(p, matrix, radical_dimension=0):
    t = len(matrix)
    assert t >= 1 and all(len(row) == t for row in matrix)
    d = t + radical_dimension
    vectors = list(itertools.product(range(p), repeat=d+1))
    vv = [x for x in vectors if any(x)]
    def adj(x, y):
        return dot(x[:t], y[:t], matrix, p) == 0
    edges = {frozenset((i, j)) for i in range(len(vv)) for j in range(i+1, len(vv)) if adj(vv[i], vv[j])}
    return vv, edges

def components(vv, edges, universal_indices):
    remaining = set(range(len(vv))) - set(universal_indices)
    nbr = {i: set() for i in remaining}
    for e in edges:
        a,b=tuple(e)
        if a in remaining and b in remaining:
            nbr[a].add(b); nbr[b].add(a)
    comps=[]
    while remaining:
        s=remaining.pop(); todo=[s]; part={s}
        while todo:
            v=todo.pop()
            for w in nbr[v]&remaining:
                remaining.remove(w);part.add(w);todo.append(w)
        comps.append(part)
    return comps

def cycle5_exists(vv, edges):
    adj = [set() for _ in vv]
    for edge in edges:
        x, y = tuple(edge); adj[x].add(y);adj[y].add(x)
    for a in range(len(vv)):
        for b in adj[a]:
            if b <= a: continue
            for c in adj[b]-adj[a]-{a}:
                for d in adj[c]-adj[a]-adj[b]-{a,b}:
                    for e in (adj[d]&adj[a])-adj[b]-adj[c]-{a,b,c}:
                        if e not in (a,b,c,d):
                            return tuple(vv[z] for z in (a,b,c,d,e))
    return None

def check(p, mat, r, label):
    t=len(mat)
    vv,edges=graph(p,mat,r)
    universal=[i for i in range(len(vv)) if all(i==j or frozenset((i,j)) in edges for j in range(len(vv)))]
    c=p**(r+1)-1
    assert len(universal)==c, (label,'universal',len(universal),c)
    comps=components(vv,edges,universal)
    B=p**(r+1)*(p-1)
    if t==1:
        assert len(comps)==B and all(len(C)==1 for C in comps)
        assert not any(frozenset((i,j)) in edges for i,j in itertools.combinations(comps[0],2))
    elif t==2:
        projective=set()
        for x in itertools.product(range(p), repeat=t):
            if any(x):
                k=next(z for z in x if z)
                projective.add(tuple(z*pow(k,-1,p)%p for z in x))
        isotropic=sum(dot(v,v,mat,p)==0 for v in projective)
        assert isotropic in (0,1,2,p+1)
        sizes=Counter(len(C) for C in comps)
        a=isotropic; b=(p+1-a)//2
        assert p+1-a==2*b
        assert sizes==Counter(([B]*a)+([2*B]*b)), (label,sizes,a,b,B)
        for C in comps:
            degs={sum(frozenset((i,j)) in edges for j in C if i!=j) for i in C}
            if len(C)==B: assert degs=={B-1}, (label,'clique',degs)
            else: assert len(C)==2*B and degs=={B}, (label,'biclique',degs)
        assert cycle5_exists(vv,edges) is None, (label,'unexpected C5')
    else:
        assert cycle5_exists(vv,edges) is not None, (label,'missing C5')
    print('PASS', label, 'q',p,'rank',t,'rad',r,'vertices',len(vv),'edges',len(edges),'components',sorted(map(len,comps)))

if __name__=='__main__':
    tests=[
      (2,[[1]],0,'rank1-binary'),(3,[[1]],1,'rank1-radical'),
      (2,[[1,0],[0,1]],0,'char2-nonalternating'),
      (2,[[0,1],[1,0]],0,'char2-alternating'),
      (2,[[0,1],[1,0]],1,'char2-alternating-radical'),
      (3,[[1,0],[0,1]],0,'odd-anisotropic'),
      (3,[[1,0],[0,2]],0,'odd-split'),
      (3,[[1,0],[0,2]],1,'odd-split-radical'),
      (5,[[1,0],[0,2]],0,'five-anisotropic'),
      (5,[[1,0],[0,4]],0,'five-split'),
      (2,[[1,0,0],[0,1,0],[0,0,1]],0,'three-nonalternating-binary'),
      (3,[[1,0,0],[0,1,0],[0,0,1]],0,'three-nonalternating-ternary'),
      (2,[[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]],0,'four-alternating-binary'),
    ]
    for p,m,r,name in tests:check(p,m,r,name)
    print('VERIFY_OK',len(tests),'independent configurations')
