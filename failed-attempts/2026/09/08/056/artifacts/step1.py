"""Count labeled dim<=2 complexes on 6 vertices; Betti fn; test examples."""
import numpy as np, itertools, json
N=6
EDGES=[(i,j) for i in range(N) for j in range(i+1,N)]
EIDX={e:k for k,e in enumerate(EDGES)}
TRIS=list(itertools.combinations(range(N),3))
T_OK=np.array([[EIDX[(t[i],t[j])] for i in range(3) for j in range(i+1,3)] for t in TRIS])

def betti_rank(faces2_mask, emask):
    # faces2_mask: 20-bit, emask: 15-bit; assume compatible+downward closed
    E=[EDGES[e] for e in range(15) if (emask>>e)&1]
    elook={e:k for k,e in enumerate(E)}
    T=[TRIS[t] for t in range(20) if (faces2_mask>>t)&1]
    b=1
    for J in range(1,64):
        V=[i for i in range(N) if (J>>i)&1]
        EJ=[e for e in E if ((J>>e[0])&1) and ((J>>e[1])&1)]
        jlook={e:k for k,e in enumerate(EJ)}
        TJ=[t for t in T if all((J>>v)&1 for v in t)]
        k=len(V); e=len(EJ); t=len(TJ)
        # comp via union find
        p=list(range(N))
        def f(a):
            while p[a]!=a: p[a]=p[p[a]]; a=p[a]
            return a
        for (a,c) in EJ:
            ra,rc=f(a),f(c)
            if ra!=rc: p[ra]=rc
        comp=len(set(f(v) for v in V))
        r=0
        if t and e:
            import numpy as np
            M=np.zeros((e,t))
            for j,(a,c,d) in enumerate(TJ):
                for (uv,s) in [((a,c),1),((a,d),-1),((c,d),1)]:
                    (u,v)=uv
                    x,y=(u,v) if u<v else (v,u)
                    M[jlook[(x,y)],j]=s
            r=int(np.linalg.matrix_rank(M))
        b+=(comp-1)+(e-k+comp-r)+(t-r)
    return b

# examples
K6=(1<<15)-1
print("K6 graph b:",betti_rank(0,K6))  # expect 112
print("6 points b:",betti_rank(0,0))   # expect 130
# octahedron: vertices 0..5, antipodal pairs (0,1),(2,3),(4,5) missing edges; 8 triangles avoiding antipodal
OCT_E=K6
for (a,c) in [(0,1),(2,3),(4,5)]: OCT_E&=~(1<<EIDX[(a,c) if a<c else (c,a)])
OCT_T=0
for ti,t in enumerate(TRIS):
    if all((OCT_E>>EIDX[(min(a,c),max(a,c))])&1 for a in t for c in t if a<c):
        # all three pairs antipodal-free?
        if not any(set([a,c])=={0,1} or set([a,c])=={2,3} or set([a,c])=={4,5} for a in t for c in t if a!=c):
            OCT_T|=1<<ti
print("oct edges:",bin(OCT_E).count('1'),"tris:",bin(OCT_T).count('1'))
print("octahedron S2 b:",betti_rank(OCT_T,OCT_E))
# cone on C6 (disk): apex 0 + cycle 1..5
cyc=[(1,2),(2,3),(3,4),(4,5),(5,1)]
CE=0
for (a,c) in cyc+[(0,v) for v in range(1,6)]: CE|=1<<EIDX[(min(a,c),max(a,c))]
CT=0
for ti,(a,c,d) in enumerate(TRIS):
    s=set([a,c,d])
    if 0 in s:
        rest=tuple(sorted(s-{0}))
        if rest in [(1,2),(2,3),(3,4),(4,5),(1,5)]: CT|=1<<ti
print("cone-disk b:",betti_rank(CT,CE))
# count complexes
NG=1<<15
G=((np.arange(NG)[:,None]>>np.arange(15))&1)
TPRES=(G[:,T_OK[:,:,0]]&G[:,T_OK[:,:,1]]&G[:,T_OK[:,:,2]])  # NG x 20 x 3 -> need all three
TPRES=(G[:,T_OK[:,:,0]]*G[:,T_OK[:,:,1]]*G[:,T_OK[:,:,2]])
tcount=TPRES.sum(axis=1)
import math
tot=0
for v in np.unique(tcount):
    tot+=int((tcount==v).sum())*(1<<int(v))
print("total labeled dim<=2 complexes:",tot)
print("tcount histogram:",{int(v):int((tcount==v).sum()) for v in sorted(set(tcount.tolist()))[:12]})
