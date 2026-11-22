#!/usr/bin/env python3
"""Self-contained small-order certificate checks for affine-plane incidence packing coloring."""
from itertools import combinations
from math import factorial
from collections import Counter,deque

def finite_affine(q):
    assert q in (2,3,5,7), 'This direct-coordinate verifier uses prime fields'
    points=[(x,y) for x in range(q) for y in range(q)]
    lines=[]
    # x=c vertical, and y=m*x+c for slopes m
    for c in range(q): lines.append(frozenset(i for i,(x,y) in enumerate(points) if x==c))
    for m in range(q):
      for c in range(q): lines.append(frozenset(i for i,(x,y) in enumerate(points) if (y-m*x-c)%q==0))
    assert len(lines)==q*(q+1) and len(set(lines))==len(lines)
    return points,lines

def build(q):
    P,L=finite_affine(q)
    n=len(P)+len(L); adj=[set() for _ in range(n)]
    for j,li in enumerate(L):
      for i in li: adj[i].add(len(P)+j);adj[len(P)+j].add(i)
    ds=[]
    for i in range(n):
      d=[-1]*n;d[i]=0; que=deque([i])
      while que:
        u=que.popleft()
        for v in adj[u]:
          if d[v]<0:d[v]=d[u]+1;que.append(v)
      assert all(x>=0 for x in d)
      ds.append(d)
    return P,L,ds

def legal_sets(n,d,color,limit):
    # Empty set included; color k only supports <=q vertices for k=2,3.
    out=[0]
    for sz in range(1,limit+1):
      for cb in combinations(range(n),sz):
        if all(d[a][b]> (2 if color==2 else 3) for a,b in combinations(cb,2)):
          out.append(sum(1<<i for i in cb))
    return out

def main():
    q=3; P,L,d=build(q); p=len(P);n=p+len(L)
    C2=legal_sets(n,d,2,q);C3=legal_sets(n,d,3,q)
    print('q',q,'points',p,'lines',len(L),'diam',max(max(row) for row in d),'candidate C2',len(C2),'candidate C3',len(C3))
    # independently enumerate every possible color-1 independent set and compute best disjoint 2/3 packings
    feasible=[]
    for pm in range(1<<p):
      eligible=[p+j for j,s in enumerate(L) if not any(pm>>v&1 for v in s)]
      for lm in range(1<<len(eligible)):
        mask=pm|sum(1<<eligible[j] for j in range(len(eligible)) if lm>>j&1)
        feasible.append(mask)
    print('independent color-1 sets',len(feasible))
    # For every C1, choose maximizing pair disjoint C2, C3 via masks, filtering using upper bound.
    globalbest=0; optimal_triplets=set()
    upper=[(mask.bit_count(),mask) for mask in C2]
    upper3=[(mask.bit_count(),mask) for mask in C3]
    upper.sort(reverse=True);upper3.sort(reverse=True)
    for one in feasible:
      s=one.bit_count()
      if s+2*q<globalbest:continue
      for a_size,second in upper:
        if s+a_size+q<globalbest:break
        if one&second:continue
        for b_size,third in upper3:
          t=s+a_size+b_size
          if t<globalbest:break
          if third&(one|second): continue
          if t>globalbest:globalbest=t;optimal_triplets.clear()
          if t==globalbest:optimal_triplets.add((one,second,third))
    print('max non-singleton coverage',globalbest,'expected',p+2*q,'opt triples',len(optimal_triplets),'expected',(q+1)*q)
    assert globalbest==p+2*q and len(optimal_triplets)==q*(q+1)
    for one,two,three in optimal_triplets:
      assert one==(1<<p)-1
      assert two.bit_count()==q and three.bit_count()==q
      assert all(i>=p for i in range(n) if (two|three)>>i&1)
      assert two&three==0
    k=n-globalbest+3
    assert k==q*q-q+3
    print('chi',k,'named optimal count',len(optimal_triplets)*factorial(n-globalbest),'expected',q*(q+1)*factorial(q*(q-1)))

if __name__=='__main__':main()
