"""Finite exhaustive cross-checks for core-periphery symmetric enemy-aversion games.
Finite enumeration is diagnostic only; the theorem uses an analytic proof.
"""
from itertools import combinations
from math import comb, factorial

def partitions(xs):
    if not xs:
        yield ()
        return
    first,*rest=xs
    for partition in partitions(rest):
        yield ((first,),)+partition
        for j in range(len(partition)):
            yield partition[:j]+(tuple(sorted(partition[j]+(first,))),)+partition[j+1:]

def status(r,s,parts):
    n=r+s
    def value(i,j):
        return -n if (i>=r and j>=r) else 1
    blocks=[tuple(z) for z in parts]
    utilities={i:sum(value(i,j) for j in block if i!=j) for block in blocks for i in block}
    if any(u<0 for u in utilities.values()):return False,False,0
    prod=1
    for u in utilities.values():prod*=u
    stable=True
    for block in blocks:
        for i in block:
            for other in blocks:
                if other==block:continue
                if sum(value(i,j) for j in other)>utilities[i]:stable=False
            if 0>utilities[i]:stable=False
    return True,stable,prod

for r in range(1,6):
  for s in range(1,5):
    if r+s>9:continue
    best=0; maxcnt=0; ns=0; ns_shapes=set(); positive_ns=0
    for p in partitions(tuple(range(r+s))):
      ir,stable,prod=status(r,s,p)
      if ir:
        if prod>best:best=prod;maxcnt=1
        elif prod==best:maxcnt+=1
        if stable:
          ns+=1
          ns_shapes.add(tuple(sorted((tuple(sorted(b)) for b in p))))
          if prod>0:positive_ns+=1
    predicted=(r-s+1)**(r-s+2) if r>=s else 0
    pcnt=(factorial(s)*comb(r,s-1) if r>s else factorial(r) if r==s else None)
    assert best==predicted,(r,s,best,predicted)
    if r>=s:assert maxcnt==pcnt,(r,s,maxcnt,pcnt)
    else:pass
    assert ns==s,(r,s,ns)
    expected_shapes=set()
    for chosen in range(r,r+s):
      giant=tuple(range(r))+(chosen,)
      parts=[giant]+[(i,) for i in range(r,r+s) if i!=chosen]
      expected_shapes.add(tuple(sorted(tuple(sorted(block)) for block in parts)))
    assert ns_shapes==expected_shapes,(r,s,ns_shapes,expected_shapes)
    assert positive_ns==(1 if s==1 else 0),(r,s,positive_ns)
    print(r,s,'best_prod',best,'max_count',maxcnt,'Nash_count',ns)
print('ALL ENUMERATED INSTANCES PASS')
