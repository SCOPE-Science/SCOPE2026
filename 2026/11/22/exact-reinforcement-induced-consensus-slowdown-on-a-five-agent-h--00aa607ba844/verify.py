"""Reproducible exact checks for a finite group-voter process.
Public scientific code; requires only Python 3 standard library.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from collections import deque

N=5
EDGES=[(0,1,2),(0,3,4)]

def poladd(a,b):
    c=[Q(0)]*max(len(a),len(b))
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return c

def polmul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
      for j,bj in enumerate(b): c[i+j]+=ai*bj
    return c

def scale(a,k): return [k*v for v in a]

# Five symmetry classes of transient configurations. The coefficients
# are induced by single-node updates, not fitted to numerical data.
A=[
 [[Q(1,5),Q(3,10)],[Q(0),Q(-1,5)],[],[Q(0),Q(-1,10)],[]],
 [[Q(0),Q(-2,5)],[Q(0),Q(2,5)],[],[],[]],
 [[Q(-2,5)],[],[Q(2,5),Q(2,5)],[Q(0),Q(-2,5)],[]],
 [[Q(-1,10),Q(-1,10)],[Q(-1,5)],[Q(0),Q(-2,5)],[Q(3,10),Q(7,10)],[Q(0),Q(-1,5)]],
 [[],[],[],[Q(0),Q(-4,5)],[Q(1,5),Q(4,5)]]
]
# Numerator of each expected time over common denominator
# D(x)=2*x*(5*x+1)*(x*x+7*x+3)
num=[
 scale([0,10,73,123,30],Q(5)),
 scale([3,32,109,128,30],Q(5)),
 scale([0,15,104,158,30],Q(5)),
 scale([2,24,103,153,30],Q(5)),
 scale([0,14,84,148,30],Q(5)),
]
D=polmul([Q(0),Q(2)],polmul([Q(1),Q(5)],[Q(3),Q(7),Q(1)]))
for i in range(5):
    val=[]
    for j in range(5): val=poladd(val,polmul(A[i][j],num[j]) if A[i][j] else [])
    assert poladd(val,scale(D,-1))==[Q(0)]*max(len(val),len(D)), (i,val,D)
print('PASS: symbolic five-class first-step identities')

# Independently generate 32-state transition matrix from the model,
# and solve for the expected time with exact rational elimination.
def build_updates(n,edges,x):
    inc={i:[e for e in edges if i in e] for i in range(n)}
    assert all(inc.values())
    result={}
    for st in product((0,1), repeat=n):
        if len(set(st))==1:continue
        r={}
        for i in range(n):
          for e in inc[i]:
            k=sum(st[i]!=st[j] for j in e if j!=i)
            prob=Q(1,n*len(inc[i]))*(Q(0) if k==0 else x if k==1 else Q(1))
            tgt=list(st);tgt[i]^=1;tgt=tuple(tgt)
            r[tgt]=r.get(tgt,Q(0))+prob
        result[st]=r
    return result

def solve(rows, start):
    states=list(rows);ids={st:i for i,st in enumerate(states)}
    n=len(states);aug=[[Q(0)]*(n+1) for _ in range(n)]
    for i,st in enumerate(states):
      aug[i][i]=sum(rows[st].values())
      for tgt,w in rows[st].items():
        if tgt in ids:aug[i][ids[tgt]]-=w
      aug[i][-1]=Q(1)
    for c in range(n):
      pivot=next(i for i in range(c,n) if aug[i][c]);aug[c],aug[pivot]=aug[pivot],aug[c]
      v=aug[c][c]; aug[c]=[z/v for z in aug[c]]
      for i in range(n):
        if i!=c and aug[i][c]:
          k=aug[i][c];aug[i]=[v-k*w for v,w in zip(aug[i],aug[c])]
    return aug[ids[start]][-1]

def val(poly,x): return sum((a*x**i for i,a in enumerate(poly)),Q(0))
for x in [Q(1,2),Q(1,4),Q(1,8),Q(1,16),Q(2,5)]:
   exact=solve(build_updates(5,EDGES,x),(0,0,0,1,1))
   predicted=val(num[1],x)/val(D,x)
   assert exact==predicted,(x,exact,predicted)
print('PASS: independent exact 30-transient-state equations at five parameters')

# Exhaustive minimum-order comparison for all connected 3-uniform
# hypergraphs on three and four labelled vertices in the q=infinity rule.
def all_can_reach_consensus(n,edges):
    nxt={}
    for st in product((0,1),repeat=n):
      reachable=set()
      for i in range(n):
        if any(sum(st[i]!=st[j] for j in e if j!=i)==2 for e in edges if i in e):
          target=list(st);target[i]^=1;reachable.add(tuple(target))
      nxt[st]=reachable
    rev={st:set() for st in nxt}
    for st,tars in nxt.items():
      for target in tars:rev[target].add(st)
    seeds=[(0,)*n,(1,)*n];seen=set(seeds); todo=deque(seeds)
    while todo:
      for st in rev[todo.popleft()]:
        if st not in seen:seen.add(st);todo.append(st)
    return len(seen)==2**n
checked=0
for n in (3,4):
  choices=list(combinations(range(n),3))
  for m in range(1,len(choices)+1):
    for edges in combinations(choices,m):
      if set.union(*(set(e) for e in edges))!=set(range(n)):continue
      assert all_can_reach_consensus(n,edges)
      checked+=1
assert not all_can_reach_consensus(5,EDGES)
print('PASS:',checked,'connected labelled 3- and 4-vertex hypergraphs have no nonconsensus closed class; five-vertex example does')

# Monotonicity: derivative numerator of T_polar(x) has 440*x^6+230*x^5
# and only negative lower terms. On 0<x<=1/2, its positive part
# is <=225*x^4, strictly below the -1318*x^4 term.
assert Q(440,4)+Q(230,2)<1318
assert val(num[1],Q(1,2))/val(D,Q(1,2))==Q(95,7)
assert val(num[1],Q(1,4))/val(D,Q(1,4))==Q(12755,693)
assert num[1][0]==15 and D[1]==6
print('PASS: monotonicity coefficient bound, two exact evaluations, asymptotic limit 5/2')
