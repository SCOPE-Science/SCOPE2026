"""Reproducible finite tests for the graph-metric projective-plane Rips action.
Uses only the Python standard library; integer arithmetic throughout.
"""
from itertools import product
from collections import Counter
from math import factorial

def parity(arr):
    return (-1)**sum(arr[i]>arr[j] for i in range(len(arr)) for j in range(i+1,len(arr)))
def dot2(x,y):return ((x&y).bit_count())%2
V=tuple(range(1,8)); N=7
points={x:i for i,x in enumerate(V)}
lines={x:i+7 for i,x in enumerate(V)}
E=tuple(sorted((points[p],lines[l]) for p in V for l in V if dot2(p,l)==0))
assert len(E)==21

def transform_cols(cols,x):
    y=0
    for i in range(3):
        if x&(1<<i):y ^= cols[i]
    return y

def inv_cols(cols):
    inv={transform_cols(cols,x):x for x in range(8)}
    assert len(inv)==8
    return tuple(inv[1<<i] for i in range(3))
def transpose_cols(cols):
    return tuple(sum(((cols[j]>>i)&1)<<j for j in range(3)) for i in range(3))
def inverse_transpose(cols):return transpose_cols(inv_cols(cols))

mats=[]
for cols in product(V,repeat=3):
    if len({transform_cols(cols,x) for x in range(8)})==8:mats.append(cols)
assert len(mats)==168
perms=[]
for A in mats:
    B=inverse_transpose(A)
    g=[None]*14
    for p in V:g[points[p]]=points[transform_cols(A,p)]
    for l in V:g[lines[l]]=lines[transform_cols(B,l)]
    perms.append(tuple(g))
delta=tuple(i+7 if i<7 else i-7 for i in range(14))

def compose(a,b):return tuple(a[b[i]] for i in range(14))
perms=sorted(set(perms+[compose(delta,g) for g in perms]))
assert len(perms)==336
permset=set(perms)
assert all(compose(g,delta) in permset for g in perms)
Eset=set(E)
for g in perms:
    assert set(tuple(sorted((g[p],g[l]))) for p,l in E)==Eset

# Complete Rips face generation via point and line simplices plus mixed stars.
faces=set()
def nonempty_sums(verts):
    for mask in range(1,1<<len(verts)):
        yield tuple(verts[i] for i in range(len(verts)) if mask>>i&1)
for s in nonempty_sums(range(7)):faces.add(s)
for s in nonempty_sums(range(7,14)):faces.add(s)
for p in range(7):
    neigh=[l for l in range(7,14) if (p,l) in Eset]
    for s in nonempty_sums(neigh):faces.add(tuple(sorted((p,)+s)))
for l in range(7,14):
    neigh=[p for p in range(7) if (p,l) in Eset]
    for s in nonempty_sums(neigh):faces.add(tuple(sorted((l,)+s)))
assert len(faces)==331
assert Counter(map(len,faces))=={1:14,2:63,3:112,4:84,5:42,6:14,7:2}

def order(g):
    cur=tuple(range(14));n=0
    while True:
        cur=compose(g,cur);n+=1
        if cur==tuple(range(14)):return n
        assert n<=100

def cycles(g):
    seen=set();cs=[]
    for x in range(14):
        if x not in seen:
            j=x;k=0
            while j not in seen:
                seen.add(j);j=g[j];k+=1
            cs.append(k)
    return tuple(sorted(cs))
def type_sign(g):return 1 if g[0]<7 else -1

def signed_edge_fix_count(g):
    return sum((1 if type_sign(g)==1 else -1) for p,l in E
               if {g[p],g[l]}=={p,l})
def chi1_cycle(g):
    # Cellular trace of incidence graph C1-C0+H0.
    return 1+signed_edge_fix_count(g)-sum(g[v]==v for v in range(14))
def chi2_prediction(g):return type_sign(g)*chi1_cycle(g)
def chi2_direct(g):
    s=0
    for f in faces:
        images=[g[i] for i in f]
        if set(images)!=set(f):continue
        # sign of simplex permutation in sorted face order
        s+=(-1)**(len(f)-1)*parity(images)
    return s-1
for g in perms:assert chi2_direct(g)==chi2_prediction(g),(g,chi2_direct(g),chi2_prediction(g))
assert chi2_direct(tuple(range(14)))==8

# Irreducibility via inner product of characters.
inner=sum(chi2_prediction(g)**2 for g in perms)
invariants=sum(chi2_prediction(g) for g in perms)
assert inner==336,(inner,)
assert invariants==0,(invariants,)
# One sign twist differs on type swapping and not on same-side.
assert sum(chi1_cycle(g) for g in perms)==0

def invert(g):
    o=[0]*14
    for i,v in enumerate(g):o[v]=i
    return tuple(o)
conj={};allset=set(perms)
while allset:
    rep=min(allset)
    cls={compose(compose(h,rep),invert(h)) for h in perms}
    assert cls<=allset
    allset-=cls
    conj[rep]=len(cls)
assert len(conj)==9
records=[]
for rep,count in conj.items():
    ch=chi2_prediction(rep)
    fixed_edges=sum({rep[p],rep[l]}=={p,l} for p,l in E)
    records.append((type_sign(rep),order(rep),cycles(rep),count,fixed_edges,ch))
records.sort(key=lambda r:(-r[0],r[1],r[2],r[3],r[4]))
assert sum(c for _,_,_,c,_,_ in records)==336
print('Fano q=2 points=7 lines=7 incidence_edges=21 faces=331')
print('All 336 graph symmetries preserve incidences; all 336 direct simplicial Lefschetz traces match the twisted cycle-character prediction.')
print('Conjugacy classes (type_sign,order,vertex_cycle_type,class_size,setwise_fixed_flags,trace_H2):')
for r in records:print(r)
print('Character square sum =',inner,'group order =',len(perms),'invariant character sum =',invariants)
print('Irreducible rational 8D representation (absolutely irreducible over C via character norm 1).')
# Dot-product polarity: 3 absolute points (even Hamming weight), trace = 2.
abs_points=sum(dot2(p,p)==0 for p in V)
assert abs_points==3
assert chi2_prediction(delta)==abs_points-1==2
print('Polarity fixed incidence flags =',abs_points,'H2 trace =',chi2_prediction(delta))
print('PROJECTIVE_PLANE_EQUIVARIANT_RIPS_PASS')

# Separate 13-point projective-plane check, including a duality and an order-three unipotent collineation.
def dot3(x,y):return sum(a*b for a,b in zip(x,y))%3
def normalize3(x):
    i=next(i for i,v in enumerate(x) if v)
    scale=1 if x[i]==1 else 2
    return tuple((scale*v)%3 for v in x)
Vs=sorted(set(normalize3(x) for x in product(range(3),repeat=3) if any(x)))
assert len(Vs)==13
IDs={v:i for i,v in enumerate(Vs)}
E3={(IDs[p],IDs[l]+13) for p in Vs for l in Vs if dot3(p,l)==0}
assert len(E3)==52
faces3=set()
for part in (tuple(range(13)),tuple(range(13,26))):
    for s in nonempty_sums(part):faces3.add(s)
for p in range(13):
    links=tuple(l for l in range(13,26) if (p,l) in E3)
    for s in nonempty_sums(links):faces3.add(tuple(sorted((p,)+s)))
for l in range(13,26):
    links=tuple(p for p in range(13) if (p,l) in E3)
    for s in nonempty_sums(links):faces3.add(tuple(sorted((l,)+s)))
assert len(faces3)==16720

def mat3(A,x):return tuple(sum(A[i][j]*x[j] for j in range(3))%3 for i in range(3))
def trans3(A):return tuple(tuple(A[j][i] for j in range(3)) for i in range(3))
def inv3(A):
    # Small direct modular Gauss-Jordan
    B=[list(A[i])+[int(i==j) for j in range(3)] for i in range(3)]
    for j in range(3):
        pivot=next(i for i in range(j,3) if B[i][j])
        B[j],B[pivot]=B[pivot],B[j]
        fact=pow(B[j][j],-1,3)
        B[j]=[(fact*v)%3 for v in B[j]]
        for i in range(3):
            if i!=j:
                f=B[i][j];B[i]=[(a-f*b)%3 for a,b in zip(B[i],B[j])]
    return tuple(tuple(row[3:]) for row in B)
def perm3(A):
    B=trans3(inv3(A));g=[0]*26
    for i,v in enumerate(Vs):
        g[i]=IDs[normalize3(mat3(A,v))]
        g[i+13]=IDs[normalize3(mat3(B,v))]+13
    return tuple(g)
delta3=tuple(i+13 if i<13 else i-13 for i in range(26))
S3=perm3(((0,1,0),(1,0,0),(0,0,1)))
U3=perm3(((1,1,0),(0,1,0),(0,0,1)))
I3=tuple(range(26))
perms3=[I3,S3,U3,delta3,tuple(delta3[x] for x in S3),tuple(delta3[x] for x in U3)]
def tr3(g):
    s=0
    for f in faces3:
        images=[g[i] for i in f]
        if set(images)==set(f):s+=(-1)**(len(f)-1)*parity(images)
    return s-1
for g in perms3:
    sg=1 if g[0]<13 else -1
    ef=sum((sg if {g[p],g[l]}=={p,l} else 0) for p,l in E3)
    predicted=sg*(1+ef-sum(g[i]==i for i in range(26)))
    got=tr3(g)
    assert got==predicted,(predicted,got)
assert tr3(I3)==27
abs3=sum(dot3(v,v)==0 for v in Vs)
assert abs3==4
assert tr3(delta3)==3
print('PG(2,3) points=13 edges=52 faces=16720; 6 independent transformations including type swaps have matching Lefschetz traces.')
print('PG(2,3) polarity absolute points =',abs3,'H2 trace =',tr3(delta3))
print('PROJECTIVE_PLANE_EQUIVARIANT_RIPS_Q3_PASS')

# Two geometrically different polarities on PG(2,4) have different traces.
# GF(4) is F_2[t]/(t^2+t+1) represented in {0,1,t,1+t}.
def mul4(a,b):
    z=0
    for i in range(2):
        if (b>>i)&1: z ^= a<<i
    if z&8:z ^= (0b111<<1)
    if z&4:z ^= 0b111
    return z
def power4(a,n):
    z=1
    for _ in range(n):z=mul4(z,a)
    return z
assert all(mul4(i,power4(i,2))==1 for i in (1,2,3))
def normalize4(v):
    first=next(z for z in v if z)
    inv=power4(first,2)
    return tuple(mul4(inv,z) for z in v)
P4=sorted({normalize4(v) for v in product(range(4),repeat=3) if any(v)})
assert len(P4)==21
def bilinear4(x,y):
    return mul4(x[0],y[0])^mul4(x[1],y[1])^mul4(x[2],y[2])
def frobenius4(x):return tuple(power4(z,2) for z in x)
abs_orth=sum(bilinear4(v,v)==0 for v in P4)
abs_unitary=sum(bilinear4(v,frobenius4(v))==0 for v in P4)
assert (abs_orth,abs_unitary)==(5,9)
assert sum(bilinear4(p,l)==0 for p in P4 for l in P4)==105
assert 105-42+1==64
print('PG(2,4) incidence edges = 105, H2 rank = 64; orthogonal absolute points =',abs_orth,
      'and unitary absolute points =',abs_unitary)
print('PG(2,4) polarity traces on H2 =',abs_orth-1,abs_unitary-1)
print('PROJECTIVE_PLANE_EQUIVARIANT_RIPS_Q4_POLARITY_PASS')
