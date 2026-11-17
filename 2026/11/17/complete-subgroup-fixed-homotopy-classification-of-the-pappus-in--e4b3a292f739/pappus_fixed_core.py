"""Exact subgroup-fixed independence-complex calculation for the Pappus graph.

All finite data are reconstructed from the LCF presentation; no graph packages needed.
To regenerate a certificate: python pappus_fixed_core.py generate
To verify the supplied certificate: python pappus_fixed_core.py verify pappus_fixed_certificate.json
"""
import collections, itertools, json, random, sys, hashlib
from collections import deque
N=18
LCF=[5,7,-7,7,-7,-5]*3
adj=[set() for _ in range(N)]
for u in range(N):
 for v in ((u+1)%N,(u+LCF[u])%N):
  adj[u].add(v);adj[v].add(u)
assert len({tuple(sorted((u,v))) for u in range(N) for v in adj[u]})==27
assert all(len(a)==3 for a in adj)
D=[]
for u in range(N):
 dist=[99]*N;dist[u]=0;todo=deque([u])
 while todo:
  a=todo.popleft()
  for b in adj[a]:
   if dist[b]==99:dist[b]=dist[a]+1;todo.append(b)
 D.append(dist)
order=[0];visited={0}
for u in order:
 for v in sorted(adj[u]):
  if v not in visited:visited.add(v);order.append(v)
permp=[-1]*N;used=[False]*N;perms=[]
def back(k):
 if k==N:
  p=tuple(permp)
  assert all((v in adj[u])==(p[v] in adj[p[u]]) for u in range(N) for v in range(N))
  perms.append(p);return
 u=order[k]
 for v in range(N):
  if used[v]:continue
  if all(D[u][order[j]]==D[v][permp[order[j]]] for j in range(k)):
   used[v]=True;permp[u]=v;back(k+1);used[v]=False;permp[u]=-1
back(0);perms.sort();assert len(perms)==216
idx={p:i for i,p in enumerate(perms)};identity=idx[tuple(range(N))];size=len(perms)
Mul=[[idx[tuple(a[b[j]] for j in range(N))] for b in perms] for a in perms]
Inv=[idx[tuple(a.index(j) for j in range(N))] for a in perms]
assert all(Mul[i][Inv[i]]==identity for i in range(size))

def generate(H,g):
 if g in H:return H
 old=set(H);todo=[g];old.add(g);hs=list(H)+[g]
 while todo:
  x=todo.pop()
  for h in hs:
   for y in (Mul[x][h],Mul[h][x]):
    if y not in old:old.add(y);todo.append(y)
 return frozenset(old)

sub=[frozenset([identity])];seen={sub[0]};i=0
while i<len(sub):
 H=sub[i]
 for g in range(size):
  if g not in H:
   Q=generate(H,g)
   if Q not in seen:seen.add(Q);sub.append(Q)
 i+=1
assert len(sub)==380
# A subgroup is closed if its multiplication table stays inside it. Check every result.
for H in sub:
 assert identity in H
 assert all(Inv[h] in H for h in H)
 assert all(Mul[a][b] in H for a in H for b in H)
remaining=set(sub);classes=[]
while remaining:
 H=min(remaining,key=lambda H:(len(H),tuple(sorted(H))))
 orbit={frozenset(Mul[Mul[a][h]][Inv[a]] for h in H) for a in range(size)}
 assert orbit<=remaining
 classes.append((H,len(orbit)));remaining-=orbit
assert len(classes)==44 and sum(c for _,c in classes)==380

def fixed_model(H):
 rest=set(range(N));orbs=[]
 while rest:
  u=min(rest);orb=tuple(sorted({perms[h][u] for h in H}));rest.difference_update(orb);orbs.append(orb)
 eligible=[orb for orb in orbs if all(v not in adj[u] for u,v in itertools.combinations(orb,2))]
 k=len(eligible)
 conflict=[0]*k
 for i in range(k):
  for j in range(i):
   if any(v in adj[u] for u in eligible[i] for v in eligible[j]):
    conflict[i]|=1<<j;conflict[j]|=1<<i
 faces=[]
 for mask in range(1,1<<k):
  if all(not(conflict[i]&mask) for i in range(k) if mask&(1<<i)):
   faces.append(mask)
 return eligible,faces

def toggle_matching(faces,order):
 unmatched=set(faces);pairs=[]
 for v in order:
  bit=1<<v
  for f in sorted(tuple(unmatched),key=lambda f:(f.bit_count(),f)):
   q=f|bit
   if not f&bit and f in unmatched and q in unmatched:
    unmatched.remove(f);unmatched.remove(q);pairs.append((f,q))
 return sorted(unmatched),pairs

def critical_sig(unmatched):
 return [[d,c] for d,c in sorted(collections.Counter(f.bit_count()-1 for f in unmatched).items())]

def check_acyclic(faces,pairs):
 # Orient each face-poset cover downward except selected pairs, oriented upward.
 S=set(faces);selected=set(pairs);indeg={f:0 for f in S};edges={f:[] for f in S};count=0
 for hi in faces:
  for bit in range(N):
   if not hi>>bit&1:continue
   lo=hi^(1<<bit)
   if not lo:continue
   assert lo in S
   a,b=(lo,hi) if (lo,hi) in selected else (hi,lo)
   edges[a].append(b);indeg[b]+=1;count+=1
 Q=deque(f for f,n in indeg.items() if n==0);visited=0
 while Q:
  f=Q.popleft();visited+=1
  for b in edges[f]:
   indeg[b]-=1
   if indeg[b]==0:Q.append(b)
 assert visited==len(faces),(visited,len(faces))
 return count

def signature_type(sig):
 if not sig:return 'empty' # no simplices
 if sig==[[0,1]]:return 'point'
 if sig==[[0,2]]:return 'two_points'
 if sig==[[0,3]]:return 'three_points'
 if len(sig)==1 and sig[0][0]==0: return str(sig[0][1])+'_points'
 assert sig[0]==[0,1] and len(sig)==2 and sig[1][0]>=1
 return 'wedge_'+str(sig[1][1])+'_S'+str(sig[1][0])

def main():
 mode=sys.argv[1] if len(sys.argv)>1 else 'verify'
 path=sys.argv[2] if len(sys.argv)>2 else 'pappus_fixed_certificate.json'
 if mode=='generate':
  cert=[]
  for ci,(H,c) in enumerate(classes):
   eligible,faces=fixed_model(H); k=len(eligible)
   rng=random.Random(83529+ci)
   opts=[list(range(k)),list(reversed(range(k)))]
   opts += [rng.sample(range(k),k) for _ in range(160 if len(H)==1 else 55)]
   best=None
   for order in opts:
    unmatched,pairs=toggle_matching(faces,order)
    score=(len(unmatched),len([f for f in unmatched if f.bit_count()>1]),tuple(order))
    if best is None or score<best[0]:best=(score,order,unmatched)
   sig=critical_sig(best[2]);assert not (sig and len(sig)>2), (ci,sig)
   if len(sig)==2:assert sig[0]==[0,1]
   cert.append({'class_index':ci,'subgroup':sorted(H),'conjugates':c,'pivot_order':best[1],
        'critical_faces':best[2], 'critical_dimensions':sig})
  with open(path,'w',encoding='utf8') as f: json.dump({'schema_version':1,'graph':'Pappus LCF [5,7,-7,7,-7,-5]^3','class_representatives':cert},f,indent=2);f.write('\n')
  print('GENERATED',path)
 elif mode=='verify':
  with open(path,encoding='utf8') as f:raw=json.load(f)
  cert=raw['class_representatives'];assert len(cert)==len(classes)
  table=collections.Counter();cv=collections.Counter();total_pairs=0;total_covers=0
  for ci,(H,c) in enumerate(classes):
   ent=cert[ci]
   assert ent['class_index']==ci and ent['subgroup']==sorted(H) and ent['conjugates']==c
   eligible,faces=fixed_model(H); assert sorted(ent['pivot_order'])==list(range(len(eligible)))
   unmatched,pairs=toggle_matching(faces,ent['pivot_order'])
   assert unmatched==ent['critical_faces'] and critical_sig(unmatched)==ent['critical_dimensions']
   assert len(pairs)*2+len(unmatched)==len(faces)
   if faces:
    total_covers+=check_acyclic(faces,pairs)
    total_pairs+=len(pairs)
   typ=signature_type(ent['critical_dimensions'])
   if not faces:assert not unmatched;typ='empty'
   table[typ]+=c;cv[typ]+=1
  print('PAPPUS_GRAPH vertices=18 edges=27 automorphisms=216')
  print('ALL_SUBGROUPS=380 CONJUGACY_CLASSES=44')
  print('CHECKED_PAIRS',total_pairs,'CHECKED_HASSE_COVERS',total_covers)
  for typ in sorted(table):print('TYPE',typ,'subgroups',table[typ],'classes',cv[typ])
  assert sum(table.values())==380 and sum(cv.values())==44
  assert table['wedge_10_S4']==1
  assert table['wedge_2_S3']==9 and table['wedge_2_S2']==18
  assert all(k in {'empty','point','two_points','three_points','wedge_1_S1','wedge_2_S1','wedge_1_S2','wedge_2_S2','wedge_2_S3','wedge_10_S4'} for k in table)
  print('PAPPUS_INDEPENDENCE_ALL_SUBGROUP_FIXED_HOMOTOPY_PASS')
 else:raise ValueError(mode)
if __name__=='__main__':main()
