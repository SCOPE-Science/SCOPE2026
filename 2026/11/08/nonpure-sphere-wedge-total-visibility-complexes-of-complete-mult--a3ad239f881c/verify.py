"""Independent finite validation of multipartite total mutual-visibility complexes.
Requires Python 3 standard library only. Run: python check_total_visibility.py.
"""
from itertools import product,combinations
from collections import Counter
from math import comb

def build(ns):
    part = tuple(i for i,n in enumerate(ns) for _ in range(n))
    N=len(part)
    adj=[sum((1<<v) for v in range(N) if part[v]!=part[u]) for u in range(N)]
    return part,adj

def distance(adj,start,end,forbidden):
    seen=1<<start
    front=seen
    d=0
    while front:
        if front & (1<<end):return d
        nxt=0
        for u in range(len(adj)):
            if front>>u&1:nxt |= adj[u]
        nxt &= ~(seen|forbidden)
        seen|=nxt
        front=nxt
        d+=1
    return None

def total_by_paths(adj,mask):
    N=len(adj)
    for u in range(N):
        for v in range(u+1,N):
            if distance(adj,u,v,mask & ~((1<<u)|(1<<v))) != distance(adj,u,v,0):
                return False
    return True

def theorem(part,mask):
    C=[v for v in range(len(part)) if not (mask>>v&1)]
    ns=Counter(part)
    return all(any(part[v]!=i for v in C) for i,n in ns.items() if n>=2)

def polynomial(ns):
    N=sum(ns);big=[n for n in ns if n>=2];a=len(big);b=len(ns)-a
    if not a:
        F=[comb(N,k) for k in range(N+1)]
        M={N:1}
    else:
        F=[comb(N,k) for k in range(N+1)]
        for n in big:
            for j in range(n+1):F[N-n+j]-=comb(n,j)
        F[N]+=a-1
        M={}
        if b: M[N-1]=b
        e2=sum(x*y for i,x in enumerate(big) for y in big[i+1:])
        if e2:M[N-2]=e2
    return F,M

def rank2(columns):
    piv={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;break
    return len(piv)

def betti_mod2(feasible,N):
    faces={d:[] for d in range(-1,N)}
    for mask in feasible:
        if mask:faces[mask.bit_count()-1].append(mask)
    ranks={}
    for d in range(1,N):
        rows={f:i for i,f in enumerate(faces[d-1])}
        cols=[]
        for f in faces[d]:
            x=0
            for bit in range(N):
                if f>>bit&1:x^=1<<rows[f^(1<<bit)]
            cols.append(x)
        ranks[d]=rank2(cols)
    return {d:val for d in range(N) if (val:=len(faces[d])-ranks.get(d,0)-ranks.get(d+1,0)-(d==0))}

def run():
    profiles=[ns for k in range(2,5) for ns in product(range(1,4),repeat=k) if sum(ns)<=8]
    profiles+= [(2,2,2,1),(3,3,1,1),(2,2,2,2)]
    masks=0; facets=0; homology=0;exchange=0
    for ns in profiles:
        part,adj=build(ns);N=len(part)
        feasible=[]
        for mask in range(1<<N):
            a=total_by_paths(adj,mask)
            assert a==theorem(part,mask),(ns,mask,a)
            if a:feasible.append(mask)
            masks+=1
        fpoly,mpoly=polynomial(ns)
        got=[0]*(N+1)
        for mask in feasible:got[mask.bit_count()]+=1
        assert got==fpoly,(ns,got,fpoly)
        good=set(feasible)
        mf=[mask for mask in good if all((mask>>v&1) or (mask|(1<<v)) not in good for v in range(N))]
        counts=Counter(m.bit_count() for m in mf)
        assert counts==Counter(mpoly),(ns,counts,mpoly)
        facets+=len(mf)
        big=sum(n>=2 for n in ns)
        if N<=7:
            B=betti_mod2(feasible,N)
            expected={} if big<=1 else {N-3:big-1}
            assert B==expected,(ns,B,expected)
            homology+=1
        if all(n>=2 for n in ns):
            bases=set(mf)
            for a,b in product(bases,repeat=2):
                for u in range(N):
                    if a>>u&1 and not b>>u&1:
                        assert any((a^(1<<u)^(1<<v)) in bases for v in range(N) if b>>v&1 and not a>>v&1),(ns,a,b,u)
                        exchange+=1
    print(f'VERIFY_OK profiles={len(profiles)} subsets={masks} facets={facets} direct_BFS=PASS face_polynomials=PASS maximal_facets=PASS matroid_basis_exchange={exchange} homology_mod2_cases={homology} PASS')
if __name__=='__main__':run()
