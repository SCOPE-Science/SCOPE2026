"""Verify finite-field alternating-rank enumeration for unicyclic support graphs.
This checker uses direct modular Gaussian elimination independently of the support/matching formula.
Python standard library only.
"""
from collections import Counter
from itertools import product


def matching_number(n, edges):
    from functools import lru_cache
    neigh = [0]*n
    for u,v in edges:
        neigh[u] |= 1<<v
        neigh[v] |= 1<<u
    @lru_cache(None)
    def f(mask):
        if not mask: return 0
        a = (mask&-mask).bit_length()-1
        rest = mask ^ (1<<a)
        ans=f(rest)
        m=neigh[a]&rest
        while m:
            bit=m&-m; m ^=bit
            ans=max(ans,1+f(rest^bit))
        return ans
    return f((1<<n)-1)


def rank_mod(mat,p):
    a=[row[:] for row in mat]
    n=len(a); r=0
    for j in range(n):
        k=next((k for k in range(r,n) if a[k][j]%p),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]
        inv=pow(a[r][j]%p,-1,p)
        a[r]=[(v*inv)%p for v in a[r]]
        for i in range(r+1,n):
            factor=a[i][j]%p
            if factor: a[i]=[(x-factor*y)%p for x,y in zip(a[i],a[r])]
        r+=1
    return r


def exceptional_support(n,edges,cycle,selected):
    # The list cycle consists of cycle vertices in cyclic order.
    if len(cycle)%2 or not all(e in selected for e in cycle_edges(cycle)):
        return False
    C=set(cycle)
    noncycle_edges=[e for e in selected if e[0] not in C and e[1] not in C]
    for v in cycle:
        roots=[u if w==v else w for (u,w) in selected if (u==v and w not in C) or (w==v and u not in C)]
        for root in roots:
            seen={root}; frontier=[root]
            while frontier:
                x=frontier.pop()
                for a,b in noncycle_edges:
                    y=b if a==x else a if b==x else None
                    if y is not None and y not in seen:
                        seen.add(y);frontier.append(y)
            ed=[(a,b) for a,b in noncycle_edges if a in seen and b in seen]
            nu=matching_number(n,ed)
            nu_minus=matching_number(n,[(a,b) for a,b in ed if a!=root and b!=root])
            if nu_minus==nu: return False
    return True


def cycle_edges(cycle):
    return {tuple(sorted((cycle[i],cycle[(i+1)%len(cycle)]))) for i in range(len(cycle))}


def predict_distribution(n,edges,cycle,q):
    out=Counter()
    for mask in range(1<<len(edges)):
        S={e for i,e in enumerate(edges) if mask>>i&1}
        r=matching_number(n,list(S))
        wt=(q-1)**len(S)
        if exceptional_support(n,edges,cycle,S):
            ex=(q-1)**(len(S)-1)
            out[r] += wt-ex
            out[r-1]+=ex
        else:
            out[r]+=wt
    return dict(out)


def direct_distribution(n,edges,p):
    out=Counter()
    for vals in product(range(p), repeat=len(edges)):
        M=[[0]*n for i in range(n)]
        for (u,v),x in zip(edges,vals):
            M[u][v]=x;M[v][u]=-x
        rk=rank_mod(M,p)
        assert rk%2==0
        out[rk//2]+=1
    return dict(out)


def check(n,edges,cycle,p):
    edges=[tuple(sorted(e)) for e in edges]
    assert len(set(edges))==len(edges) and len(edges)==n
    a=predict_distribution(n,edges,cycle,p)
    b=direct_distribution(n,edges,p)
    assert a==b,(n,edges,p,a,b)
    print(f'PASS n={n} m={len(edges)} q={p}: {dict(sorted(b.items()))}')


if __name__=='__main__':
    tests=[(4,[(0,1),(1,2),(2,3),(3,0)],[0,1,2,3]),
           (5,[(0,1),(1,2),(2,3),(3,0),(0,4)],[0,1,2,3]),
           (6,[(0,1),(1,2),(2,3),(3,0),(0,4),(4,5)],[0,1,2,3]),
           (6,[(0,1),(1,2),(2,3),(3,0),(0,4),(0,5)],[0,1,2,3]),
           (6,[(0,1),(1,2),(2,3),(3,0),(0,4),(2,5)],[0,1,2,3]),
           (5,[(0,1),(1,2),(2,3),(3,4),(4,0)],[0,1,2,3,4]),
           (6,[(0,1),(1,2),(2,3),(3,4),(4,0),(0,5)],[0,1,2,3,4])]
    count=0
    for n,ed,cyc in tests:
        for p in (2,3,5) if n<=5 else (2,3):
            check(n,ed,cyc,p);count+=1
    import random
    rng=random.Random(8871)
    for n in (7,8):
        for cyc in (3,4,5):
            for sample in range(2):
                edges=[(i,(i+1)%cyc) for i in range(cyc)]
                for i in range(cyc,n):
                    edges.append((i,rng.randrange(i)))
                check(n,edges,list(range(cyc)),3)
                count+=1
    print('VERIFY_OK_UNICYCLIC_WEIGHTED_RANK',count,'complete graph-field configurations')
