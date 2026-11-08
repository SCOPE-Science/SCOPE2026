# Reproducible exact finite certificate for the dihedral homology character
# of the independence complex of the 25-vertex stable Kneser graph.
# Uses only the Python standard library. All orientations are increasing in
# the lexicographically enumerated list of stable four-subsets.
from itertools import combinations
from collections import Counter, deque
import ast
n=4;m=2*n+2
V=[c for c in combinations(range(m),n) if all((c[(j+1)%n]-c[j])%m>=2 for j in range(n))]
print('vertices',len(V),flush=True)
N=len(V)
E=[(i,j) for i,j in combinations(range(N),2) if not(set(V[i])&set(V[j]))]
nei=[0]*N
for i,j in E:nei[i]|=1<<j;nei[j]|=1<<i
print('edges',len(E),flush=True)
faces=[0]
def visit(mask, candidates):
 while candidates:
  bit=candidates&-candidates
  i=bit.bit_length()-1
  candidates-=bit
  w=mask|bit
  faces.append(w)
  visit(w,candidates&~nei[i])
visit(0,(1<<N)-1)
print('facecount',len(faces),'counts',Counter(f.bit_count()-1 for f in faces),flush=True)

idx={a:i for i,a in enumerate(V)}
ORDER=[4, 23, 14, 12, 10, 0, 5, 11, 16, 7, 17, 18, 13, 20, 15, 21, 8, 2, 19, 9, 22, 6, 3, 1, 24]
rem=set(faces); paired={}
for v in ORDER:
 pairs=[(a,a|(1<<v)) for a in list(rem) if not a>>v&1 and (a|(1<<v)) in rem]
 for lo,hi in pairs:
  rem.remove(lo);rem.remove(hi); paired[lo]=hi
assert Counter(x.bit_count()-1 for x in rem)=={3:1,4:2},Counter(x.bit_count()-1 for x in rem)
critical3=[x for x in rem if x.bit_count()==4][0]

def orient(f,child):
 # boundary coefficient of f->child
 return (-1)**(sum(1 for i in range(N) if (f>>i)&1 and i<(f^child).bit_length()-1))

def boundary(f):
 return [(f&~(1<<i),(-1)**sum((f>>j&1) for j in range(i))) for i in range(N) if f>>i&1]
low_to_high={lo:hi for lo,hi in paired.items() if lo.bit_count()==3}
lowset=set(low_to_high)
succ={lo:set() for lo in lowset};indeg={lo:0 for lo in lowset}
for lo,hi in low_to_high.items():
 for child,_ in boundary(hi):
  if child!=lo and child in lowset:
   succ[lo].add(child)
for lo in lowset:
 for to in succ[lo]:indeg[to]+=1
q=deque(sorted(lo for lo in lowset if not indeg[lo]));top=[]
while q:
 lo=q.popleft();top.append(lo)
 for to in succ[lo]:
  indeg[to]-=1
  if indeg[to]==0:q.append(to)
assert len(top)==len(lowset)

def reduce_z(z):
 z=dict(z);b=Counter()
 for f,c in z.items():
  for child,sg in boundary(f):b[child]+=c*sg
 for lo in top:
  coeff=b[lo]
  if coeff:
   hi=low_to_high[lo]
   eps=next(s for child,s in boundary(hi) if child==lo)
   k=-coeff*eps
   z[hi]=z.get(hi,0)+k
   for child,sg in boundary(hi):b[child]+=k*sg
 assert not any(b.values()),[(bin(i),n) for i,n in b.items() if n][:10]
 return {f:c for f,c in z.items() if c}

def mapped_chain(z,f):
 p=[idx[tuple(sorted(f(i) for i in v))] for v in V]
 res=Counter()
 for mask,c in z.items():
  mapped=[p[i] for i in range(N) if mask>>i&1]
  target=sum(1<<i for i in mapped)
  s=(-1)**sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
  res[target]+=c*s
 return {f:c for f,c in res.items() if c}


lo4={lo:hi for lo,hi in paired.items() if lo.bit_count()==4}
lowset4=set(lo4)
succ4={lo:set() for lo in lowset4};indeg4={lo:0 for lo in lowset4}
for lo,hi in lo4.items():
 for child,_ in boundary(hi):
  if child!=lo and child in lowset4: succ4[lo].add(child)
for lo in lowset4:
 for to in succ4[lo]:indeg4[to]+=1
q=deque(sorted(lo for lo in lowset4 if not indeg4[lo]));top4=[]
while q:
 lo=q.popleft();top4.append(lo)
 for to in succ4[lo]:
  indeg4[to]-=1
  if indeg4[to]==0:q.append(to)
assert len(top4)==len(lo4)

def homolog_mod_b4(y):
 y=Counter(y)
 for lo in top4:
  c=y[lo]
  if c:
   hi=lo4[lo]
   ep=next(v for f,v in boundary(hi) if f==lo)
   for f,v in boundary(hi): y[f]-=c*ep*v
 return {f:c for f,c in y.items() if c}

z=reduce_z({critical3:1})
print('cycle len',len(z), 'critical3',critical3)
red=homolog_mod_b4(z);print('reduced original',len(red),red.get(critical3), 'other',len(red)-1)
for op,f in [('r',lambda i:(i+1)%m),('s',lambda i:(-i)%m),('r2',lambda i:(i+2)%m)]:
 image=mapped_chain(z,f)
 rd=homolog_mod_b4(image)
 print(op,'red_len',len(rd),'critical3',rd.get(critical3,0),'others',len(rd)-int(critical3 in rd))
for f in rem:
 if f.bit_count()==5:
  rd=homolog_mod_b4(dict(boundary(f))); print('critical4_boundary_projection',rd.get(critical3,0),'otherlen',len(rd))
bad=[]
for f in faces:
 if f.bit_count()==5:
  x=homolog_mod_b4(dict(boundary(f)))
  if x.get(critical3,0): bad.append((f,x.get(critical3)))
print('ALL_4_BOUNDARY_CRITICAL_PROJECTION_ZERO',not bad,'bad',bad[:5])

F=set(faces); p2={hi:lo for lo,hi in paired.items()}
# Directed Hasse edges: unmatched high->low, matched low->high. If acyclic, the matching is valid.
indeg={a:0 for a in faces};children={a:[] for a in faces}
for hi in faces:
 for lo,_ in boundary(hi):
  if hi not in F or lo not in F: continue
  if paired.get(lo)==hi: u,v=lo,hi
  else: u,v=hi,lo
  indeg[v]+=1;children[u].append(v)
q=deque(a for a in faces if indeg[a]==0);count=0
while q:
 u=q.popleft();count+=1
 for v in children[u]:
  indeg[v]-=1
  if indeg[v]==0:q.append(v)
print('HASSE_MATCHING_DAG',count,len(faces),count==len(faces))
assert count==len(faces)

def action(f):return [idx[tuple(sorted(f(x) for x in v))] for v in V]
def t(p):
 tr=0
 for mask in faces:
  ids=[i for i in range(N) if mask>>i&1]
  aim=[p[i] for i in ids]
  if set(ids)==set(aim):
   inversions=sum(aim[i]>aim[j] for i in range(len(aim)) for j in range(i+1,len(aim)))
   tr+=(-1 if (len(aim)+inversions)%2==0 else 1)
 return tr
rot=[t(action(lambda i,a=a:(i+a)%m)) for a in range(m)]
ref=[t(action(lambda i,a=a:(a-i)%m)) for a in range(m)]
print('rot',rot,'refl',ref)

assert rot==[1,-1]*5 and ref==[3,1]*5
print('SCHRIJVER_4_2_DIHERAL_HOMOLOGY_PASS')
