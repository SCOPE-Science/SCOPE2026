#!/usr/bin/env python3
"""Reproduce integral cellular homology of the ordinary 6-by-6 queen-complex D4 orbit space.

Only Python's standard library is required. Integer chain operations are exact.
"""
import collections
import itertools
import math
import time

N = 6
SQUARES = [(i,j) for i in range(N) for j in range(N)]

def symmetries():
    transformations=[]
    for transpose in (False,True):
        for turns in range(4):
            def t(i,j):
                if transpose: i,j=j,i
                for _ in range(turns): i,j=j,N-1-i
                return i,j
            transformations.append(tuple(SQUARES.index(t(*p)) for p in SQUARES))
    return list(dict.fromkeys(transformations))

G=symmetries()
assert len(G)==8
attacks=[]
for i,j in SQUARES:
    attacks.append(sum(1<<k for k,(a,b) in enumerate(SQUARES)
                       if i==a or j==b or abs(i-a)==abs(j-b)))

# Every nonempty independent face, generated exactly once by increasing indices.
faces=[]
layer=[0]
face_counts=[]
for n in range(1,7):
    layer=[x|(1<<v) for x in layer for v in range(x.bit_length(),N*N)
           if not (attacks[v]&x)]
    faces.extend(layer)
    face_counts.append(len(layer))
assert face_counts==[36,340,1024,982,248,4]
faces.sort(key=lambda x:(x.bit_count(),x))
face_set=set(faces)

# All strict cofaces: take the upward closure in the face poset.
cover={x:[] for x in faces}
for y in faces:
    rem=y
    while rem:
        bit=rem&-rem;rem-=bit
        x=y^bit
        if x in cover:cover[x].append(y)
for x in faces:
    reach=set(); current=[x]
    for _ in range(x.bit_count()+1,7):
        current=list(set(z for y in current for z in cover[y]))
        reach.update(current)
    cover[x]=sorted(reach)

# Group acts on subsets of squares and on flags by acting on every face.
transforms={}
for x in faces:
    transformed=[]
    for g in G:
        value=0; rem=x
        while rem:
            bit=rem&-rem;rem-=bit
            value|=1<<g[bit.bit_length()-1]
        transformed.append(value)
    transforms[x]=tuple(transformed)

def canonical(chain):
    return min(tuple(transforms[f][g] for f in chain) for g in range(8))

# Barycentric subdivision quotiented by all eight square symmetries.
levels=[]
current=sorted({canonical((f,)) for f in faces})
levels.append(current)
for k in range(1,6):
    successors=set()
    for chain in current:
        for f in cover[chain[-1]]:
            successors.add(canonical(chain+(f,)))
    current=sorted(successors)
    if not current:break
    levels.append(current)
assert [len(s) for s in levels]==[337,3541,10110,11166,4620,360]
cells=[cell for level in levels for cell in level]
index={cell:i for i,cell in enumerate(cells)}
dimension=[len(cell)-1 for cell in cells]

# Rank-ordered barycentric flags furnish cells without inversions.
# Each orbit cell has its oriented cellular boundary given by face deletion.
boundary=[]
incidence=[]
cofaces=[set() for _ in cells]
for j,chain in enumerate(cells):
    terms=collections.Counter()
    occurrence=collections.Counter()
    if len(chain)>1:
        for k in range(len(chain)):
            i=index[canonical(chain[:k]+chain[k+1:])]
            occurrence[i]+=1
            terms[i]+=(-1)**k
            cofaces[i].add(j)
    assert all(count==1 for count in occurrence.values())
    boundary.append({i:a for i,a in terms.items() if a})
    incidence.append(occurrence)
assert sum((-1)**k*len(levels[k]) for k in range(len(levels)))==0

# Verify d∘d=0 in the original quotient cellular chain complex.
for j,col in enumerate(boundary):
    total=collections.Counter()
    for i,a in col.items():
        for h,c in boundary[i].items():total[h]+=a*c
    assert not any(total.values()),j

# Topological elementary collapses in the regular rank-flag quotient CW complex.
alive=[True]*len(cells)
queue=collections.deque(sorted(range(len(cells)),key=lambda j:(-dimension[j],j)))
free_pairs=0
while queue:
    i=queue.popleft()
    if not alive[i]:continue
    uppers=[j for j in cofaces[i] if alive[j]]
    if len(uppers)!=1:continue
    j=uppers[0]
    if dimension[j]!=dimension[i]+1 or incidence[j][i]!=1:continue
    alive[i]=False;alive[j]=False;free_pairs+=1
    for k in incidence[j]:
        if alive[k]:cofaces[k].discard(j);queue.append(k)
assert free_pairs==11550
remaining={j for j in range(len(cells)) if alive[j]}
assert collections.Counter(dimension[j] for j in remaining)=={0:227,1:1751,2:3290,3:1766}
for j in remaining:
    assert all(i in remaining for i in boundary[j]),'collapse did not leave subcomplex'

# Integer cellular chain contraction: if d(e_j)=a e_i+v with a=±1,
# cancel e_j with e_i, and for every e_k of the same dimension change
# d(e_k) to d(e_k)-[e_i]d(e_k)/a*d(e_j). Drop their coordinates in adjacent differentials.
col={j:{i:a for i,a in boundary[j].items()} for j in remaining}
row={j:set() for j in remaining}
for j,c in col.items():
    for i in c:row[i].add(j)
pivots=0
pivot_by_degree={}
for d in (3,2,1):
    count=0
    while True:
        best=None;best_score=None
        for j in remaining:
            if dimension[j]!=d:continue
            for i,a in col[j].items():
                if abs(a)!=1:continue
                score=(len(col[j])-1)*(len(row[i])-1)
                if best_score is None or score<best_score:
                    best=(i,j,a);best_score=score
        if best is None:break
        i,j,a=best
        cj=col[j]
        for k in list(row[i]):
            if k==j:continue
            ck=col[k]
            factor=ck[i]*a  # since a = ±1 = 1/a
            for h,v in cj.items():
                old=ck.get(h,0);new=old-factor*v
                if new:
                    ck[h]=new
                    if not old:row[h].add(k)
                elif old:
                    del ck[h];row[h].remove(k)
        for h in cj:row[h].remove(j)
        assert not row[i]
        for k in list(row[j]):
            col[k].pop(j)
            row[j].remove(k)
        for h in col[i]:row[h].remove(i)
        del col[i],col[j],row[i],row[j]
        remaining.remove(i);remaining.remove(j)
        count+=1;pivots+=1
    pivot_by_degree[d]=count
assert pivot_by_degree=={3:1760,2:1525,1:226}
assert len(remaining)==12
assert collections.Counter(dimension[j] for j in remaining)=={0:1,2:5,3:6}
rows2=sorted(j for j in remaining if dimension[j]==2)
cols3=sorted(j for j in remaining if dimension[j]==3)
assert all(col[j]=={} for j in remaining if dimension[j]!=3)
mat=[[col[j].get(i,0) for j in cols3] for i in rows2]
assert all(x%2==0 for r in mat for x in r)

# The halved 5x6 matrix has a 5x5 unimodular minor; thus the full rank-five
# Smith invariants of the integral boundary are all 2. No other boundary survives.
def det(a):
    if len(a)==1:return a[0][0]
    return sum((-1)**k*a[0][k]*det([r[:k]+r[k+1:] for r in a[1:]]) for k in range(len(a)))
minor=det([[x//2 for x in r[:5]] for r in mat])
assert abs(minor)==1
print('QUEENS6_D4_INTEGRAL_QUOTIENT_OK')
print('nonempty face vector:',face_counts)
print('quotient flag cells:',[len(x) for x in levels])
print('topological collapse pairs:',free_pairs)
print('integral algebraic cancellation pivots:',pivot_by_degree)
print('residual cells (degree:count):',dict(sorted(collections.Counter(dimension[j] for j in remaining).items())))
print('residual boundary matrix:',mat)
print('halved minor determinant:',minor)
print('H_0=Z, reduced H_2=(Z/2)^5, H_3=Z, other reduced H_i=0')
