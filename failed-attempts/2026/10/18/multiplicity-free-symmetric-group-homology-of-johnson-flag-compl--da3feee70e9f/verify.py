"""Exact face-action and symmetric-function checks for Johnson flag-complex homology.
Uses only Python's standard library."""
import itertools,math

def parts(n,low=1):
 if n==0: yield []
 else:
  for k in range(low,n+1):
   for v in parts(n-k,k): yield [k]+v

def perm_from_parts(parts):
 a=[]
 for length in parts:
  i=len(a);a.extend(list(range(i+1,i+length))+[i])
 return a

def sgn_map_order(old,new):
 pos={x:i for i,x in enumerate(old)};perm=[pos[x] for x in new]
 return (-1)**sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))

def trial(n,k):
 V=list(itertools.combinations(range(n),k));vertex={v:i for i,v in enumerate(V)}
 ed=[(i,j) for i in range(len(V)) for j in range(i+1,len(V)) if len(set(V[i])&set(V[j]))==k-1]
 ss=[tuple(i for i,v in enumerate(V) if set(a)<set(v)) for a in itertools.combinations(range(n),k-1)]
 ts=[tuple(i for i,v in enumerate(V) if set(v)<set(a)) for a in itertools.combinations(range(n),k+1)]
 faces=set((i,) for i in range(len(V)))|set(ed)
 for block in ss+ts:
  for j in range(3,len(block)+1):faces.update(itertools.combinations(block,j))
 counts={}
 for f in faces:counts[len(f)]=counts.get(len(f),0)+1
 print('FACES',n,k,sorted(counts.items()))
 for p in parts(n):
  x=perm_from_parts(p)
  vp=[vertex[tuple(sorted(x[t] for t in v))] for v in V]
  chis=0
  for f in faces:
   z=tuple(sorted(vp[t] for t in f))
   if z==f:
    chis+=(-1)**(len(f)-1)*sgn_map_order([vp[t] for t in f],list(f))
  lef=chis-1
  # correctly count fixed set k-subsets
  fixedv=sum(tuple(sorted(x[t] for t in v))==v for v in V)
  fixeds=sum(set(x[t] for t in ac)==set(ac) for ac in itertools.combinations(range(n),k-1))
  fixedt=sum(set(x[t] for t in ac)==set(ac) for ac in itertools.combinations(range(n),k+1))
  edgechar=0
  for i,j in ed:
   if {vp[i],vp[j]}=={i,j}:edgechar+=1 if (vp[i]==i and vp[j]==j) else -1
  fd=sum(tuple(sorted(x[t] for t in v))==v and tuple(sorted(x[t] for t in a))==a for v in V for a in itertools.combinations(v,k-1))
  fu=sum(tuple(sorted(x[t] for t in v))==v and tuple(sorted(x[t] for t in b))==b for v in V for b in itertools.combinations(range(n),k+1) if set(v).issubset(b))
  out=fixeds+fixedt+edgechar+fixedv-fd-fu-1
  if lef!=out:
   print('FAIL',p,'chi',lef,'formula',out);return False
 print('PASS',len(list(parts(n))),'conjugacy classes')
 return True



from collections import Counter
from itertools import product

def partitions(n,maxpart=None):
 if maxpart is None:maxpart=n
 if n==0:yield ()
 else:
  for x in range(min(n,maxpart),0,-1):
   for rest in partitions(n-x,x):yield(x,)+rest

def horiz(lam,m):
 n=sum(lam)+m
 for mu in partitions(n):
  if all((mu[i] if i<len(mu) else 0) >= (lam[i] if i<len(lam) else 0) >= (mu[i+1] if i+1<len(mu) else 0) for i in range(max(len(lam),len(mu)))):yield mu

def vert(lam,m):
 for mu in partitions(sum(lam)+m):
  if all(0 <= (mu[i] if i<len(mu) else 0) -(lam[i] if i<len(lam) else 0) <=1 for i in range(max(len(lam),len(mu)))):yield mu

def schur_seq(seq):
 rep=Counter({():1})
 for typ,m in seq:
  r=Counter()
  for lam,v in rep.items():
   for x in (horiz(lam,m) if typ=='h' else vert(lam,m)):r[x]+=v
  rep=r
 return rep

def coeff(n,k):
 terms=[(+1,[('h',k-1),('e',2),('h',n-k-1)]),
        (+1,[('h',k-1),('h',n-k+1)]),
        (+1,[('h',k),('h',n-k)]),
        (+1,[('h',k+1),('h',n-k-1)]),
        (-1,[('h',k-1),('h',1),('h',n-k)]),
        (-1,[('h',k),('h',1),('h',n-k-1)]),
        (-1,[('h',n)])]
 r=Counter()
 for sign, seq in terms:
  for lam,v in schur_seq(seq).items():r[lam]+=sign*v
 return {lam:v for lam,v in sorted(r.items(),reverse=True) if v}



def core_betti(n,k):
 vertices=list(itertools.combinations(range(n),k))
 index={v:i for i,v in enumerate(vertices)}
 edges=[(i,j) for i in range(len(vertices)) for j in range(i+1,len(vertices)) if len(set(vertices[i])&set(vertices[j]))==k-1]
 eidx={e:i for i,e in enumerate(edges)}
 blocks=[]
 for a in itertools.combinations(range(n),k-1):
  blocks.append(sorted(index[a+(x,)] if tuple(a+(x,)) in index else index[tuple(sorted(a+(x,)))] for x in range(n) if x not in a))
 for b in itertools.combinations(range(n),k+1):
  blocks.append(sorted(index[tuple(x for x in b if x!=s)] for s in b))
 triangles=[]
 for block in blocks:
  apex=block[0]
  triangles.extend((apex,x,y) for x,y in itertools.combinations(block[1:],2))
 piv={}
 for a,b,c in triangles:
  vec=(1<<eidx[(a,b)])^(1<<eidx[(a,c)])^(1<<eidx[(b,c)])
  while vec:
   bit=vec.bit_length()-1
   if bit in piv:vec^=piv[bit]
   else:
    piv[bit]=vec;break
 assert len(piv)==len(edges)-len(vertices)+1
 beta=len(triangles)-len(piv)
 want=len(vertices)-len(edges)+sum(math.comb(len(block)-1,2) for block in blocks)-1
 assert beta==want
 print('CORE',n,k,'vertices',len(vertices),'edges',len(edges),'triangles',len(triangles),'rank_d2',len(piv),'beta2',beta)
 return beta

def verify():
 for n,k in [(8,4),(9,4),(10,5),(12,5)]:
  result=coeff(n,k)
  expected={(n-j-2,j,1,1):1 for j in range(1,k)}
  assert result==expected,(n,k,result,expected)
  print('SPECHT',n,k,result)
 for n,k in [(8,4),(9,4)]:
  core_betti(n,k)
 assert trial(8,4)
 print('VERIFY_OK')

if __name__=='__main__':verify()
