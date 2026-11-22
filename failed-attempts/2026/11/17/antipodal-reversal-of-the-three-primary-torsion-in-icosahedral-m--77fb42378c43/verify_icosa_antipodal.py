"""Exact finite-field proof checker for antipodal homology of the icosahedral matching complex.
Python 3 standard library only. All simplices and matrices reconstructed from the 30 edges.
"""
from collections import Counter,deque

EDGES=[(0,1),(0,5),(0,7),(0,8),(0,11),(1,2),(1,5),(1,6),(1,8),
 (2,3),(2,6),(2,8),(2,9),(3,4),(3,6),(3,9),(3,10),(4,5),(4,6),
 (4,10),(4,11),(5,6),(5,11),(7,8),(7,9),(7,10),(7,11),(8,9),
 (9,10),(10,11)]
assert len(EDGES)==30 and EDGES==sorted(EDGES)
adj={i:set() for i in range(12)}
for u,v in EDGES:adj[u].add(v);adj[v].add(u)
assert all(len(s)==5 for s in adj.values())
triangles=sum(all(v in adj[u] for u,v in [(a,b),(a,c),(b,c)])
              for a in range(12) for b in range(a+1,12) for c in range(b+1,12))
assert triangles==20

def distances(root):
 d={root:0};queue=deque([root])
 while queue:
  u=queue.popleft()
  for v in adj[u]:
   if v not in d:d[v]=d[u]+1;queue.append(v)
 return d
TAU={v:next(u for u,d in distances(v).items() if d==3) for v in range(12)}
assert all(TAU[TAU[v]]==v for v in TAU)
assert all(tuple(sorted((TAU[u],TAU[v]))) in EDGES for u,v in EDGES)
edge_index={edge:i for i,edge in enumerate(EDGES)}
tau_edges=[edge_index[tuple(sorted((TAU[u],TAU[v])))] for u,v in EDGES]
levels=[[] for _ in range(7)]
def enumerate_matchings(start,used,face):
 levels[len(face)].append(face)
 for j in range(start,len(EDGES)):
  u,v=EDGES[j]
  if (used>>u)&1 or (used>>v)&1:continue
  enumerate_matchings(j+1,used|(1<<u)|(1<<v),face+(j,))
enumerate_matchings(0,0,())
assert [len(x) for x in levels]==[1,30,315,1400,2535,1482,125]

def image(face):
 x=[tau_edges[e] for e in face]
 sign=(-1)**sum(x[i]>x[j] for i in range(len(x)) for j in range(i+1,len(x)))
 return tuple(sorted(x)),sign
for faces in levels:
 for f in faces:
  tf,s=image(f)
  assert image(tf)==(f,s)
  for j in range(len(f)):
   assert f[:j]+f[j+1:] in levels[len(f)-1]

def eigen_basis(faces,eps):
 reps=[];where={}
 for f in faces:
  if f in where:continue
  tf,sign=image(f)
  if tf==f and sign!=eps:continue
  k=len(reps);reps.append(f)
  where[f]=(k,1)
  if tf!=f:where[tf]=(k,eps*sign)
 return reps,where

def rank(columns,prime):
 pivots={}
 for col in columns:
  vec={}
  for r,c in col:
   t=(vec.get(r,0)+c)%prime
   if t:vec[r]=t
   else:vec.pop(r,None)
  while vec:
   pivot=min(vec)
   if pivot not in pivots:
    inv=pow(vec[pivot],-1,prime)
    pivots[pivot]={r:(v*inv)%prime for r,v in vec.items()}
    break
   c=vec[pivot]
   for r,v in pivots[pivot].items():
    t=(vec.get(r,0)-c*v)%prime
    if t:vec[r]=t
    else:vec.pop(r,None)
 return len(pivots)

def eigen_ranks(prime,eps):
 b=[eigen_basis(f,eps) for f in levels]
 dims=[len(reps) for reps,_ in b];ranks=[0]
 for j in range(1,len(levels)):
  reps,_=b[j];prev,ind=b[j-1]
  columns=[]
  for f in reps:
   tf,s=image(f)
   terms=[(f,1)] if f==tf else [(f,1),(tf,eps*s)]
   col=[]
   for g,coef in terms:
    for k in range(len(g)):
     sub=g[:k]+g[k+1:]
     if sub in ind and sub==prev[ind[sub][0]]:
      col.append((ind[sub][0],coef*(-1)**k))
   columns.append(col)
  ranks.append(rank(columns,prime))
 betti=[dims[j]-ranks[j]-ranks[j+1] for j in range(1,6)]
 return dims,ranks,betti

def full_ranks(prime):
 ranks=[0]
 for j in range(1,len(levels)):
  prev={s:k for k,s in enumerate(levels[j-1])}
  cols=[[(prev[f[:i]+f[i+1:]],(-1)**i) for i in range(j)] for f in levels[j]]
  ranks.append(rank(cols,prime))
 return ranks

EXPECTED={
 (3,1):([1,15,150,700,1290,741,55],[0,1,14,136,564,686,55],[0,0,0,40,0]),
 (3,-1):([0,15,165,700,1245,741,70],[0,0,15,150,550,670,70],[0,0,0,25,1]),
 (5,1):([1,15,150,700,1290,741,55],[0,1,14,136,564,686,55],[0,0,0,40,0]),
 (5,-1):([0,15,165,700,1245,741,70],[0,0,15,150,550,671,70],[0,0,0,24,0]),
}
for prime in (3,5):
 s=[]
 for eps in (1,-1):
  got=eigen_ranks(prime,eps)
  assert got==EXPECTED[(prime,eps)],(prime,eps,got)
  s.append(got)
  print('prime',prime,'antipodal_eigenvalue',eps,'chain_dimensions',got[0],
        'boundary_ranks',got[1],'reduced_betti_deg0_to4',got[2])
 full=full_ranks(prime)
 assert full==[s[0][1][k]+s[1][1][k] for k in range(7)]
 assert full==( [0,1,29,286,1114,1357,125] if prime==5 else
               [0,1,29,286,1114,1356,125] ),full
 print('prime',prime,'independent_full_chain_boundary_ranks',full)
print('ICOSAHEDRAL_ANTIPODAL_TORSION_SIGN_PASS')
