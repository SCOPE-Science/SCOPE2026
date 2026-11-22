import sys,time,collections
from quot import qcomplex

def collapse(basis, n, verbose=False):
 gmaps=[[ (eps*i+k)%n for i in range(n)] for eps in (1,-1) for k in range(n)]
 transforms=[{f:sum(1<<mp[i] for i in range(n) if f>>i&1) for f in {face for B in basis for flag in B for face in flag}} for mp in gmaps]
 def can(flag):return min(tuple(m[f] for f in flag) for m in transforms)
 dims=len(basis); idx=[{f:i for i,f in enumerate(B)} for B in basis]
 cofaces=[[set() for c in B] for B in basis]
 bd=[[] for d in range(dims)]
 for d,B in enumerate(basis):
  bb=[]
  for c in B:
   if d:
    ids=[idx[d-1][can(c[:k]+c[k+1:])] for k in range(d+1)]
    bb.append(ids)
    for q in ids:cofaces[d-1][q].add((d,idx[d][c]))
   else:bb.append([])
  bd[d]=bb
 alive=[[True]*len(B) for B in basis]
 # max heap of cells (dim,-lower index,-upper index)
 import heapq
 heap=[]
 for d in range(1,dims):
  for q in range(len(basis[d-1])):
   if len(cofaces[d-1][q])==1:
    _,top=next(iter(cofaces[d-1][q]));heapq.heappush(heap,(-d,q,top))
 pairs=[]
 while heap:
  md,q,top=heapq.heappop(heap);d=-md
  if not alive[d-1][q] or not alive[d][top] or cofaces[d-1][q]!={(d,top)}:continue
  alive[d-1][q]=False;alive[d][top]=False;pairs.append((d-1,q,d,top))
  # remove lower faces of both cells: for d-1 cell, dimension d-2 and d cell dimension d-1
  for e,z in ((d-1,q),(d,top)):
   if e:
    for lo in bd[e][z]:
     cofaces[e-1][lo].discard((e,z))
     if alive[e-1][lo] and len(cofaces[e-1][lo])==1:
      D,TOP=next(iter(cofaces[e-1][lo]));heapq.heappush(heap,(-D,lo,TOP))
 remain=[sum(x) for x in alive]
 if verbose:print('after',remain,'pairs',len(pairs),flush=True)
 return alive,pairs

if __name__=='__main__':
 for n in range(int(sys.argv[1]),int(sys.argv[2])+1):
  t=time.time();B,D=qcomplex(n)
  alive,pairs=collapse(B,n,True)
  print(n,len(B),time.time()-t)
