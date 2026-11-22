import itertools,collections

def check(n,E):
 C=set(E)
 sig=[]
 for i in range(n):
  for j in range(n):
   s=frozenset((r,c) for r,c in C if r==i or c==j)
   if not s:return False
   sig.append(s)
 return len(set(sig))==n*n

def shape(n,E):
 deg=[0]*(2*n)
 adj=[[] for _ in range(2*n)]
 for i,j in E:
  deg[i]+=1;deg[n+j]+=1;adj[i].append(n+j);adj[n+j].append(i)
 comp=[]; seen=set()
 for u in range(2*n):
  if u in seen:continue
  todo=[u];seen.add(u); nodes=[]
  while todo:
   v=todo.pop();nodes.append(v)
   for w in adj[v]:
    if w not in seen:seen.add(w);todo.append(w)
  comp.append((len(nodes),sum(deg[v] for v in nodes)//2, tuple(sorted(deg[v] for v in nodes))))
 return tuple(sorted(comp))

for n in (4,):
 shapes=collections.Counter();cnt=0
 for ids in itertools.combinations(range(n*n),3*n//2):
  E=[divmod(v,n) for v in ids]
  if check(n,E):
   cnt+=1; shapes[shape(n,E)]+=1
 print(n,cnt)
 for a,b in shapes.most_common():print(b,a)
