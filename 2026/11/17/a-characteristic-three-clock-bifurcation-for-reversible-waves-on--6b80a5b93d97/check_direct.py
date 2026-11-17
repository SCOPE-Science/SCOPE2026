"""Independent neighbor-by-neighbor simulation of finite-plane reversible waves.
Uses affine coordinate charts rather than normalized-vector enumeration.
"""
from random import Random

GF4_MUL=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))

def fadd(x,y,q):return x^y if q==4 else (x+y)%q

def fmul(x,y,q):return GF4_MUL[x][y] if q==4 else (x*y)%q

def vectors(q):
 return ([(1,a,b) for a in range(q) for b in range(q)]
         + [(0,1,b) for b in range(q)] +[(0,0,1)])

def graph(q):
 pts=vectors(q);ls=vectors(q);v=len(pts);nn=2*v
 nbr=[[] for _ in range(nn)]
 for i,p in enumerate(pts):
  for j,l in enumerate(ls):
   z=0
   for a,b in zip(p,l):z=fadd(z,fmul(a,b,q),q)
   if z==0:
    nbr[i].append(v+j);nbr[v+j].append(i)
 assert all(len(x)==q+1 for x in nbr)
 return nbr

def update(cur,prev,nbr):
 return tuple((sum(cur[j] for j in nbr[i])-prev[i])%3 for i in range(len(nbr))),cur

def primitive_period(cur,prev,nbr,max_t):
 start=(cur,prev)
 for t in range(1,max_t+1):
  cur,prev=update(cur,prev,nbr)
  if (cur,prev)==start:return t
 raise AssertionError('order exceeds proposed bound')

def check(q):
 nbr=graph(q);n=len(nbr);M=18 if q%3==1 else 8
 rng=Random(10000+q)
 states=[]
 # independent canonical seeds, random labelled configurations
 for x in range(min(n,20)):
  v=[0]*n;v[x]=1
  states.append((tuple(v),tuple([0]*n)))
 for _ in range(250):
  states.append((tuple(rng.randrange(3) for _ in range(n)),
                 tuple(rng.randrange(3) for _ in range(n))))
 periods={}
 for a,b in states:
  p=primitive_period(a,b,nbr,M)
  assert M%p==0 and (p in ((1,2,3,6,9,18) if M==18 else (1,4,8)))
  periods[p]=periods.get(p,0)+1
 assert M in periods
 return dict(plane_order=q,graph_vertices=n,samples=len(states),primitive_period_histogram=periods)

if __name__=='__main__':
 for q in (2,4,5):print(check(q))
 print('ALL INDEPENDENT DIRECT-UPDATE TESTS PASSED')
