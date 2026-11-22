from itertools import combinations
from collections import defaultdict

def make():
 n=16; bad=[]
 def d(a,b):return (a%4!=b%4)+(a//4!=b//4)
 for a,b,c in combinations(range(n),3):
  if d(a,b)+d(b,c)==d(a,c) or d(b,a)+d(a,c)==d(b,c) or d(a,c)+d(c,b)==d(a,b):bad.append((1<<a)|(1<<b)|(1<<c))
 return {s for s in range(1,1<<16) if not any(s&t==t for t in bad)}

def homology(faces,p):
 dims=defaultdict(list)
 for f in faces:dims[f.bit_count()-1].append(f)
 ranks={}
 for d in range(1,max(dims)+1):
  idx={x:i for i,x in enumerate(dims[d-1])}
  pivots={}
  for face in dims[d]:
   ids=[i for i in range(16) if face>>i&1]
   v={idx[face^(1<<i)]:(-1)**j%p for j,i in enumerate(ids)}
   while v:
    pivot=max(v);pv=pivots.get(pivot)
    if pv is None:
     mult=pow(v[pivot],-1,p)
     pivots[pivot]={k:c*mult%p for k,c in v.items()}
     break
    factor=v[pivot]
    for k,c in pv.items():
     new=(v.get(k,0)-factor*c)%p
     if new:v[k]=new
     else:v.pop(k,None)
  ranks[d]=len(pivots)
 return {d:len(fs)-ranks.get(d,0)-ranks.get(d+1,0) for d,fs in dims.items()},ranks

faces=make()
for p in [2,3,5]:
 h,r=homology(faces,p)
 print('field',p,'homology',dict(sorted(h.items())),'boundary_ranks',r,flush=True)
