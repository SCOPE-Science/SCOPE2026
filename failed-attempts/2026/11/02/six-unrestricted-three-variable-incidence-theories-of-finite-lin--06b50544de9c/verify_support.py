from itertools import product,combinations
from collections import defaultdict

def inv(a,q):return pow(a,-1,q)
def norm(v,q):
 for x in v:
  if x%q:
   z=inv(x%q,q)
   return tuple(y*z%q for y in v)
 raise ValueError

def geom(kind,d,q):
 vec=list(product(range(q), repeat=d+(kind=='PG')))
 if kind=='AG':
  points=vec
  line_sets={frozenset(tuple((a[i]+t*b[i])%q for i in range(d)) for t in range(q)) for a in points for b in vec if any(b)}
 else:
  points=sorted({norm(v,q) for v in vec if any(v)})
  line_sets=set()
  for u,v in combinations(points,2):
   ss=frozenset(norm(tuple((a*u[i]+b*v[i])%q for i in range(d+1)),q) for a in range(q) for b in range(q) if a or b)
   if len(ss)==q+1: line_sets.add(ss)
 lines=sorted(line_sets,key=lambda x:tuple(sorted(x)))
 return points,lines

def profiles(points,lines):
 n=len(points);m=len(lines);N=n+m
 inc=[[p in lines[j] for j in range(m)] for p in points]
 sets=[set(i for i in range(n) if inc[i][j]) for j in range(m)]
 def color(a,b):
  if a<n and b<n: return 'PP=' if a==b else 'PP!='
  if a>=n and b>=n:
   if a==b:return 'LL='
   return 'LLM' if sets[a-n]&sets[b-n] else 'LLD'
  if a<n:return 'PL+' if inc[a][b-n] else 'PL-'
  return 'LP+' if inc[b][a-n] else 'LP-'
 # First verify type supports uniform in same geometry.
 cs=[[color(a,b) for b in range(N)] for a in range(N)]
 possible={};bad=[]
 for a in range(N):
  for b in range(N):
   t=cs[a][b]
   pat=set((cs[a][z],cs[b][z]) for z in range(N))
   if t not in possible:possible[t]=pat
   elif possible[t]!=pat:
    bad.append((t,a,b,sorted(possible[t]^pat)))
 return {t:sorted(s) for t,s in sorted(possible.items())},bad

def edge_geometry(n):
 from itertools import combinations
 return list(range(n)), [frozenset(x) for x in combinations(range(n),2)]

if __name__=='__main__':
 import json,hashlib
 examples={
  'projective_plane_2':geom('PG',2,2),
  'projective_plane_3':geom('PG',2,3),
  'affine_plane_2':geom('AG',2,2),
  'affine_plane_3':geom('AG',2,3),
  'affine_plane_5':geom('AG',2,5),
  'affine_space_3_2':geom('AG',3,2),
  'affine_space_3_3':geom('AG',3,3),
  'projective_space_3_2':geom('PG',3,2),
  'projective_space_3_3':geom('PG',3,3),
  'affine_space_4_2':geom('AG',4,2),
  'projective_space_4_2':geom('PG',4,2),
 }
 for n in range(3,9): examples[f'edge_geometry_{n}']=edge_geometry(n)
 groups={}
 for name,obj in examples.items():
  tab,bad=profiles(*obj)
  assert not bad,(name,bad[:1])
  serial=json.dumps(tab,sort_keys=True)
  h=hashlib.sha256(serial.encode()).hexdigest()[:20]
  groups.setdefault(h,[]).append(name)
  print(name,'points',len(obj[0]),'lines',len(obj[1]),'profile_sha256_prefix',h)
 assert len(groups)==6,groups
 assert any(set(names)>={'affine_space_3_2','projective_space_3_2','affine_space_3_3','projective_space_3_3','edge_geometry_6','edge_geometry_7','edge_geometry_8'} for names in groups.values())
 assert any(set(names)>={'affine_plane_2','edge_geometry_4'} for names in groups.values())
 assert any(set(names)>={'projective_plane_2','projective_plane_3'} for names in groups.values())
 assert any(set(names)>={'affine_plane_3','affine_plane_5'} for names in groups.values())
 for g,names in sorted(groups.items()):print('CLASS',g,','.join(sorted(names)))
 print('PASS: six pair-extension-support classes and uniformity in every example')
