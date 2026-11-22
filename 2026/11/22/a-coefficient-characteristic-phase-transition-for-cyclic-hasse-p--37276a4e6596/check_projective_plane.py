"""Standalone checks for a six-vertex projective-plane triangulation and cyclic Hasse degree-one path cohomology."""
from itertools import combinations
from collections import defaultdict
TRIANGLES=((0,1,2),(0,1,3),(0,2,4),(0,3,5),(0,4,5),
           (1,2,5),(1,3,4),(1,4,5),(2,3,4),(2,3,5))
EDGES=tuple(combinations(range(6),2))
CELLS=tuple((0,(i,)) for i in range(6))+tuple((1,e) for e in EDGES)+tuple((2,t) for t in TRIANGLES)
INDEX={c:i for i,c in enumerate(CELLS)}
ARROWS=[]
for i,(dim,face) in enumerate(CELLS):
    if dim==0: ARROWS += [(i,INDEX[(1,e)]) for e in EDGES if face[0] in e]
    if dim==1: ARROWS += [(i,INDEX[(2,t)]) for t in TRIANGLES if set(face).issubset(t)]
    if dim==2: ARROWS += [(i,INDEX[(0,(v,))]) for v in range(6)]
OUT=defaultdict(list); IN=defaultdict(list)
for a,b in ARROWS: OUT[a].append(b); IN[b].append(a)


def rank_sparse(cols,p):
    piv={}
    for co in cols:
        col={i:v%p for i,v in co.items() if v%p}
        while col:
            key=min(col)
            if key not in piv:
                z=pow(col[key],-1,p)
                piv[key]={r:v*z%p for r,v in col.items() if v*z%p}
                break
            fac=col[key]
            for r,v in piv[key].items():
                vv=(col.get(r,0)-fac*v)%p
                if vv: col[r]=vv
                elif r in col: del col[r]
    return len(piv)


def simplicial_betti(p):
    b1=[]
    for e in EDGES: b1.append({e[0]:-1,e[1]:1})
    edge_id={e:i for i,e in enumerate(EDGES)}
    b2=[]
    for t in TRIANGLES:
        a,b,c=t
        b2.append({edge_id[(b,c)]:1,edge_id[(a,c)]:-1,edge_id[(a,b)]:1})
    r1=rank_sparse(b1,p);r2=rank_sparse(b2,p)
    return (6-r1,15-r1-r2,10-r2), (r1,r2)


def path_betti1(p):
    twopath=[(a,b,c) for (a,b) in ARROWS for c in OUT[b]]
    paired=defaultdict(list)
    for j,(a,b,c) in enumerate(twopath): paired[(a,c)].append(j)
    # Direct arrows forbidden at path length 2 by cyclic rank mod 3.
    assert not set(paired).intersection(ARROWS)
    selected={t:i for i,t in enumerate((j for js in paired.values() for j in js[:-1]))}
    id_twopath={t:i for i,t in enumerate(twopath)}
    # Each relation is the sum of 2-paths with a fixed ordered pair of endpoints.
    # Coordinates of last path are replaced by minus sum of the other paths.
    def reduced_terms(co):
        out=defaultdict(int)
        for j,v in co.items():
            a,b,c=twopath[j]; group=paired[(a,c)]
            if j==group[-1]:
                for k in group[:-1]: out[selected[k]]-=v
            else:out[selected[j]]+=v
        return dict(out)
    cob1=[]
    for a,b in ARROWS:
        co=defaultdict(int)
        for u in IN[a]:co[id_twopath[(u,a,b)]]+=1
        for w in OUT[b]:co[id_twopath[(a,b,w)]]+=1
        cob1.append(reduced_terms(co))
    r1=rank_sparse(cob1,p)
    # degree zero coboundary of a connected graph has rank number of vertices minus one
    r0=30
    return (len(ARROWS)-r1-r0),r1,len(twopath),len(selected)

if __name__=='__main__':
    assert len(CELLS)==31 and len(ARROWS)==120
    assert all(sum(e in tuple(combinations(t,2)) for t in TRIANGLES)==2 for e in EDGES)
    for v in range(6):
        adj={w:set() for w in range(6) if w!=v}
        for t in TRIANGLES:
            if v in t:
                a,b=(x for x in t if x!=v)
                adj[a].add(b);adj[b].add(a)
        seen={next(iter(adj))}
        for _ in range(5):
            seen.update(z for w in tuple(seen) for z in adj[w])
        assert len(seen)==5 and all(len(z)==2 for z in adj.values())
    assert (6-15+10)==1
    for p in (2,3,5):
        simplicial,ranks=simplicial_betti(p)
        b1,rankd1,npaths,nq=path_betti1(p)
        print('prime',p,'ordinary_cohomology_ranks',simplicial,'boundary_ranks',ranks,
              'cyclic_hasse_H1',b1,'d1_rank',rankd1,'two_paths',npaths,'quotient_dim2',nq)
        assert b1==1
        assert simplicial==((1,1,1) if p==2 else (1,0,0))
    print('PASS')
