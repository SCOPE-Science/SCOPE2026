from collections import defaultdict,Counter
from itertools import permutations
from functools import lru_cache
n=3
V=tuple(range(6))
Lrot=(1,2,0,3,4,5);Ltrans=(1,0,2,3,4,5)
Rrot=(0,1,2,4,5,3);Rtrans=(0,1,2,4,3,5)
swap=(3,4,5,0,1,2)

def mul(p,q):return tuple(p[q[i]] for i in V)
gens=[Lrot,Ltrans,Rrot,Rtrans,swap]
G=[V];S={V}
for p in G:
 for q in gens:
  r=mul(p,q)
  if r not in S:G.append(r);S.add(r)
assert len(G)==72
idx={g:i for i,g in enumerate(G)}
tab=[[idx[mul(p,q)] for q in G] for p in G]
ident=idx[V]
@lru_cache(None)
def closure(Q):
 S=set(Q); L=list(Q)
 while L:
  a=L.pop()
  for b in list(S):
   for c in (tab[a][b],tab[b][a]):
    if c not in S:S.add(c);L.append(c)
 return frozenset(S)
subs={frozenset({ident})}; queue=[frozenset({ident})]
for H in queue:
 for j in range(72):
  if j in H:continue
  K=closure(tuple(sorted(H|{j})))
  if K not in subs:subs.add(K);queue.append(K)
print('subgroups',len(subs))
print('orders',Counter(map(len,subs)))

E=[(a,b) for a in range(3) for b in range(3,6)]
C0=[tuple(p) for p in __import__('itertools').combinations(V,2)]
C1=[(e,v) for e in E for v in V if v not in e]
C2=[(e,f) for e,f in __import__('itertools').combinations(E,2) if not set(e)&set(f)]
C=[C0,C1,C2]
inc01=[];inc12=[];inc02=[]
for a in C0:
 for b in C1:
  if a==tuple(sorted((b[0][0],b[1]))) or a==tuple(sorted((b[0][1],b[1]))):inc01.append((a,b))
 for z in C2:
  if len(set(a)&set(z[0]))==1 and len(set(a)&set(z[1]))==1:inc02.append((a,z))
for b in C1:
 for z in C2:
  if b[0] in z and b[1] in (z[0] if b[0]==z[1] else z[1]):inc12.append((b,z))
inc12_by_b=defaultdict(list)
for b,z in inc12:inc12_by_b[b].append(z)
T=[(a,b,z) for a,b in inc01 for z in inc12_by_b[b]]
assert(len(T),len(inc01)+len(inc12)+len(inc02))==(144,216)
# globally index all barycentric faces
vertices=[((d,c),) for d,L in enumerate(C) for c in L]
edges=[((0,a),(1,b)) for a,b in inc01]+[((1,b),(2,z)) for b,z in inc12]+[((0,a),(2,z)) for a,z in inc02]
tris=[((0,a),(1,b),(2,z)) for a,b,z in T]
faces=[vertices,edges,tris]
fidx=[{f:i for i,f in enumerate(F)} for F in faces]

def apply_c(d,c,p):
 if d==0:return tuple(sorted(p[v] for v in c))
 if d==1:return (tuple(sorted((p[c[0][0]],p[c[0][1]]))),p[c[1]])
 if d==2:return tuple(sorted((tuple(sorted((p[a],p[b]))) for a,b in c)))
Fperms=[]
for dim,F in enumerate(faces):
 Fperms.append([[fidx[dim][tuple((d,apply_c(d,c,p)) for d,c in f)] for f in F] for p in G])
# vertex edge indices for every simplex, oriented barycentric edges by rank
E_end=[(fidx[0][(a,)],fidx[0][(b,)]) for a,b in edges]
T_ed=[]
for t in tris:
 T_ed.append((fidx[1][(t[1],t[2])],fidx[1][(t[0],t[2])],fidx[1][(t[0],t[1])]))
# compute quotient orbit representative maps

def quotient(H,full=False):
 maps=[];reps=[]
 for k,F in enumerate(faces):
  orbit=[-1]*len(F); rep=[]
  for i in range(len(F)):
   if orbit[i]>=0:continue
   j=len(rep);rep.append(i)
   for p in H:
    q=Fperms[k][p][i]
    assert orbit[q] in (-1,j)
    orbit[q]=j
  maps.append(orbit);reps.append(rep)
 tedges=[tuple(maps[1][j] for j in T_ed[t]) for t in reps[2]]
 ends=[tuple(maps[0][j] for j in E_end[e]) for e in reps[1]]
 edge_inc=defaultdict(list)
 for i,ted in enumerate(tedges):
  for sign,e in ((1,ted[0]),(-1,ted[1]),(1,ted[2])):
   edge_inc[e].append((i,sign))
 assert len(edge_inc)==len(reps[1])
 assert all(len(v) in (1,2) for v in edge_inc.values())
 bdry={e for e,ts in edge_inc.items() if len(ts)==1}
 # Verify every quotient vertex has a circle or interval as link.
 for v in range(len(reps[0])):
  lk=defaultdict(list)
  for t,e3 in enumerate(tedges):
   around=[e for e in e3 if v in ends[e]]
   if len(around)==2:
    a,b=around;lk[a].append(b);lk[b].append(a)
   elif len(around)!=0:
    raise AssertionError(('invalid link triangle',len(H),v,t,around))
  if not lk:raise AssertionError(('isolated quotient vertex',len(H),v))
  degree=[len(x) for x in lk.values()]
  assert all(k in (1,2) for k in degree),('link valence',len(H),v,degree)
  assert degree.count(1) in (0,2),('link endpoints',len(H),v,degree)
  unseen_lk=set(lk);stack=[unseen_lk.pop()]
  while stack:
   a=stack.pop()
   for b in lk[a]:
    if b in unseen_lk:unseen_lk.remove(b);stack.append(b)
  assert not unseen_lk,('link disconnected',len(H),v)

 # boundary connected components
 graph=defaultdict(set)
 for e in bdry:
  a,b=ends[e];graph[a].add(b);graph[b].add(a)
 comps=0;unseen=set(graph)
 while unseen:
  comps+=1;stack=[unseen.pop()]
  while stack:
   a=stack.pop()
   for b in graph[a]:
    if b in unseen:unseen.remove(b);stack.append(b)
 # orientation via parity adjacency
 oriented={}; orientable=True
 for t in range(len(tedges)):
  if t in oriented:continue
  oriented[t]=1;stack=[t]
  while stack:
   i=stack.pop()
   for e in tedges[i]:
    inc=edge_inc[e]
    if len(inc)!=2:continue
    (u,su),(v,sv)=inc
    if i==u:other=v;wanted=-oriented[i]*su*sv
    else:other=u;wanted=-oriented[i]*su*sv
    if other in oriented:
     if oriented[other]!=wanted:orientable=False
    else:oriented[other]=wanted;stack.append(other)
 chi=len(reps[0])-len(reps[1])+len(reps[2]);b=comps
 # if orientable: chi=2-2g-b; else chi=2-g-b
 val=2-chi-b
 if val<0 or (orientable and val%2):print('SURFACE PROBLEM',len(H),chi,b,orientable,val)
 genus=val//2 if orientable else val
 key=('orientable' if orientable else 'nonorientable',genus,b)
 if full:return key,(len(reps[0]),len(reps[1]),len(reps[2])),len(bdry),maps,reps,tedges,edge_inc,ends
 return key

sigs=defaultdict(list)
for H in subs:
 assert ident in H and all(tab[a][b] in H for a in H for b in H)
 # Burnside's fixed-face formula supplies an independent Euler-characteristic check.
 burnside_sum = 0
 for g in H:
  burnside_sum += sum((-1)**k * sum(Fperms[k][g][i]==i for i in range(len(faces[k]))) for k in range(3))
 assert burnside_sum % len(H) == 0
 cert = quotient(H,True)
 qchi = cert[1][0] - cert[1][1] + cert[1][2]
 assert burnside_sum // len(H) == qchi
 sigs[cert[0]].append(H)
print('signatures',Counter({str(k):len(v) for k,v in sigs.items()}))
# conjugacy classes of subgroups
inv=[next(j for j in range(72) if tab[i][j]==ident and tab[j][i]==ident) for i in range(72)]
unseen=set(subs);classes=[]
while unseen:
 H=next(iter(unseen));cl=frozenset(frozenset(tab[tab[g][h]][inv[g]] for h in H) for g in range(72));assert cl <= subs
 unseen-=cl;classes.append(cl)
print('conjugacy classes',len(classes))
for key,hs in sorted(sigs.items(),key=lambda kv:(kv[0][2],kv[0][0],kv[0][1])):
 print(key,'subgroups',len(hs),'conj classes',sum(any(H in cl for H in hs) for cl in classes),'orders',sorted(Counter(map(len,hs)).items()))
# identify natural actions
for name,g in [('diagonal rotation',mul(Lrot,Rrot)),('left rotation',Lrot),('left transposition',Ltrans),('diagonal reflection',mul(Ltrans,Rtrans)),('bipartition swap',swap)]:
 H=closure((ident,idx[g]));print(name, 'H=',len(H),quotient(H,True)[0:3])
print('full',quotient(frozenset(range(72)),True)[0:3])
expected = {
    ('nonorientable',5,0): 1,
    ('nonorientable',3,0): 2,
    ('nonorientable',1,0): 3,
    ('nonorientable',2,1): 9,
    ('nonorientable',1,1): 36,
    ('orientable',1,1): 6,
    ('orientable',0,1): 55,
}
assert {k:len(v) for k,v in sigs.items()} == expected
assert len(subs)==112 and len(classes)==26
assert sorted([len(cl) for cl in classes])
assert sum(map(len,classes))==112
assert quotient(frozenset(range(72)))[0]=='orientable'
print('K33_TWO_CONFIGURATION_ALL_SUBGROUP_SURFACES_PASS')
