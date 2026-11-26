import itertools, collections, functools
N=21

def build():
 a=[0]*21
 for i in range(7):
  for c in range(3):
   x=3*i+c
   for d in (-1,1):
    j=(i+d)%7
    for h in range(3):
     if h!=c: a[x]|=1<<(3*j+h)
 return a

def enum(a):
 f=[0]
 for i in range(N):
  bit=1<<i
  f+= [s|bit for s in f if not(s&a[i])]
 return set(f)

def match(faces,order):
 remaining=set(faces)-{0};pairs=[]
 for i in order:
  b=1<<i
  for l in sorted(remaining):
   if l in remaining and not(l&b) and l|b in remaining:
    h=l|b;remaining.remove(l);remaining.remove(h);pairs.append((l,h))
 return pairs,remaining

def sign(upper,lower):
 bit=upper^lower
 assert bit.bit_count()==1 and lower & upper == lower
 idx=(upper & (bit-1)).bit_count()
 return -1 if idx%2 else 1

def isacyclic(faces,pairs):
 down_up={a:b for a,b in pairs};in_deg={x:0 for x in faces if x}; edges={x:[] for x in faces if x}
 for g in edges:
  v=g
  while v:
   t=v&-v;v-=t;f=g^t
   if not f:continue
   if down_up.get(f)==g:
    edges[f].append(g);in_deg[g]+=1
   else:
    edges[g].append(f);in_deg[f]+=1
 q=collections.deque(v for v in in_deg if in_deg[v]==0);seen=0
 while q:
  x=q.popleft();seen+=1
  for y in edges[x]:
   in_deg[y]-=1
   if in_deg[y]==0:q.append(y)
 return seen==len(in_deg),seen,len(in_deg)

def morseboundary(pairs,crit,topdim=4):
 up={a:b for a,b in pairs};down={b:a for a,b in pairs}
 @functools.lru_cache(None)
 def r(f):
  if f in crit:return {f:1}
  if f in down:return {}
  g=up[f];sgn=sign(g,f);o=collections.Counter()
  v=g
  while v:
   t=v&-v;v-=t;lower=g^t
   if lower==f:continue
   for z,coeff in r(lower).items():o[z] += -sgn*sign(g,lower)*coeff
  return {x:k for x,k in o.items() if k}
 result={}
 for f in crit:
  if f.bit_count()!=topdim+1:continue
  o=collections.Counter()
  v=f
  while v:
   t=v&-v;v-=t;lower=f^t
   for z,coeff in r(lower).items():o[z]+=sign(f,lower)*coeff
  result[f]={x:y for x,y in o.items() if y}
 return result

if __name__=='__main__':
 G=build();F=enum(G);Yadj=G.copy();u=0;v=4;assert G[u]&(1<<v);Yadj[u]^=1<<v;Yadj[v]^=1<<u;Y=enum(Yadj)
 U=(1<<N)-1;allowed=U &~(G[u]|G[v]|(1<<u)|(1<<v));K={f for f in F if not f&~allowed}
 orders={
 'full':[3,10,4,0,19,15,18,13,8,9,14,12,17,5,2,16,7,6,11,1,20],
 'fault':[3,13,4,0,20,10,17,15,5,7,9,8,11,12,14,1,18,6,16,2,19],
 'link':[16,10,6,8,13,11,4,1,15,2,18,0,9,19,20,12,17,7,5,3,14]
 }
 expectations={"full":(2638,{0:1,3:1,4:3}),"fault":(2821,{0:1,4:3}),"link":(181,{0:1,2:1})}
 for name,fs in [("full",F),("fault",Y),("link",K)]:
  pairs,crit=match(fs,orders[name]);dims=dict(collections.Counter(x.bit_count()-1 for x in crit).items())
  assert len(pairs)==expectations[name][0] and dims==expectations[name][1]
  assert 2*len(pairs)+len(crit)==len(fs)-1
  assert isacyclic(fs,pairs)==(True,len(fs)-1,len(fs)-1)
  for lower,upper in pairs:
   assert lower in fs and upper in fs and (upper^lower).bit_count()==1 and upper&lower==lower
  if name=="full":
   boundary=morseboundary(pairs,crit,4)
   assert len(boundary)==3 and all(not v for v in boundary.values())
  print(name,"faces",len(fs),"pairs",len(pairs),"critical_dimensions",dims,"acyclic_PASS",flush=True)
 # Independent second enumeration over the entire Boolean cube, not merely known faces.
 for label,adj,faces in (("intact",G,F),("faulted",Yadj,Y)):
  ind=bytearray(1<<N);ind[0]=1;count=1
  for mask in range(1,1<<N):
   b=mask&-mask;i=b.bit_length()-1;p=mask^b
   ind[mask]=ind[p] and not(adj[i]&p)
   if ind[mask]:count+=1
   assert bool(ind[mask])==(mask in faces), (label,mask)
  assert count==len(faces)
  print(label,"independent-exhaustive-cube",count)
 assert F<=Y
 assert len(F)==5282 and len(Y)==5647 and len(K)==365
 extra=Y-F
 assert extra=={f | (1<<u) | (1<<v) for f in K}
 # Orbit argument: dihedral permutations of cycle positions and symmetric color
 # permutations act transitively on the set of graph edges.
 edge_set={(a,b) for a in range(N) for b in range(a+1,N) if (G[a]>>b)&1}
 orbit=set()
 for shift in range(7):
  for eps in (-1,1):
   for perm in itertools.permutations(range(3)):
    def phi(w):return 3*((eps*(w//3)+shift)%7)+perm[w%3]
    a,b=sorted([phi(u),phi(v)]);orbit.add((a,b))
 assert orbit==edge_set and len(orbit)==42, (len(orbit),len(edge_set))
 print("single-edge orbit",len(orbit))
 print("C7_K3_SINGLE_EDGE_FAULT_CERTIFICATE_OK")
