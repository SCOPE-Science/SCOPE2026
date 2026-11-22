#!/usr/bin/env python3
"""Exact exhaustive finite census of random greedy parking size laws.
Only Python standard library needed. The graph catalogue is generated from
one vertex using the non-cut-vertex deletion lemma; isomorphism is checked by
exact adjacency-preserving backtracking. No external graph data are loaded.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from collections import Counter, defaultdict
from time import perf_counter
import sys, json

def neighbors(a,i):
 return tuple(j for j in range(len(a)) if (a[i]>>j)&1)

def signature(a):
 n=len(a);deg=[x.bit_count() for x in a]
 local=[(deg[i], tuple(sorted(deg[j] for j in neighbors(a,i)))) for i in range(n)]
 # Two rounds of one-dimensional WL refinement with within-graph sorted signatures.
 cols=deg
 for _ in range(3):
  signs=[(cols[i],tuple(sorted(cols[j] for j in neighbors(a,i)))) for i in range(n)]
  items=sorted(set(signs)); ids={v:i for i,v in enumerate(items)}
  cols=[ids[x] for x in signs]
 return (n,tuple(sorted(deg)),tuple(sorted(local)),tuple(sorted(cols)))

def equivalent(a,b):
 n=len(a)
 da=[x.bit_count() for x in a];db=[x.bit_count() for x in b]
 la=[(da[i],tuple(sorted(da[j] for j in neighbors(a,i)))) for i in range(n)]
 lb=[(db[i],tuple(sorted(db[j] for j in neighbors(b,i)))) for i in range(n)]
 options={i:[j for j in range(n) if la[i]==lb[j]] for i in range(n)}
 if any(not x for x in options.values()):return False
 order=sorted(range(n),key=lambda i:(len(options[i]),-da[i]))
 assign={};taken=set()
 def rec(k):
  if k==n:return True
  i=order[k]
  for j in options[i]:
   if j in taken:continue
   if any(bool(a[i]>>u&1)!=bool(b[j]>>v&1) for u,v in assign.items()):continue
   assign[i]=j;taken.add(j)
   if rec(k+1):return True
   taken.remove(j);del assign[i]
  return False
 return rec(0)

def extend(base):
 classes=defaultdict(list);raw=0
 for a in base:
  n=len(a);avail=[i for i in range(n) if a[i].bit_count()<3]
  for size in range(1,min(3,len(avail))+1):
   for group in combinations(avail,size):
    b=list(a)+[0]
    for v in group:b[v]|=1<<n;b[n]|=1<<v
    b=tuple(b);raw+=1
    bucket=classes[signature(b)]
    if not any(equivalent(b,x) for x in bucket):bucket.append(b)
 return [x for bucket in classes.values() for x in bucket],raw

def distribution(a):
 n=len(a);closed=[a[i]|(1<<i) for i in range(n)]
 @lru_cache(None)
 def greedy(mask):
  if mask==0:return (Fraction(1),)
  z=[Fraction(0)]*(n+1);m=mask.bit_count()
  for v in range(n):
   if mask>>v&1:
    q=greedy(mask&~closed[v]);
    for j,p in enumerate(q):
     if p:z[j+1]+=p/m
  return tuple(z)
 law=greedy((1<<n)-1)
 counts=Counter()
 for subset in range(1<<n):
  if any((subset>>v&1) and (subset&a[v]) for v in range(n)):continue
  if any(not (subset & closed[v]) for v in range(n)):continue
  counts[subset.bit_count()]+=1
 total=sum(counts.values())
 assert total>0 and sum(law)==1
 sl=Fraction(0);st=Fraction(0);positive=False;minpositive=None
 support=sorted(counts)
 ratios=[law[k]*total/counts[k] for k in support]
 assert all(ratios[i]<=ratios[i+1] for i in range(len(ratios)-1)), (n,a,ratios)
 for k in range(n+1):
  sl+=law[k] if k<len(law) else 0
  st+=Fraction(counts[k],total)
  gap=st-sl
  assert gap>=0,(n,a,k,st,sl)
  if gap>0:
   positive=True
   minpositive=gap if minpositive is None else min(minpositive,gap)
 assert sl==st==1
 return positive,minpositive

def run(maxn=10):
 t=perf_counter();a=[(0,)];record=[]
 for n in range(1,maxn+1):
  if n>1:a,raw=extend(a)
  else:raw=1
  strict=0;mingap=None
  for graph in a:
   yes,gap=distribution(graph)
   if yes: strict+=1;mingap=gap if mingap is None else min(gap,mingap)
  row={'n':n,'isomorphism_classes':len(a),'strict_distribution_cases':strict,'equal_distribution_cases':len(a)-strict,'raw_extensions':raw,'minimum_positive_gap':str(mingap) if mingap else None,'likelihood_ratio_failures':0}
  record.append(row)
  print(json.dumps(row), 'seconds',round(perf_counter()-t,2),flush=True)
 return record
if __name__=='__main__':
 n=int(sys.argv[1]) if len(sys.argv)>1 else 10
 print('RESULT',json.dumps(run(n)))
