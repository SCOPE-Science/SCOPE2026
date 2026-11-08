"""Exhaustive stable-config burning census, distinct from addition-orbit verifier.
No third-party dependencies; Python 3.10+.
"""
from itertools import product
from collections import Counter

def graphs():
 cube=tuple(tuple(v^(1<<j) for j in range(3)) for v in range(8))
 octa=tuple(tuple(w for w in range(6) if w//2!=v//2) for v in range(6))
 return [('Q3',cube),('Octahedron',octa)]

def recurrent(h,adj):
 remaining=set(range(1,len(adj)))
 while remaining:
  burning={v for v in remaining if h[v]>=sum(w in remaining for w in adj[v])}
  if not burning:return False
  remaining-=burning
 return True

def avalanche(h,adj,site):
 z=list(h);z[site]+=1
 topp=[0]*len(adj)
 for cycle in range(10000):
  v=next((j for j in range(1,len(adj)) if z[j]>=len(adj[j])),None)
  if v is None:
   return tuple(topp),sum(topp[w] for w in adj[0])
  z[v]-=len(adj[v]);topp[v]+=1
  for w in adj[v]:
   if w!=0:z[w]+=1
 raise AssertionError('no stabilization')

EXPECTED={
 'Q3':{'recurrent':384,'zero_avalanche':1162,'zero_burst':1226,'positive_nondiss':64,'total':2688},
 'Octahedron':{'recurrent':384,'zero_avalanche':1133,'zero_burst':1133,'positive_nondiss':0,'total':1920},
}
def census(name,adj):
 n=len(adj);sizes=Counter();bursts=Counter();nrec=0;nd=0
 for x in product(*(range(len(adj[v])) for v in range(1,n))):
  h=(0,)+x
  if not recurrent(h,adj):continue
  nrec+=1
  for v in range(1,n):
   top,b=avalanche(h,adj,v)
   k=sum(top);sizes[k]+=1;bursts[b]+=1
   nd+=(k>0 and b==0)
 out=dict(recurrent=nrec,zero_avalanche=sizes[0],zero_burst=bursts[0],positive_nondiss=nd,total=sum(sizes.values()))
 assert out==EXPECTED[name],(name,out)
 print(name,'PASS',out)
 return sizes,bursts

if __name__=='__main__':
 for name,adj in graphs():census(name,adj)
