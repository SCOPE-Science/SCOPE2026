#!/usr/bin/env python3
"""Reconstruct the integral homotopy and rational orbit-homology claims
for the graph-geodesic general-position complex of the Franklin graph.
Only Python's standard library is required.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
from fractions import Fraction

N=12
# LCF [5,-5]^6. The vertex labels are residues modulo 12.
EDGES={tuple(sorted((i,(i+1)%N))) for i in range(N)}
EDGES|={tuple(sorted((i,(i+(5 if i%2==0 else -5))%N))) for i in range(N)}
assert len(EDGES)==18
ADJ={i:set() for i in range(N)}
for a,b in EDGES: ADJ[a].add(b);ADJ[b].add(a)
assert all(len(ADJ[i])==3 for i in range(N))

D=[]
for a in range(N):
 d=[N+1]*N;d[a]=0;queue=deque([a])
 while queue:
  v=queue.popleft()
  for w in ADJ[v]:
   if d[w]>d[v]+1:d[w]=d[v]+1;queue.append(w)
 D.append(d)
assert max(max(x) for x in D)==3
bad=[]
for a,b,c in combinations(range(N),3):
 if (D[a][c]==D[a][b]+D[b][c] or
     D[a][b]==D[a][c]+D[c][b] or
     D[b][c]==D[b][a]+D[a][c]):
  bad.append((1<<a)|(1<<b)|(1<<c))
assert len(bad)==144
ALL=set(); BYDIM=defaultdict(list)
for m in range(1,1<<N):
 if any((m&t)==t for t in bad): continue
 ALL.add(m);BYDIM[m.bit_count()-1].append(m)
assert [len(BYDIM[k]) for k in range(6)]==[12,66,76,45,12,2]
assert len(ALL)==213

# Elementary simplicial collapses: every removed facet has exactly one
# immediate or higher-dimensional containing cell, namely the chosen coface.
active=set(ALL); collapses=[]
while True:
 candidate=None
 for cell in sorted(active,key=lambda t:(-t.bit_count(),t)):
  if cell.bit_count()<2: continue
  for v in range(N):
   if not cell>>v&1:continue
   face=cell^(1<<v)
   if face not in active:continue
   if sum(1 for other in active if other!=face and other&face==face)==1:
    candidate=(face,cell);break
  if candidate:break
 if candidate is None:break
 face,coface=candidate
 assert (coface^face).bit_count()==1
 active.remove(face);active.remove(coface)
 collapses.append(candidate)
assert len(collapses)==56
assert [sum(x.bit_count()==k+1 for x in active) for k in range(3)]==[12,57,32]
assert not any(x.bit_count()>3 for x in active)

# Contract a spanning tree of the remaining one-skeleton.
G1={i:set() for i in range(N)}
for m in active:
 if m.bit_count()==2:
  a,b=[v for v in range(N) if m>>v&1]
  G1[a].add(b);G1[b].add(a)
seen={0}; Q=deque([0]); TREE=set()
while Q:
 v=Q.popleft()
 for w in sorted(G1[v]):
  if w not in seen:
   seen.add(w);Q.append(w);TREE.add(tuple(sorted((v,w))))
assert len(TREE)==11 and len(seen)==12
OTHERS=sorted(tuple(sorted((a,b))) for a in G1 for b in G1[a] if a<b and (a,b) not in TREE)
assert len(OTHERS)==46
GEN={edge:i+1 for i,edge in enumerate(OTHERS)}
def inv(word):return [-x for x in reversed(word)]
def red(word):
 stack=[]
 for x in word:
  if stack and stack[-1]==-x:stack.pop()
  else:stack.append(x)
 return stack
def ew(a,b):
 g=GEN.get(tuple(sorted((a,b))))
 return [] if g is None else ([g] if a<b else [-g])
REL=[]
for m in sorted(x for x in active if x.bit_count()==3):
 a,b,c=[i for i in range(N) if m>>i&1]
 REL.append(red(ew(a,b)+ew(b,c)+ew(c,a)))
assert len(REL)==32

# Free-group Tietze/CW cancellations: a relator containing a generator
# precisely once can be changed to that generator by a Nielsen basis
# substitution, then its 1-cell and 2-cell cancel. This preserves homotopy.
remaining=set(GEN.values()); cancellations=[]
while True:
 options=[]
 for j,rel in enumerate(REL):
  for x in set(map(abs,rel)):
   if sum(abs(y)==x for y in rel)==1:options.append((len(rel),j,x))
 if not options:break
 _,j,x=min(options)
 r=REL[j]; pos=next(i for i,y in enumerate(r) if abs(y)==x)
 U,V=r[:pos],r[pos+1:]
 replacement=red(inv(U)+inv(V)) if r[pos]>0 else red(V+U)
 assert all(abs(y)!=x for y in replacement)
 new=[]
 for jj,rel in enumerate(REL):
  if jj==j:continue
  out=[]
  for y in rel:
   out+=(replacement if y==x else inv(replacement) if y==-x else [y])
  new.append(red(out))
 REL=new;remaining.remove(x);cancellations.append(x)
assert len(cancellations)==28
assert len(remaining)==18
assert len(REL)==4 and all(not rel for rel in REL)
# CW conclusion: 1 vertex, 18 loops, 4 nullattached 2-cells.

# Enumerate all automorphisms by adjacency compatibility.
PERMS=[]
def backtrack(mapping,used):
 if len(mapping)==N:
  PERMS.append(tuple(mapping[i] for i in range(N)));return
 u=min((i for i in range(N) if i not in mapping),key=lambda i:(-sum(x in mapping for x in ADJ[i]),i))
 for v in range(N):
  if v in used:continue
  if all(((u in ADJ[x])==(v in ADJ[y])) for x,y in mapping.items()):
   mapping[u]=v;used.add(v)
   backtrack(mapping,used)
   used.remove(v);del mapping[u]
backtrack({},set())
assert len(PERMS)==48 and len(set(PERMS))==48

def transform(face,p):
 ids=[p[i] for i in range(N) if face>>i&1]
 perm_sign= -1 if sum(ids[i]>ids[j] for i in range(len(ids)) for j in range(i+1,len(ids)))%2 else 1
 return sum(1<<i for i in ids),perm_sign

# A basis of invariant rational simplicial chains is the signed orbit-sum
# of each face orbit whose stabilizer fixes its orientation.
INV={};ORBIT_DATA={}
for k in range(6):
 unseen=set(BYDIM[k]);basis=[];nonorient=0;orbits=0
 while unseen:
  rep=min(unseen); img={};conflict=False
  for p in PERMS:
   q,sgn=transform(rep,p)
   if q in img and img[q]!=sgn:conflict=True
   img[q]=sgn
  assert set(img)<=set(BYDIM[k]);unseen-=set(img);orbits+=1
  if conflict:nonorient+=1
  else:
   assert img[rep]==1
   basis.append((rep,img))
 INV[k]=basis;ORBIT_DATA[k]=(orbits,nonorient)
assert [len(INV[k]) for k in range(6)]==[1,1,2,0,0,0]

def rank(M):
 if not M:return 0
 B=[[Fraction(v) for v in row] for row in M]
 rows=len(B);cols=len(B[0]);rr=0
 for col in range(cols):
  pivot=next((i for i in range(rr,rows) if B[i][col]),None)
  if pivot is None:continue
  B[rr],B[pivot]=B[pivot],B[rr]
  factor=B[rr][col]
  B[rr]=[v/factor for v in B[rr]]
  for i in range(rows):
   if i!=rr and B[i][col]:
    coeff=B[i][col]
    B[i]=[a-coeff*b for a,b in zip(B[i],B[rr])]
  rr+=1
  if rr==rows:break
 return rr

R={0:0}
for k in range(1,6):
 M=[[0]*len(INV[k]) for _ in INV[k-1]]
 for j,(rep,orbit) in enumerate(INV[k]):
  boundary=Counter()
  for f,sgn in orbit.items():
   vs=[i for i in range(N) if f>>i&1]
   for ii,v in enumerate(vs):boundary[f^(1<<v)]+=sgn*(-1 if ii%2 else 1)
  for i,(r,base) in enumerate(INV[k-1]):
   M[i][j]=boundary[r]
   assert all(boundary[f]==M[i][j]*sg for f,sg in base.items())
 R[k]=rank(M)
assert R=={0:0,1:0,2:1,3:0,4:0,5:0}
BETTI={k:len(INV[k])-R[k]-R.get(k+1,0)-(1 if k==0 else 0) for k in range(6)}
assert BETTI=={0:0,1:0,2:1,3:0,4:0,5:0}
print('PASS: graph (12,18), bad triples 144, face vector (12,66,76,45,12,2).')
print('PASS: 56 elementary collapses; 11 tree edges; 28 CW cancellations; 18 free loops and 4 nullattached two-cells.')
print('PASS: 48 graph automorphisms, invariant chain ranks', [len(INV[k]) for k in range(6)], ', boundary ranks',R)
print('PASS: full symmetry quotient has reduced rational Betti 1 in degree 2, 0 otherwise.')
