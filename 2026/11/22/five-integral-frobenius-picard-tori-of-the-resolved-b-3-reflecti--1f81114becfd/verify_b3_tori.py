#!/usr/bin/env python3
"""Exact finite certificate for Coxeter B3 resolved-line Picard tori.

Standard library only. Reconstructs projective incidence, 24 symmetries,
signed actions on graph cycles, and explicit unimodular block bases.
"""
from collections import Counter, deque
from itertools import combinations, permutations, product
from math import gcd

LINES = [(1,0,0),(0,1,0),(0,0,1),
         (1,-1,0),(1,1,0),(1,0,-1),(1,0,1),(0,1,-1),(0,1,1)]

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def normalize(a):
    t=gcd(*a)
    assert t != 0
    a=tuple(x//t for x in a)
    return a if next(x for x in a if x)>0 else tuple(-x for x in a)

def intersections(lines):
    out={}
    for i,j in combinations(range(len(lines)),2):
        p=normalize(cross(lines[i],lines[j]))
        out.setdefault(p,set()).update((i,j))
    out={p:tuple(i for i,a in enumerate(lines) if sum(a[k]*p[k] for k in range(3))==0) for p in out}
    assert all(len(s)>=2 for s in out.values())
    assert sum(len(s)*(len(s)-1)//2 for s in out.values())==len(lines)*(len(lines)-1)//2
    return out

POINTS=intersections(LINES)
HIGH=sorted(p for p,s in POINTS.items() if len(s)>=3)
EDGES=sorted([(i,9+j) for j,p in enumerate(HIGH) for i in POINTS[p]]+
             [tuple(POINTS[p]) for p in POINTS if len(POINTS[p])==2])
N=9+len(HIGH)
EID={e:i for i,e in enumerate(EDGES)}
ADJ=[[] for _ in range(N)]
for a,b in EDGES:
    ADJ[a].append(b);ADJ[b].append(a)
for x in ADJ: x.sort()
assert len(POINTS)==13 and [sum(len(s)==j for s in POINTS.values()) for j in (2,3,4)]==[6,4,3]
assert N==16 and len(EDGES)==30 and len(EDGES)-N+1==15
assert min(map(len,ADJ))>=3

# Canonical BFS spanning tree rooted at component 0.
parent={0:-1}; order=deque([0]); TREE=set()
while order:
    a=order.popleft()
    for b in ADJ[a]:
        if b not in parent:
            parent[b]=a;order.append(b);TREE.add(tuple(sorted((a,b))))
assert len(parent)==N and len(TREE)==N-1
CHORDS=[e for e in EDGES if e not in TREE]
assert len(CHORDS)==15

def path_tree(a,b):
    q=deque([a]); par={a:None}
    while q:
        x=q.popleft()
        if x==b:break
        for y in ADJ[x]:
            if tuple(sorted((x,y))) in TREE and y not in par:
                par[y]=x;q.append(y)
    path=[b]
    while path[-1]!=a:path.append(par[path[-1]])
    return path[::-1]

def cycle(chord):
    a,b=chord;z=[0]*len(EDGES);z[EID[chord]]=1
    walk=path_tree(b,a)
    for x,y in zip(walk,walk[1:]):
        edge=tuple(sorted((x,y)))
        z[EID[edge]]+=(1 if (x,y)==edge else -1)
    return z
B=[cycle(e) for e in CHORDS] # columns
for z in B:
    assert all(sum(z[k]*(int(a==v)-int(b==v)) for k,(a,b) in enumerate(EDGES))==0 for v in range(N))
CHORD_INDICES=[EID[e] for e in CHORDS]
assert [[z[k] for k in CHORD_INDICES] for z in B]==[[int(i==j) for j in range(15)] for i in range(15)]

def perm_coords(a,perm,signs):
    return normalize(tuple(a[perm[i]]*signs[i] for i in range(3)))

AUT={}
for perm in permutations(range(3)):
    for signs in product((-1,1),repeat=3):
        u=tuple(LINES.index(perm_coords(a,perm,signs)) for a in LINES)
        if u in AUT:continue # central scalar matrices act trivially
        hp=tuple(HIGH.index(perm_coords(p,perm,signs)) for p in HIGH)
        P=u+tuple(9+k for k in hp)
        assert all(tuple(sorted((P[a],P[b]))) in EID for a,b in EDGES)
        AUT[P]=(perm,signs)
assert len(AUT)==24

def orbit_lengths(P):
    seen=set();lens=[]
    for i in range(len(P)):
        if i not in seen:
            c=0;j=i
            while j not in seen:
                seen.add(j);j=P[j];c+=1
            lens.append(c)
    return tuple(sorted(lens))

def edge_action(P):
    out=[]
    for a,b in EDGES:
        t=tuple(sorted((P[a],P[b])))
        out.append((EID[t],1 if (P[a],P[b])==t else -1))
    return out

def flag_action(P):
    F=[(v,i) for i,(a,b) in enumerate(EDGES) for v in (a,b)]
    indices={z:i for i,z in enumerate(F)}
    eperm=edge_action(P)
    return tuple(indices[(P[v],eperm[i][0])] for (v,i) in F)

def cycle_matrix(P):
    signed=edge_action(P); cols=[]
    for cyclevec in B:
        moved=[0]*len(EDGES)
        for k,x in enumerate(cyclevec):
            if x:
                i,sg=signed[k];moved[i]+=sg*x
        coords=[moved[i] for i in CHORD_INDICES]
        assert moved==[sum(coords[j]*B[j][i] for j in range(15)) for i in range(len(EDGES))]
        cols.append(coords)
    return [[cols[j][i] for j in range(15)] for i in range(15)]

CLASSES={}
for P in AUT:
    signature=(orbit_lengths(P),
               orbit_lengths(tuple(x[0] for x in edge_action(P))),
               orbit_lengths(flag_action(P)))
    CLASSES.setdefault(signature,[]).append(P)
CLS=sorted(CLASSES.items(),key=lambda item:(len(item[1]),item[0]))
assert [len(members) for sig,members in CLS]==[1,3,6,6,8]
# Confirm profiles are actual complete conjugacy classes, not merely equal cycle signatures.
def compose(a,b): return tuple(a[b[i]] for i in range(len(a)))
def inverse(a): return tuple(a.index(i) for i in range(len(a)))
for signature,members in CLS:
    representative=members[0]
    conjugacy={compose(compose(h,representative),inverse(h)) for h in AUT}
    assert conjugacy==set(members)
EXPECTED=[
 ({1:16},{1:30},{1:60},1),
 ({1:8,2:4},{1:10,2:10},{1:20,2:20},2),
 ({1:6,2:5},{1:6,2:12},{1:12,2:24},2),
 ({1:2,2:3,4:2},{2:5,4:5},{2:10,4:10},4),
 ({1:1,3:5},{3:10},{3:20},3),
]

def as_counts(lengths):return dict(Counter(lengths))
for idx,(sig, members) in enumerate(CLS):
    vc,ec,fc,ordg=EXPECTED[idx]
    assert as_counts(sig[0])==vc and as_counts(sig[1])==ec and as_counts(sig[2])==fc
    assert all(sum(x==1 for x in sig[1])==sum(x==1 for x in sig[2])//2 for sig in [sig])
    assert all((edge_action(P)[i][1]==1) or edge_action(P)[i][0]!=i for P in members for i in range(len(EDGES)))
    for P in members:
        power=tuple(range(N))
        for j in range(ordg):power=tuple(P[i] for i in power)
        assert power==tuple(range(N))
        F=cycle_matrix(P)
        # Exact matrix power is identity of stated order.
        def mm(A,B):
            return [[sum(A[i][k]*B[k][j] for k in range(15)) for j in range(15)] for i in range(15)]
        temp=[[int(i==j) for j in range(15)] for i in range(15)]
        for j in range(ordg):temp=mm(F,temp)
        assert temp==[[int(i==j) for j in range(15)] for i in range(15)]

# Certificates for each class representative, in the fundamental-chord basis.
# A seed (i,...) lists coefficients of the standard integral basis e_i,
# with optional signs. The columns v,Fv,... form the indicated cyclic block.
SEEDS={
 1: ([(12,),(8,),(13,),(6,),(1,),(5,)], [(4,),(3,4),(2,-6)]),
 2: ([(12,),(6,),(3,),(9,),(5,),(1,),(11,)], [(14,)]),
 3: ([(1,),(2,9),(12,13)], [(2,)], [(14,)]),
 4: ([(7,),(6,),(2,),(13,),(4,)],),
}
# In SEEDS a negative index entry -6 denotes -e_(6-1)=-e_5.
def seed(t):
    out=[0]*15
    for j in t:
        out[j if j>=0 else -j-1]+=1 if j>=0 else -1
    return out

def mat_vec(A,v):return [sum(A[i][k]*v[k] for k in range(15)) for i in range(15)]

def orbit_columns(A,v,n):
    out=[]
    for _ in range(n):out.append(v);v=mat_vec(A,v)
    return out

def det_int(A):
    # Fraction-free Bareiss determinant with exact divisions.
    A=[list(x) for x in A];n=len(A);sgn=1;den=1
    for k in range(n-1):
        if A[k][k]==0:
            l=next((i for i in range(k+1,n) if A[i][k]!=0),None)
            if l is None:return 0
            A[k],A[l]=A[l],A[k];sgn=-sgn
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=A[i][j]*pivot-A[i][k]*A[k][j]
                assert numerator%den==0
                A[i][j]=numerator//den
        for i in range(k+1,n):A[i][k]=0
        den=pivot
    return sgn*A[-1][-1]

EXPECTED_BLOCKS=[('one',)*15,('reg2',)*6+('one',)*3,
                 ('reg2',)*7+('one',),
                 ('reg4',)*3+('reg2',)+('negative',),('reg3',)*5]
for idx,(sig,members) in enumerate(CLS):
    F=cycle_matrix(members[0])
    columns=[];block_labels=[]
    if idx==0:
        columns=[[int(i==j) for i in range(15)] for j in range(15)]
        block_labels=['one']*15
    elif idx in (1,2):
        full,trivs=SEEDS[idx]
        for z in full:
            columns.extend(orbit_columns(F,seed(z),2));block_labels.append('reg2')
        for z in trivs:
            columns.append(seed(z));block_labels.append('one')
    elif idx==3:
        full,two,neg=SEEDS[idx]
        for z in full:
            columns.extend(orbit_columns(F,seed(z),4));block_labels.append('reg4')
        for z in two:
            columns.extend(orbit_columns(F,seed(z),2));block_labels.append('reg2')
        for z in neg:
            columns.append(seed(z));block_labels.append('negative')
    else:
        for z in SEEDS[idx][0]:
            columns.extend(orbit_columns(F,seed(z),3));block_labels.append('reg3')
    assert len(columns)==15 and tuple(block_labels)==EXPECTED_BLOCKS[idx][:len(block_labels)]
    for lab,j in zip(block_labels, (lambda ls:[sum({'one':1,'negative':1,'reg2':2,'reg3':3,'reg4':4}[x] for x in ls[:i]) for i in range(len(ls))])(block_labels)):
        d={'one':1,'negative':1,'reg2':2,'reg3':3,'reg4':4}[lab]
        last=mat_vec(F,columns[j+d-1])
        assert last==([-x for x in columns[j]] if lab=='negative' else columns[j])
    W=[[columns[j][i] for j in range(15)] for i in range(15)]
    assert abs(det_int(W))==1, (idx,det_int(W))
    print('class',idx,'size',len(members),'order',EXPECTED[idx][3],
          'block_types',block_labels,'det_certificate',det_int(W),
          'fixed_components',EXPECTED[idx][0].get(1,0),flush=True)
print('B3_RESOLVED_FROBENIUS_INTEGRAL_PICARD_TORI_OK')
