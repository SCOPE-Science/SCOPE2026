from collections import Counter,deque
from itertools import combinations

def matrices(n):
    for a in range(n+1):
      for b in range(n-a+1):
       c=n-a-b
       for d in range(n+1):
        for e in range(n-d+1):
         f=n-d-e
         g=n-a-d;h=n-b-e;i=n-c-f
         if min(g,h,i)>=0 and g+h+i==n:
          yield (a,b,c,d,e,f,g,h,i)

def graph(n):
 v=list(matrices(n));lookup={a:i for i,a in enumerate(v)};adj=[set() for _ in v]
 for ix,x in enumerate(v):
  for i,j in combinations(range(3),2):
   for k,l in combinations(range(3),2):
    for sign in (-1,1):
     z=list(x);t=((i,k,sign),(j,l,sign),(i,l,-sign),(j,k,-sign))
     for r,c,d in t:z[3*r+c]+=d
     if min(z)>=0:adj[ix].add(lookup[tuple(z)])
 ecc=[];pairs=Counter()
 for ix in range(len(v)):
  dist={ix:0};q=deque([ix]);
  while q:
   a=q.popleft()
   for b in adj[a]:
    if b not in dist:dist[b]=dist[a]+1;q.append(b)
  assert len(dist)==len(v)
  ecc.append(max(dist.values()))
  for j,d in dist.items():
   if j>ix:pairs[d]+=1
 return len(v),sum(map(len,adj))//2,Counter(ecc), pairs
if __name__=='__main__':
 for n in range(1,9):
  v,e,ec,p=graph(n)
  print(n,v,e,dict(ec),'diam=',max(ec),'pairs_last',p[max(ec)],flush=True)
