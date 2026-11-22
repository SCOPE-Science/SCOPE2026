"""Exact endpoint-local magnitude homology of the 18-vertex Pappus graph.
Requires Python 3 and SymPy. Prints complete integral Smith evidence.
"""
from collections import Counter, deque
from itertools import product
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

N=18
S=[5,7,-7,7,-7,-5]*3
edges={tuple(sorted((i,(i+1)%N))) for i in range(N)}
edges|={tuple(sorted((i,(i+S[i])%N))) for i in range(N)}
adj={i:set() for i in range(N)}
for a,b in edges:adj[a].add(b);adj[b].add(a)
assert len(edges)==27 and all(len(adj[x])==3 for x in adj)
dist={}
for s in range(N):
 d={s:0};q=deque([s]);
 while q:
  u=q.popleft()
  for v in adj[u]:
   if v not in d:d[v]=d[u]+1;q.append(v)
 assert len(d)==N
 dist[s]=d

# All magnitude chains have fixed endpoints and total length four.
def chains(x,z,k):
 out=[]
 def extend(path,length):
  if len(path)==k:
   y=path[-1]
   if y!=z and length+dist[y][z]==4:out.append(tuple(path)+(z,))
   return
  for y in range(N):
   if y==path[-1]:continue
   D=dist[path[-1]][y]
   if length+D+(k-len(path))>4 or length+D+dist[y][z]>4:continue
   extend(path+[y],length+D)
 extend([x],0)
 return out

def boundary(higher,lower):
 look={c:i for i,c in enumerate(lower)}
 b=[[0]*len(higher) for _ in lower]
 for j,c in enumerate(higher):
  for i in range(1,len(c)-1):
   if dist[c[i-1]][c[i+1]]==dist[c[i-1]][c[i]]+dist[c[i]][c[i+1]]:
    b[look[c[:i]+c[i+1:]]][j]+=(-1)**i
 return Matrix(b)

def smith_diag(b):
 if b.rows==0 or b.cols==0:return []
 m=smith_normal_form(b,domain=ZZ)
 return [abs(int(m[i,i])) for i in range(min(b.rows,b.cols)) if m[i,i]]

rank_profile=Counter(); size_profile=Counter(); matrices=0
for x in range(N):
 for z in range(N):
  c2,c3,c4=(chains(x,z,k) for k in (2,3,4))
  b3,b4=boundary(c3,c2),boundary(c4,c3)
  assert b3*b4==Matrix.zeros(len(c2),len(c4))
  s3,s4=smith_diag(b3),smith_diag(b4)
  assert all(i==1 for i in s4), ('torsion in C3/im B4',x,z,s4)
  assert all(i==1 for i in s3), ('nonprimitive d3',x,z,s3)
  h3=len(c3)-len(s3)-len(s4)
  assert h3>=0
  # Saturated image(d4) in C3 proves torsion-free H3.
  rank_profile[(dist[x][z],h3)]+=1
  size_profile[(dist[x][z],len(c2),len(c3),len(c4),len(s3),len(s4))]+=1
  matrices+=2
print('vertices',N,'edges',len(edges),'diameter',max(max(d.values()) for d in dist.values()))
print('distance/homology multiplicities',sorted(rank_profile.items()))
print('chain/boundary profiles',sorted(size_profile.items()))
print('homology free rank',sum(h*count for (_,h),count in rank_profile.items()))
print('checked exact integral boundary matrices',matrices)
print('ALL EXACT SMITH DIAGONALS UNITS: PASS')
