#!/usr/bin/env python3
"""Independent exact state-orbit census for the three-step Fibonacci map."""
from collections import Counter
from sympy import Matrix
A=Matrix([[0,1,0],[0,0,1],[1,1,1]])
Q=(A**13-Matrix.eye(3))/3
assert all(x%3==0 for x in A**13-Matrix.eye(3))
assert int(Q.det())==106 and int(Q.det())%3!=0
assert any(int(x)%3 for x in A-Matrix.eye(3))
for k in range(1,4):
 m=3**k
 seen=set();cycles=Counter()
 for x in range(m**3):
  if x in seen:continue
  start=(x//(m*m),x//m%m,x%m)
  v=start;length=0
  while True:
   z=(v[0]*m+v[1])*m+v[2]
   assert z not in seen or v==start
   if v==start and length:break
   seen.add(z);length+=1
   v=(v[1],v[2],(v[0]+v[1]+v[2])%m)
  cycles[length]+=1
 expected={1:1}
 for t in range(1,k+1):expected[13*3**(t-1)]=2*9**(t-1)
 assert dict(cycles)==expected,(k,cycles,expected)
 assert len(seen)==m**3
 print(k,dict(sorted(cycles.items())))
print('VERIFY_OK: exact matrix lifting certificate and all 20439 state traces for k=1..3')
