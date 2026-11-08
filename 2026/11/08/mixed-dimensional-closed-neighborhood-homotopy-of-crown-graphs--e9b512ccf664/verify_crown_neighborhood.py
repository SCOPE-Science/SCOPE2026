"""Finite checks for the closed-neighborhood complex of crown graphs.

Python 3 standard library only. Every simplex is built from graph adjacency.
The general homotopy statement is proved in RESULT.md, not by this sampling.
"""
from collections import defaultdict
from itertools import combinations

def faces_from_facets(facets):
    ans={frozenset()}
    for facet in facets:
        q=sorted(facet)
        for k in range(1,len(q)+1):
            ans.update(frozenset(c) for c in combinations(q,k))
    return ans

def graph(n, missing_matching=True):
    adj={i:set() for i in range(2*n)}
    for i in range(n):
        for j in range(n):
            if missing_matching and i==j: continue
            adj[i].add(n+j)
            adj[n+j].add(i)
    return adj

def material(n, missing_matching=True):
    adj=graph(n, missing_matching)
    closed=[{i}|adj[i] for i in range(2*n)]
    ka=faces_from_facets(closed[:n])
    kb=faces_from_facets(closed[n:])
    x=faces_from_facets(closed)
    assert x==ka|kb
    return x,ka,kb,adj

def rank_gf2(rows):
    basis={}
    for v in rows:
        while v:
            p=v.bit_length()-1
            if p in basis: v^=basis[p]
            else:
                basis[p]=v
                break
    return len(basis)

def betti_gf2(faces):
    bydim=defaultdict(list)
    for f in faces:
        if f: bydim[len(f)-1].append(tuple(sorted(f)))
    for d in bydim:bydim[d].sort()
    ranks={}
    for d in range(1,max(bydim)+1):
        index={s:i for i,s in enumerate(bydim[d-1])}
        vectors=[]
        for s in bydim[d]:
            v=0
            for j in range(len(s)):
                v^=1<<index[s[:j]+s[j+1:]]
            vectors.append(v)
        ranks[d]=rank_gf2(vectors)
    b={d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in bydim}
    b[0]-=1
    return {d:r for d,r in sorted(b.items()) if r}

def boundary_sphere(n,offset):
    vertices=set(range(offset,offset+n))
    return faces_from_facets([vertices-{v} for v in vertices])

def collapse_to_boundary(k,n,pivot_offset):
    # A cone on each facet B\{b_i} collapses to its base: all unique
    # apex-containing faces disappear in decreasing dimension.
    target=boundary_sphere(n,pivot_offset)
    existing=set(k)
    for i in range(n):
        apex=i if pivot_offset==n else n+i
        facet={pivot_offset+j for j in range(n) if j!=i}
        pivot=min(facet)
        other=sorted(facet-{pivot})
        for size in range(len(other),-1,-1):
            for sub in combinations(other,size):
                low=frozenset({apex,*sub})
                high=low|{pivot}
                assert low in existing and high in existing
                # Verify actual free face before each removal.
                containing=[s for s in existing if low<=s and len(s)>len(low)]
                assert containing==[high],(n,i,low,containing)
                existing.remove(low)
                existing.remove(high)
    assert existing==target

def checks(n):
    x,ka,kb,adj=material(n)
    inter=ka&kb
    expected_inter=faces_from_facets([{i,n+j} for i in range(n) for j in range(n) if i!=j])
    assert inter==expected_inter
    collapse_to_boundary(ka,n,n)
    collapse_to_boundary(kb,n,0)
    beta=betti_gf2(x)
    if n==2:expected={0:1}
    elif n==3:expected={1:1}
    else:
        expected={2:n*n-3*n+1}
        expected[n-2]=expected.get(n-2,0)+2
    assert beta==expected,(n,beta,expected)
    edges=sum(len(v) for v in adj.values())//2
    assert edges==n*(n-1)
    return n,len(x)-1,edges,beta

if __name__=='__main__':
    for n in range(2,9):
        a=checks(n)
        print('n=%d nonempty_faces=%d edges=%d reduced_F2_betti=%s'%(a))
    for n in range(2,7):
        x,_,_,_=material(n,False)
        assert betti_gf2(x)=={2:(n-1)**2}
        print('K_%d,%d baseline: wedge rank %d in degree 2'%(n,n,(n-1)**2))
    print('ALL_VERIFY_OK')
