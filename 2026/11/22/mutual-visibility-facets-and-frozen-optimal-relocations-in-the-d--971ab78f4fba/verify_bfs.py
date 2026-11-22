"""Independent full 2^20 enumeration for mutual visibility using BFS through unselected interiors."""
from collections import Counter
from itertools import combinations
N=20
adj=[0]*N
for i in range(10):
 for a,b in [(i,(i+1)%10),(i,10+i),(10+i,10+(i+3)%10)]:
  adj[a]|=1<<b;adj[b]|=1<<a
assert all(x.bit_count()==3 for x in adj)
def dists(s):
 d=[-1]*N;d[s]=0;todo=[s]
 for u in todo:
  q=adj[u]
  while q:
   bit=q&-q;v=bit.bit_length()-1;q-=bit
   if d[v]<0:d[v]=d[u]+1;todo.append(v)
 return d
baseline=[dists(i) for i in range(N)]

def distance_through_free(u,v,occupied):
 # visited vertices have no blocked interiors. Endpoints are always permitted.
 forbidden=occupied & ~((1<<u)|(1<<v))
 level=[u];seen=1<<u;depth=0
 while level and depth<baseline[u][v]:
  following=[];depth+=1
  for w in level:
   q=adj[w]&~forbidden&~seen
   while q:
    bit=q&-q;q-=bit
    z=bit.bit_length()-1
    if z==v:return depth
    seen|=bit;following.append(z)
  level=following
 return 100

def good(s):
 bits=[i for i in range(N) if (s>>i)&1]
 for u,v in combinations(bits,2):
  if distance_through_free(u,v,s)>baseline[u][v]:return False
 return True

if __name__=='__main__':
 import time
 t=time.monotonic();good_status=bytearray(1<<N);good_status[0]=1
 ct=Counter({0:1})
 for s in range(1,1<<N):
  if not good_status[s&(s-1)]:continue
  if good(s):
   good_status[s]=1;ct[s.bit_count()]+=1
 print('independent GP census',dict(sorted(ct.items())), 'total',sum(ct.values()),'time',time.monotonic()-t,flush=True)
 assert [ct[i] for i in range(10)]==[1,20,190,1080,3925,8944,11300,5840,150,0]
 print('VERIFY_BFS_OK')
