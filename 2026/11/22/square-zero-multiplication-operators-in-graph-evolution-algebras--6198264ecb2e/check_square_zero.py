#!/usr/bin/env python3
"""Independent exhaustive finite tests for square-zero left multiplication in graph evolution algebras."""
from collections import Counter
from itertools import product
from math import comb

def edges_cycle(n): return [(i,(i+1)%n) for i in range(n)]
def adjacency(n,edges):
 A=[[0]*n for _ in range(n)]
 for i,j in edges: A[i][j]=A[j][i]=1
 return A

def rank_mod(M,p):
 M=[row[:] for row in M]; m=len(M); n=len(M[0]) if m else 0; r=0
 for c in range(n):
  k=next((i for i in range(r,m) if M[i][c]%p),None)
  if k is None: continue
  M[r],M[k]=M[k],M[r]
  inv=pow(M[r][c]%p,-1,p); M[r]=[(v*inv)%p for v in M[r]]
  for i in range(m):
   if i!=r and M[i][c]%p:
    mul=M[i][c]
    M[i]=[(a-mul*b)%p for a,b in zip(M[i],M[r])]
  r+=1
  if r==m:break
 return r

def direct(n, edges, q):
 A=adjacency(n,edges); out=Counter()
 for x in product(range(q),repeat=n):
  # M=A diag(x), its square
  M=[[A[i][j]*x[j]%q for j in range(n)] for i in range(n)]
  sq=all(sum(M[i][k]*M[k][j] for k in range(n))%q==0 for i in range(n) for j in range(n))
  indep=all(not(x[i] and x[j]) for i,j in edges)
  if sq!=indep:raise AssertionError((n,q,edges,x,sq,indep))
  if sq:out[rank_mod(M,q)]+=1
 return out

def predicted(n,q):
 w=q-1; out=Counter()
 for k in range(n//2+1):
  out[k]+= n*comb(n-k,k)//(n-k)*w**k
 if n%2==0 and (q%2==0 or n%4==0):
  out[n//2]-=2*w**(n//2)
  out[n//2-1]+=2*w**(n//2)
 return +out

def run():
 count=0
 for n in range(5,10):
  for q in (2,3,5):
   if q**n>250000:continue
   seen=direct(n,edges_cycle(n),q); want=predicted(n,q)
   assert seen==want,(n,q,seen,want)
   print('cycle',n,q,'distribution',sorted(seen.items()),'total',sum(seen.values()))
   count+=1
 print('VERIFIED_CASES',count)
 # C4 shows failure: non-independent full support with L^2=0
 n=4;q=3;x=(1,1,2,2);A=adjacency(n,edges_cycle(n));M=[[A[i][j]*x[j]%q for j in range(n)] for i in range(n)]
 assert all(sum(M[i][k]*M[k][j] for k in range(n))%q==0 for i in range(n) for j in range(n))
 assert rank_mod(M,q)==2
 print('C4_BOUNDARY_CHECK',True)
if __name__=='__main__':run()

def exhaustive_c4_free():
 from itertools import combinations
 count_graph=0;count_vectors=0
 for n,q in [(1,3),(2,3),(3,3),(4,3),(5,2)]:
  edges_all=list(combinations(range(n),2))
  for bitmask in range(1<<len(edges_all)):
   edges=[edge for i,edge in enumerate(edges_all) if bitmask>>i&1]
   es={frozenset(e) for e in edges}
   has4=any(all(frozenset(e) in es for e in [(a,b),(b,c),(c,d),(d,a)]) for a,b,c,d in __import__('itertools').permutations(range(n),4))
   if has4:continue
   A=adjacency(n,edges)
   for x in product(range(q),repeat=n):
    sq=True
    for j in range(n):
     if not x[j]:continue
     for i in range(n):
      if x[j]*sum(A[i][k]*x[k]*A[k][j] for k in range(n))%q:
       sq=False;break
     if not sq:break
    indep=all(not(x[i] and x[j]) for i,j in edges)
    assert sq==indep,(n,q,edges,x,sq,indep)
    count_vectors+=1
   count_graph+=1
 print('C4_FREE_COMPLETE_GRAPHS',count_graph,'CHECKED_VECTORS',count_vectors)
if __name__=='__main__':exhaustive_c4_free()
