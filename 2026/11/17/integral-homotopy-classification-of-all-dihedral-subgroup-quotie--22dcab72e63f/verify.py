"""Exact simplicial orbit-flag and elementary-collapse verification for the pentagonal wheel.

Python 3, standard library only. Quotients are ordinary geometric orbit spaces.
"""
import json
from collections import Counter,defaultdict

N=5
VERTICES=range(6)
RIM_EDGES=[tuple(sorted((i,1+(i%5)))) for i in range(1,6)]
SPOKES=[(0,i) for i in range(1,6)]
EDGES=sorted(RIM_EDGES+SPOKES)
GROUPS={
 'trivial':[(0,1)],
 'rotation_C5':[(s,1) for s in range(5)],
 'reflection_C2':[(0,1),(0,-1)],
 'full_D5':[(s,t) for s in range(5) for t in (1,-1)]
}

def atom_v(v):return ('v',v)
def atom_e(e):return ('e',e)
def cfg(*atoms):return tuple(sorted(atoms))
def rank(c):return sum(a=='e' for a,x in c)
def cell_boundary(c):
 result=[]
 for j,(typ,obj) in enumerate(c):
  if typ=='e':
   for x in obj:
    z=list(c);z[j]=atom_v(x)
    result.append(cfg(*z))
 return result

CELLS=[[],[],[]]
for a in VERTICES:
 for b in VERTICES:
  if a<b:CELLS[0].append(cfg(atom_v(a),atom_v(b)))
for v in VERTICES:
 for e in EDGES:
  if v not in e:CELLS[1].append(cfg(atom_v(v),atom_e(e)))
for i,e in enumerate(EDGES):
 for f in EDGES[i+1:]:
  if not (set(e)&set(f)):CELLS[2].append(cfg(atom_e(e),atom_e(f)))
CELL_SETS=[set(L) for L in CELLS]
assert len(CELL_SETS[0])==15 and len(CELL_SETS[1])==40 and len(CELL_SETS[2])==20
B1={c:cell_boundary(c) for c in CELLS[1]}
B2={c:cell_boundary(c) for c in CELLS[2]}
assert all(set(B1[c]).issubset(CELL_SETS[0]) for c in CELLS[1])
assert all(set(B2[c]).issubset(CELL_SETS[1]) for c in CELLS[2])

def face_flags():
 fs=[set() for _ in range(3)]
 for j in range(3):
  for c in CELLS[j]:fs[0].add((c,))
 for c,bs in B1.items():
  for b in bs:fs[1].add((b,c))
 for c2,bs in B2.items():
  for c1 in bs:
   fs[1].add((c1,c2))
   for c0 in B1[c1]:
    fs[1].add((c0,c2))
    fs[2].add((c0,c1,c2))
 return [sorted(t) for t in fs]
FLAGS=face_flags()

def group_action(c,g):
 shift,sgn=g
 def v(v):return 0 if v==0 else (shift+sgn*(v-1))%5+1
 return cfg(*[(typ,v(x) if typ=='v' else tuple(sorted(v(y) for y in x))) for typ,x in c])
def action_flag(flag,g):return tuple(group_action(c,g) for c in flag)
def quotient(group):
 canon=lambda flag:min(action_flag(flag,g) for g in group)
 orbit_flags=[sorted({canon(f) for f in flags}) for flags in FLAGS]
 ids=[{f:i for i,f in enumerate(L)} for L in orbit_flags]
 boundaries=[{}, {}, {}]
 for k in (1,2):
  for i,f in enumerate(orbit_flags[k]):
   boundaries[k][i]=[ids[k-1][canon(f[:j]+f[j+1:])] for j in range(k+1)]
   assert len(set(boundaries[k][i]))==k+1
 # Separate orbit enumeration via Burnside fixed-flag formula.
 burnside=[]
 for fs in FLAGS:
  total=sum(sum(action_flag(f,g)==f for f in fs) for g in group)
  assert total%len(group)==0
  burnside.append(total//len(group))
 assert burnside==list(map(len,orbit_flags))
 return orbit_flags,boundaries,burnside

def collapse(flags,bd):
 live=[set(range(len(x))) for x in flags]
 pairs=[]
 # Every move is an elementary free-face collapse in a regular triangulated orbit-flag CW complex.
 for k in (2,1):
  while True:
   neighbors=defaultdict(list)
   for i in sorted(live[k]):
    for e in bd[k][i]:neighbors[e].append(i)
   free=next(((f,inc[0]) for f,inc in sorted(neighbors.items()) if len(inc)==1 and f in live[k-1]),None)
   if free is None:break
   f,t=free
   assert len(neighbors[f])==1
   pairs.append((k,f,t))
   live[k-1].remove(f)
   live[k].remove(t)
 return live,pairs

def subgroup_completeness():
 all_g=GROUPS['full_D5']
 unit=(0,1)
 def mul(a,b):return ((a[0]+a[1]*b[0])%5,a[1]*b[1])
 subgroups=[]
 for bits in range(1<<len(all_g)):
  members={g for j,g in enumerate(all_g) if bits & (1<<j)}
  if unit not in members:continue
  if all(mul(x,y) in members for x in members for y in members):subgroups.append(members)
 assert Counter(map(len,subgroups))=={1:1,2:5,5:1,10:1}
 assert all(any(H=={mul(mul(g,x),((-g[1]*g[0])%5,g[1])) for x in rep}
                 for g in all_g for rep in map(set,GROUPS.values())) for H in subgroups)
 return len(subgroups)

def verify():
 assert subgroup_completeness()==8
 result={}
 for name,group in GROUPS.items():
  flags,bd,burn=quotient(group)
  live,pairs=collapse(flags,bd)
  dims=[len(s) for s in live]
  assert len(live[2])==0
  # Remaining graph must be connected. The quotient is connected, and collapses preserve it.
  verts=live[0]
  adjacency={v:set() for v in verts}
  for e in live[1]:
   a,b=bd[1][e]
   assert a in verts and b in verts and a!=b
   adjacency[a].add(b);adjacency[b].add(a)
  start=next(iter(verts));seen={start};todo=[start]
  while todo:
   for v in adjacency[todo.pop()]:
    if v not in seen:seen.add(v);todo.append(v)
  assert seen==verts
  beta1=len(live[1])-len(live[0])+1
  assert sum((-1)**i*len(flags[i]) for i in range(3))==1-beta1
  assert len(pairs)==len(flags[2])+(len(flags[0])-len(live[0]))
  result[name]={'group_order':len(group),'flag_cells_by_dim':list(map(len,flags)),
                'burnside_orbit_counts':burn,'collapse_pairs_2d':sum(k==2 for k,_,_ in pairs),
                'collapse_pairs_1d':sum(k==1 for k,_,_ in pairs),
                'residual_cells_by_dim':dims,'residual_graph_components':1,'circle_rank':beta1,
                'collapse_certificate':pairs}
 assert [result[g]['circle_rank'] for g in GROUPS]==[6,2,2,0]
 return result

if __name__=='__main__':
 print(json.dumps(verify(),sort_keys=True,separators=(',',':')))
