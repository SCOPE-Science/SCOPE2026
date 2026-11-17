"""Exact finite checks of vertex-punctured projective incidence Rips complexes.
Requires Python >=3.9 standard library. Finite checks support but do not prove
all-parameter statements; those are proved separately by cover decompositions.
"""
from itertools import product,combinations
from collections import deque

def plane(q):
    def norm(t):
        j=next(v for v in t if v)
        inv=pow(j,-1,q)
        return tuple((x*inv)%q for x in t)
    vec=sorted({norm(v) for v in product(range(q),repeat=3) if any(v)})
    N=len(vec); assert N==q*q+q+1
    adj=[set() for _ in range(2*N)]
    for i,p in enumerate(vec):
        for j,l in enumerate(vec):
            if sum(a*b for a,b in zip(p,l))%q==0:
                adj[i].add(N+j);adj[N+j].add(i)
    assert all(len(a)==q+1 for a in adj)
    adj[0].clear()
    for a in adj: a.discard(0)
    return {v:adj[v] for v in range(1,2*N)},N

def distance_cliques(adj):
    V=sorted(adj)
    R={v:set() for v in V}
    for v in V:
        d={v:0};Q=deque([v])
        while Q:
            a=Q.popleft()
            for w in adj[a]:
                if w not in d:
                    d[w]=d[a]+1;Q.append(w)
        assert len(d)==len(V)
        R[v]={w for w in V if w!=v and d[w]<=2}
    maximal=[]
    def bk(Rset,P,X):
        if not P and not X:
            maximal.append(tuple(sorted(Rset)));return
        u=max(P|X,key=lambda a:len(P & R[a]),default=None)
        for v in sorted(P-(R[u] if u is not None else set())):
            bk(Rset|{v},P & R[v],X & R[v]);P.remove(v);X.add(v)
    bk(set(),set(V),set())
    return maximal

def faces(facets):
    f={}
    for s in facets:
        for k in range(1,len(s)+1):
            for t in combinations(s,k):
                f.setdefault(k-1,set()).add(t)
    return f

def rank_boundary(F,k):
    if k==0:return len(F[0])-1
    if k not in F:return 0
    lower={x:i for i,x in enumerate(sorted(F[k-1]))}
    piv={}
    for face in sorted(F[k]):
        col=0
        for sub in combinations(face,k):col^=1<<lower[sub]
        while col:
            bit=col.bit_length()-1
            if bit in piv:col^=piv[bit]
            else:piv[bit]=col;break
    return len(piv)

def run(q):
    adj,N=plane(q)
    facets=distance_cliques(adj)
    F=faces(facets)
    P=set(range(1,N)); L=set(range(N,2*N))
    predicted=[tuple(sorted(P))]
    through={v for v in L if v in range(N,2*N) and (q+1)==(len(adj[v])+1)}  # unused
    # Line-side maximal cliques: one line through the missing point plus all others.
    punctured_line_set={i for i in L if len(adj[i])==q}
    not_punctured=L-punctured_line_set
    predicted += [tuple(sorted(not_punctured|{i})) for i in punctured_line_set]
    predicted += [tuple(sorted({ell}|adj[ell])) for ell in L]
    predicted += [tuple(sorted({p}|adj[p])) for p in P]
    FF=faces(predicted)
    assert F==FF, 'exact face-cover classification failed'
    edges=sum(len(a) for a in adj.values())//2
    b=edges-len(adj)+1
    assert b==q**3-q
    r1=rank_boundary(F,1);r2=rank_boundary(F,2);r3=rank_boundary(F,3)
    assert len(F[1])-r1-r2==0
    beta2=len(F[2])-r2-r3
    assert beta2==q**3-q
    print('q=%d vertices=%d graph_edges=%d graph_cycles=%d faces=%s ranks_d1_d2_d3=%s beta2=%d' % (q,len(adj),edges,b,[len(F[i]) for i in sorted(F)],(r1,r2,r3),beta2))
for q in [2,3]:run(q)
print('Finite checks PASS; general theorem requires independent combinatorial proof.')
