"""Independent exact enumeration of realizable four-gram supports (requires NumPy).
The two halves are constructed by Cartesian doubling, not Gray-code traversal.
"""
import itertools
import numpy as np

K=3
alphabet=range(K)
def neg(e):return tuple((-a)%3 for a in e)
E=list(itertools.product(alphabet,repeat=4))
pairs=[(e,neg(e)) for e in E if e<neg(e)]
assert len(pairs)==40
V=list(itertools.product(alphabet,repeat=3))
vid={v:i for i,v in enumerate(V)}
reps=[v for v in V if v<neg(v)]
assert len(reps)==13

def data(e):
 a=e[:3];b=e[1:]
 f=np.fromiter((int(a==v)-int(b==v) for v in reps),dtype=np.int8,count=13)
 return f,int(e[0]==1)

def half(ps):
 flows=np.zeros((1,13),dtype=np.int8); counts=np.zeros(1,dtype=np.uint8)
 for p0,p1 in ps:
  f0,c0=data(p0);f1,c1=data(p1)
  flows=np.concatenate((flows+f0,flows+f1))
  counts=np.concatenate((counts+c0,counts+c1))
 assert len(flows)==1<<20
 assert np.all((-7<flows)&(flows<7))
 # Encode as thirteen independent 4-bit digits. Equal keys iff flow vectors equal.
 keys=np.zeros(len(flows),dtype=np.uint64)
 for i in range(13):keys|=(flows[:,i].astype(np.int16)+7).astype(np.uint64)<<(4*i)
 return keys,counts

lkey,lcount=half(pairs[:20]);rkey,rcount=half(pairs[20:])
perm=np.argsort(rkey,kind='stable');rkey=rkey[perm];rcount=rcount[perm]
# The original unpermuted masks are the branch indices in Cartesian doubling.
# First edge gives the highest bit; connectivity needs the same convention.
rmasks=perm.astype(np.uint32)
comp=np.zeros(len(lkey),dtype=np.uint64)
for i in range(13):comp|=(14-((lkey>>(4*i))&15)).astype(np.uint64)<<(4*i)
lo=np.searchsorted(rkey,comp,side='left');hi=np.searchsorted(rkey,comp,side='right')

hist=[0]*28;connected=[0]*28

def graph_connected(lm,rm):
 parent=list(range(27));degree=[0]*27
 def root(x):
  while parent[x]!=x:
   parent[x]=parent[parent[x]];x=parent[x]
  return x
 for j,p in enumerate(pairs):
  if j<20:choose=(lm>>j)&1
  else:choose=(rm>>(j-20))&1
  e=p[choose];a=vid[e[:3]];b=vid[e[1:]]
  degree[a]+=1;degree[b]+=1
  parent[root(a)]=root(b)
 found=None
 for i,d in enumerate(degree):
  if not d:continue
  v=root(i)
  if found is None:found=v
  elif found!=v:return False
 return True

for lm in np.flatnonzero(hi>lo):
 for j in range(lo[lm],hi[lm]):
  cnt=int(lcount[lm])+int(rcount[j])
  hist[cnt]+=1
  if graph_connected(int(lm),int(rmasks[j])):connected[cnt]+=1
assert sum(hist)==274624, sum(hist)
assert sum(connected)==218564, sum(connected)
expected_balanced={8:58,9:840,10:5522,11:19740,12:44266,13:66886,14:66886,15:44266,16:19740,17:5522,18:840,19:58}
expected_connected={8:58,9:774,10:4596,11:15444,12:34694,13:53716,14:53716,15:34694,16:15444,17:4596,18:774,19:58}
assert hist==[expected_balanced.get(i,0) for i in range(28)]
assert connected==[expected_connected.get(i,0) for i in range(28)]
# Explicit distinct cyclic-factor witnesses; negative all letters to obtain opposite counts.
witnesses={
 8:'0001020012002201220202121022112022212222',
 9:'0001020012002201122020222101221210212222',
 10:'0002011221020211021222001200220222212101',
 11:'0001001221100220210102022212102122220112',
 12:'0001001220101021002202120112212111202222',
 13:'0001001102120012010102210122121112202222'}
for j,w in witnesses.items():
 assert len(w)==40 and w.count('1')==j and w.count('0')==13
 windows={tuple(int(w[(i+t)%40]) for t in range(4)) for i in range(40)}
 assert len(windows)==40
 assert all(neg(x) not in windows for x in windows)

print('BALANCED',[(i,x) for i,x in enumerate(hist) if x])
print('CONNECTED',[(i,x) for i,x in enumerate(connected) if x])
print('TOTAL',sum(hist),sum(connected))
