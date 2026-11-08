import itertools,collections,functools
P=list(itertools.permutations(range(4)));idp={p:i for i,p in enumerate(P)}
N=24
adj=[set()for _ in P]
for i,p in enumerate(P):
 for j in range(3):
  q=list(p);q[j],q[j+1]=q[j+1],q[j];adj[i].add(idp[tuple(q)])
d=[]
for i in range(N):
 x={i:0};q=collections.deque([i])
 while q:
  j=q.popleft()
  for k in adj[j]:
   if k not in x:x[k]=x[j]+1;q.append(k)
 d.append([x[j] for j in range(N)])
forbidden=[0]*N
for i in range(N):
 forbidden[i]=sum(1<<j for j in range(N) if d[i][j]>4)
faces={0}
def rec(mask, avail):
 if mask:faces.add(mask)
 while avail:
  b=avail&-avail;v=b.bit_length()-1;avail^=b
  rec(mask|b,avail&~forbidden[v])
rec(0,(1<<N)-1)
print('faces',len(faces),flush=True)
bydim=collections.defaultdict(list)
for s in faces:bydim[s.bit_count()-1].append(s)
for key in bydim:bydim[key].sort()
upper2lower={}; lower2upper={};unpaired=set(faces)
for v in range(N):
 bit=1<<v
 for low in sorted(x for x in unpaired if not x&bit and x|bit in unpaired):
  up=low|bit;unpaired.remove(low);unpaired.remove(up);lower2upper[low]=up;upper2lower[up]=low
critical=sorted(unpaired,key=lambda s:(s.bit_count(),s))
print('critical',[(x.bit_count()-1,x)for x in critical],flush=True)

def boundary(s):
 vertices=[i for i in range(N) if (s>>i)&1]
 return [(s^(1<<v),(-1)**j)for j,v in enumerate(vertices)]
# All face poset matching digraph, orientation sigma -> facet except matched reverse.
indeg=collections.Counter();out=collections.defaultdict(list)
for s in faces:
 if not s:continue
 for f,c in boundary(s):
  if upper2lower.get(s)==f: u,v=f,s
  else:u,v=s,f
  out[u].append(v);indeg[v]+=1
queue=collections.deque([s for s in faces if indeg[s]==0]);seen=0
while queue:
 s=queue.popleft();seen+=1
 for t in out[s]:
  indeg[t]-=1
  if indeg[t]==0:queue.append(t)
print('acyclic:',seen==len(faces), 'pairs',len(lower2upper),flush=True)
# P(lower) expression from other facets of paired upper. Cache critical coordinate dictionary
crit_by_dim={k:[x for x in critical if x.bit_count()-1==k]for k in [4,5]}
ci={k:{x:j for j,x in enumerate(crit_by_dim[k])}for k in [4,5]}
@functools.lru_cache(None)
def proj(s):
 dim=s.bit_count()-1
 if s in ci.get(dim,{}):return {s:1}
 if s in upper2lower:return {}
 if s not in lower2upper: return {}
 up=lower2upper[s];a=dict(boundary(up))[s]
 z=collections.defaultdict(int)
 for f,b in boundary(up):
  if f==s:continue
  for t,n in proj(f).items():z[t]-=a*b*n
 return {t:n for t,n in z.items()if n}
for k in [4,5]:
 for s in bydim[k]:proj(s)
 print('P',k, 'cached:',proj.cache_info(),flush=True)
# For each k, order matching lower k-1 cells using dependency digraph from alpha to all other matched lower facets beta.
def mk_lift(k):
 lowers=[s for s in bydim[k-1] if s in lower2upper]
 lowerset=set(lowers);indeg={s:0 for s in lowers};out={s:[] for s in lowers}
 for s in lowers:
  b=lower2upper[s]
  for f,_ in boundary(b):
   if f!=s and f in lowerset:out[s].append(f);indeg[f]+=1
 q=collections.deque(s for s in lowers if indeg[s]==0);order=[]
 while q:
  s=q.popleft();order.append(s)
  for t in out[s]:
   indeg[t]-=1
   if indeg[t]==0:q.append(t)
 assert len(order)==len(lowers)
 lifts={}
 for crit in crit_by_dim[k]:
  chain=collections.defaultdict(int,{crit:1});bd=collections.defaultdict(int)
  for f,c in boundary(crit):bd[f]+=c
  for s in order:
   coeff=bd[s]
   if not coeff:continue
   b=lower2upper[s];inc=dict(boundary(b))[s];c=-coeff*inc
   chain[b]+=c
   for f,a in boundary(b):bd[f]+=c*a
  assert all(bd[s]==0 for s in lowers)
  lifts[crit]={t:n for t,n in chain.items()if n}
 return lifts
I={k:mk_lift(k)for k in [4,5]}
for k in [4,5]:
 print('I',k,'sizes', [len(I[k][s])for s in crit_by_dim[k]],'maxcoef',max(abs(n) for c in I[k].values()for n in c.values()),flush=True)
 for s in crit_by_dim[k]:
  z=collections.defaultdict(int)
  for t,n in I[k][s].items():
   for f,a in proj(t).items():z[f]+=n*a
  assert z=={s:1}, (s,z)

def projchain(c):
 z=collections.defaultdict(int)
 for t,n in c.items():
  for f,a in proj(t).items():z[f]+=n*a
 return {t:n for t,n in z.items()if n}
# boundary on critical 5 -> 4 after lifted, expected rank1
B=[]
for s in crit_by_dim[5]:
 bd=collections.defaultdict(int)
 for t,n in I[5][s].items():
  for f,a in boundary(t):bd[f]+=n*a
 z=projchain(bd)
 B.append([z.get(t,0)for t in crit_by_dim[4]])
print('B rows 5 columns 4',B,flush=True)
# group actions left label a and right reversing positions
w0=(3,2,1,0)
def perm_action(a,b):
 return [idp[tuple(a[p[w0[j] if b else j]]for j in range(4))] for p in P]
def sign_and_face(s,g):
 old=[j for j in range(N)if (s>>j)&1];new=[g[j]for j in old];inv=sum(new[i]>new[j]for i in range(len(new))for j in range(i+1,len(new)))
 return sum(1<<i for i in new), (-1)**inv
def mat(k,g):
 basis=crit_by_dim[k]
 M=[[0 for _ in basis] for _ in basis]
 for j,s in enumerate(basis):
  z=collections.defaultdict(int)
  for t,n in I[k][s].items():
   tg,sg=sign_and_face(t,g)
   for c,a in proj(tg).items():z[c]+=n*sg*a
  for c,v in z.items():M[ci[k][c]][j]=v
 return M
# cycle structure of permutation of [0,1,2,3]
def ctype(p):
 seen=set();lens=[]
 for i in range(4):
  if i not in seen:
   j=i;k=0
   while j not in seen:seen.add(j);j=p[j];k+=1
   lens.append(k)
 return tuple(sorted(lens,reverse=True))
class_p={ctype(p):p for p in P}
# exact characters on all 48 symmetries, verify signed Lefschetz against original augmented chain complex
from fractions import Fraction
C=[[B[j][i]for j in range(len(B))] for i in range(len(crit_by_dim[4]))]

def mm(A,B):
 return [[sum(A[i][k]*B[k][j]for k in range(len(B)))for j in range(len(B[0]))]for i in range(len(A))]
# Exact chain equations: I4 cycles, I5 boundaries agree with I4 times the Morse matrix.
for k in [4,5]:
 for s,lift in I[k].items():
  bd=collections.defaultdict(int)
  for t,n in lift.items():
   for f,a in boundary(t):bd[f]+=n*a
  bd={f:n for f,n in bd.items()if n}
  if k==4:assert not bd
  else:
   pb=projchain(bd);expected=collections.defaultdict(int)
   for c,n in pb.items():
    for t,v in I[4][c].items():expected[t]+=n*v
   assert bd=={f:n for f,n in expected.items()if n}
for k in [4,5]:
 for s in bydim[k]:
  image_bd=projchain(dict(boundary(s))) if k==5 else {}
  should=collections.defaultdict(int)
  for c,n in proj(s).items():
   if k==5:
    j=ci[5][c]
    for i,t in enumerate(crit_by_dim[4]):should[t]+=n*B[j][i]
  assert image_bd=={t:v for t,v in should.items()if v}
print('CHAIN_MAP_EQUATIONS_PASS')
chars={}; raw={}
for a in P:
 for b in (0,1):
  g=perm_action(a,b)
  assert all(d[i][j]==d[g[i]][g[j]] for i in range(N)for j in range(N))
  M4=mat(4,g);M5=mat(5,g)
  assert mm(M4,C)==mm(C,M5)
  v=[C[i][2]for i in range(6)]
  mv=[sum(M4[i][k]*v[k]for k in range(6))for i in range(6)]
  t=next(i for i in range(6)if v[i]);alpha=mv[t]//v[t];assert all(mv[i]==alpha*v[i]for i in range(6))
  ch4=sum(M4[i][i]for i in range(6))-alpha
  ch5=sum(M5[i][i]for i in range(3))-alpha
  # The first two lifted critical 5-cells are genuine cycles, yielding an independent direct 2x2 action.
  assert M5[2][0]==M5[2][1]==0
  assert ch5==M5[0][0]+M5[1][1]
  lefsum=-1
  for s in faces:
   if s==0:continue
   t,sg=sign_and_face(s,g)
   if t==s:lefsum+=(-1)**(s.bit_count()-1)*sg
  assert lefsum == ch4-ch5, (ctype(a),b,lefsum,ch4,ch5)
  label=(ctype(a),b)
  if label in chars:assert chars[label]==(ch4,ch5)
  else:chars[label]=(ch4,ch5)
print('ALL_48_LEFSCHETZ_CHECKS_PASS')
for key in sorted(chars):print('CHAR',key,chars[key])
# Use fixed character table to verify decomposition H4 = S^(2,1,1) tensor triv C2 + S^(2,2) tensor sign C2;
# H5=(trivial + alternating) tensor triv C2.
tab={
 (1,1,1,1):(3,2,1,1),
 (2,1,1):(-1,0,1,-1),
 (2,2):(-1,2,1,1),
 (3,1):(0,-1,1,1),
 (4,):(1,0,1,-1),
}
for (ct,b),(x,y) in chars.items():
 stdsign,twod,triv,sign=tab[ct]
 assert (x,y)==(stdsign+((-1)**b)*twod,triv+sign)
print('IRREDUCIBLE_DECOMPOSITION_PASS')
# Enumerate all graph automorphisms by exact distance-preserving bijection backtracking.
# Fix the image of vertex 0 and a permutation of the three neighbors, then extend.
# A valid graph automorphism is exactly a distance-preserving bijection.
aut_nodes=0
def count_extensions(mapping,used):
 global aut_nodes
 aut_nodes+=1
 if len(mapping)==N:return 1
 ranked=[]
 for u in range(N):
  if u in mapping:continue
  options=[v for v in range(N) if v not in used and all(d[u][a]==d[v][b] for a,b in mapping.items())]
  if not options:return 0
  ranked.append((len(options),u,options))
 _,u,options=min(ranked)
 result=0
 for v in options:
  mapping[u]=v;used.add(v)
  result+=count_extensions(mapping,used)
  used.remove(v);del mapping[u]
 return result
n_aut=0
for target in range(N):
 for order in itertools.permutations(adj[target]):
  mapping={0:target,**dict(zip(sorted(adj[0]),order))}
  n_aut+=count_extensions(mapping,set(mapping.values()))
assert n_aut==48
print('AUTOMORPHISM_COUNT_48_PASS')
print('ALL_CHECKS_PASS')
