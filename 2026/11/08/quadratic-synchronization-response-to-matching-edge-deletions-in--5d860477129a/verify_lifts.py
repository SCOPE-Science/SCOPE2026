from itertools import product
from collections import deque

def count_via_lift(n,t):
 E=[(i,n+j) for i in range(n) for j in range(n) if i!=j or i>=t]
 adj=[[] for _ in range(2*n)]
 for u,v in E:adj[u].append(v);adj[v].append(u)
 found=0
 for X in product(range(3),repeat=2*n):
  h=[None]*(2*n);h[0]=0; q=deque([0]); okay=True
  while q and okay:
   v=q.popleft()
   for u in adj[v]:
    d=(X[u]-X[v])%3
    d=-1 if d==2 else d
    z=h[v]+d
    if h[u] is None:h[u]=z;q.append(u)
    elif h[u]!=z:okay=False;break
  if okay:found+=1
 return found

def Z(n,t):return 3*(4**n+2*3**n-2**(n+2)+1+t*2**(n+1)+t*(t-1))
for n in range(3,7):
 for t in range(n+1):
  a=count_via_lift(n,t);b=Z(n,t)
  assert a==b,(n,t,a,b)
  print(n,t,a,b)
print('ALL_PASS')
