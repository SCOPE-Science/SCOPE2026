import itertools,collections
import numpy as np,networkx as nx
n=16;G=nx.Graph();G.add_nodes_from(range(n))
for i in range(8): G.add_edges_from([(i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)])
adj=[set(G.neighbors(v)) for v in range(n)]
faces=[[] for _ in range(8)]
for mask in range(1,1<<16):
 s=tuple(i for i in range(16) if mask>>i&1)
 if len(s)<=8 and all(j not in adj[i] for z,i in enumerate(s) for j in s[z+1:]):faces[len(s)-1].append(s)
idx=[{s:i for i,s in enumerate(fs)} for fs in faces]
print('f', [len(fs) for fs in faces],flush=True)
def bd(k):
 A=np.zeros((len(faces[k-1]),len(faces[k])),dtype=np.uint8)
 for j,s in enumerate(faces[k]):
  for i in range(len(s)):A[idx[k-1][s[:i]+s[i+1:]],j]=1 if i%2==0 else 100
 return A
D4=bd(4);D5=bd(5);assert not (D4.astype('int32')@D5.astype('int32')%101).any()
p=101
def rref(M):
 a=M.copy().astype(np.int64);m,n=a.shape;rs=[];i=0
 for j in range(n):
  piv=next((r for r in range(i,m) if a[r,j]%p),None)
  if piv is None:continue
  a[[piv,i]]=a[[i,piv]];a[i,j:]=a[i,j:]*pow(int(a[i,j]),-1,p)%p
  nonzero=np.flatnonzero(a[:,j]);nonzero=nonzero[nonzero!=i]
  if len(nonzero):a[nonzero,j:]=(a[nonzero,j:] - a[nonzero,j,None]*a[i,j:])%p
  rs.append(j);i+=1
  if i==m:break
 return a[:i].astype('int64'),rs
B,pivb=rref(D4)
R,pivr=rref(D5.T)
print('ranks d4 d5',len(pivb),len(pivr),'h4',len(faces[4])-len(pivb)-len(pivr),flush=True)

def rem(v):
 v=v.astype('int64').copy()
 for r,j in enumerate(pivb):
  a=int(v[j]);
  if a:v[j:]=(v[j:]-a*B[r,j:])%p
 return v.astype('uint8')
z=None
for j in range(len(faces[4])):
 if j in pivr:continue
 v=np.zeros(len(faces[4]),dtype='uint8');v[j]=1
 for i,x in enumerate(pivr):v[x]=(-int(R[i,j]))%p
 if rem(v).any():z=v;print('z free',j,'support',np.count_nonzero(v));break
assert z is not None
print('cocycle condition',np.count_nonzero(D5.T.astype('int32')@z.astype('int32')%101))
print('D4 row cocycle condition',np.count_nonzero(D5.T.astype('int32')@B[0].astype('int32')%101))
perms=[]
for m in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter():perms.append(tuple(m[i] for i in range(n)))
perms=sorted(set(perms));print('group size',len(perms),flush=True)
assert len(perms)==96
ident=tuple(range(16))
def cyc(g):
 seen=set();out=[]
 for i in range(16):
  if i not in seen:
   a=[];j=i
   while j not in seen:a.append(j);seen.add(j);j=g[j]
   out.append(tuple(a))
 return out

def invs(g):
 w=np.zeros_like(z)
 for j,s in enumerate(faces[4]):
  t=tuple(g[x] for x in s);sgn=1 if sum(t[a]>t[b] for a in range(5) for b in range(a+1,5))%2==0 else -1
  w[idx[4][tuple(sorted(t))]]=int(z[j]) if sgn==1 else (-int(z[j]))%p
 for a in (1,-1):
  if not rem((w.astype('int64')-a*z.astype('int64'))%p).any():return a
 print('bad',g, 'w_cocycle',np.count_nonzero(D5.T.astype('int32')@w.astype('int32')%p),'z',np.count_nonzero(z),'w',np.count_nonzero(w), 'rrem', np.count_nonzero(rem(w)), 'zrem', np.count_nonzero(rem(z)), 'wrempos',list(zip(*np.where(rem(w))))[:10], 'zrempos',list(zip(*np.where(rem(z))))[:10], 'wremvals',rem(w)[np.flatnonzero(rem(w))][:15], 'zremvals',rem(z)[np.flatnonzero(rem(z))][:15])
 raise Exception('not ±1')

def lefs(g):
 val=-1
 for k,ss in enumerate(faces):
  for s in ss:
   t=[g[x] for x in s]
   if sorted(t)==list(s):val+=(-1)**k *(-1 if sum(t[a]>t[b] for a in range(k+1) for b in range(a+1,k+1))%2 else 1)
 return val

def mul(g,h):return tuple(g[h[i]] for i in range(n))
def inverse(g):
 q=[0]*n
 for i,j in enumerate(g):q[j]=i
 return tuple(q)
classes=[];todo=set(perms)
while todo:
 g=min(todo);cl={mul(mul(h,g),inverse(h)) for h in perms};classes.append((g,cl));todo.difference_update(cl)

res=[]
for g,cl in sorted(classes,key=lambda t:(len(t[1]),t[0])):
 eta=invs(g);L=lefs(g);chi3=eta-L;order=1;cur=g
 while cur!=ident:order+=1;cur=mul(cur,g)
 res.append((len(cl),order,tuple(sorted(collections.Counter(map(len,cyc(g))).items())),eta,chi3, L, g))
 print('class',res[-1],flush=True)
print('all 96 top signs verified',len({g:invs(g) for g in perms}),flush=True)
print('invariant dims',sum(v[0]*v[3] for v in res)//96,sum(v[0]*v[4] for v in res)//96,flush=True)
print('inner product H3',sum(v[0]*v[4]**2 for v in res)/96,flush=True)
print('inner product H4-H3',sum(v[0]*v[3]*v[4] for v in res)/96,flush=True)
print('FULL_AUTOMORPHISM_CHARACTER_VERIFIED',flush=True)
