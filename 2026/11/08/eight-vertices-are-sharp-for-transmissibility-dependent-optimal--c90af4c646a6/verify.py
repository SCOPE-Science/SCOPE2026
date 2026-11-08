from itertools import product
from math import comb
from collections import Counter
from heapq import heapify, heappop, heappush
from fractions import Fraction

def edge_poly(n,edges):
 adj=[[] for _ in range(n)]
 for a,b in edges:
  adj[a].append(b);adj[b].append(a)
 dist=[]
 for a in range(n):
  dd={a:0};q=[a]
  for b in q:
   for x in adj[b]:
    if x not in dd:dd[x]=dd[b]+1;q.append(x)
  assert len(dd)==n
  dist.append(dd)
 output=[]
 for a,b in edges:
  U={a};q=[a]
  for u in q:
   for v in adj[u]:
    if (u==a and v==b) or (u==b and v==a):continue
    if v not in U:U.add(v);q.append(v)
  c=[0]*n
  for u in U:
   for v in range(n):
    if v not in U:c[dist[u][v]]+=1
  output.append(tuple(c))
 return output

def prufer_edges(seq,n):
 deg=[1]*n
 for x in seq:deg[x]+=1
 leaves=[i for i in range(n) if deg[i]==1];heapify(leaves)
 edges=[]
 for x in seq:
  leaf=heappop(leaves);edges.append((leaf,x));deg[leaf]-=1;deg[x]-=1
  if deg[x]==1:heappush(leaves,x)
 a,b=leaves;edges.append((a,b))
 return edges

def bernstein_nonnegative(poly,d):
 # f(p)=sum_i a_i p^i = sum_j b_j C(d,j) p^j (1-p)^(d-j)
 # b_j = sum_i a_i C(j,i)/C(d,i)
 for j in range(d+1):
  b=sum((Fraction(poly[i]*comb(j,i),comb(d,i)) for i in range(j+1)),Fraction(0))
  if b<0:return False
 return True

def check_small():
 for n in range(2,8):
  total=0
  for s in product(range(n),repeat=n-2):
   edges=prufer_edges(s,n);polys=edge_poly(n,edges)
   d=n-1
   score=lambda poly:sum(poly[i]*(2**(d-i)) for i in range(1,d+1))
   best=max(range(len(polys)),key=lambda j:score(polys[j]))
   for j,poly in enumerate(polys):
    diff=[polys[best][i]-poly[i] for i in range(n)]
    if not bernstein_nonnegative(diff,d):
     raise AssertionError((n,s,edges,best,j,diff))
   total+=1
  print('n',n,'verified',total,'labeled trees')

def witness():
 # two degree-3 hubs at 0,3 separated by path 0-1-2-3; two pendant leaves on each hub
 edges=[(0,1),(1,2),(2,3),(0,4),(0,5),(3,6),(3,7)]
 P=edge_poly(8,edges)
 for e,q in zip(edges,P):print(e, q)
 # ehub (0,1), ecentral (1,2)
 H=P[0];M=P[1]; assert tuple(H[i]-M[i] for i in range(8)) == (0,0,1,-2,0,0,0,0)
 assert P[2]==H
 for j in range(3,7):
  assert all(x>=0 for x in [M[i]-P[j][i] for i in range(8)]) # maybe fail
  assert all(x>=0 for x in [H[i]-P[j][i] for i in range(8)]) # maybe fail
 # Independent full Bernoulli bond-percolation enumeration on the witness.
 for prob in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
  vals=[]
  for removed in range(len(edges)):
   surviving=[e for j,e in enumerate(edges) if j!=removed]
   expectation=Fraction(0)
   for mask in range(1<<len(surviving)):
    parent=list(range(8))
    def root(x):
     while parent[x]!=x: x=parent[x]
     return x
    for j,(u,v) in enumerate(surviving):
     if mask&(1<<j): parent[root(u)]=root(v)
    sizes=Counter(root(u) for u in range(8))
    # Start uniformly at one vertex. The average component size is sum_C |C|^2/8.
    avg=Fraction(sum(z*z for z in sizes.values()),8)
    m=mask.bit_count();weight=prob**m*(1-prob)**(len(surviving)-m)
    expectation+=weight*avg
   vals.append(expectation)
  # Direct independent comparison to polynomial expected-component-size differences.
  for a in range(len(edges)):
   for b in range(len(edges)):
    assert vals[b]-vals[a] == Fraction(2,8)*sum((P[a][j]-P[b][j])*prob**j for j in range(8))
  print('independent full percolation check p=',prob,'passed')
 print('witness verified')

if __name__=='__main__':
 check_small();witness()
