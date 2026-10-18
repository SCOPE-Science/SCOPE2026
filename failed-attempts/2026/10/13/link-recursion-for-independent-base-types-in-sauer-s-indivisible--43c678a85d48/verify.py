from itertools import combinations


def active(edges):
    v=set()
    for e in edges:
        v.update(e)
    return v


def irreducible(vertices, edges):
    V=set(vertices)
    if len(V)<=1:
        return True
    for a,b in combinations(sorted(V),2):
        if not any(e <= V and a in e and b in e for e in edges):
            return False
    return True


def omega(edges):
    V=active(edges)
    if not V:
        return 0
    ans=1
    for r in range(2,len(V)+1):
        for S in combinations(sorted(V),r):
            if irreducible(S,edges):
                ans=max(ans,r)
    return ans


def all_hypergraphs(m,r):
    E=[frozenset(c) for c in combinations(range(m),r)]
    for mask in range(1<<len(E)):
        yield {E[i] for i in range(len(E)) if (mask>>i)&1}


def cone(L,m):
    x=m
    return {frozenset(set(e)|{x}) for e in L}


def has_large_irreducible(edges,n):
    V=active(edges)
    if len(V)<n:
        return False
    for r in range(n,len(V)+1):
        for S in combinations(sorted(V),r):
            if irreducible(S,edges):
                return True
    return False

checks=0
# The cone over a (k-1)-graph has a forbidden irreducible set of size >= n
# exactly when its link has an irreducible set of size >= n-1.
for k,n,mmax in [(3,4,6),(3,5,5),(4,5,5),(4,6,5)]:
    for m in range(k-1,mmax+1):
        for L in all_hypergraphs(m,k-1):
            cone_bad=has_large_irreducible(cone(L,m),n)
            link_bad=omega(L)>=n-1
            assert cone_bad==link_bad,(k,n,m,L)
            checks+=1

# For k=3 the legal links are exactly K_{n-1}-free labeled graphs.
def clique_number(G,m):
    if not G:
        return 1 if m else 0
    ans=2
    for r in range(3,m+1):
        for S in combinations(range(m),r):
            if all(frozenset(e) in G for e in combinations(S,2)):
                ans=r
    return ans

triangle_free_counts=[1,1,2,7,41,388,5789]
for n,mmax in [(4,6),(5,5),(6,5)]:
    for m in range(mmax+1):
        legal=0
        for G in all_hypergraphs(m,2):
            cone_ok=not has_large_irreducible(cone(G,m),n)
            krfree=clique_number(G,m)<n-1
            assert cone_ok==krfree
            checks+=1
            legal+=int(cone_ok)
        if n==4:
            assert legal==triangle_free_counts[m],(m,legal,triangle_free_counts[m])
            checks+=1

print(f"VERIFY_OK {checks} exact assertions")
