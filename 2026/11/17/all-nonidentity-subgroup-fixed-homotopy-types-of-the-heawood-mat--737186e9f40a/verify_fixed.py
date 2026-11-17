from itertools import permutations,combinations
from collections import defaultdict,deque,Counter
from functools import lru_cache
import json, pathlib
# Fano plane nonzero binary triple, lines are closed under XOR
points=tuple(range(1,8))
lines=tuple(sorted({tuple(sorted([x,y,x^y])) for x in points for y in points if x<y}))
assert len(lines)==7
# GL3(F2) from images of 1,2,4, invertible iff independent
basis=[]
for a,b,c in permutations(points,3):
 if a^b!=c: basis.append((a,b,c))
assert len(basis)==168
line_ids={line:i for i,line in enumerate(lines)}
vertex_index=lambda x:x-1

def perm_from_basis(abc):
 def im(x):
  a,b,c=abc
  return ((a if x&1 else 0)^(b if x&2 else 0)^(c if x&4 else 0))
 out=[]
 for x in points:out.append(im(x)-1)
 for line in lines:
  out.append(7+line_ids[tuple(sorted(im(y) for y in line))])
 return tuple(out)
G0=[perm_from_basis(b) for b in basis]
# dot product polarity: line perp to point

def dot(x,y):return (x&y).bit_count()%2
pol=[]
for x in points:
 lin=tuple(sorted(y for y in points if dot(x,y)==0))
 pol.append(7+line_ids[lin])
for lin in lines:
 perp=[x for x in points if all(dot(x,y)==0 for y in lin)]
 assert len(perp)==1
 pol.append(perp[0]-1)
pol=tuple(pol)
G=G0+[tuple(pol[g[j]] for j in range(14)) for g in G0]
assert len(set(G))==336
identity=tuple(range(14)); assert identity in G
G=sorted(G); gid={g:i for i,g in enumerate(G)}; e=gid[identity]
# group table
mul=[[gid[tuple(a[b[i]] for i in range(14))] for b in G] for a in G]
inv=[next(j for j in range(336) if mul[i][j]==e) for i in range(336)]
# enumeration by subgroup generators with fast bitset closure

# speed alternative subgroup closure via generators known from BFS
@lru_cache(maxsize=None)
def closure_pair(H,g):
 # H is subgroup, extend by g; right coset closure under H and g via left multiplication
 hlist=[i for i in range(336) if H>>i&1]
 seen=set(hlist)
 queue=deque(hlist)
 while queue:
  u=queue.popleft()
  v=mul[u][g]
  if v not in seen:
   seen.add(v);queue.append(v)
  # every new coset: generated left multiplications using elements H, but expensive
  for h in hlist:
   v=mul[u][h]
   if v not in seen:
    seen.add(v);queue.append(v)
 return sum(1<<h for h in seen)

# Exhaustive subgroup generation: any finite subgroup is reached by iteratively adjoining generators
subgroups=[1<<e]; subids={1<<e:0}
for H in subgroups:
 for g in range(336):
  if (H>>g)&1:continue
  J=closure_pair(H,g)
  if J not in subids:subids[J]=len(subgroups);subgroups.append(J)
print('subgroups',len(subgroups),flush=True)
assert len(subgroups)==413
# conj classes
conj=[];left=set(subgroups)
while left:
 H=min(left)
 # conjugate H by g
 gs=[i for i in range(336) if H>>i&1]
 c={sum(1<<mul[mul[g][h]][inv[g]] for h in gs) for g in range(336)}
 assert c<=left or not c.isdisjoint(left)
 conj.append((H,len(c),len(gs)))
 left-=c
print('classes',len(conj),flush=True)
assert len(conj)==23
# graph edges and group perms on edges
edges=[]
for i,li in enumerate(lines):
 for x in li:edges.append((x-1,7+i))
assert len(edges)==21
idx={e:i for i,e in enumerate(edges)}
eperms=[]
for g in G:
 eperms.append(tuple(idx[tuple(sorted((g[a],g[b])))] for a,b in edges))

# Independently enumerate the complete original matching complex in edge-bitmask form.
original=[(0,0)]
for i,(a,b) in enumerate(edges):
    conflict=(1<<a)|(1<<b)
    original += [(sel|(1<<i),occupied|conflict) for sel,occupied in original if not (occupied&conflict)]
original_faces={sel for sel,_ in original}
assert len(original_faces)==3462
bydimension=Counter(sel.bit_count()-1 for sel in original_faces if sel)
assert tuple(bydimension[i] for i in range(7))==(21,168,644,1218,1050,336,24)

def faces_for_H(H):
 hs=[i for i in range(336) if H>>i&1]
 unseen=set(range(21));parts=[]
 while unseen:
  i=min(unseen)
  orb={eperms[h][i] for h in hs}
  unseen-=orb
  mask=0
  for j in orb:
   for v in edges[j]:mask|=1<<v
  if mask.bit_count()==2*len(orb):parts.append((tuple(sorted(orb)),mask))
 k=len(parts)
 faces=[]
 for sel in range(1,1<<k):
  umask=0;ok=True
  for j in range(k):
   if sel>>j&1:
    if umask&parts[j][1]:ok=False;break
    umask|=parts[j][1]
  if ok:faces.append(sel)
 return parts,faces

def reduce_faces(faces):
 fs=set(faces);steps=[]
 while True:
  # free codim1 face plus unique coface; prune by trying greatest maximal face
  by_dim=sorted(fs,key=lambda x:(x.bit_count(),x),reverse=True)
  done=False
  for hi in by_dim:
   n=hi.bit_count()
   if n<=1: continue
   for j in range(hi.bit_length()):
    if hi>>j&1:
     lo=hi^(1<<j)
     if lo in fs and sum(1 for a in fs if a & lo == lo)==2:
      fs.remove(lo);fs.remove(hi);steps.append((lo,hi));done=True;break
   if done:break
  if not done:break
 return fs,steps

def ranks_f2(faces):
 by=defaultdict(list)
 for f in faces:by[f.bit_count()-1].append(f)
 ranks={};cycle={}
 for d in sorted(by):
  if d==0: continue
  lower={f:j for j,f in enumerate(by[d-1])}
  b=[]
  for f in by[d]:
   vec=0
   for j in range(f.bit_length()):
    if f>>j&1:vec^=1<<lower[f^(1<<j)]
   b.append(vec)
  piv={};rank=0
  for v in b:
   while v:
    k=v.bit_length()
    if k in piv:v^=piv[k]
    else:piv[k]=v;rank+=1;break
  ranks[d]=rank
 betti={d:len(x)-ranks.get(d,0)-ranks.get(d+1,0) for d,x in by.items()}
 betti[0]=betti.get(0,0)-1
 return {k:v for k,v in betti.items() if v}

rows=[]
for H,size,order in sorted(conj,key=lambda x:(x[2],x[1],x[0])):
 if order==1:continue
 parts,faces=faces_for_H(H)
 rem,steps=reduce_faces(faces)
 rows.append({'H':str(H),'order':order,'size':size,'n_orbits':len(parts),'n_faces':len(faces),'n_rem':len(rem),'dim_rem':max((f.bit_count()-1 for f in rem),default=-1),'betti':ranks_f2(faces),'remaining_faces':list(rem),'parts':parts,'steps':steps})
print('rows',len(rows),'status',(sum(a['size'] for a in rows)),flush=True)
for a in rows:
 print('order,size',a['order'],a['size'],'orbs',a['n_orbits'],'faces',a['n_faces'],'rem',a['n_rem'],'dim',a['dim_rem'],'b',a['betti'],flush=True)

package={'rows':rows,'edges':edges,'lines':lines,'groups':G,'subgroups_count':len(subgroups),'conj_class_count':len(conj)}
path=pathlib.Path(__file__).resolve().parent/'census.json'
assert path.exists(), 'census.json required beside verifier'
with path.open(encoding='utf-8') as fh: certificate=json.load(fh)
assert json.loads(json.dumps(package))==certificate, 'recomputed finite census differs from delivered certificate'
# Verify the full geometric fixed-point classification, not just homology ranks.
expected={'empty':46,'contractible':105,'S0':140,'three_points':30,'two_circles':42,'four_two_spheres':28,'circle_and_two_sphere':21}
counts={name:0 for name in expected}

def present_pi1(rem):
    fs=set(rem)
    vs=sorted(x.bit_length()-1 for x in fs if x.bit_count()==1)
    eds=sorted(tuple(j for j in vs if x>>j&1) for x in fs if x.bit_count()==2)
    triangles=sorted(tuple(j for j in vs if x>>j&1) for x in fs if x.bit_count()==3)
    parent={vs[0]}; tree=set()
    while len(parent)<len(vs):
        chosen=None
        for edge in eds:
            a,b=edge
            if (a in parent)^(b in parent):chosen=edge;break
        assert chosen is not None
        a,b=chosen
        tree.add(chosen);parent.add(a);parent.add(b)
    gens=[edge for edge in eds if edge not in tree]
    idg={edge:i+1 for i,edge in enumerate(gens)}
    def reduce_word(w):
        out=[]
        for letter in w:
            if out and out[-1]==-letter:out.pop()
            else:out.append(letter)
        while len(out)>1 and out[0]==-out[-1]:out=out[1:-1]
        return out
    rel=[]
    for a,b,c in triangles:
        w=[]
        for x,y in ((a,b),(b,c),(c,a)):
            g=idg.get(tuple(sorted((x,y))))
            if g is not None:w.append(g if x<y else -g)
        rel.append(reduce_word(w))
    active=set(range(1,len(gens)+1)); eliminations=[]
    while True:
        one=next((w[0] for w in rel if len(w)==1 and abs(w[0]) in active),None)
        if one is None:break
        active.remove(abs(one));eliminations.append(one)
        rel=[reduce_word([x for x in w if abs(x)!=abs(one)]) for w in rel]
    return {'generators':len(gens),'eliminations':eliminations,'remaining':sorted(active),'remaining_relations':rel}

for a in rows:
    F=set(a['remaining_faces']);b={str(k):v for k,v in a['betti'].items()}
    if not F:
        typ='empty'
    elif all(x.bit_count()==1 for x in F):
        typ={1:'contractible',2:'S0',3:'three_points'}[len(F)]
    elif a['dim_rem']==1:
        # The fully reduced complex must be a connected graph with two independent cycles.
        vs=sum(f.bit_count()==1 for f in F)
        es=sum(f.bit_count()==2 for f in F)
        assert es-vs+1==2 and b=={'1':2}
        typ='two_circles'
    elif b=={'1':1,'2':1}:
        # After elementary collapses there is the join of a four-cycle and two points,
        # together with a length-two arc attached at the join's suspension vertices.
        assert len(F)==29 and len([x for x in F if x.bit_count()==3])==8
        triangles={tuple(j for j in range(9) if x>>j&1) for x in F if x.bit_count()==3}
        cycle=[(1,3),(3,2),(2,4),(4,1)]
        assert triangles=={tuple(sorted((*ab,s))) for ab in cycle for s in (5,6)}
        assert {x for x in F if x.bit_count()==2 and x&1}=={(1<<0)|(1<<5),(1<<0)|(1<<6)}
        typ='circle_and_two_sphere'
    elif b=={'2':4}:
        assert a['dim_rem']==2 and len(F)==73
        pi=present_pi1(F)
        assert pi['generators']==23 and len(pi['eliminations'])==23
        assert pi['remaining']==[] and all(not x for x in pi['remaining_relations'])
        # Simply connected finite 2-complex with Euler characteristic five has
        # H_2=Z^4 and is homotopy equivalent to a wedge of four 2-spheres.
        typ='four_two_spheres'
    else:
        raise AssertionError('unclassified residual complex: '+str(a))
    counts[typ]+=a['size']
assert counts==expected,(counts,expected)
assert sum(counts.values())==412
print('ALL_HEAWOOD_MATCHING_SUBGROUP_FIXED_HOMOTOPY_TYPES_PASS',flush=True)
print(json.dumps(counts,sort_keys=True),flush=True)
print('subgroups=413;conjugacy_classes=23;nonidentity=412;nonidentity_classes=22',flush=True)


