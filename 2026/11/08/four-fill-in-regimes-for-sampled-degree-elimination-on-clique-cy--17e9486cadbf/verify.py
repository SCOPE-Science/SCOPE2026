"""Exact independent tests of the sampled-degree elimination fill law.
Standard-library only. This is a numerical/symbolic checker, not a proof of the infinite theorem.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, factorial
import sys, math

checks=0

def assert_eq(a,b,msg):
 global checks
 checks+=1
 if a!=b: raise AssertionError((msg,a,b))

def graph(h,m):
 n=h+m
 a=[set() for _ in range(n)]
 for i in range(h):
  for j in range(i+1,h):a[i].add(j);a[j].add(i)
  for j in range(h,n):a[i].add(j);a[j].add(i)
 for j in range(m):
  u=h+j;v=h+(j+1)%m;a[u].add(v);a[v].add(u)
 return tuple(tuple(sorted(s)) for s in a)

def graph_state(h,m):
 a=graph(h,m)
 return tuple(range(h+m)),frozenset((i,j) for i in range(h+m) for j in a[i] if i<j)

def eliminate(state,v):
 remaining,edges=state
 nbr=[u for u in remaining if u!=v and (min(u,v),max(u,v)) in edges]
 fresh=[(min(u,w),max(u,w)) for u,w in combinations(nbr,2) if (min(u,w),max(u,w)) not in edges]
 remaining2=tuple(u for u in remaining if u!=v)
 edges2=frozenset((a,b) for a,b in (edges|set(fresh)) if a!=v and b!=v)
 return (remaining2,edges2),len(fresh)

def exact_graph_pmf(h,m,q):
 @lru_cache(None)
 def rec(remaining,edges):
  if not remaining:return {0:Fraction(1)}
  t=min(q,len(remaining))
  degrees={v:sum(1 for w in remaining if w!=v and (min(v,w),max(v,w)) in edges) for v in remaining}
  choices={v:Fraction(0) for v in remaining}
  for subset in combinations(remaining,t):
   mn=min(degrees[v] for v in subset)
   winners=[v for v in subset if degrees[v]==mn]
   for v in winners:choices[v]+=Fraction(1,comb(len(remaining),t)*len(winners))
  out={}
  for v,p in choices.items():
   if p==0:continue
   state2,added=eliminate((remaining,edges),v)
   for k,p2 in rec(*state2).items():out[k+added]=out.get(k+added,Fraction(0))+p*p2
  return out
 return rec(*graph_state(h,m))

def theory_pmf(h,m,q):
 # q sampled distinct vertices from all available at each decision
 p={k:Fraction(comb(h,q),comb(h+k,q)) if q<=h else Fraction(0) for k in range(4,m+1)}
 s=Fraction(1)
 out={}
 for k in range(m,3,-1):
  bad=s*p[k];delta=(k-2)*(k-3)//2
  out[m-3+delta]=out.get(m-3+delta,Fraction(0))+bad
  s*=1-p[k]
 out[m-3]=out.get(m-3,Fraction(0))+s
 return {x:y for x,y in out.items() if y!=0}

print('EXACT_GRAPH_PMF_CHECKS',flush=True)
for h in range(1,5):
 for m in range(3,7):
  if h+m>8:continue
  for q in range(1,min(h+m,5)+1):
   theoretical=theory_pmf(h,m,q)
   enumerated=exact_graph_pmf(h,m,q)
   assert_eq(enumerated,theoretical,f'full graph {h=} {m=} {q=}')
   assert_eq(sum(enumerated.values()),1,'normalization')
print('GRAPH_CHECKS_PASSED',checks,flush=True)

# Alternative exact calculation: enumerating all total vertex permutations when q=1
from itertools import permutations
for h,m in [(1,4),(1,5),(2,4),(2,5),(3,4)]:
 freq={}
 for perm in permutations(range(h+m)):
  state=graph_state(h,m);filled=0
  for v in perm:
   state,k=eliminate(state,v);filled+=k
  freq[filled]=freq.get(filled,0)+1
 count=factorial(h+m)
 empirical={k:Fraction(c,count) for k,c in freq.items()}
 assert_eq(empirical,theory_pmf(h,m,1),f'permutation enumeration {h,m}')
print('PERMUTATIONS_PASSED',checks,flush=True)

# Exact formula for q=1 expectation (beta-binomial factorial moments)
for h in range(1,10):
 for m in range(3,40):
  pmf=theory_pmf(h,m,1)
  mean=sum(x*p for x,p in pmf.items())
  excess=Fraction(h*m*(m-1),2*(h+2))-Fraction(2*h*m,h+1)+3-Fraction(h+3,comb(h+m,h))
  assert_eq(mean,Fraction(m-3)+excess,f'closed mean {h,m}')
print('CLOSED_MEAN_PASSED',checks,flush=True)

# Independent large-m hazard recurrence and four mean regimes.
def mean_excess(h,m,q):
 survive=1.0;ans=0.0
 for k in range(m,3,-1):
  pk=math.prod((h-i)/(h+k-i) for i in range(q)) if q<=h else 0.0
  ans += survive*pk*(k-2)*(k-3)/2
  survive *= 1-pk
 return ans
for h in [2,3,4,5,6]:
 for q in range(1,h+2):
  values=[mean_excess(h,m,q) for m in [1000,2000,4000]]
  if q==1:
   ratio=values[-1]/(4000**2)
   target=h/(2*(h+2))
   assert abs(ratio-target)<0.002,(h,q,ratio,target)
  elif q==2:
   ratio=(values[-1]-values[-2])/2000
   target=h*(h-1)/2
   assert abs(ratio-target)<0.3,(h,q,ratio,target)
  elif q==3:
   ratio=(values[-1]-values[-2])/math.log(2)
   target=h*(h-1)*(h-2)/2
   assert abs(ratio-target)<1.0,(h,q,ratio,target)
  elif q>h:
   assert values==[0.,0.,0.],(h,q,values)
  else:
   assert 0<values[0]<values[1]<values[2],(h,q,values)
  checks+=1
print('ASYMPTOTIC_SANITY_PASSED',checks,flush=True)
print('ALL_PASS',checks)
