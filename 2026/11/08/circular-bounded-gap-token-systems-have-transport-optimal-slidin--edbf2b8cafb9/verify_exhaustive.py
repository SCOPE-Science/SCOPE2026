from itertools import combinations
from collections import deque

def dist_transport(U,V,n):
 k=len(U)
 return min(sum(abs(U[i]-(V[(i+j)%k]+n*((i+j)//k+h))) for i in range(k)) for j in range(k) for h in range(-2,2))
def check(n,k,a,b):
 X={c for c in combinations(range(n),k) if all(a<=((c[(i+1)%k]-c[i])%n)<=b for i in range(k))}
 if not X:return (0,0,0)
 g={t:set() for t in X}
 for t in X:
  for u in t:
   for v in ((u-1)%n,(u+1)%n):
    q=tuple(sorted((set(t)-{u})|{v}))
    if q in X:g[t].add(q)
 num=0
 for x in X:
  d={x:0};Q=deque([x]);
  while Q:
   v=Q.popleft()
   for w in g[v]:
    if w not in d:d[w]=d[v]+1;Q.append(w)
  if len(d)!=len(X):return ('DISCONNECTED',n,k,a,b,x,len(d),len(X))
  for y,dist in d.items():
   w=dist_transport(x,y,n)
   if w!=dist:return ('NONISOMETRIC',n,k,a,b,x,y,dist,w)
   num+=1
 return (len(X),sum(map(len,g.values()))//2,num)
for a,b in ((2,3),(2,4),(3,4),(3,5),(2,5)):
 for k in range(2,5):
  for n in range(a*k+1,min(b*k,14)):
   r=check(n,k,a,b)
   print((n,k,a,b),r,flush=True)
   if isinstance(r[0],str):quit()
