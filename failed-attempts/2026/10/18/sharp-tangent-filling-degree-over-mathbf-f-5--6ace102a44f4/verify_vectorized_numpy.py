#!/usr/bin/env python3
"""Optional separate vectorized enumeration; requires NumPy."""
import numpy as np,time
p=5;mon=[(a,b,3-a-b) for a in range(3,-1,-1) for b in range(3-a,-1,-1)]
pts=[(x,y,1) for x in range(p) for y in range(p)]+[(x,1,0) for x in range(p)]+[(1,0,0)]
V=np.array([[np.prod([a**e for a,e in zip(pt,m)])%p for m in mon] for pt in pts],dtype=np.int16)
D=[np.array([[m[t]*np.prod([a**(e-(j==t)) for j,(a,e) in enumerate(zip(pt,m))])%p if m[t] else 0 for m in mon]for pt in pts],dtype=np.int16) for t in range(3)]
lines=np.zeros(125,dtype=np.uint32)
for x in range(p):
 for y in range(p):
  for z in range(p):
   if x==y==z==0:continue
   lines[x+5*y+25*z]=sum(1<<j for j,pt in enumerate(pts) if (x*pt[0]+y*pt[1]+z*pt[2])%5==0)
full=(1<<31)-1
count=0;accepted=0;start=time.monotonic()
for first in range(10):
 dim=9-first;total=5**dim
 for lo in range(0,total,10000):
  ids=np.arange(lo,min(total,lo+10000),dtype=np.int32)
  A=np.zeros((len(ids),10),dtype=np.int16);A[:,first]=1
  for k in range(first+1,10):
   A[:,k]=ids%5;ids//=5
  Q=(A@V.T)%5;D0=(A@D[0].T)%5;D1=(A@D[1].T)%5;D2=(A@D[2].T)%5
  covered=np.zeros(len(A),dtype=np.uint32)
  for j in range(31):
   loc=(Q[:,j]==0)&((D0[:,j]!=0)|(D1[:,j]!=0)|(D2[:,j]!=0))
   idx=(D0[:,j]+5*D1[:,j]+25*D2[:,j])
   covered|=np.where(loc,lines[idx],0)
  count+=len(A);accepted+=np.count_nonzero(covered==full)
 print('first leading index',first,'processed',count,'accepted',accepted,flush=True)
print('vectorized numpy census',count,accepted,'seconds',time.monotonic()-start)
