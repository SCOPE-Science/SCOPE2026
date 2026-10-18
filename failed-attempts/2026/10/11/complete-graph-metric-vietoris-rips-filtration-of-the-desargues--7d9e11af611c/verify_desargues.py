#!/usr/bin/env python3
"""Exact integer, simplicial and finite topological checks for the Desargues Rips filtration.
Standalone: only the Python standard library.  No external inputs.
"""
from collections import Counter, deque
from itertools import combinations

V = tuple(range(20))

BITSETS=tuple(sum(1 << i for i in seq)
              for k in (2,3) for seq in combinations(range(5),k))

def graph():
    # Desargues point-line incidence graph: 2-subsets contained in 3-subsets.
    ad=[set() for _ in V]
    for i in V:
        for j in V:
            if i!=j and (BITSETS[i]^BITSETS[j]).bit_count()==1:
                ad[i].add(j)
    assert len(BITSETS)==20 and sum(map(len,ad))//2==30
    assert {len(x) for x in ad}=={3}
    assert all((j<10)!=(i<10) for i in V for j in ad[i])
    return ad

def all_distances(adj):
    ans = []
    for s in V:
        d={s:0};todo=deque([s])
        while todo:
            x=todo.popleft()
            for y in sorted(adj[x]):
                if y not in d:
                    d[y]=d[x]+1
                    todo.append(y)
        assert len(d)==20
        ans.append(d)
    assert max(max(z.values()) for z in ans)==5
    return ans

def all_simplices(d,r):
    nbr={i:{j for j in V if j!=i and d[i][j]<=r} for i in V}
    facets=[]
    def bronk(R,P,X):
        if not P and not X:
            facets.append(tuple(sorted(R)))
            return
        pivot=max(sorted(P|X),key=lambda v: len(P&nbr[v])) if P|X else None
        for v in sorted(P-(nbr[pivot] if pivot is not None else set())):
            bronk(R+[v],P&nbr[v],X&nbr[v])
            P.remove(v)
            X.add(v)
    bronk([],set(V),set())
    faces=set()
    for facet in facets:
        for k in range(1,len(facet)+1):
            faces.update(combinations(facet,k))
    assert all(all(d[a][b]<=r for a,b in combinations(f,2)) for f in faces)
    return faces,facets

def freestep_collapse(faces, upper_dim):
    faces=set(faces)
    history=[]
    while max(map(len,faces))-1>upper_dim:
        found=False
        highest=max(map(len,faces))
        for t in range(highest,upper_dim+1,-1):
            top=sorted(f for f in faces if len(f)==t)
            counts=Counter(y for x in top for y in combinations(x,t-1))
            for sigma in sorted(x for x in faces if len(x)==t-1 and counts[x]==1):
                tau=next(x for x in top if set(sigma).issubset(x))
                assert len([f for f in faces if set(sigma).issubset(f)])==2
                assert len(tau)==len(sigma)+1
                faces.remove(sigma)
                faces.remove(tau)
                history.append((sigma,tau))
                found=True
                break
            if found:break
        assert found, 'no certified elementary collapse available'
    return faces,history

def rank_gf2(cols):
    piv={}
    for c in cols:
        while c:
            lead=c.bit_length()-1
            if lead in piv:c^=piv[lead]
            else:piv[lead]=c;break
    return len(piv)

def gf2_betti(faces):
    by=[sorted(x for x in faces if len(x)==k) for k in range(1,max(map(len,faces))+1)]
    ranks={}
    for k in range(1,len(by)):
        lower={s:j for j,s in enumerate(by[k-1])}
        cols=[sum(1<<lower[t] for t in combinations(s,k)) for s in by[k]]
        ranks[k]=rank_gf2(cols)
    B=[len(by[k])-ranks.get(k,0)-ranks.get(k+1,0)-(k==0) for k in range(len(by))]
    return [len(x) for x in by], B

def r2_simple_connectivity(faces):
    edges={s for s in faces if len(s)==2}
    triangles=[s for s in sorted(faces) if len(s)==3]
    vertices={0};tree=set()
    while len(vertices)<20:
        possibilities=[(a,b) for a,b in sorted(edges) if (a in vertices)!=(b in vertices)]
        assert possibilities
        a,b=possibilities[0]
        tree.add((a,b))
        vertices.update((a,b))
    known=set(tree)
    rounds=0
    while True:
        new=set()
        for a,b,c in triangles:
            tri={(a,b),(a,c),(b,c)}
            if len(tri&known)>=2:new.update(tri-known)
        if not new:break
        known.update(new)
        rounds+=1
    assert known==edges, ('unreduced edge generator',len(edges-known))
    assert len(tree)==19
    return rounds,len(known),len(tree)

def integral_unit_elimination(faces):
    triangles=sorted(x for x in faces if len(x)==3)
    tetrahedra=sorted(x for x in faces if len(x)==4)
    index={f:i for i,f in enumerate(triangles)}
    # matrix columns of oriented simplicial boundary over integers
    columns={j:{index[t[:i]+t[i+1:]]:(-1)**i for i in range(4)}
             for j,t in enumerate(tetrahedra)}
    pivots=0
    while True:
        row_to_cols={}
        for j,col in columns.items():
            for row,x in col.items():
                if abs(x)==1: row_to_cols.setdefault(row,[]).append(j)
        choices=[]
        for row,js in row_to_cols.items():
            all_js=[j for j,col in columns.items() if row in col]
            for j in js:
                choices.append(((len(all_js)-1)*(len(columns[j])-1), len(all_js)+len(columns[j]),row,j))
        if not choices:break
        _,_,row,j=min(choices)
        pivot=columns.pop(j)
        u=pivot[row]
        assert abs(u)==1
        for other in columns.values():
            if row not in other:continue
            coeff=other.pop(row)*u
            for x,val in pivot.items():
                if x==row:continue
                new=other.get(x,0)-coeff*val
                if new:other[x]=new
                else:other.pop(x,None)
        pivots+=1
    nonzero=sum(bool(c) for c in columns.values())
    assert (pivots,len(columns),nonzero)==(409,1,0), (pivots,len(columns),nonzero)
    return pivots,len(columns),nonzero

def subset_metric_check(dist):
    # The graph-geodesic metric is exactly the symmetric difference metric.
    assert all(dist[i][j]==(BITSETS[i]^BITSETS[j]).bit_count()
               for i in V for j in V)
    forbidden4={(i,j) for i in V for j in V if i<j and dist[i][j]==4}
    forbidden5={(i,j) for i in V for j in V if i<j and dist[i][j]==5}
    assert len(forbidden4)==30 and len(forbidden5)==10
    assert {sum(i in pair for pair in forbidden5) for i in V}=={1}
    assert {sum(i in pair for pair in forbidden4) for i in V}=={3}
    # Explicit graph equality after complementing the triple layer:
    # within each layer Petersen disjointness, across layers identity matching.
    paired_masks=[BITSETS[i] if i<10 else (31^BITSETS[i]) for i in V]
    predicted=set()
    for i in V:
        for j in range(i+1,20):
            if (i<10)==(j<10):
                if paired_masks[i]&paired_masks[j]==0:predicted.add((i,j))
            elif paired_masks[i]==paired_masks[j]:
                predicted.add((i,j))
    assert predicted==forbidden4|forbidden5
    assert not any((i<10)!=(j<10) for i,j in forbidden4)
    assert all((i<10)!=(j<10) for i,j in forbidden5)
    return len(forbidden4),len(forbidden5)

def main():
    adj=graph();d=all_distances(adj)
    observed={r:Counter(x for row in d for x in row.values())[r]//(2 if r else 1) for r in range(6)}
    assert observed=={0:20,1:30,2:60,3:60,4:30,5:10}, observed
    f1,fac1=all_simplices(d,1)
    c1,b1=gf2_betti(f1)
    assert c1==[20,30] and b1==[0,11]
    f2,fac2=all_simplices(d,2)
    c2,b2=gf2_betti(f2)
    assert c2==[20,90,120,30] and b2==[0,0,19,0]
    core2,pairs2=freestep_collapse(f2,2)
    c2c,b2c=gf2_betti(core2)
    assert len(pairs2)==30 and c2c==[20,90,90] and b2c==[0,0,19]
    rounds,edges,tree=r2_simple_connectivity(f2)
    f3,fac3=all_simplices(d,3)
    c3,b3=gf2_betti(f3)
    assert c3==[20,150,540,1000,960,450,80] and b3==[0,0,0,1,0,0,0]
    core3,pairs3=freestep_collapse(f3,3)
    c3c,b3c=gf2_betti(core3)
    assert len(pairs3)==1040 and c3c==[20,150,540,410] and b3c==[0,0,0,1]
    pivot=integral_unit_elimination(core3)
    f4_pairs={(a,b) for a in V for b in V if a<b and d[a][b]==5}
    assert len(f4_pairs)==10 and {sum(v in p for p in f4_pairs) for v in V}=={1}
    # Thus the scale-4 flag complex is the join of 10 zero-spheres, i.e. S^9.
    f4facets=2**10
    far=subset_metric_check(d)
    print('VERIFY_OK')
    print('distance_spheres',observed)
    print('r1_fvector',c1,'h1',b1[1])
    print('r2_fvector',c2,'collapse_pairs',len(pairs2),'core',c2c,'h2',b2[2],'fundamental_triangle_rounds',rounds,'trivial_edges',edges,'tree_edges',tree)
    print('r3_fvector',c3,'maximal_facets',len(fac3),'collapse_pairs',len(pairs3),'core',c3c,'integer_unit_pivots',pivot,'h3',b3[3])
    print('r4_antipodal_pairs',len(f4_pairs),'facets',f4facets,'sphere_dimension',9,'subset_metric_far_edges',far)
    print('persistence',{'H1':[1,2,11],'H2':[2,3,19],'H3':[3,4,1],'H9':[4,5,1]})

if __name__=='__main__':main()
