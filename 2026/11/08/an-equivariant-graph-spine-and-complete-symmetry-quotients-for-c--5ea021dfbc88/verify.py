"""Finite checks of categorical complete-graph independence complexes and equivariant graph spines. Uses only Python standard library."""
from itertools import combinations, permutations
from collections import defaultdict

PRIME = 1009

def rank_mod(matrix, p=PRIME):
    if not matrix: return 0
    rows=[list(map(lambda x:x%p,r)) for r in matrix]
    h=len(rows); w=len(rows[0]); q=0
    for c in range(w):
        pivot=next((r for r in range(q,h) if rows[r][c]),None)
        if pivot is None: continue
        rows[q],rows[pivot]=rows[pivot],rows[q]
        inv=pow(rows[q][c],-1,p)
        rows[q][c:]=[(x*inv)%p for x in rows[q][c:]]
        for r in range(q+1,h):
            if rows[r][c]:
                f=rows[r][c]
                rows[r][c:]=[(x-f*y)%p for x,y in zip(rows[r][c:],rows[q][c:])]
        q+=1
        if q==h:break
    return q

def betti(cells):
    # cells by dimension, face boundary coefficients are determined by deletion of one vertex.
    ranks=[]
    for d in range(1,len(cells)):
        idx={c:i for i,c in enumerate(cells[d-1])}
        mat=[[0]*len(cells[d]) for _ in cells[d-1]]
        for j,cell in enumerate(cells[d]):
            for i in range(len(cell)):
                f=cell[:i]+cell[i+1:]
                mat[idx[f]][j]+=(-1)**i
        ranks.append(rank_mod(mat))
    return [len(cells[d])-(ranks[d-1] if d else 0)-(ranks[d] if d<len(ranks) else 0) for d in range(len(cells))]

def faces(m,n):
    points=[(i,j) for i in range(m) for j in range(n)]
    f={frozenset()}
    for i in range(m):
        row=[(i,j) for j in range(n)]
        for k in range(1,n+1):f.update(map(frozenset,combinations(row,k)))
    for j in range(n):
        col=[(i,j) for i in range(m)]
        for k in range(1,m+1):f.update(map(frozenset,combinations(col,k)))
    # verify faces are exact independent sets, without using the row-column classification in the test
    for k in range(len(points)+1):
        for c in combinations(points,k):
            ok=all(a==b or x==y for ((a,x),(b,y)) in combinations(c,2))
            assert (frozenset(c) in f)==ok,(m,n,c)
    return f

def generators(m,n,kind):
    ident=lambda i:i
    if kind=='trivial':return [(tuple(range(m)),tuple(range(n)),0)]
    if kind=='rows-cycle':return [(tuple((i+1)%m for i in range(m)),tuple(range(n)),0)]
    if kind=='cols-cycle':return [(tuple(range(m)),tuple((i+1)%n for i in range(n)),0)]
    if kind=='both-cycles':return [(tuple((i+1)%m for i in range(m)),tuple((j+1)%n for j in range(n)),0)]
    assert m==n
    if kind=='diagonal-cycle':return [(tuple((i+1)%n for i in range(n)),tuple((i+1)%n for i in range(n)),0)]
    if kind=='diagonal-symmetric':
        return [(tuple([1,0]+list(range(2,n))),tuple([1,0]+list(range(2,n))),0), (tuple((i+1)%n for i in range(n)),tuple((i+1)%n for i in range(n)),0)]
    if kind=='swap':return [(tuple(range(n)),tuple(range(n)),1)]
    if kind=='swap-diagonal':return [(tuple(range(n)),tuple(range(n)),1),(tuple((i+1)%n for i in range(n)),tuple((i+1)%n for i in range(n)),0)]
    if kind=='full':return [(tuple([1,0]+list(range(2,n))),tuple(range(n)),0),(tuple((i+1)%n for i in range(n)),tuple(range(n)),0),(tuple(range(n)),tuple(range(n)),1)]
    raise ValueError(kind)

def act_point(pt,g):
    a,b,t=g; i,j=pt
    return (a[i],b[j]) if t==0 else (b[j],a[i])

def act_object(o,g):
    ty,i,j=o; a,b,t=g
    if ty=='x':
        p=act_point((i,j),g);return ('x',*p)
    if ty=='r':return ('r',a[i],-1) if not t else ('c',a[i],-1)
    if ty=='c':return ('c',b[i],-1) if not t else ('r',b[i],-1)

def orbit_partition(items,gens,action):
    items=set(items);orbit=[];mapping={}
    while items:
        st=min(items); q=[st]; S={st}
        for v in q:
            for g in gens:
                w=action(v,g)
                if w not in S:S.add(w);q.append(w)
        assert S<=items or S<=items.union(mapping)
        orbit.append(S)
        for v in S:mapping[v]=len(orbit)-1
        items-=S
    return orbit,mapping

def graph_rank(m,n,gens):
    vertices=[('r',i,-1) for i in range(m)]+[('c',j,-1) for j in range(n)]+[('x',i,j) for i in range(m) for j in range(n)]
    edges=[tuple(sorted((('r',i,-1),('x',i,j)))) for i in range(m) for j in range(n)]+[tuple(sorted((('c',j,-1),('x',i,j)))) for i in range(m) for j in range(n)]
    vo,vm=orbit_partition(vertices,gens,act_object)
    eo,em=orbit_partition(edges,gens,lambda e,g:tuple(sorted(act_object(v,g) for v in e)))
    return len(eo)-len(vo)+1

def quotient_betti(m,n,gens,ff):
    # barycentric subdivision simplices are nested chains of nonempty original faces
    all_faces=sorted((tuple(sorted(f)) for f in ff if f),key=lambda f:(len(f),f))
    layers={}
    for face in all_faces:
        choices=[(face,)]
        for d in range(1,len(face)):
            choices.extend((c+(face,) for c in layers[d] if set(c[-1])<set(face)))
        for chain in choices:layers.setdefault(len(chain),set()).add(chain)
    # process all chains of sd(K) by rank, no inversion (vertices retain their cardinalities)
    cells=[];idmap=[]
    for d in range(1,max(layers)+1):
        orbit,mp=orbit_partition(layers[d],gens,lambda c,g:tuple(tuple(sorted(act_point(x,g) for x in face)) for face in c))
        cells.append(sorted([min(o) for o in orbit]))
        idmap.append(mp)
    # matrix using quotient simplices as oriented orbit-cells: no stabilizer reverses a chain
    rs=[]
    for d in range(1,len(cells)):
        mat=[[0]*len(cells[d]) for _ in cells[d-1]]
        for j,chain in enumerate(cells[d]):
            for i in range(len(chain)):
                f=chain[:i]+chain[i+1:]
                mat[idmap[d-1][f]][j]+=(-1)**i
        rs.append(rank_mod(mat))
    b=[len(cells[d])-(rs[d-1] if d else 0)-(rs[d] if d<len(rs) else 0) for d in range(len(cells))]
    return b,sum(len(z) for z in cells)

from fractions import Fraction

def simplex_retraction(x):
    n=len(x); b=Fraction(1,n)
    ordered=sorted(x,reverse=True)
    t=ordered[0]-ordered[1]
    if t==0:return tuple(b for _ in x)
    i=x.index(ordered[0])
    return tuple((1-t)*b+(t if j==i else 0) for j in range(n))

local_retraction_checks=0
for d in range(2,6):
    for k in range(1,8):
        for comp in __import__('itertools').product(range(k+1),repeat=d):
            if sum(comp)!=k:continue
            x=tuple(Fraction(v,k) for v in comp)
            r=simplex_retraction(x)
            assert simplex_retraction(r)==r
            assert sum(r)==1 and all(v>=0 for v in r)
            for perm in permutations(range(d)):
                xp=tuple(x[perm[j]] for j in range(d))
                rp=tuple(r[perm[j]] for j in range(d))
                assert simplex_retraction(xp)==rp
                local_retraction_checks+=1
        for i in range(d):
            for k in range(8):
                t=Fraction(k,7)
                x=tuple((1-t)*Fraction(1,d)+(t if j==i else 0) for j in range(d))
                assert simplex_retraction(x)==x
                local_retraction_checks+=1

swap_character_checks=0
for n in range(2,7):
    for g in permutations(range(n)):
        fixed=sum(i==g[i] for i in range(n))
        squared=sum(i==g[g[i]] for i in range(n))
        # Lefschetz trace of label action on K_n with edges oriented by increasing indices.
        edge_trace=sum((1 if g[i]==i and g[j]==j else -1 if g[i]==j and g[j]==i else 0)
                       for i in range(n) for j in range(i+1,n))
        hom_trace=edge_trace-fixed+1
        wedge_trace=((fixed-1)**2-(squared-1))//2
        assert hom_trace==wedge_trace,(n,g,hom_trace,wedge_trace)
        swap_character_checks+=1

checks=0; simplices=0; quotient_cells=0
for m in range(2,5):
 for n in range(2,5):
    ff=faces(m,n)
    simplices+=len(ff)-1
    # direct original complex homology
    fc=[[tuple(sorted(f)) for f in ff if len(f)==d] for d in range(1,max(map(len,ff))+1)]
    b=betti(fc)
    assert b[0]==1 and b[1]==(m-1)*(n-1) and all(x==0 for x in b[2:]),(m,n,b)
    checks+=1
    for kind in (['trivial','rows-cycle','cols-cycle','both-cycles']+(['diagonal-cycle','diagonal-symmetric','swap','swap-diagonal','full'] if m==n else [])):
        gs=generators(m,n,kind)
        bq,ct=quotient_betti(m,n,gs,ff)
        expect=graph_rank(m,n,gs)
        assert bq[:2]==[1,expect] and all(v==0 for v in bq[2:]),(m,n,kind,bq,expect)
        quotient_cells+=ct;checks+=1
        if m==n and kind=='swap':assert expect==(n-1)*(n-2)//2
        if m==n and kind=='diagonal-symmetric': assert expect==1
        if m==n and kind=='diagonal-cycle':assert expect==n-1
        if m==n and kind=='full':assert expect==0
print('ALL_VERIFY_OK', 'cases=',checks, 'independence_faces=',simplices,'barycentric_quotient_cells=',quotient_cells,'local_retraction_checks=',local_retraction_checks,'swap_character_checks=',swap_character_checks)
