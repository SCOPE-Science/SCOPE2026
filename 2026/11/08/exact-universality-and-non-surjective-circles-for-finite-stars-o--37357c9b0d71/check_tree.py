#!/usr/bin/env python3
"""Finite combinatorial checks for the star of regular rooted directed trees.
This checks selected truncations and explicit wavelets, not infinite spectral claims.
"""
from math import sqrt, isclose

def check(branches, depth):
    assert sorted(set(branches)) == branches and len(branches)>=2
    root=('root',)
    children={root:[]}
    parent={}
    vertices=[root]
    for j,b in enumerate(branches):
        v=(j,())
        parent[v]=root
        children[root].append(v)
        vertices.append(v)
        queue=[v]
        for _ in range(depth):
            nq=[]
            for x in queue:
                jj,w=x
                children[x]=[]
                for t in range(b):
                    y=(jj,w+(t,))
                    parent[y]=x
                    children[x].append(y)
                    nq.append(y)
                    vertices.append(y)
            queue=nq
        for x in queue: children[x]=[]
    counts=0
    def descendants(v,n):
        pool=[v]
        for _ in range(n):pool=[y for x in pool for y in children[x]]
        return pool
    for n in range(1,depth+1):
        # Root produces sum_j b_j^(n-1), each intact branch gives b_j^n.
        assert len(descendants(root,n))==sum(b**(n-1) for b in branches)
        for j,b in enumerate(branches):
            assert len(descendants((j,()),n))==b**n
            counts+=1
    b=branches[-1]; j=len(branches)-1
    # At a maximal-branch vertex, antisymmetrize over the first two children;
    # these are reducing backward-shift wavelets on the full infinite tree.
    v=(j,())
    def wavelet(n):
        out={}
        for digit,sgn in [(0,1),(1,-1)]:
            for u in descendants((j,(digit,)),n):
                out[u]=sgn/sqrt(2*b**n)
        return out
    def dot(x,y):return sum(a*y.get(u,0) for u,a in x.items())
    def S(x):
        out={}
        for u,c in x.items():
            if u==root:continue
            p=parent[u];out[p]=out.get(p,0)+c
        return {u:c for u,c in out.items() if abs(c)>1e-14}
    def St(x):
        out={}
        for u,c in x.items():
            for ch in children[u]:out[ch]=c
        return out
    for n in range(depth):
        f=wavelet(n)
        assert isclose(dot(f,f),1,abs_tol=1e-12)
        for m in range(n):
            assert isclose(dot(f,wavelet(m)),0,abs_tol=1e-12)
        desired={} if n==0 else {u:sqrt(b)*c for u,c in wavelet(n-1).items()}
        z=S(f)
        assert set(z)==set(desired) and all(isclose(c,desired[u],abs_tol=1e-11) for u,c in z.items())
        if n<depth-1:
            z=St(f)
            desired={u:sqrt(b)*c for u,c in wavelet(n+1).items()}
            assert set(z)==set(desired) and all(isclose(c,desired[u],abs_tol=1e-11) for u,c in z.items())
        counts+=4
    # The child-root relation is genuinely coupled to the global root.
    for j in range(len(branches)):
        assert S({(j,()):1})=={root:1}
        counts+=1
    return counts

if __name__=='__main__':
    total=0
    for branches in ([1,2],[1,2,3],[2,4,5],[1,3,5],[3,5,7]):
        for depth in range(2,6):
            n=check(list(branches),depth)
            total+=n
    print(f'PASS: {total} finite structural check groups; 20 finite star truncations.')
