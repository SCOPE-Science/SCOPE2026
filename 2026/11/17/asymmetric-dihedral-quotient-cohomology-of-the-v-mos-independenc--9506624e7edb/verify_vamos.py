#!/usr/bin/env python3
"""Exact combinatorial checks for the Vámos independence-complex character."""
import itertools
from collections import Counter

E = tuple(range(8))
BADS = {frozenset(t) for t in ((0,1,2,3),(0,1,4,5),
        (6,7,2,3),(6,7,4,5),(2,3,4,5))}
ID = E
A = (1,0,2,3,4,5,6,7)
B = (6,7,2,3,4,5,0,1)
C = (0,1,3,2,4,5,6,7)
D = (0,1,4,5,2,3,6,7)

def compose(p,q): return tuple(p[q[i]] for i in E)

def subgroup(gens):
    reached = {ID}; queue = [ID]
    for p in queue:
        for g in gens:
            v = compose(p,g)
            if v not in reached:
                reached.add(v);queue.append(v)
    return queue

G1, G2, G = subgroup([A,B]), subgroup([C,D]), subgroup([A,B,C,D])
assert len(G1)==len(G2)==8 and len(G)==64
assert set(G)=={p for p in itertools.permutations(E)
                if {frozenset(p[i] for i in f) for f in BADS}==BADS}
assert {sum(t in f for f in BADS) for t in E}=={2,3}
FACES={k:list(itertools.combinations(E,k)) for k in range(1,4)}
FACES[4]=[f for f in itertools.combinations(E,4) if frozenset(f) not in BADS]
assert [len(FACES[k]) for k in range(1,5)]==[8,28,56,65]
# Rank-four matroid basis-exchange axioms checked exhaustively.
BASES=[set(f) for f in FACES[4]]
for x in BASES:
    for y in BASES:
        for i in x-y:
            assert any((x-{i})|{j} in BASES for j in y-x)

def parity(xs):
    return -1 if sum(xs[i]>xs[j] for i in range(len(xs))
            for j in range(i+1,len(xs)))%2 else 1

def trace_on(p,faces):
    return sum(parity([p[i] for i in s]) for s in faces
               if {p[i] for i in s}==set(s))

def chi_lefschetz(p):
    return 1-sum((-1)**(k-1)*trace_on(p,FACES[k]) for k in range(1,5))

def lengths(p):
    seen=set(); answer=[]
    for i in E:
        if i in seen:continue
        length=0; j=i
        while j not in seen:
            seen.add(j);length+=1;j=p[j]
        answer.append(length)
    return answer

def exterior_four_std(p):
    # det(I+t P_8)/(1+t), coefficient t^4.
    v=[1,0,0,0,0]
    for ell in lengths(p):
        w=v[:]
        for k in range(ell,5):
            w[k]-=(-1)**ell*v[k-ell]
        v=w
    q=[1]
    for k in range(1,5): q.append(v[k]-q[-1])
    return q[4]

def chi_relative(p):
    return exterior_four_std(p)-trace_on(p,[tuple(sorted(f)) for f in BADS])

assert all(chi_lefschetz(g)==chi_relative(g) for g in G)
assert chi_relative(ID)==30

# Exact D4xD4 characters; generators are two reflections with product order 4.
IRREPS=((1,1),(1,-1),(-1,1),(-1,-1),None)

def char_1d(g,gens,eps):
    h,j=gens; seen={ID:1}; queue=[ID]
    for x in queue:
        for gen,sgn in ((h,eps[0]),(j,eps[1])):
            y=compose(x,gen)
            if y not in seen:seen[y]=seen[x]*sgn;queue.append(y)
            assert seen[y]==seen[x]*sgn
    return seen[g]

def char_d4(g,gens,typ):
    if typ is not None:return char_1d(g,gens,typ)
    r=compose(*gens);r2=compose(r,r)
    return 2 if g==ID else (-2 if g==r2 else 0)

DECOMP=[]
for i,xi in enumerate(IRREPS):
    row=[]
    for j,xj in enumerate(IRREPS):
        s=sum(chi_relative(compose(x,y))*char_d4(x,(A,B),xi)
              *char_d4(y,(C,D),xj) for x in G1 for y in G2)
        assert s%64==0
        row.append(s//64)
    DECOMP.append(row)
assert DECOMP==[[0,0,0,0,0],[0,0,1,1,1],[1,1,0,0,1],
                 [0,1,0,1,2],[0,1,1,2,2]]
assert sum(DECOMP[i][j]*(2 if i==4 else 1)*(2 if j==4 else 1)
           for i in range(5) for j in range(5))==30

# Independent boundary calculation over three primes.
def rank_mod(matrix, p):
    if not matrix:return 0
    m=[row[:] for row in matrix];rank=0;cols=len(m[0])
    for col in range(cols):
        pivot=next((i for i in range(rank,len(m)) if m[i][col]%p),None)
        if pivot is None:continue
        m[rank],m[pivot]=m[pivot],m[rank]
        z=pow(m[rank][col]%p,-1,p)
        for j in range(col,cols):m[rank][j]=(m[rank][j]*z)%p
        for i in range(rank+1,len(m)):
            z=m[i][col]%p
            if z:
                for j in range(col,cols):m[i][j]=(m[i][j]-z*m[rank][j])%p
        rank+=1
    return rank

def boundary_matrix(k):
    if k==1:return [[1]*len(FACES[1])]
    dest={s:i for i,s in enumerate(FACES[k-1])}
    mat=[[0]*len(FACES[k]) for _ in dest]
    for j,s in enumerate(FACES[k]):
        for q in range(k):mat[dest[s[:q]+s[q+1:]]][j]=(-1)**q
    return mat

for prime in (2,3,101):
    ranks=[rank_mod(boundary_matrix(k),prime) for k in range(1,5)]
    assert ranks==[1,7,21,35],(prime,ranks)

# A second calculation of quotient homology via invariant oriented chain orbits.
def invariant_basis(k,H):
    faces=FACES[k]; face_set=set(faces);remaining=face_set.copy()
    out=[]
    while remaining:
        rep=min(remaining);coeff={};consistent=True
        for g in H:
            moved=tuple(sorted(g[i] for i in rep)); sg=parity([g[i] for i in rep])
            if moved in coeff and coeff[moved]!=sg:consistent=False
            coeff[moved]=sg
        remaining-=set(coeff)
        if consistent:out.append((rep,coeff))
    return out

def invariants_betti(H):
    bases={k:invariant_basis(k,H) for k in range(1,5)}
    ranks=[]
    for k in (1,2,3,4):
        if k==1:
            mat=[[sum(coeff.values()) for _,coeff in bases[1]]]
        else:
            lower={rep:i for i,(rep,_) in enumerate(bases[k-1])}
            mat=[[0]*len(bases[k]) for _ in lower]
            for j,(_,coeff) in enumerate(bases[k]):
                for s,scalar in coeff.items():
                    for t in range(k):
                        face=s[:t]+s[t+1:]
                        if face in lower:mat[lower[face]][j]+=scalar*(-1)**t
        ranks.append(rank_mod(mat,101))
    dims=[len(bases[k]) for k in range(1,5)]
    assert dims[0]-ranks[0]-ranks[1]==0
    assert dims[1]-ranks[1]-ranks[2]==0
    assert dims[2]-ranks[2]-ranks[3]==0
    return dims[3]-ranks[3]

assert [invariants_betti(H) for H in (G1,G2,G)]==[0,1,0]
assert [sum(chi_relative(g) for g in H)//len(H) for H in (G1,G2,G)]==[0,1,0]
R1=compose(A,B); R2=compose(C,D)
reps1=(ID,compose(R1,R1),R1,A,B)
reps2=(ID,compose(R2,R2),R2,C,D)
character_table=[[chi_relative(compose(x,y)) for y in reps2] for x in reps1]
assert character_table==[[30,-2,0,-4,-6],[-2,-2,0,4,2],[-2,-2,0,0,-2],[-6,2,0,-4,2],[-6,2,0,4,2]]
print('VAMOS_MATROID_BASIS_EXCHANGE_PASS')
print('AUTOMORPHISM_GROUP_ORDER=64; DIHEDRAL_FACTORS=8x8')
print('FACE_VECTOR=8,28,56,65; BOUNDARY_RANKS=1,7,21,35; TOP_HOMOLOGY_RANK=30')
print('CHARACTER_AGREEMENT_ALL_64_PASS; CLASS_MATRIX:')
for row in character_table:print(','.join(map(str,row)))
print('IRREDUCIBLE_MULTIPLICITY_MATRIX:')
for row in DECOMP:print(','.join(map(str,row)))
print('INVARIANT_CHAIN_QUOTIENT_BETTI_3=0,1,0 (LOW-INCIDENCE,HIGH-INCIDENCE,FULL)')
print('VAMOS_CANONICAL_DIHEDRAL_QUOTIENTS_PASS')
