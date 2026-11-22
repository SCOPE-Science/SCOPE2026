from itertools import product, combinations
from math import prod

def construct(ns):
 vs=list(product(*(range(n) for n in ns)))
 idx={v:i for i,v in enumerate(vs)}
 nbs=[]
 for v in vs:
  b=0
  for i in range(len(ns)):
   for st in [-1,1]:
    w=list(v);w[i]+=st
    if 0<=w[i]<ns[i]:b|=1<<idx[tuple(w)]
  nbs.append(b)
 return vs,nbs

def direct(ns):
 vs,nbs=construct(ns);N=len(vs); p=[0,0,0,0,0]
 for k in range(5):
  for S in combinations(range(N),k):
   patterns=set()
   for row in nbs:
    mask=0
    for j,u in enumerate(S):
     if row>>u&1:mask|=1<<j
    patterns.add(mask)
    if len(patterns)==2**k:break
   if len(patterns)==2**k: p[k]+=1
 return p

def predicted(ns):
 d=len(ns);N=prod(ns)
 if N==1:return [1,0,0,0,0]
 one=N
 if d==1:
  two=max(0,ns[0]-4);three=0
 else:
  two=sum(max(0,ns[i]-2)*prod(ns[j] for j in range(d) if j!=i) for i in range(d))
  two+=sum(2*(ns[i]-1)*(ns[j]-1)*prod(ns[k] for k in range(d) if k not in (i,j)) for i,j in combinations(range(d),2))
  if d==2:
   two-=4
   if ns==[2,2] or ns==(2,2):two+=2
  if d==3:
   three=8*(int(all(n>=3 for n in ns)) + sum(max(0,n-3) for n in ns)+sum((ns[i]-2)*(ns[j]-2) for i,j in combinations(range(3),2))+prod(n-2 for n in ns))
  elif d>=4:
   three=sum(8*prod(ns[i]-1 for i in I)*prod(ns[k] for k in range(d) if k not in I) for I in combinations(range(d),3))
  else:three=0
 return [1,one,two,three,0]

if __name__=='__main__':
 import sys
 samples=[(2,),(3,),(4,),(5,),(6,),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4), (2,2,2),(2,2,3),(2,2,4),(2,3,3),(2,3,4),(3,3,3),(3,3,4),(2,2,2,2),(2,2,2,3),(2,2,2,2,2)]
 for ns in samples:
  if prod(ns)>36:continue
  a=direct(ns); b=predicted(ns)
  print(ns,a,b,'OK' if a==b else 'FAIL',flush=True)
  if a!=b:sys.exit(1)
 print('ALL_PATHBOX_NEIGHBORHOOD_CHECKS_PASS')
