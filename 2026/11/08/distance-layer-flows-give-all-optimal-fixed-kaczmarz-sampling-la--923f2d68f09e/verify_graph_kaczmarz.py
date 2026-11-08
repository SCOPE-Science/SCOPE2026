#!/usr/bin/env python3
"""Exact check of explicit designs for graph-anchor Kaczmarz; needs Python stdlib only.
The verifier uses the algebraic parameter t=sqrt(2) with t*t=2 represented
as pairs of rational numbers.  It checks identities, not the infinite theorem.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import deque

class Q:
 def __init__(self,a=0,b=0):self.a,self.b=F(a),F(b)
 def __add__(self,o):
  if not isinstance(o,Q):o=Q(o)
  return Q(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return Q(-self.a,-self.b)
 def __sub__(self,o):return self+-o if isinstance(o,Q) else self+Q(-o)
 def __mul__(self,o):
  if not isinstance(o,Q):o=Q(o)
  return Q(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __truediv__(self,o):
  if not isinstance(o,Q):o=Q(o)
  d=o.a*o.a-2*o.b*o.b
  return Q((self.a*o.a-2*self.b*o.b)/d,(self.b*o.a-self.a*o.b)/d)
 def __eq__(self,o):
  if not isinstance(o,Q):o=Q(o)
  return self.a==o.a and self.b==o.b
 def __repr__(self):return f'({self.a}+{self.b}sqrt2)'
T=Q(0,1); ONE=Q(1); ZERO=Q()

def evaluate(n,edges,anchors):
 adj=[[] for _ in range(n)]
 for u,v in edges:adj[u].append(v);adj[v].append(u)
 dist=[-1]*n; parent={}; q=deque()
 for a in anchors:dist[a]=0;q.append(a)
 while q:
  u=q.popleft()
  for v in adj[u]:
   if dist[v]<0:
    dist[v]=dist[u]+1; parent[v]=u; q.append(v)
 assert -1 not in dist
 v=[ONE+T*d for d in dist]; S=sum((x*x for x in v),ZERO)
 descendants={u:v[u] for u in range(n)}
 for u in sorted(parent,key=lambda u:dist[u],reverse=True):descendants[parent[u]]+=descendants[u]
 probs={('a',u):descendants[u]/S for u in anchors}
 for u in parent:probs[('e',tuple(sorted((u,parent[u]))))]=T*descendants[u]/S
 assert sum(probs.values(),ZERO)==ONE
 # Row squared inner product: anchor row (1), normalized edge row (delta/sqrt2).
 M=[[ZERO for j in range(n)] for i in range(n)]
 for (kind,k),prob in probs.items():
  if kind=='a': M[k][k]+=prob
  else:
   u,w=k;c=prob/Q(2)
   M[u][u]+=c; M[w][w]+=c;M[u][w]-=c;M[w][u]-=c
 for i in range(n):assert sum((M[i][j]*v[j] for j in range(n)),ZERO)==v[i]/S
 # All available rows have squared inner product <=1 with v.
 for u,vv in edges:assert abs(dist[u]-dist[vv])<=1
 for a in anchors:assert dist[a]==0
 # Unique iff each nonanchor has exactly one neighbor at preceding layer.
 predicted=all(sum(dist[w]==dist[u]-1 for w in adj[u])==1 for u in range(n) if u not in anchors)
 return predicted,probs,S

def main():
 checks=0; multi=0; unique=0
 for n in range(2,6):
  poss=list(combinations(range(n),2))
  for mask in range(1,1<<len(poss)):
   edges=[e for i,e in enumerate(poss) if mask>>i&1]
   if len(edges)<n-1:continue
   adj=[[] for _ in range(n)]
   for a,b in edges:adj[a].append(b);adj[b].append(a)
   visited={0};q=[0]
   for u in q:
    for w in adj[u]:
     if w not in visited:visited.add(w);q.append(w)
   if len(visited)<n:continue
   for amask in range(1,1<<n):
    A=[i for i in range(n) if amask>>i&1]
    predicted,probs,S=evaluate(n,edges,A)
    checks+=1;unique+=predicted; multi+=not predicted
 # a four-cycle with one anchor has two shortest paths
 u,p,S=evaluate(4,[(0,1),(1,2),(2,3),(3,0)],[0]);assert not u
 print('VERIFY_OK',checks,'cases; unique',unique,'nonunique',multi)
if __name__=='__main__':main()
