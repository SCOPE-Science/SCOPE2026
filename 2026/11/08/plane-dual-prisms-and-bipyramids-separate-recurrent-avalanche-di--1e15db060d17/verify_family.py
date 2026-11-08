"""Constructive check for the prism/bipyramid sandpile theorem.
Only the finite tests are computational; the all-n result is proved in RESULT.md.
Python 3.10+, standard library only.
"""
from itertools import product

def prism(n):
 assert n>=4
 N=2*n; adj=[set() for _ in range(N)]
 def edge(i,j):adj[i].add(j);adj[j].add(i)
 for i in range(n):
  edge(i,(i+1)%n);edge(n+i,n+(i+1)%n);edge(i,n+i)
 return tuple(tuple(sorted(x)) for x in adj)

def bipyramid(n):
 assert n>=3
 N=n+2;adj=[set() for _ in range(N)]
 def edge(i,j):adj[i].add(j);adj[j].add(i)
 for i in range(n):
  r=2+i;edge(r,2+(i+1)%n);edge(0,r);edge(1,r)
 return tuple(tuple(sorted(x)) for x in adj)

def is_recurrent(adj,h):
 rem=set(range(1,len(adj)))
 while rem:
  chosen=[v for v in rem if h[v]>=sum(w in rem for w in adj[v])]
  if not chosen:return False
  rem-=set(chosen)
 return True

def addition(adj,h,start):
 z=list(h);z[start]+=1;tops=[0]*len(adj)
 for step in range(1000):
  unstable=next((v for v in range(1,len(adj)) if z[v]>=len(adj[v])),None)
  if unstable is None:break
  tops[unstable]+=1;z[unstable]-=len(adj[unstable])
  for w in adj[unstable]:
   if w!=0:z[w]+=1
 else:raise RuntimeError('nontermination')
 burst=sum(tops[u] for u in adj[0]);return tuple(tops),burst

def witness(n):
 g=prism(n);v=n+2
 h=[0]+[2]*(2*n-1)
 for w in g[v]:h[w]=1
 h[v]=2
 assert is_recurrent(g,h)
 od,b=addition(g,h,v)
 assert sum(od)==1 and od[v]==1 and b==0
 return h

def dual_recurrents(n):
 g=bipyramid(n)
 count=0; nd=0
 for x in product(range(n),*(range(4) for _ in range(n))):
  h=(0,)+x
  if is_recurrent(g,h):
   count+=1
   for v in range(1,n+2):
    t,b=addition(g,h,v)
    if sum(t)>0 and b==0:nd+=1
 return count,nd

if __name__=='__main__':
 for n in [4,5,6,8,12,30]:
  witness(n);print('prism witness n=',n,'PASS')
 for n in [3,4,5,6]:
  r,nd=dual_recurrents(n)
  assert nd==0
  print('bipyramid n=',n,'recurrent',r,'nondissipative positive',nd,'PASS')
