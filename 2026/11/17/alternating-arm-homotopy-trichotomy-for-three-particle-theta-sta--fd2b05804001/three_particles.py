import itertools as it,collections,sys,time,json,hashlib,datetime

def calc(m=3,L=4,n=3,alt=False,flip=False):
 vs=[('p',0),('p',1)]+[('v',a,j) for a in range(m) for j in range(1,L)]
 es=[('e',a,j) for a in range(m) for j in range(L)]
 def edgevs(e):
  _,a,j=e
  return [ ('p',0) if j==0 else ('v',a,j), ('p',1) if j+1==L else ('v',a,j+1) ]
 def cover(x):return {x} if x[0]!='e' else set(edgevs(x))
 ccov={x:cover(x) for x in vs+es}
 C=[[] for _ in range(n+1)]
 for c in it.combinations(vs+es,n):
  if len(set.union(*(ccov[x] for x in c)))!=sum(len(ccov[x]) for x in c):continue
  k=sum(x[0]=='e' for x in c)
  C[k].append(tuple(sorted(c)))
 C=[sorted(set(z)) for z in C]
 print('cells',m,[len(c) for c in C],flush=True)
 faces={}
 cs=[set(x) for x in C]
 for k in range(1,n+1):
  for c in C[k]:
   fs=[]
   for i,x in enumerate(c):
    if x[0]!='e':continue
    for v in ccov[x]:
     sub=tuple(sorted(c[:i]+(v,)+c[i+1:]))
     if sub in cs[k-1]:fs.append(sub)
   faces[c]=tuple(fs)
 allacts=[(p,r) for p in it.permutations(range(m)) if not alt or sum(p[i]>p[j] for i in range(m) for j in range(i+1,m))%2==0 for r in ([0,1] if flip else [0])]
 def actx(x,perm,r):
  if x[0]=='p':return ('p',1-x[1] if r else x[1])
  if x[0]=='v':return ('v',perm[x[1]],L-x[2] if r else x[2])
  return ('e',perm[x[1]],L-1-x[2] if r else x[2])
 def actc(c,perm,r):return tuple(sorted(actx(x,perm,r) for x in c))
 keycache={}
 def canonical(chain):
  if chain not in keycache:
   keycache[chain]=min(tuple(actc(c,perm,r) for c in chain) for perm,r in allacts)
  return keycache[chain]
 orbs=[set() for _ in range(n+1)]
 # DFS chains top-down
 def fchains(chain):
  orbs[len(chain)-1].add(canonical(chain))
  last=chain[0]
  for k in range(sum(x[0]=='e' for x in last)):
   for c in suball[last][k]:fchains((c,)+chain)
 suball={}
 for k in range(n+1):
  for c in C[k]:
   d={j:set() for j in range(k)}; current={c}
   for j in range(k-1,-1,-1):
    current=set(t for s in current for t in faces[s]);d[j]=current
   suball[c]=d
 for k in range(n+1):
  for c in C[k]:fchains((c,))
 orbs=[sorted(x) for x in orbs]
 print('orbits',m,[len(x) for x in orbs],flush=True)
 ids=[{x:i for i,x in enumerate(layer)} for layer in orbs]
 bd=[]
 for k in range(1,n+1):
  b=[[] for _ in orbs[k]]
  for j,ch in enumerate(orbs[k]):
   for i in range(k+1):b[j].append((ids[k-1][canonical(ch[:i]+ch[i+1:])], (-1)**i))
  bd.append(b)
 # elementary collapse iterate coface count
 active=[set(range(len(o))) for o in orbs]
 collapsed=[]
 while True:
  found=None
  for k in range(n,0,-1):
   count=collections.defaultdict(list)
   for j in active[k]:
    for i,z in bd[k-1][j]:
     if i in active[k-1]:count[i].append(j)
   opts=sorted((i,L[0]) for i,L in count.items() if len(L)==1)
   if opts:
    found=(k,opts[0]);break
  if found is None:break
  k,(i,j)=found
  active[k-1].remove(i);active[k].remove(j);collapsed.append((k,i,j))
 print('collapse',m,alt,flip,'pairs',len(collapsed),'remaining',[len(x) for x in active],flush=True)
 return orbs,bd,active,collapsed
def check_final(orbs,bd,active):
  # Incidence counts, not just Betti numbers: elementary collapses must leave
  # exactly a cycle, a triangulated sphere, or a point.
  sizes=[len(z) for z in active]
  if sizes==[1,0,0,0]:return {'kind':'point','cells':sizes}
  # Each edge has two endpoints (face ranks are distinct), and the 1-skeleton is connected.
  edges={j:[i for i,_ in bd[0][j]] for j in active[1]}
  assert all(len(set(vs))==2 and all(v in active[0] for v in vs) for vs in edges.values())
  ad={v:set() for v in active[0]}
  for e,vs in edges.items():
   ad[vs[0]].add(vs[1]);ad[vs[1]].add(vs[0])
  seen={next(iter(active[0]))}; stack=list(seen)
  while stack:
   for z in ad[stack.pop()]:
    if z not in seen:seen.add(z);stack.append(z)
  assert seen==active[0]
  if sizes[2]==sizes[3]==0:
   assert len(active[0])==len(active[1])
   assert all(sum(v in endpoints for endpoints in edges.values())==2 for v in active[0])
   return {'kind':'circle','cells':sizes,'connected':True,'all_vertex_degrees':2}
  assert sizes[3]==0 and sizes[2]>0
  tri={j:[i for i,_ in bd[1][j]] for j in active[2]}
  assert all(len(set(es))==3 and all(e in active[1] for e in es) for es in tri.values())
  incident={e:[] for e in active[1]}
  for t,es in tri.items():
   for e in es:incident[e].append(t)
  assert all(len(x)==2 for x in incident.values())
  for v in active[0]:
   incident_edges={e for e,end in edges.items() if v in end}
   assert incident_edges
   link={e:set() for e in incident_edges}
   for t,es in tri.items():
    pair=[e for e in es if e in incident_edges]
    if pair:
     assert len(pair)==2
     link[pair[0]].add(pair[1]);link[pair[1]].add(pair[0])
   assert all(len(ns)==2 for ns in link.values())
   reached={next(iter(link))}; stack=list(reached)
   while stack:
    for z in link[stack.pop()]:
     if z not in reached:reached.add(z);stack.append(z)
   assert reached==set(link)
  assert len(active[0])-len(active[1])+len(active[2])==2
  return {'kind':'sphere','cells':sizes,'connected':True,'all_edge_degrees':2,'all_vertex_links':'cycles','euler_characteristic':2}

if __name__=='__main__':
 results=[]
 for m,alt in [(3,False),(3,True),(4,True)]:
  orbs,bd,active,collapsed=calc(m,4,3,alt,False)
  topology=check_final(orbs,bd,active)
  sequence=';'.join('%d,%d,%d'%entry for entry in collapsed).encode('ascii')
  results.append({'arms':m,'group':'A_'+str(m) if alt else 'S_'+str(m),'orbit_chain_counts':[len(x) for x in orbs], 'collapse_pairs':len(collapsed),'collapse_certificate_sha256':hashlib.sha256(sequence).hexdigest(),'remaining':topology})
 print('RESULT_JSON_BEGIN')
 print(json.dumps({'schema_version':1,'configurations':3,'edges_per_arm':4,'results':results,'stability':'Every chain of cubical faces uses <=3 distinct arms; S_m is 3-transitive for m>=3, A_m is 3-transitive for m>=5, hence all m>=5 alternating quotients have the same orbit-chain complex as the S_3 quotient.'},indent=2,sort_keys=True))
 print('RESULT_JSON_END')
