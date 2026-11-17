#!/usr/bin/env python3
"""Independent exact arithmetic and Monte Carlo checks of the cactus distance-law identity.
Run: python3 verify.py. Standard library only; fixed random seed.
"""
from fractions import Fraction as Q
from collections import deque, defaultdict
from itertools import combinations
import heapq, random

def F(s): return Q(str(s))

def positive(t): return max(Q(0), t)

def simplex_cdf(z,a,b):
    return (positive(z)**2-positive(z-a)**2-positive(z-b)**2+positive(z-a-b)**2)/(2*a*b)

def simplex_pdf(z,a,b):
    return (positive(z)-positive(z-a)-positive(z-b)+positive(z-a-b))/(a*b)

class Example:
 def __init__(self, pieces):
    # each piece ('cycle'|'bridge', [(u,v,length),...]); interiors partition graph.
    self.pieces=[(kind,[(u,v,F(w)) for u,v,w in edges]) for kind,edges in pieces]
    self.edges=[e for _,arr in self.pieces for e in arr]
    self.lengths=[sum((l for _,_,l in arr),Q(0)) for _,arr in self.pieces]
    self.h=[(l/2 if k=='cycle' else l) for (k,_),l in zip(self.pieces,self.lengths)]
    self.L=sum(self.lengths,Q(0))
    adj=defaultdict(list)
    for u,v,l in self.edges:
      adj[u].append((v,l)); adj[v].append((u,l))
    self.shortest={}
    for source in adj:
      dd={source:Q(0)}; hp=[(Q(0),source)]
      while hp:
        d,u=heapq.heappop(hp)
        if d!=dd[u]: continue
        for v,w in adj[u]:
          if v not in dd or d+w<dd[v]:
            dd[v]=d+w; heapq.heappush(hp,(dd[v],v))
      self.shortest[source]=dd
    incidence=defaultdict(set)
    for i,(_,arr) in enumerate(self.pieces):
      for v in set([v for u,w,l in arr for v in (u,w)]):
        incidence[('b',i)].add(('v',v)); incidence[('v',v)].add(('b',i))
    self.deltas={}
    for i,j in combinations(range(len(self.pieces)),2):
      a,b=('b',i),('b',j)
      parent={a:None}; q=deque([a])
      while q and b not in parent:
       u=q.popleft()
       for v in incidence[u]:
        if v not in parent: parent[v]=u;q.append(v)
      assert b in parent
      chain=[]; t=b
      while t is not None: chain.append(t); t=parent[t]
      chain.reverse()
      va,vb=chain[1][1],chain[-2][1]
      self.deltas[(i,j)]=self.shortest[va][vb]
 def cdf(self,r):
   r=Q(r)
   if r<=0:return Q(0)
   total=Q(0)
   for (kind,_),l in zip(self.pieces,self.lengths):
     if kind=='cycle':total+= l*l*min(Q(1),2*r/l)
     else:total+=l*l-positive(l-r)**2
   for (i,j),delta in self.deltas.items():
     total+=2*self.lengths[i]*self.lengths[j]*simplex_cdf(r-delta,self.h[i],self.h[j])
   return total/self.L**2
 def pdf(self,r):
   r=Q(r); assert r>0
   total=Q(0)
   for (kind,_),l in zip(self.pieces,self.lengths):
     if kind=='cycle':total+=2*l*int(r<l/2)
     else:total+=2*positive(l-r)
   for (i,j),delta in self.deltas.items():
     total+=2*self.lengths[i]*self.lengths[j]*simplex_pdf(r-delta,self.h[i],self.h[j])
   return total/self.L**2
 def sample_cdf(self,points,rng):
   edge_cumulative=[]; s=0.
   for u,v,l in self.edges:
    s+=float(l);edge_cumulative.append(s)
   sample=[]
   for _ in range(points):
    pp=[]
    for z in range(2):
      sel=rng.random()*s; ix=next(i for i,b in enumerate(edge_cumulative) if sel<b)
      u,v,l=self.edges[ix]; x=rng.random()*float(l)
      pp.append((ix,u,v,float(l),x))
    i,u,v,le,x=pp[0];j,p,q,lf,y=pp[1]
    d=min(x+float(self.shortest[u][p])+y,
       x+float(self.shortest[u][q])+(lf-y),
       (le-x)+float(self.shortest[v][p])+y,
       (le-x)+float(self.shortest[v][q])+(lf-y))
    if i==j:d=min(d,abs(x-y))
    sample.append(d)
   return sample

def test():
 graphs=[
  [('bridge',[(0,1,'3')])],
  [('cycle',[(0,1,'1'),(1,2,'2'),(2,0,'2')])],
  [('cycle',[(0,1,'1'),(1,2,'2'),(2,0,'2')]), ('bridge',[(0,3,'2')])],
  [('cycle',[(0,1,'1'),(1,2,'2'),(2,0,'2')]), ('cycle',[(0,3,'1.5'),(3,4,'1.5'),(4,0,'2')]),
   ('bridge',[(0,5,'2')]),('bridge',[(5,6,'1.3')]),('cycle',[(6,7,'1'),(7,8,'1'),(8,6,'1')])],
 ]
 rng=random.Random(900000071)
 max_err=0
 derivative_count=0
 for j,g in enumerate(graphs):
  graph=Example(g); L=graph.L
  eps=Q(1,10**7)
  assert 2*graph.pdf(eps)-graph.pdf(2*eps)==2/L,('f0',j)
  cycle_lengths=defaultdict(int)
  for (kind,_),l in zip(graph.pieces,graph.lengths):
    if kind=='cycle':cycle_lengths[l]+=1
  for c,m in cycle_lengths.items():
   r=c/2
   # Choose epsilon smaller than any other spline breakpoint, and verify exact coefficient.
   e=Q(1,10**7)
   jump=graph.pdf(r+e)-graph.pdf(r-e)
   assert abs(jump+2*c*m/L**2) < Q(1,10**4),('jump',j,c,jump)
   # Use left and right limits from piecewise-affine expressions (Richardson cancellation).
   j1=graph.pdf(r+e)-graph.pdf(r-e)
   j2=graph.pdf(r+2*e)-graph.pdf(r-2*e)
   exact=2*j1-j2
   assert exact == -2*c*m/L**2,('exact jump',j,c,exact)
  assert graph.cdf(Q(0))==0
  assert graph.cdf(10000)==1,('mass',j)
  # Fundamental theorem of calculus where density is affine (small intervals away from knots).
  for n in range(10,90):
    x=Q(n,17); h=Q(1,10**6)
    knots=[l/2 for l in cycle_lengths]+[l for (kind,_),l in zip(graph.pieces,graph.lengths) if kind=='bridge']
    for (i,jj),delta in graph.deltas.items():knots.extend([delta,delta+graph.h[i],delta+graph.h[jj],delta+graph.h[i]+graph.h[jj]])
    if any(x-h<=t<=x+h for t in knots):continue
    derivative=(graph.cdf(x+h)-graph.cdf(x-h))/(2*h)
    assert derivative == graph.pdf(x),('derivative',j,n)
    derivative_count+=1
  samples=sorted(graph.sample_cdf(35000,rng))
  for k in range(1,22):
   r=Q(k,3)
   import bisect
   empirical=bisect.bisect_right(samples,float(r))/len(samples)
   expected=float(graph.cdf(r))
   max_err=max(max_err,abs(empirical-expected))
  print('GRAPH',j,'total',L,'cycle_lengths',dict(cycle_lengths),'max_abs_CDF_err_so_far',f'{max_err:.6f}')
 assert max_err<0.019,('sampling',max_err)
 print('CACTUS_VERIFICATION_OK exact_mass=4 exact_density_derivatives=%d jump_groups=4 independent_pairs=140000 max_abs_cdf_error=%.6f'%(derivative_count,max_err))

if __name__=='__main__':test()
