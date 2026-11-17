#!/usr/bin/env python3
"""Exact integer certificates for a four-row bounded-rook complex.

Pure standard-library executable; run: python3 verify.py
Row-major vertex i*m+j, zero-based row and column labels.
"""
import itertools, collections, functools, math, json
R,C=4,5
N=R*C

def faces_for_columns(m):
    out={0}
    for k in range(1,m+1):
        for cols in itertools.combinations(range(m),k):
            for rows in itertools.product(range(R),repeat=k):
                if max(rows.count(r) for r in range(R))<=2:
                    out.add(sum(1<<(r*m+c) for r,c in zip(rows,cols)))
    return out

def facets(mask):
    return [(mask^(1<<v),(-1)**i) for i,v in enumerate(v for v in range(N) if mask>>v&1)]

def matching(m,F):
    order=[r*m+c for c in range(m) for r in range(R)]
    left=set(F);pairs=[];partner={}
    for v in order:
        for a in sorted(left,key=lambda x:(x.bit_count(),x)):
            b=a|(1<<v)
            if a in left and not (a>>v&1) and b in left:
                left.remove(a);left.remove(b)
                partner[a]=b;partner[b]=a;pairs.append((a,b))
    indeg={x:0 for x in F}; adj={x:[] for x in F};E=0
    for b in F:
        for i,v in enumerate(x for x in range(R*m) if b>>x&1):
            a=b^(1<<v)
            x,y=(a,b) if partner.get(a)==b else (b,a)
            adj[x].append(y);indeg[y]+=1;E+=1
    q=collections.deque(x for x in F if indeg[x]==0);visited=0
    while q:
        x=q.popleft();visited+=1
        for y in adj[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    assert visited==len(F),('cyclic matching',visited,len(F))
    return pairs,left,partner,E,visited

F=faces_for_columns(C)
assert F=={m for m in range(1<<N) if m.bit_count()<=C and all(sum((m>>(r*C+c))&1 for c in range(C))<=2 for r in range(R)) and all(sum((m>>(r*C+c))&1 for r in range(R))<=1 for c in range(C))}
assert len(F)==2401
count=[sum(f.bit_count()==i for f in F) for i in range(C+1)]
assert count==[1,20,160,600,1020,600]
pairs,critical,partner,E,visited=matching(C,F)
assert len(pairs)==1178 and E==9220 and len(critical)==45
crit3=sorted(f for f in critical if f.bit_count()==4)
crit4=sorted(f for f in critical if f.bit_count()==5)
assert len(crit3)==3 and len(crit4)==42 and len(critical)==45

low4={a:b for a,b in pairs if a.bit_count()==4}
@functools.lru_cache(None)
def reduce3(face):
    if face not in low4:return {face:1}
    fac=dict(facets(low4[face]));p=fac[face]
    d=collections.Counter()
    for f,co in fac.items():
        if f==face:continue
        for x,v in reduce3(f).items():d[x]-=p*co*v
    return {x:v for x,v in d.items() if v}
M=[]
for top in crit4:
    row=collections.Counter()
    for f,sign in facets(top):
        for x,v in reduce3(f).items():row[x]+=sign*v
    M.append([row[x] for x in crit3])
assert len(M)==42 and all(v==0 for row in M for v in row)

low2={a:b for a,b in pairs if a.bit_count()==3}
@functools.lru_cache(None)
def fill2(face):
    upper=low2[face];fac=dict(facets(upper));p=fac[face]
    d=collections.Counter({upper:p})
    for t,co in fac.items():
        if t!=face and t in low2:
            for x,v in fill2(t).items():d[x]-=p*co*v
    return {x:v for x,v in d.items() if v}
cycles=[]
for critical_face in crit3:
    d=collections.Counter({critical_face:1})
    for face,co in facets(critical_face):
        if face in low2:
            for x,v in fill2(face).items():d[x]-=co*v
    d={x:v for x,v in d.items() if v}
    bd=collections.Counter()
    for x,v in d.items():
        for t,co in facets(x):bd[t]+=co*v
    assert all(z==0 for z in bd.values()),'three-cycle boundary nonzero'
    cycles.append(d)

def image(mask,rr,cc):
    old=[v for v in range(N) if mask>>v&1]
    new=[rr[i]*C+cc[j] for v in old for i,j in [divmod(v,C)]]
    inversions=sum(a>b for i,a in enumerate(new) for b in new[i+1:])
    return sum(1<<v for v in new),(-1)**inversions

def projected(c):
    d=collections.Counter()
    for x,v in c.items():
        for y,w in reduce3(x).items():
            if y in crit3:d[y]+=v*w
    return tuple(d[x] for x in crit3)
for k,z in enumerate(cycles):
    assert projected(z)==tuple(int(j==k) for j in range(3))

def actcycle(z,rr,cc):
    d=collections.Counter()
    for f,v in z.items():
        y,sign=image(f,rr,cc);d[y]+=v*sign
    return projected(d)

def mat_times(A,v):return tuple(sum(A[i][j]*v[j] for j in range(3)) for i in range(3))

row_matrices={}
for rr in itertools.permutations(range(R)):
    columns=[actcycle(z,rr,tuple(range(C))) for z in cycles]
    row_matrices[rr]=tuple(tuple(columns[j][i] for j in range(3)) for i in range(3))
assert len({mat for mat in row_matrices.values()})==6
pairing_basis=[(-1,1,0),(0,-1,0),(0,1,-1)]
assert abs((pairing_basis[0][0]*(pairing_basis[1][1]*pairing_basis[2][2]-pairing_basis[1][2]*pairing_basis[2][1])-pairing_basis[0][1]*(pairing_basis[1][0]*pairing_basis[2][2]-pairing_basis[1][2]*pairing_basis[2][0])+pairing_basis[0][2]*(pairing_basis[1][0]*pairing_basis[2][1]-pairing_basis[1][1]*pairing_basis[2][0])))==1
pairings=[((0,2),(1,3)),((0,3),(1,2)),((0,1),(2,3))]
canon=lambda p:tuple(sorted(tuple(sorted(pair)) for pair in p))
for rr,A in row_matrices.items():
    for j,v in enumerate(pairing_basis):
        transformed=mat_times(A,v)
        assert transformed in pairing_basis
        assert canon(pairings[pairing_basis.index(transformed)])==canon(tuple(tuple(rr[r] for r in pair) for pair in pairings[j]))
for cc in itertools.permutations(range(C)):
    sg=(-1)**sum(cc[i]>cc[j] for i in range(C) for j in range(i+1,C))
    for j,z in enumerate(cycles):
        assert actcycle(z,tuple(range(R)),cc)==tuple(sg*int(i==j) for i in range(3))

# Independent mod-2 boundary-rank calculation on directly enumerated simplices.
bycount=[sorted(x for x in F if x.bit_count()==k) for k in range(6)]
ranks=[0]
for k in range(1,6):
    lower={face:j for j,face in enumerate(bycount[k-1])}
    basis={}
    for top in bycount[k]:
        val=0
        for face,_ in facets(top):val^=1<<lower[face]
        while val:
            p=val.bit_length()-1
            if p in basis:val^=basis[p]
            else:basis[p]=val;break
    ranks.append(len(basis))
assert ranks==[0,1,19,141,459,558]
red_betti=[len(bycount[k])-ranks[k]-(ranks[k+1] if k+1<len(ranks) else 0) for k in range(6)]
assert red_betti==[0,0,0,0,3,42]

# Full rational character in degrees 3 and 4, via signed simplicial Lefschetz.
def partitions(n,top=None):
    if n==0:yield ();return
    top=n if top is None else top
    for a in range(min(n,top),0,-1):
        for q in partitions(n-a,a):yield (a,)+q

def representative(parts):
    p=[];offset=0
    for k in parts:
        p.extend([offset+(j+1)%k for j in range(k)]);offset+=k
    return tuple(p)

def fixed_pairings(rr):
    all_p=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
    return sum(canon(tuple(tuple(rr[i] for i in a) for a in p))==canon(p) for p in all_p)

def lefschetz(rr,cc):
    s=0
    for f in F:
        mapped,sg=image(f,rr,cc)
        if f==mapped:s+=(-1 if not f else ((-1)**(f.bit_count()-1))*sg)
    return s
rowparts=list(partitions(4));colparts=list(partitions(5))
char3=[];char4=[]
for a in rowparts:
    r=representative(a);row3=[];row4=[]
    for b in colparts:
        c=representative(b);sg=(-1)**(5-len(b))
        h3=sg*fixed_pairings(r)
        row3.append(h3);row4.append(h3+lefschetz(r,c))
    char3.append(row3);char4.append(row4)
assert char4[-1][-1]==42 and char3[-1][-1]==3

def class_size(p):
    ct=collections.Counter(p)
    return math.factorial(sum(p))//math.prod(i**v*math.factorial(v) for i,v in ct.items())
@functools.lru_cache(None)
def chi(lam,mu):
    if not mu:return int(not lam)
    old={(i,j) for i,v in enumerate(lam) for j in range(v)}
    ans=0
    for nu in partitions(sum(lam)-mu[0]):
        if any(nu[i]>(lam[i] if i<len(lam) else 0) for i in range(len(nu))):continue
        remaining={(i,j) for i,v in enumerate(nu) for j in range(v)}
        shape=old-remaining
        if len(shape)!=mu[0]:continue
        visited={next(iter(shape))};stack=list(visited)
        while stack:
            i,j=stack.pop()
            for point in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if point in shape and point not in visited:visited.add(point);stack.append(point)
        if visited!=shape:continue
        if any({(i,j),(i+1,j),(i,j+1),(i+1,j+1)}<=shape for i,j in shape):continue
        ans+=(-1)**(len({i for i,j in shape})-1)*chi(nu,mu[1:])
    return ans
for n,P in [(4,rowparts),(5,colparts)]:
    assert all(sum(class_size(p)*chi(a,p)*chi(b,p) for p in P)==math.factorial(n)*int(a==b) for a in P for b in P)
mult={}
for a in rowparts:
    for b in colparts:
        s=sum(class_size(r)*class_size(c)*char4[i][j]*chi(a,r)*chi(b,c) for i,r in enumerate(rowparts) for j,c in enumerate(colparts))
        assert s%2880==0
        v=s//2880
        assert v>=0
        if v:mult[f'{a}|{b}']=v
assert mult=={'(3, 1)|(3, 2)':1,'(2, 2)|(3, 1, 1)':1,'(2, 1, 1)|(2, 2, 1)':1}

small=[]
for m in range(1,5):
    fm=faces_for_columns(m)
    pm,cm,_,_,_=matching(m,fm)
    d=collections.Counter(x.bit_count()-1 for x in cm)
    assert d=={m-1:[3,9,23,45][m-1]},(m,d)
    small.append({'columns':m,'wedge_dimension':m-1,'wedge_rank':[3,9,23,45][m-1]})

out={'status':'PASS','rows':4,'columns':5,'row_capacities':[2,2,2,2],
 'face_counts_by_cardinality':count,'matched_pairs':len(pairs),'hasse_edges':E,
 'acyclic_vertices_checked':visited,'critical_three_cell_masks':crit3,
 'critical_four_cell_masks':crit4,'morse_zero_attaching_coefficients':len(M)*3,
 'reduced_mod_two_betti_dimensions_0_to_4':red_betti[1:],'mod_two_boundary_ranks_augmented':ranks[1:],
 'integral_three_cycle_support_sizes':[len(c) for c in cycles],
 'integral_permutation_basis_coordinates':pairing_basis,
 'integral_basis_pairings':[str(p) for p in pairings],
 'row_group_elements_checked':24,'column_group_elements_checked':120,
 'row_cycle_types':[list(p) for p in rowparts],'column_cycle_types':[list(p) for p in colparts],
 'third_homology_character_table':char3,'fourth_homology_character_table':char4,
 'fourth_rational_specht_multiplicities':mult,'earlier_column_wedges':small}
print(json.dumps(out,ensure_ascii=False,sort_keys=True,separators=(',',':')))
