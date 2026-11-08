import itertools,collections,math
V=list(itertools.permutations(range(4)))
N=len(V);ix={v:i for i,v in enumerate(V)}
S4=list(itertools.permutations(range(4)));S3=list(itertools.permutations(range(3)))
nei=[set() for _ in V]
for i,v in enumerate(V):
 for k in range(3):
  w=list(v);w[k],w[3]=w[3],w[k];nei[i].add(ix[tuple(w)])

# An explicit graph isomorphism with the canonical generalized Petersen
# presentation GP(12,5) removes any dependence on external graph libraries.
GP_MAPPING=[0,1,14,2,19,12,22,15,4,3,5,17,8,20,18,13,6,7,9,10,23,11,16,21]
GP_EDGES=set()
for i in range(12):
 for x,y in ((i,(i+1)%12),(i,i+12),(i+12,12+(i+5)%12)):
  GP_EDGES.add(tuple(sorted((x,y))))
assert {tuple(sorted((GP_MAPPING[x],GP_MAPPING[y]))) for x in range(24) for y in nei[x] if x<y}==GP_EDGES

def parity(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
side=[0 if parity(v)==1 else 1 for v in V];A=[[i for i in range(N) if side[i]==s] for s in (0,1)]
D=[[9]*N for _ in V]
for i in range(N):
 D[i][i]=0;q=[i]
 for x in q:
  for y in nei[x]:
   if D[i][y]>D[i][x]+1:D[i][y]=D[i][x]+1;q.append(y)
assert max(max(row) for row in D)==4
S=[]
for s in (0,1):
 vs=A[s];tri=list(itertools.combinations(vs,3));tri=[t for t in tri if all(D[a][b]==2 for a,b in itertools.combinations(t,2))]
 es=list(itertools.combinations(vs,2));es=[e for e in es if D[e[0]][e[1]]==2]
 ef=collections.defaultdict(list)
 for t in tri:
  for j in range(3):ef[t[:j]+t[j+1:]].append((t,(-1)**j))
 assert len(vs)==12 and len(es)==36 and len(tri)==24
 assert len(ef)==36 and all(len(x)==2 for x in ef.values())
 ori={tri[0]:1};q=[tri[0]]
 links={i:(set(),set()) for i in vs}
 for t in tri:
  for z in t:
   edge=tuple(w for w in t if w!=z);links[z][1].add(edge)
   links[z][0].update(edge)
 assert all(len(ls[0])==6 and len(ls[1])==6 for ls in links.values())
 for i in vs:
  # link 6-cycle via connectedness
  le=links[i][1];vv=links[i][0]
  assert all(sum(i2 in e for e in le)==2 for i2 in vv)
  seen={min(vv)}
  queue=[min(vv)]
  while queue:
   x=queue.pop()
   for edge in le:
    if x not in edge:continue
    y=edge[0] if edge[1]==x else edge[1]
    if y not in seen:seen.add(y);queue.append(y)
  assert seen==vv
 while q:
  t=q.pop()
  for j in range(3):
   e=t[:j]+t[j+1:]
   (u,sgn_u),(v,sgn_v)=ef[e]
   oth,sgn_oth=(v,sgn_v) if u==t else (u,sgn_u)
   need=-ori[t]*((-1)**j)*sgn_oth
   if oth in ori: assert ori[oth]==need
   else:ori[oth]=need;q.append(oth)
 assert len(ori)==24
 S.append({'v':vs,'edges':es,'tri':tri,'orient':ori})
def permutation_sign(indices):
 return (-1)**sum(indices[i]>indices[j] for i in range(len(indices)) for j in range(i+1,len(indices)))
def gmap(a,b):
 inv=[b.index(i) for i in range(3)]
 return tuple(ix[tuple([a[v[inv[i]]] for i in range(3)]+[a[v[3]]])] for v in V)
def face_sign(t,pm):
 mapped=[pm[x] for x in t]
 return permutation_sign(mapped)
def iso_delta(si,ti,pm):
 gen=S[si]['orient'];tar=S[ti]['orient']; src=next(iter(gen))
 image=tuple(sorted(pm[x] for x in src))
 return gen[src]*face_sign(src,pm)*tar[image]
def tr1(si,pm):
 assert all(side[pm[x]]==si for x in S[si]['v'])
 T=S[si]
 fix0=sum(pm[x]==x for x in T['v'])
 fix1=sum(face_sign(e,pm) for e in T['edges'] if tuple(sorted(pm[x] for x in e))==e)
 fix2=sum(face_sign(t,pm) for t in T['tri'] if tuple(sorted(pm[x] for x in t))==t)
 delta=iso_delta(si,si,pm)
 return 1+delta-(fix0-fix1+fix2), delta

def cycle_type(p):
 seen=set();ans=[]
 for i in range(len(p)):
  if i in seen:continue
  cur=i;size=0
  while cur not in seen:seen.add(cur);cur=p[cur];size+=1
  ans.append(size)
 return tuple(sorted(ans,reverse=True))
P4=[(1,1,1,1),(2,1,1),(2,2),(3,1),(4,)]; P3=[(1,1,1),(2,1),(3,)]
c4={x:next(p for p in S4 if cycle_type(p)==x) for x in P4};c3={x:next(p for p in S3 if cycle_type(p)==x) for x in P3}
ch={}; reps={}
for u in P4:
 for v in P3:
  a,b=c4[u],c3[v];pm=gmap(a,b)
  assert all({pm[y] for y in nei[x]}==nei[pm[x]] for x in range(24))
  preserve=side[pm[0]]==side[0]
  if preserve:
   trA,da=tr1(0,pm);trB,db=tr1(1,pm)
   ans=(trA*trB,trA*db+da*trB,da*db)
  else:
   pm2=tuple(pm[pm[x]] for x in range(24))
   tr,delta=tr1(0,pm2)
   ans=(tr,0,-delta)
  ch[u,v]=ans;reps[u,v]=pm
  print(u,v,'pres',preserve,'tr(H3,H4,H5)',ans)
C4={'4':[1,1,1,1,1],'31':[3,1,-1,0,-1],'22':[2,0,2,-1,0],'211':[3,-1,-1,0,1],'1111':[1,-1,1,1,-1]}
C3={'3':[1,1,1],'21':[2,0,-1],'111':[1,-1,1]}
Z4=[1,6,3,8,6];Z3=[1,3,2]
for d in range(3):
 print('DECOMPOSE',d+3)
 for name4,char4 in C4.items():
  for name3,char3 in C3.items():
   num=sum(Z4[i]*Z3[j]*ch[u,v][d]*char4[i]*char3[j] for i,u in enumerate(P4) for j,v in enumerate(P3))
   assert num%144==0
   if num:print(name4,name3,num//144)
 print('invariant dim',sum(Z4[i]*Z3[j]*ch[u,v][d] for i,u in enumerate(P4) for j,v in enumerate(P3))//144)

# Independent whole-complex Lefschetz check.  Each side factor has all
# 1+12+36+24=73 (including empty) faces, so their join has 73^2-1 faces.
SIDEF=[]
for C in S:
 SIDEF.append([tuple()]+[(x,) for x in C['v']]+C['edges']+C['tri'])
fullfaces=[tuple(sorted(x+y)) for x in SIDEF[0] for y in SIDEF[1] if x or y]
assert len(fullfaces)==5328 and len(set(fullfaces))==5328
assert collections.Counter(len(f)-1 for f in fullfaces)=={0:24,1:216,2:912,3:1872,4:1728,5:576}
expected={3:{('4','3'):1,('4','111'):1,('22','3'):1},4:{('22','3'):1,('22','111'):1},5:{('1111','111'):1}}
for dim in (3,4,5):
 actual={}
 for n4,z4 in C4.items():
  for n3,z3 in C3.items():
   t=sum(Z4[i]*Z3[j]*ch[u,v][dim-3]*z4[i]*z3[j] for i,u in enumerate(P4) for j,v in enumerate(P3))
   assert t%144==0 and t>=0
   if t:actual[n4,n3]=t//144
 assert actual==expected[dim], (dim,actual)

def rational_character(dim,a,b):
 iu=P4.index(cycle_type(a));iv=P3.index(cycle_type(b))
 return sum(m*C4[name4][iu]*C3[name3][iv] for (name4,name3),m in expected[dim].items())

# All 144 group maps are distinct, and they saturate the 24*3! upper
# bound because initial root and its three neighbors determine all vertices
# under iterated neighborhood-color refinement.
for root in range(24):
 colors=[0]*24; colors[root]=1
 for j,x in enumerate(sorted(nei[root])):colors[x]=j+2
 for _ in range(6):
  keys=[(colors[x],tuple(sorted(colors[y] for y in nei[x]))) for x in range(24)]
  cod={k:j for j,k in enumerate(sorted(set(keys)))}
  colors=[cod[k] for k in keys]
 assert len(set(colors))==24
maps=set()
for a in S4:
 for b in S3:
  pm=gmap(a,b); maps.add(pm)
  assert all({pm[y] for y in nei[x]}==nei[pm[x]] for x in range(24))
  swaps=side[pm[0]]!=side[0]
  if not swaps:
   tA,dA=tr1(0,pm);tB,dB=tr1(1,pm)
   predicted=(tA*tB,tA*dB+dA*tB,dA*dB)
  else:
   p2=tuple(pm[pm[x]] for x in range(24))
   t,d=tr1(0,p2);predicted=(t,0,-d)
  expected_chr=tuple(rational_character(d,a,b) for d in (3,4,5))
  assert predicted==expected_chr,(a,b,predicted,expected_chr)
  lef=sum((-1)**(len(f)-1)*face_sign(f,pm) for f in fullfaces if tuple(sorted(pm[x] for x in f))==f)
  assert lef==1-predicted[0]+predicted[1]-predicted[2],(a,b,lef,predicted)
assert len(maps)==144
print('NAURU_COMPLETE_S4_S3_RIPS3_CHARACTER_PASS 144_AUTOMORPHISMS 5328_FACES 15_CLASSES')
