"""Independent firing-word interval and generating-polynomial checker."""
from itertools import product
from collections import Counter
from math import comb

def choices(degree, F, arrivals):
    displacement=0
    low, high=0, 2*degree-1
    for t in range(3):
        if F[t]: low=max(low,degree-displacement)
        else: high=min(high,degree-1-displacement)
        displacement+=arrivals[t]-degree*F[t]
    if displacement!=0: return []
    return list(range(low,high+1)) if high>=low else []

def result(k):
    degree=2*k
    result=Counter()
    for hub_phase in range(3):
      for active in (1,2):
        hub=tuple(int((t!=hub_phase) if active==2 else (t==hub_phase)) for t in range(3))
        pattern=lambda p:tuple(int((t!=p) if active==2 else (t==p)) for t in range(3))
        arm=Counter()
        for pa,pb in product(range(3),repeat=2):
            a,b=pattern(pa),pattern(pb)
            for xa in choices(2,a,tuple(hub[t]+b[t] for t in range(3))):
              for xb in choices(2,b,tuple(hub[t]+a[t] for t in range(3))):
                arm[(tuple(a[t]+b[t] for t in range(3)),xa+xb)]+=1
        dp=Counter({((0,0,0),0):1})
        for _ in range(k):
            nxt=Counter()
            for (arr, mass), ways in dp.items():
                for (fa, ma), cw in arm.items():
                    nxt[(tuple(arr[t]+fa[t] for t in range(3)),mass+ma)]+=ways*cw
            dp=nxt
        for (arr,mass),ways in dp.items():
            for xh in choices(degree,hub,arr):
                result[xh+mass]+=ways
    return result

def target(k):
  out=Counter()
  for j in range(k):
    c=3*sum(comb(k,a)*2**(k-a) for a in range(j+1))
    out[3*k+j]+=c
    out[7*k-1-j]+=c
  return out

for k in range(1,13):
    a=result(k)
    b=target(k)
    assert a==b,(k,a,b)
    print('k=%d patterns=%d primitive3=%d masses=%d'%(k,len(a),sum(a.values()),len(a)))
print('FIRING WORD PASS')
