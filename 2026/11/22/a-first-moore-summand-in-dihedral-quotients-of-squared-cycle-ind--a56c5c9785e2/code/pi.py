from quot import qcomplex
from collapse import collapse
import collections,sys,time

def pi(n):
 B,_=qcomplex(n);active,pairs=collapse(B,n)
 # full orbit transformations
 maps=[[ (eps*i+k)%n for i in range(n)] for eps in (1,-1) for k in range(n)]
 facelist=set(f for c in B for flag in c for f in flag)
 transforms=[{f:sum(1<<mp[i] for i in range(n) if f>>i&1) for f in facelist} for mp in maps]
 def can(flag):return min(tuple(m[f] for f in flag) for m in transforms)
 edgeidx={f:i for i,f in enumerate(B[1])}
 vertidx={f:i for i,f in enumerate(B[0])}
 parent=list(range(len(B[0])))
 def root(x):
  while parent[x]!=x: x=parent[x]
  return x
 tree=set()
 for i,f in enumerate(B[1]):
  if not active[1][i]:continue
  a,b=(vertidx[can((x,))] for x in f)
  if root(a)!=root(b):parent[root(a)]=root(b);tree.add(i)
 genera={i:j+1 for j,i in enumerate(k for k in range(len(B[1])) if active[1][k] and k not in tree)}
 rel=[]
 for t,f in enumerate(B[2]):
  if not active[2][t]:continue
  edges=[edgeidx[can((f[0],f[1]))],edgeidx[can((f[1],f[2]))],edgeidx[can((f[0],f[2]))]]
  w=[genera.get(edges[0],0),genera.get(edges[1],0),-genera.get(edges[2],0)]
  w=tuple(x for x in w if x)
  rel.append(w)
 def inverse(w):return tuple(-x for x in w[::-1])
 def reduce(w,cyclic=True):
  st=[]
  for x in w:
   if st and st[-1]==-x:st.pop()
   else:st.append(x)
  if cyclic:
   while len(st)>1 and st[0]==-st[-1]:st=st[1:-1]
  return tuple(st)
 rel=[reduce(w) for w in rel]
 gens=set(genera.values());steps=0;maxlen=0;stuck=None
 while gens:
  occ=collections.Counter(abs(x) for w in rel for x in w)
  opts=[]
  for i,w in enumerate(rel):
   for z,x in enumerate(w):
    if sum(abs(y)==abs(x) for y in w)==1:
     opts.append((len(w), occ[abs(x)],i,z,abs(x)))
  if not opts:
   stuck={'generators':len(gens),'rels':len(rel),'lengths':collections.Counter(map(len,rel))};break
  _,_,i,z,g=min(opts)
  w=rel[i];q=w[:z]+w[z+1:]
  # conjugate cyclic: rotate to x first, then solve x * other =1
  t=w[z+1:]+w[:z];x=w[z]
  replacement=inverse(t) if x>0 else t
  def substitute(word):
   out=[]
   for y in word:
    if abs(y)==g:out+=replacement if y>0 else inverse(replacement)
    else:out.append(y)
   return reduce(out)
  rel=[substitute(z) for k,z in enumerate(rel) if k!=i]
  rel=[x for x in rel if x]
  gens.remove(g);steps+=1
  maxlen=max([maxlen]+[len(x) for x in rel]);
  if maxlen>10000 or sum(len(x) for x in rel)>100000:
   stuck={'generator':len(gens),'blowup':True};break
 return dict(n=n,edges=len(genera),originalrels=len(rel)+steps,eliminations=steps,stuck=stuck,maxlen=maxlen,remaining_gens=len(gens),tree=len(tree))

if __name__=='__main__':
 for n in range(int(sys.argv[1]),int(sys.argv[2])+1):
  t=time.time();print(pi(n),time.time()-t,flush=True)
