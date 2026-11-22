"""Independent brute-force check of the visibility/Turan correspondence, small n.
No mathematical proof for unbounded n is inferred from finite checks.
"""
from itertools import combinations
from collections import deque

def check(n):
    E=list(combinations(range(n),2)); k=len(E)
    blocked=[]
    for quad in combinations(range(n),4):
        blocked.append(sum(1<<E.index(e) for e in combinations(quad,2)))
    feasible=[]
    maxc=-1
    for bits in range(1<<k):
        if any((bits&b)==b for b in blocked):continue
        pop=bits.bit_count()
        if pop>maxc:feasible=[bits];maxc=pop
        elif pop==maxc:feasible.append(bits)
    q,r=divmod(n,3)
    expected=n*(n-1)//2-(3-r)*(q*(q-1)//2)-r*(q*(q+1)//2)
    assert maxc==expected,(n,maxc,expected)
    if n>=4:
      t=q if r else 2*(q-1)
      def delta(a,b):(a^b).bit_count()//2
      vals=[(a^b).bit_count()//2 for i,a in enumerate(feasible) for b in feasible[i+1:]]
      assert min(vals)==t,(n,min(vals),t)
      adj=[[] for _ in feasible]
      for i,a in enumerate(feasible):
        for j in range(i+1,len(feasible)):
          if (a^feasible[j]).bit_count()//2 <=t:
            adj[i].append(j);adj[j].append(i)
      seen={0};pending=[0]
      while pending:
        for j in adj[pending.pop()]:
          if j not in seen:seen.add(j);pending.append(j)
      assert len(seen)==len(feasible)
    print('visibility',n,len(feasible),maxc,'ok')
for n in range(4,7):check(n)
print('VISIBILITY_OK')
