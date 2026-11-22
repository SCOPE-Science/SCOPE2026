"""Independent exact enumerative check for GP(n,2) orbit-complex Lefschetz traces.

Usage: python check_gp_dihedral.py

The finite checks corroborate, but do not prove, the uniform character formula.
"""

from functools import lru_cache

def quotient_graph(n,kind,s):
 e=set()
 for i in range(n):
  for a,b in [((0,i),(0,(i+1)%n)),((1,i),(1,(i+2)%n)),((0,i),(1,i))]:
   if a>b:a,b=b,a
   e.add((a,b))
 V=[(k,i) for k in range(2) for i in range(n)]
 def f(v):
  k,i=v
  return (k,(i+s)%n) if kind=='rotation' else (k,(s-i)%n)
 orbit={};oid={}
 for v in V:
  if v in oid:continue
  curr=[];w=v
  while w not in curr:
   curr.append(w);w=f(w)
  idx=len(orbit)
  orbit[idx]=curr
  for w in curr:oid[w]=idx
 bad=set();es=set()
 for a,b in e:
  x,y=oid[a],oid[b]
  if x==y:bad.add(x)
  else:es.add(tuple(sorted((x,y))))
 active=[x for x in orbit if x not in bad]
 rel={j:i for i,j in enumerate(active)}
 ed={tuple(sorted((rel[a],rel[b]))) for a,b in es if a in rel and b in rel}
 return len(active),ed

def independence_at_minus_one(n,edges):
 neighbors=[0]*n
 for a,b in edges:
  neighbors[a]|=1<<b;neighbors[b]|=1<<a
 @lru_cache(None)
 def go(mask):
  if not mask:return 1
  # drop disconnected comps not needed; select max degree pivot
  x=max((i for i in range(n) if mask>>i&1),key=lambda i: (neighbors[i]&mask).bit_count())
  return go(mask&~(1<<x))-go(mask&~(1<<x)&~neighbors[x])
 v=go((1<<n)-1)
 return v,go.cache_info().currsize



def check():
    count = 0
    for n in (5, 10, 15, 20):
        q = n // 5
        for s in range(n):
            nv, edges = quotient_graph(n, 'rotation', s)
            val, _ = independence_at_minus_one(nv, edges)
            trace = (-1)**q * val
            target = (-1)**((n+1)*s) * (4 if s % 5 == 0 else -1)
            assert trace == target, ('rotation',n,s,trace,target)
            count += 1
            nv, edges = quotient_graph(n, 'reflection', s)
            val, _ = independence_at_minus_one(nv, edges)
            assert val == 0, ('reflection',n,s,val)
            count += 1
        print(f'n={n}: {2*n} action traces verified')
    print(f'PASS {count} independent exact traces')

if __name__ == '__main__':
    check()
