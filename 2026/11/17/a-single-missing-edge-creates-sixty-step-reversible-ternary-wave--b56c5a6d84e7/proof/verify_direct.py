#!/usr/bin/env python3
"""Independent exhaustive state iteration for three-state reversible waves on K_n-e."""
from itertools import product

def step(state,n):
 u=state[:n];v=state[n:];su=sum(u)
 new=[]
 for i in range(n):
  neighbor_sum=su-u[i]
  if i==0:neighbor_sum-=u[1]
  if i==1:neighbor_sum-=u[0]
  new.append((neighbor_sum-v[i])%3)
 return tuple(new)+tuple(u)

def count(n):
 L={3:8,4:60,5:36}[n];dist={}
 for state in product(range(3),repeat=2*n):
  now=state
  for t in range(1,L+1):
   now=step(now,n)
   if now==state:
    dist[t]=dist.get(t,0)+1
    break
  else:raise AssertionError(('not returned',n,state))
 return dict(sorted(dist.items()))

def main():
 expected={
 3:{1:1,4:8,8:720},
 4:{1:3,3:6,4:24,10:240,12:48,20:1920,30:480,60:3840},
 5:{1:9,3:234,4:720,9:486,12:18720,36:38880},
 }
 for n in (3,4,5):
  actual=count(n)
  assert actual==expected[n],(n,actual,expected[n])
  assert sum(actual.values())==3**(2*n)
  print('n=%d, configurations=%d, primitive_period_states=%s'%(n,3**(2*n),actual))
 print('PASS: direct updates matched exhaustive primitive period populations')
if __name__=='__main__':main()
