#!/usr/bin/env python3
"""Reproduce the exact graph-metric Rips homotopy and symmetry calculation.
Requires only the Python standard library, Python 3.9+.
"""
from collections import Counter, deque
from itertools import permutations, combinations

N=12
VERTICES=tuple(range(N))
EDGES={tuple(sorted((i,(i+1)%N))) for i in VERTICES}
for i in VERTICES:
    d=(6,4,-4)[i%3]
    EDGES.add(tuple(sorted((i,(i+d)%N))))
assert len(EDGES)==18
ADJ=[set() for _ in VERTICES]
for a,b in EDGES:
    ADJ[a].add(b); ADJ[b].add(a)
assert all(len(ADJ[i])==3 for i in VERTICES)

def distances_from(v):
    dist=[-1]*N;dist[v]=0;Q=deque([v])
    while Q:
        a=Q.popleft()
        for b in sorted(ADJ[a]):
            if dist[b]<0:
                dist[b]=dist[a]+1;Q.append(b)
    assert min(dist)>=0
    return dist
D=[distances_from(v) for v in VERTICES]
assert max(map(max,D))==3

def complexes_at(r):
    # Enumerate all nonempty subsets; the empty simplex is implicit.
    return {m for m in range(1,1<<N)
            if all(D[i][j]<=r for i in VERTICES for j in range(i+1,N)
                   if m&(1<<i) and m&(1<<j))}
F={r:complexes_at(r) for r in range(4)}
assert [len(F[r]) for r in range(4)]==[12,30,166,4095]
assert Counter(m.bit_count()-1 for m in F[2])=={0:12,1:46,2:68,3:36,4:4}

def matching_certificate(faces):
    free=set(faces);pairs=[]
    for v in VERTICES:
        bit=1<<v
        # This exact pivot order defines a disjoint matching on the face poset.
        for lower in sorted(list(free),key=lambda m:(m.bit_count(),m)):
            upper=lower|bit
            if lower in free and not (lower&bit) and upper in free:
                free.remove(lower);free.remove(upper);pairs.append((lower,upper))
    paired=set(pairs)
    arrows={m:[] for m in faces};indegree={m:0 for m in faces}
    ninc=0
    for upper in faces:
        bits=upper
        while bits:
            lowbit=bits&-bits;bits-=lowbit
            lower=upper^lowbit
            if lower==0 or lower not in faces:continue
            # Reverse the standard decreasing face-arrow on each matching pair.
            src,dst=(lower,upper) if (lower,upper) in paired else (upper,lower)
            arrows[src].append(dst);indegree[dst]+=1;ninc+=1
    Q=deque(m for m in faces if indegree[m]==0)
    visited=0
    while Q:
        u=Q.popleft();visited+=1
        for v in arrows[u]:
            indegree[v]-=1
            if indegree[v]==0:Q.append(v)
    assert visited==len(faces),'closed gradient path encountered'
    assert 2*len(pairs)+len(free)==len(faces)
    return pairs,free,ninc

P1,C1,E1=matching_certificate(F[1]);P2,C2,E2=matching_certificate(F[2])
assert len(P1)==11 and Counter(m.bit_count()-1 for m in C1)=={0:1,1:7} and E1==36
assert len(P2)==82 and Counter(m.bit_count()-1 for m in C2)=={0:1,2:1} and E2==460
assert sum((-1)**(m.bit_count()-1) for m in F[2])==2

# Independently compute mod-two boundary ranks from raw simplex incidences.
def rank_f2(rows):
    piv={}
    for row in rows:
        x=row
        while x:
            k=x.bit_length()-1
            if k not in piv:
                piv[k]=x;break
            x^=piv[k]
    return len(piv)
def boundary_rank(r,k):
    faces=[sorted(m for m in F[r] if m.bit_count()==d+1) for d in range(5)]
    if k<=0:return 0
    pos={m:i for i,m in enumerate(faces[k-1])}
    rows=[]
    for upper in faces[k]:
        row=0
        for i in VERTICES:
            if upper&(1<<i):
                lower=upper^(1<<i)
                row^=1<<pos[lower]
        rows.append(row)
    return rank_f2(rows)
ranks=[0]+[boundary_rank(2,k) for k in range(1,5)]+[0]
assert ranks==[0,11,35,32,4,0],ranks
betti=[sum(1 for m in F[2] if m.bit_count()==k+1)-ranks[k]-ranks[k+1] for k in range(5)]
assert betti==[1,0,1,0,0],betti

def compose(p,q):return tuple(p[q[i]] for i in VERTICES)
I=VERTICES
r=tuple((i+3)%N for i in VERTICES)
s=tuple((-i)%N for i in VERTICES)
assert all(tuple(sorted((p[a],p[b]))) in EDGES for p in (r,s) for a,b in EDGES)
assert compose(compose(r,r),compose(r,r))==I and compose(s,s)==I
assert compose(s,compose(r,s))==compose(compose(r,r),r)

# Count all automorphisms independently by a finite adjacency-preserving backtrack.
ORDER=[0]+sorted(ADJ[0])+[i for i in VERTICES if i not in {0,*ADJ[0]}]
def count_automorphisms():
    used=set();mapped={};total=0
    def rec(j):
        nonlocal total
        if j==N:
            total+=1;return
        u=ORDER[j]
        for v in VERTICES:
            if v in used:continue
            if any(((u in ADJ[w]) != (v in ADJ[mapped[w]])) for w in mapped):continue
            mapped[u]=v;used.add(v);rec(j+1);used.remove(v);del mapped[u]
    rec(0);return total
assert count_automorphisms()==8

# Every group element uniquely has the form r^a s^b.
D4=[];power=I
for a in range(4):
    for b in range(2):D4.append((a,b,power if b==0 else compose(power,s)))
    power=compose(r,power)
assert len({p for a,b,p in D4})==8

def sign(values):
    return -1 if sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))%2 else 1

def simplicial_lefschetz(faces,p):
    out=0
    for m in faces:
        verts=[v for v in VERTICES if m&(1<<v)]
        if {p[v] for v in verts}!={v for v in verts}:continue
        out+=(-1)**(len(verts)-1)*sign([p[v] for v in verts])
    return out
TABLE=[]
for a,b,p in D4:
    chi1=1-simplicial_lefschetz(F[1],p)
    chi2=simplicial_lefschetz(F[2],p)-1
    assert chi2==(-1)**(a+b)
    TABLE.append((a,b,chi1,chi2))
assert [row[2] for row in TABLE]==[7,-3,1,-1,-1,-3,1,-1]
# Four rational linear characters and the standard two-dimensional character.
mults={(alpha,beta):sum(chi1*(alpha**a)*(beta**b) for a,b,chi1,chi2 in TABLE)//8
       for alpha in (-1,1) for beta in (-1,1)}
assert mults=={(-1,-1):1,(-1,1):0,(1,-1):2,(1,1):0}
mult_std=sum(chi1*((2 if a==0 else -2 if a==2 else 0) if b==0 else 0)
             for a,b,chi1,chi2 in TABLE)//8
assert mult_std==2
assert sum(chi1 for a,b,chi1,chi2 in TABLE)==0
assert sum(chi2 for a,b,chi1,chi2 in TABLE)==0

print('GRAPH: 12 vertices, 18 edges, diameter 3; full automorphism group D4 (8 elements)')
print('RIPS_FACE_COUNTS: r=0:12 r=1:30 r=2:166 r=3:4095')
print('RIPS2_F_VECTOR: (12,46,68,36,4)')
print('RIPS1_MATCHING: 11 pairs, critical one vertex and seven edges, 36 oriented incidences, acyclic')
print('RIPS2_MATCHING: 82 pairs, critical one vertex and one 2-face, 460 oriented incidences, acyclic')
print('RIPS2_MOD2_BOUNDARY_RANKS:',ranks,'BETTI:',betti)
print('D4_CHARACTER_TABLE (rotation exponent,reflection exponent,H1@r1,H2@r2):')
for row in TABLE:print(*row)
print('H1_DECOMPOSITION: linear(-1,-1)=1, linear(+1,-1)=2, standard_2D=2')
print('H2_DECOMPOSITION: linear(-1,-1)=1')
print('INTEGER_BARCODES: H0 one infinite, eleven [0,1); H1 seven [1,2); H2 one [2,3)')
print('BIDIAKIS_RIPS_EQUIVARIANT_CERTIFICATE_PASS')
