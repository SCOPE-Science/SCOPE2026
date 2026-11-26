"""Exact integral cubical computation for two unordered points on four-arm theta graph.
Python standard library only; run `python theta4_verifier.py`."""
from collections import deque
from itertools import combinations, permutations

M=4
N=2+2*M
arms=[(2+2*i,3+2*i) for i in range(M)]
E=[]
for a,b in arms:E.extend([(0,a),(a,b),(b,1)])
V0=list(combinations(range(N),2))
V1=[(e,x) for e,(u,v) in enumerate(E) for x in range(N) if x not in (u,v)]
V2=[(i,j) for i,j in combinations(range(len(E)),2) if set(E[i]).isdisjoint(E[j])]
idx0={t:i for i,t in enumerate(V0)}
idx1={t:i for i,t in enumerate(V1)}
idxe={frozenset(t):i for i,t in enumerate(E)}
D1=[]
for e,x in V1:
 u,v=E[e]
 D1.append({idx0[tuple(sorted((v,x)))]:1,idx0[tuple(sorted((u,x)))]:-1})
D2=[]
for ei,ej in V2:
 a,b=E[ei];c,d=E[ej]
 col={idx1[(ej,b)]:1,idx1[(ej,a)]:-1,idx1[(ei,d)]:-1,idx1[(ei,c)]:1}
 D2.append(col)

def cycle(i,j):
 ai,bi=arms[i];aj,bj=arms[j]
 P=[(0,1),(ai,1),(ai,bj),(bi,bj),(bi,aj),(1,aj),(1,0)]
 z={}
 for src,dst in zip(P,P[1:]):
  ss,dd=set(src),set(dst)
  s=next(iter(ss-dd));t=next(iter(dd-ss));x=next(iter(ss&dd))
  e=idxe[frozenset((s,t))];sgn=1 if E[e]==(s,t) else -1
  k=idx1[(e,x)];z[k]=z.get(k,0)+sgn
 return {x:y for x,y in z.items() if y}

def boundary1(z):
 d={}
 for k,c in z.items():
  for v,s in D1[k].items():d[v]=d.get(v,0)+c*s
 return {v:c for v,c in d.items() if c}

# Collapse every 2-cube along a free 1-cell, retaining exact substitution records.
faces=[set() for _ in V1]
for j,bd in enumerate(D2):
 for k in bd:faces[k].add(j)
q=deque(k for k in range(len(V1)) if len(faces[k])==1)
removed1=set();removed2=set();steps=[]
while q:
 k=q.popleft()
 if k in removed1 or len(faces[k])!=1:continue
 j=next(iter(faces[k])); assert j not in removed2
 removed1.add(k);removed2.add(j);steps.append((k,j))
 for t in D2[j]:
  faces[t].discard(j)
  if len(faces[t])==1:q.append(t)
assert len(removed2)==len(V2)

def reduce(z):
 z=dict(z)
 for k,j in steps:
  coeff=z.pop(k,0)
  if coeff:
   pivot=D2[j][k]
   for t,a in D2[j].items():
    if t!=k:z[t]=z.get(t,0)-coeff*a//pivot
 return {k:c for k,c in z.items() if c}

# Spanning tree in the surviving graph; chord coordinates give an integral H1 basis.
keep=[k for k in range(len(V1)) if k not in removed1]
parent=list(range(len(V0)))
def find(i):
 while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
 return i
chords=[];tree=[]
for k in keep:
 verts=list(D1[k]);a,b=map(find,verts)
 if a!=b:parent[a]=b;tree.append(k)
 else:chords.append(k)
assert len(tree)==len(V0)-1 and len(chords)==M*(M-1)//2
P=list(combinations(range(M),2))
Z=[cycle(i,j) for i,j in P]
assert all(not boundary1(z) for z in Z)
assert all(not boundary1(b) for b in D2)
C=[[reduce(z).get(k,0) for z in Z] for k in chords]

def determinant(A):
 A=[list(map(int,row)) for row in A];n=len(A);sgn=1;prev=1
 for i in range(n-1):
  if A[i][i]==0:
   swap=next(j for j in range(i+1,n) if A[j][i])
   A[i],A[swap]=A[swap],A[i];sgn*=-1
  p=A[i][i]
  for j in range(i+1,n):
   for k in range(i+1,n):
    num=A[j][k]*p-A[j][i]*A[i][k];assert num%prev==0
    A[j][k]=num//prev
   A[j][i]=0
  prev=p
 return sgn*A[-1][-1]

assert abs(determinant(C))==1,('integral basis failure',C)

def perm_image(z,p,flip):
 vm={0:1 if flip else 0,1:0 if flip else 1}
 for i,(a,b) in enumerate(arms):
  aa,bb=arms[p[i]]
  vm[a]=bb if flip else aa
  vm[b]=aa if flip else bb
 out={}
 for k,c in z.items():
  e,x=V1[k];a,b=E[e]
  e2=idxe[frozenset((vm[a],vm[b]))]
  sign=1 if E[e2]==(vm[a],vm[b]) else -1
  t=idx1[(e2,vm[x])];out[t]=out.get(t,0)+c*sign
 return {k:c for k,c in out.items() if c}

for p in permutations(range(M)):
 for flip in (False,True):
  for r,(i,j) in enumerate(P):
   a,b=p[i],p[j]
   expected=(-1 if a>b else 1)*(-1 if flip else 1)
   t=P.index(tuple(sorted((a,b))))
   image=perm_image(Z[r],p,flip)
   delta=image.copy()
   for k,c in Z[t].items():delta[k]=delta.get(k,0)-expected*c
   assert not any(reduce(delta).values()),('symmetry failed',p,flip,i,j)
print('PASS: vertices=%d one_cells=%d two_cells=%d free_square_collapses=%d graph_chords=%d integral_det=%d group_maps=%d'%(len(V0),len(V1),len(V2),len(steps),len(chords),determinant(C),48*len(P)))
print('Integral H1 basis is represented by the 6 two-arm exchange cycles.')
print('All 48 group elements act as pole-sign tensor exterior-square of the 4-arm permutation lattice.')
print('H0=Z, H1=Z^6 and Hk=0 for k>=2; all checked via elementary collapses.')
