"""Independent recurrent-state generation by sandpile addition group orbit,
with parallel legal topplings and exact avalanche enumerators.
Run with Python 3.10+; no third-party dependencies.
"""
from collections import Counter,deque

def graphs():
 cube=tuple(tuple(x ^ (1<<j) for j in range(3)) for x in range(8))
 octa=tuple(tuple(y for y in range(6) if y//2 != x//2) for x in range(6))
 return [('Q3',cube),('Octahedron',octa)]

def stabilize(adj,c,v):
 z=list(c);z[v]+=1
 topp=[0]*len(z)
 for it in range(500):
  fire=[u for u in range(1,len(z)) if z[u]>=len(adj[u])]
  if not fire:
   return tuple(z),tuple(topp)
  for u in fire:
   z[u]-=len(adj[u]);topp[u]+=1
  for u in fire:
   for w in adj[u]:
    if w: z[w]+=1
 raise RuntimeError('toppling failed to terminate')

def orbit(adj):
 init=tuple([0]+[len(adj[v])-1 for v in range(1,len(adj))])
 seen={init};q=deque([init]);poly=Counter();sinkpoly=Counter();nondiss=Counter();odpoly=Counter()
 while q:
  c=q.popleft()
  for v in range(1,len(c)):
   aft,top=stabilize(adj,c,v)
   if aft not in seen:seen.add(aft);q.append(aft)
   t=sum(top);b=sum(top[w] for w in adj[0]);poly[t]+=1;sinkpoly[b]+=1
   if t>0 and b==0:nondiss[v.bit_count() if len(c)==8 else v]+=1
   odpoly[top[1:]]+=1
 return seen,poly,sinkpoly,nondiss,odpoly

expected={
 'Q3': {'N':384,'P':{0:1162,1:214,2:180,3:144,4:213,5:138,6:207,7:186,8:108,9:36,10:36,11:36,12:9,13:9,15:6,18:3,19:1},'B':{0:1226,1:666,2:450,3:282,4:48,5:12,6:4},'ND':{2:45,3:19}},
 'Octahedron': {'N':384,'P':{0:1133,1:180,2:128,3:126,4:128,5:180,6:45},'B':{0:1133,1:244,2:178,3:140,4:225},'ND':{}}
}
if __name__=='__main__':
 for name,graph in graphs():
  seen,poly,burst,nd,od=orbit(graph)
  ref=expected[name]
  assert len(seen)==ref['N'] and dict(poly)==ref['P'] and dict(burst)==ref['B'] and dict(nd)==ref['ND']
  assert sum(poly.values())==ref['N']*(len(graph)-1)
  print(name,'PASS',len(seen),'recurrent states; events',sum(poly.values()),'nontrivial nondissipative',sum(nd.values()),'distinct odometers',len(od))
