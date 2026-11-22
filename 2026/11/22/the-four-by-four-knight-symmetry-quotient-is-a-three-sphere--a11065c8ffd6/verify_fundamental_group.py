from collections import deque,Counter
x=open('quotient_reduced.txt').readlines(); D=int(x[0]);sizes=list(map(int,x[1:1+D]));i=1+D
B=[[] for _ in sizes]
for d in range(1,D):
 for col in range(sizes[d]):
  a=list(map(int,x[i].split()));i+=1;B[d].append({a[j+1]:a[j+2] for j in range(0,2*a[0],2)})
assert x[i].strip()=='FLAGS';i+=1
flags=[[] for _ in sizes]
for d in range(D):
 for _ in range(sizes[d]):
  a=list(map(int,x[i].split()));i+=1;assert a[0]==d;flags[d].append(tuple(a[1:]))
assert i==len(x)
# derive geometric perms acting on face mask from original face ordering
n=4;N=n*n; adj=[0]*N
for i in range(N):
 for j in range(N):
  if sorted([abs(i//n-j//n),abs(i%n-j%n)])==[1,2]:adj[i]|=1<<j
faces=[]
def rec(s,p):
 if s:faces.append(s)
 while p:
  b=p&-p;p-=b;v=b.bit_length()-1;rec(s|b,p&~adj[v])
rec(0,(1<<N)-1);faces.sort();face_ix={f:i for i,f in enumerate(faces)}
perms=[]
for a in range(8):
 p=[]
 for v in range(N):
  r,c=divmod(v,n)
  if a>=4:c=n-1-c
  for _ in range(a%4):r,c=c,n-1-r
  p.append(r*n+c)
 perms.append(p)
trans=[[face_ix[sum(1<<p[v] for v in range(N) if f>>v&1)] for f in faces] for p in perms]
def canon(f):return min(tuple(t[v] for v in f) for t in trans)
vid={f:i for i,f in enumerate(flags[0])};eid={f:i for i,f in enumerate(flags[1])}
# all quotient endpoint ids and edges
endpoints=[]
for k,(a,b) in enumerate(flags[1]):
 p=vid[canon((a,))];q=vid[canon((b,))]
 endpoints.append((p,q)); assert p!=q
 assert B[1][k]=={p:-1,q:1},(k,p,q,B[1][k])
# spanning tree
parent=list(range(sizes[0]));defroot=lambda a:a
def find(x):
 while x!=parent[x]:x=parent[x]
 return x
gen={};N=0
for e,(p,q) in enumerate(endpoints):
 fp,fq=find(p),find(q)
 if fp!=fq:parent[fp]=fq
 else:
  N+=1;gen[e]=N
assert len({find(v) for v in range(sizes[0])})==1
print('tree edges',sizes[1]-N,'generators',N)
# triangle edge orbits: oriented ∂[a,b,c]=[b,c]-[a,c]+[a,b]
rels=[]
for t,(a,b,c) in enumerate(flags[2]):
 es=[eid[canon((a,b))],eid[canon((b,c))],eid[canon((a,c))]]
 assert B[2][t]=={es[0]:1,es[1]:1,es[2]:-1},(t,es,B[2][t])
 rel=tuple(z for z in (gen.get(es[0],0),gen.get(es[1],0),-gen.get(es[2],0)) if z)
 rels.append(rel)
def reduce_word(w):
 o=[]
 for x in w:
  if o and o[-1]==-x:o.pop()
  else:o.append(x)
 while len(o)>1 and o[0]==-o[-1]:o=o[1:-1]
 return tuple(o)
def invert(w):return tuple(-a for a in reversed(w))
rels=[reduce_word(r) for r in rels if reduce_word(r)]
print('initial nonempty rels',len(rels),'lengths',Counter(map(len,rels)))
active=set(range(1,N+1));ops=[]
while True:
 occ=Counter(abs(g) for w in rels for g in w)
 candidates=[]
 for k,w in enumerate(rels):
  cnt=Counter(map(abs,w))
  for g,c in cnt.items():
   if c==1:
    candidates.append(( (len(w)-1)*max(occ[g]-1,0),len(w),occ[g],g,k))
 if not candidates:break
 _,__,___,g,k=min(candidates)
 w=rels[k]
 idx=next(j for j,v in enumerate(w) if abs(v)==g)
 w=w[idx:]+w[:idx]
 assert abs(w[0])==g
 rhs = invert(w[1:]) if w[0]>0 else w[1:]
 new=[]
 for j,word in enumerate(rels):
  if j==k:continue
  out=[]
  for z in word:
   if abs(z)==g:out.extend(rhs if z>0 else invert(rhs))
   else:out.append(z)
  rr=reduce_word(out)
  if rr:new.append(rr)
 rels=new
 active.remove(g);ops.append((g,len(w)))
 if len(ops)%10==0:print('eliminated',len(ops),'remain',len(active),'relators',len(rels),'maxlength',max(map(len,rels),default=0),flush=True)
print('FINAL eliminated',len(ops),'active',sorted(active),'relators',len(rels),'maxword',max(map(len,rels),default=0),'lengths',Counter(map(len,rels)))
assert not active and not rels
print('KNIGHT4_D4_PI1_TRIVIAL_OK', len(ops))
