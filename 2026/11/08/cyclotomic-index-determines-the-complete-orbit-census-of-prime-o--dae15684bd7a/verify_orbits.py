"""Direct exhaustive functional graph for GPaley(7,2) over F7; no linear algebra library."""
from collections import Counter
p,k=7,3
H={pow(a,k,p) for a in range(1,p)}
assert H=={1,6}
weights=[p**i for i in range(p)]
limit=p**p
visited=bytearray(limit)
cycles=Counter()
visited_count=0

def step(z):
 digits=[];temp=z
 for _ in range(p):
  digits.append(temp%p);temp//=p
 return sum((sum(digits[(i+h)%p] for h in H)%p)*weights[i] for i in range(p))

for start in range(limit):
 if visited[start]:continue
 cur=start;path=[]
 while not visited[cur]:
  visited[cur]=1
  path.append(cur)
  cur=step(cur)
 assert cur==start,(start,cur)
 cycles[len(path)]+=1
 visited_count+=len(path)
assert visited_count==limit
ell=3
expected={1:1,ell:(p**len(H)-1)//ell,p*ell:(p**p-p**len(H))//(p*ell)}
assert dict(cycles)==expected,(cycles,expected)
print('PASS exhaustive states=',visited_count,'cycle counts=',dict(sorted(cycles.items())))
