import itertools,collections,json
from functools import reduce
from pathlib import Path

def intersect(a,b):return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))
L=[]
for i in range(6):
 m=[0]*6;m[i]=-1;L.append((0,*m))
for i,j in itertools.combinations(range(6),2):
 m=[0]*6;m[i]=m[j]=1;L.append((1,*m))
for absent in range(6):
 m=[int(i!=absent) for i in range(6)];L.append((2,*m))
assert len(L)==27 and len(set(L))==27
alpha=[]
for i in range(5):
 m=[0]*6;m[i]=-1;m[i+1]=1;alpha.append((0,*m))
alpha.append((1,1,1,1,0,0,0))
assert all(intersect(x,x)==-2 for x in alpha)
ref=[]
for r in alpha:
 p=[]
 for x in L:
  v=intersect(x,r)
  z=tuple(xi+v*ri for xi,ri in zip(x,r))
  p.append(L.index(z))
 ref.append(bytes(p))
assert all(all(ref[i][ref[i][j]]==j for j in range(27)) for i in range(6))

def mul(a,b):return bytes(a[b[i]] for i in range(27))
idperm=bytes(range(27)); perms=[idperm]; inds={idperm:0}
for p in perms:
 for g in ref:
  q=mul(p,g)
  if q not in inds:
   inds[q]=len(perms);perms.append(q)
assert len(perms)==51840, len(perms)
print('GROUP_ORDER',len(perms),flush=True)
# supports recursively adding eligible lines by bitsets
nonadj=[sum(1<<j for j in range(27) if j!=i and intersect(L[i],L[j])==0) for i in range(27)]
supports=[0];bylen=collections.Counter({0:1})
def dfs(mask,eligible,size):
 while eligible:
  bit=eligible&-eligible;eligible-=bit
  j=bit.bit_length()-1;nxt=mask|bit
  supports.append(nxt);bylen[size+1]+=1
  dfs(nxt, eligible&nonadj[j],size+1)
dfs(0,(1<<27)-1,0)
assert len(supports)==2764,(len(supports),bylen)
print('SUPPORTS',len(supports),sorted(bylen.items()),flush=True)
# conjugation by s: s p s
classes=[];unseen=set(perms)
while unseen:
 rep=min(unseen);orbit={rep};queue=[rep]
 for p in queue:
  for s in ref:
   q=mul(s,mul(p,s))
   if q not in orbit:
    orbit.add(q);queue.append(q)
 unseen.difference_update(orbit)
 classes.append((rep,len(orbit)))
assert len(classes)==25,len(classes)
print('CLASSES',len(classes), 'sizes', sorted(x[1] for x in classes),flush=True)
# The element order, class size and 27-line cycle type together identify the listed classes.

def cyc(p):
 seen=set();cs=[]
 for i in range(len(p)):
  if i in seen:continue
  j=i;k=0
  while j not in seen:
   seen.add(j);k+=1;j=p[j]
  cs.append(k)
 return tuple(sorted(collections.Counter(cs).items()))

def act(mask,p):
 t=0
 while mask:
  bit=mask&-mask;mask-=bit
  t|=1<<p[bit.bit_length()-1]
 return t

ans=[]
for rep,size in classes:
 seen=set();cycles=collections.Counter();fixed_by_size=collections.Counter()
 for start in supports:
  if start in seen:continue
  cur=start;l=0
  while cur not in seen:
   seen.add(cur);l+=1;cur=act(cur,rep)
  assert cur==start
  cycles[l]+=1
  if l==1:fixed_by_size[start.bit_count()]+=1
 assert len(seen)==2764
 order=reduce(lambda a,b:a*b//__import__('math').gcd(a,b),[x for x,n in cyc(rep)]+[1],1)
 ans.append(dict(rep=rep.hex(),class_size=size,order=order,line_cycles=dict(cyc(rep)),chamber_cycles=dict(sorted(cycles.items())),fixed_by_size=dict(sorted(fixed_by_size.items())),fixed=sum(n for l,n in cycles.items() if l==1)))
ans.sort(key=lambda x:(x['order'],tuple(sorted(x['line_cycles'].items())),x['class_size'],x['rep']))
print('results')
for i,a in enumerate(ans):
 print(i+1,a['order'],a['class_size'],a['line_cycles'],a['fixed'],a['chamber_cycles'],flush=True)
expected=json.loads(Path(__file__).with_name('e6_spectra.json').read_text(encoding='utf-8'))
assert json.loads(json.dumps(dict(bylen=dict(bylen),classes=ans))) == expected
assert sum(x['class_size'] for x in ans)==51840
print('W_E6_CHAMBER_CYCLE_TABLE_VERIFIED_OK',flush=True)
