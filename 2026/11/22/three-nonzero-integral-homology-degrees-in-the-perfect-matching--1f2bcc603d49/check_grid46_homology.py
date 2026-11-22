import time,collections,functools,sys
R,C=4,6
edges=[]
for i in range(R):
 for j in range(C):
  if i+1<R: edges.append((i*C+j,(i+1)*C+j))
  if j+1<C: edges.append((i*C+j,i*C+j+1))
inc=[[] for _ in range(R*C)]
for k,(a,b) in enumerate(edges):inc[a].append((b,k));inc[b].append((a,k))
facets=[]
def rec(todo,mask):
 if not todo:facets.append(mask);return
 a=(todo&-todo).bit_length()-1
 for b,k in inc[a]:
  if todo>>b&1:rec(todo ^ (1<<a) ^ (1<<b),mask|(1<<k))
rec((1<<(R*C))-1,0)
faces=set()
for f in facets:
 subs=[0]
 while f:
  x=f&-f;subs+=[a|x for a in subs];f^=x
 faces.update(subs)
faces.remove(0)
U=set(faces); low_high={};high_low={}
for k in range(len(edges)):
 bit=1<<k
 todos=[f for f in U if not f&bit and f|bit in U]
 for f in todos:
  high=f|bit
  if f in U and high in U:
   U.remove(f); U.remove(high)
   low_high[f]=high;high_low[high]=f
assert (len(facets),len(faces),len(low_high),len(U))==(281,511338,255663,12)
assert collections.Counter(x.bit_count()-1 for x in U)=={0:1,3:2,4:8,5:1}
print('facets',len(facets),'faces',len(faces),'pairs',len(low_high),'critical',len(U),'crit_dims',dict(collections.Counter(x.bit_count()-1 for x in U)),flush=True)
# graph gradient edges down except each matched pair reversed
indeg={f:0 for f in faces}
for f in faces:
 if f in low_high: indeg[low_high[f]]+=1
 b=f
 paired_low=high_low.get(f,-1)
 while b:
  bit=b&-b;g=f^bit;b^=bit
  if g and g!=paired_low:indeg[g]+=1
from collections import deque
qu=deque(f for f in faces if indeg[f]==0);visited=0
while qu:
 f=qu.popleft();visited+=1
 if f in low_high:
  x=low_high[f]; indeg[x]-=1
  if indeg[x]==0:qu.append(x)
 b=f;paired_low=high_low.get(f,-1)
 while b:
  bit=b&-b;g=f^bit;b^=bit
  if g and g!=paired_low:
   indeg[g]-=1
   if indeg[g]==0:qu.append(g)
print('gradient_acyclic',visited==len(faces),'visited',visited,flush=True)
if visited!=len(faces):sys.exit(1)
# Hasse boundary coefficient for removing bit from high face
def sign(f,bit):return -1 if (f&(bit-1)).bit_count()%2 else 1
crit={d:sorted(f for f in U if f.bit_count()-1==d) for d in range(0,12)}
for dim in [4,5]:
 target=crit[dim-1]; ids={f:i for i,f in enumerate(target)}
 @functools.lru_cache(None)
 def reduce(f):
  if f in ids:return {ids[f]:1}
  if f not in low_high:return {}
  high=low_high[f]
  if high.bit_count()!=dim+1:return {}
  bit=high^f
  sr=sign(high,bit)
  out=collections.defaultdict(int)
  bits=high
  while bits:
   bit2=bits&-bits; bits^=bit2;g=high^bit2
   if g==f:continue
   co=-sr*sign(high,bit2)
   for j,v in reduce(g).items():out[j]+=co*v
  return {i:v for i,v in out.items() if v}
 mat=[]
 for high in crit[dim]:
  val=collections.defaultdict(int)
  b=high
  while b:
   bit=b&-b;b^=bit;g=high^bit
   for j,v in reduce(g).items(): val[j]+=sign(high,bit)*v
  mat.append([val.get(j,0) for j in range(len(target))])
 assert mat==([[-1,0]]+[[0,0]]*7 if dim==4 else [[0]*8])
 print('boundary',dim,'x',dim-1,'critical high',len(crit[dim]),'critical low',len(target),'matrix ROWS high:',mat,flush=True)
