#!/usr/bin/env python3
"""Reproducible exact simplicial and character checks for a tetrahedral Rips filtration."""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

NAMES = tuple((i,j) for i in range(4) for j in range(4) if i != j)
POS = {x:i for i,x in enumerate(NAMES)}
N = len(NAMES)
assert N == 12
E = {tuple(sorted((a,b))) for a,b in combinations(range(N),2)
     if NAMES[a][0]==NAMES[b][0] or NAMES[a]==NAMES[b][::-1]}
assert len(E)==18
ADJ = [set() for _ in range(N)]
for a,b in E:
    ADJ[a].add(b); ADJ[b].add(a)
assert set(map(len,ADJ))=={3}
DIST=[]
for a in range(N):
    d=[99]*N;d[a]=0
    q=deque([a])
    while q:
        v=q.popleft()
        for w in ADJ[v]:
            if d[w] ==99:
                d[w]=d[v]+1;q.append(w)
    assert 99 not in d
    DIST.append(d)
assert max(map(max,DIST))==3

# Independently enumerate every nonempty subset at each threshold.
def complex_faces(t):
    out=[[] for _ in range(N)]
    for mask in range(1,1<<N):
        face=tuple(i for i in range(N) if (mask>>i)&1)
        if all(DIST[i][j]<=t for i,j in combinations(face,2)):
            out[len(face)-1].append(face)
    while out and not out[-1]:out.pop()
    return out

def binary_rank(cols, row_index):
    pivots={};inds=[]
    for j, f in enumerate(cols):
        x=0
        for a in combinations(f, len(f)-1):
            x ^= 1<<row_index[a]
        while x:
            lead=x.bit_length()-1
            if lead in pivots:
                x ^= pivots[lead]
            else:
                pivots[lead]=x
                inds.append(j)
                break
    return len(pivots),inds

def permutation_sign(image_tuple):
    inv=sum(image_tuple[i]>image_tuple[j]
            for i in range(len(image_tuple)) for j in range(i+1,len(image_tuple)))
    return -1 if inv%2 else 1

def class_label(perm):
    seen=set();cycles=[]
    for i in range(4):
        if i in seen:continue
        j=i; size=0
        while j not in seen:
            seen.add(j);size+=1;j=perm[j]
        cycles.append(size)
    return tuple(sorted(cycles,reverse=True))

F1=complex_faces(1)
F2=complex_faces(2)
assert list(map(len,F1))==[12,18,4]
assert list(map(len,F2))==[12,42,48,12]
for F in (F1,F2):
    inds=[{f:i for i,f in enumerate(fs)} for fs in F]
    for d in range(1,len(F)):
        rank,piv=binary_rank(F[d],inds[d-1])
        print('boundary-rank-mod2',len(F[0]),'dimension',d,'rank',rank,'pivots',piv)
        if F is F1: assert (d,rank)==(1,11) if d==1 else (d,rank)==(2,4)
        if F is F2: assert (d,rank) in [(1,11),(2,31),(3,12)]

# Rational Betti dimensions follow from lower bounds on rational ranks by mod-2
# and exact upper bounds from d^2=0 and source ranks.
# For r=1: rank(d1)=11; 4 independent triangle columns => rank(d2)=4.
# For r=2: rank(d2)<=42-rank(d1)=31 and >=31 mod 2;
# rank(d3)<=12 and >=12 mod 2. Thus (betti1,betti2)=(0,5).

def lefschetz(F, vperm):
    total=0
    for d,faces in enumerate(F):
        for f in faces:
            images=tuple(vperm[k] for k in f)
            if set(images)==set(f):
                total+=(-1 if d%2 else 1)*permutation_sign(images)
    return total

classes=defaultdict(list)
vertex_actions=[]
for p in permutations(range(4)):
    vperm=tuple(POS[(p[i],p[j])] for i,j in NAMES)
    assert len(set(vperm))==N
    assert {tuple(sorted((vperm[a],vperm[b]))) for a,b in E}==E
    for F in (F1,F2):
        for d,fs in enumerate(F):
            assert set(tuple(sorted(vperm[k] for k in f)) for f in fs)==set(fs)
    # Lefschetz on reduced homology: r=1: tr(H1)=1-L1;
    # r=2: tr(H2)=L2-1 (H1=0).
    char1=1-lefschetz(F1,vperm)
    char2=lefschetz(F2,vperm)-1
    classes[class_label(p)].append((char1,char2))
    vertex_actions.append((p,vperm))
expected={
    (1,1,1,1):(1,3,5),
    (2,1,1):(6,-1,1),
    (2,2):(3,-1,1),
    (3,1):(8,0,2),
    (4,):(6,1,-1),
}
assert set(classes)==set(expected)
for shape in sorted(expected):
    size,h1,h2=expected[shape]
    assert len(classes[shape])==size
    assert set(classes[shape])=={(h1,h2)}
    print('cycle-type',shape,'size',size,'trace-H1-r1',h1,'trace-H2-r2',h2)
# For S4, std(g) = fixed_points(g)-1; sign(g) is permutation parity.
for p,_ in vertex_actions:
    shape=class_label(p)
    fix=sum(p[i]==i for i in range(4))
    parity=(-1)**(4-len(shape))
    h1,h2=classes[shape][0]
    assert h1 == parity*(fix-1)  # sign-twisted standard module
    assert h2 == fix+parity      # vertex permutation module plus sign
print('CHECK_OK: 24 distinct tetrahedral symmetries; positive-degree rational equivariant barcode verified')
