"""Exact integer and combinatorial verification of the Petersen line-graph neighborhood complex.
Run: python3 verify.py (Python standard library only)."""
from itertools import combinations, permutations
from collections import deque, Counter, defaultdict

V = list(combinations(range(5),2))
P = [(i,j) for i,u in enumerate(V) for j,v in enumerate(V) if j>i and set(u).isdisjoint(v)]
N = len(P)
EI = {tuple(sorted((V[i],V[j]))):k for k,(i,j) in enumerate(P)}
H = [(i,j) for i,(a,b) in enumerate(P) for j,(c,d) in enumerate(P) if j>i and len({a,b}&{c,d})>0]
nei=[sum(1<<j for j in range(N) if i!=j and tuple(sorted((i,j))) in H) for i in range(N)]
faces={0}
for n in nei:
 f=n
 while True:
  faces.add(f)
  if f==0: break
  f=(f-1)&n
faces.remove(0)
assert len(faces)==180
fvec=tuple(sum(f.bit_count()==k for f in faces) for k in range(1,5))
assert fvec==(15,90,60,15)
# direct test for absence of four-cycles; equivalent: pairwise common-neighbor count <= 1.
assert all((nei[i]&nei[j]).bit_count()<=1 for i in range(N) for j in range(i+1,N))
# Verify toggle matching acyclic on full directed Hasse diagram.
remaining=set(faces); pairs=[]
for bit in range(N):
 for f in sorted(remaining):
  if not(f>>bit&1) and f|(1<<bit) in remaining:
   h=f|(1<<bit); remaining.remove(f);remaining.remove(h);pairs.append((f,h))
assert len(pairs)==74 and Counter(x.bit_count()-1 for x in remaining)=={0:1,1:31}
matched=set(pairs)
indegree={f:0 for f in faces}; out={f:[] for f in faces};count=0
for f in faces:
 for i in range(N):
  if f>>i&1:
   g=f^(1<<i)
   if g==0:continue
   # Reverse matched edge and orient other edges downwards.
   if (g,f) in matched: u,v=g,f
   else:u,v=f,g
   out[u].append(v);indegree[v]+=1;count+=1
assert count==sum(k*sum(f.bit_count()==k for f in faces) for k in range(1,5))-15
q=deque(f for f,d in indegree.items() if d==0);vis=0
while q:
 u=q.popleft();vis+=1
 for v in out[u]:
  indegree[v]-=1
  if indegree[v]==0:q.append(v)
assert vis==len(faces)

# Equivariant graph model B: bipartite double cover of H.
B=sorted([(i,N+j) for i,j in H]+[(j,N+i) for i,j in H]);ED={e:i for i,e in enumerate(B)}
assert len(B)==60
adj=[[] for _ in range(2*N)]
for j,(a,b) in enumerate(B):adj[a].append((b,j));adj[b].append((a,j))
seen={0};parent={};q=deque([0]);tree=[]
while q:
 u=q.popleft()
 for v,j in adj[u]:
  if v not in seen:seen.add(v);parent[v]=(u,j);tree.append(j);q.append(v)
assert len(seen)==30 and len(tree)==29
chords=[j for j in range(60) if j not in set(tree)];assert len(chords)==31
# Fundamental oriented edge cycles with chord coefficient exactly +1.
cycles=[]
for chord in chords:
 a,b=B[chord];ancestors={a};z=a
 while z in parent:z=parent[z][0];ancestors.add(z)
 path=[];z=b
 while z not in ancestors:
  pa,j=parent[z];path.append((z,pa,j));z=pa
 meet=z;path2=[];z=a
 while z!=meet:
  pa,j=parent[z];path2.append((z,pa,j));z=pa
 vec={chord:1}
 for x,y,j in path+[(y,x,j) for x,y,j in reversed(path2)]:
  vec[j]=vec.get(j,0)+(1 if B[j]==(x,y) else -1)
 bd=[0]*30
 for j,c in vec.items():x,y=B[j];bd[x]-=c;bd[y]+=c
 assert bd==[0]*30
 cycles.append(vec)

def get_perm(p):
 q={i:V.index(tuple(sorted(p[x] for x in v))) for i,v in enumerate(V)}
 return [EI[tuple(sorted((V[q[a]],V[q[b]])))] for a,b in P]

def action(p):
 q=get_perm(p)
 eperm=[ED[(q[a],N+q[b-N])] for a,b in B]
 inv=[0]*60
 for i,j in enumerate(eperm):inv[j]=i
 return [[cycles[j].get(inv[ch],0) for j in range(31)] for ch in chords]

# Compute exact Smith invariant factors with integral elementary row/column operations.
def smith_diag(data):
 A=[r[:] for r in data]; nr=len(A); nc=len(A[0]);k=0;steps=0
 while k<min(nr,nc):
  poss=[(abs(A[i][j]),i,j) for i in range(k,nr) for j in range(k,nc) if A[i][j]]
  if not poss:break
  _,i,j=min(poss);A[k],A[i]=A[i],A[k]
  for row in A:row[k],row[j]=row[j],row[k]
  while True:
   steps+=1
   assert steps<250000
   pivot=A[k][k];assert pivot
   change=False
   for i in range(k+1,nr):
    if not A[i][k]:continue
    quo=A[i][k]//pivot
    if quo:A[i]=[a-quo*b for a,b in zip(A[i],A[k])]
    if A[i][k]:A[k],A[i]=A[i],A[k]
    change=True;break
   if change:continue
   for j in range(k+1,nc):
    if not A[k][j]:continue
    quo=A[k][j]//pivot
    if quo:
     for i in range(nr):A[i][j]-=quo*A[i][k]
    if A[k][j]:
     for row in A:row[k],row[j]=row[j],row[k]
    change=True;break
   if change:continue
   # Divisibility condition fixes invariant-factor order, not only diagonalization.
   bad=next(((i,j) for i in range(k+1,nr) for j in range(k+1,nc) if A[i][j]%pivot),None)
   if bad:
    i,j=bad;A[k]=[a+b for a,b in zip(A[k],A[i])]
    continue
   break
  if A[k][k]<0:A[k]=[-x for x in A[k]]
  assert all(A[i][k]==0 for i in range(k+1,nr))
  assert all(A[k][j]==0 for j in range(k+1,nc))
  k+=1
 assert all(A[i][j]==0 for i in range(nr) for j in range(nc) if i!=j)
 d=[A[i][i] for i in range(k)]
 assert all(d[i+1]%d[i]==0 for i in range(len(d)-1))
 return d

I=[[int(i==j) for j in range(31)] for i in range(31)]
p1=(1,0,2,3,4);p2=(1,2,3,4,0)
A1=action(p1);A2=action(p2)
R=[[A1[i][j]-I[i][j] for j in range(31)]+[A2[i][j]-I[i][j] for j in range(31)] for i in range(31)]
d=smith_diag(R)
assert Counter(d)=={1:29,2:2}
# Verify character via two distinct methods, for every group element: signed Lefschetz on X,
# and cellular fixed-vertex/edge trace on the double cover B.
def sgn(order):return -1 if sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))%2 else 1
chars=defaultdict(set);sizes=Counter()
for p in permutations(range(5)):
 q=get_perm(p)
 trace=0
 for f in faces:
  inds=[i for i in range(N) if f>>i&1]
  img=[q[i] for i in inds]
  if set(img)==set(inds):trace+=(-1)**(len(inds)-1)*sgn([inds.index(j) for j in img])
 ch=1-trace
 fixedv=sum(q[i]==i for i in range(N))
 fixedarcs=sum(q[a]==a and q[b-N]==b-N for a,b in B)
 # Each undirected edge of B corresponds to a directed edge of H, fixed iff its endpoints fixed.
 assert ch==1-2*fixedv+fixedarcs
 seen=set();ct=[]
 for u in range(5):
  if u in seen:continue
  x=u;t=0
  while x not in seen:seen.add(x);t+=1;x=p[x]
  ct.append(t)
 cls=tuple(sorted(ct,reverse=True));chars[cls].add(ch);sizes[cls]+=1
assert all(len(x)==1 for x in chars.values())
expect={(1,1,1,1,1):31,(2,1,1,1):1,(2,2,1):-5,(3,1,1):1,(3,2):1,(4,1):-1,(5,):1}
assert {k:next(iter(v)) for k,v in chars.items()}==expect
assert sum(sizes[k]*v for k,v in expect.items())==0
print('Petersen-line neighborhood: vertices=15 edges=30 faces=180 fvector='+str(fvec))
print('Morse matching: 74 pairs; critical=(0:1, 1:31); full Hasse DAG verified')
print('Double-cover model: vertices=30 edges=60 spanning-tree=29, cycle rank=31')
print('Exact integral coinvariants S5: Smith factors 1 x29, 2 x2')
print('All 120 simplicial Lefschetz and double-cover traces agree: '+str(sorted(expect.items())))
print('PASS')
