from itertools import product,combinations
from collections import defaultdict,Counter
from math import prod
# GF2 vectors 1..7, bits in 3-bit
P=tuple(range(1,8)); triangle_lines={frozenset((a,b,a^b)) for a in P for b in P if a!=b}
assert len(triangle_lines)==7
faces=[frozenset((v,)) for v in P]+[frozenset(e) for e in combinations(P,2)]+[frozenset(t) for t in combinations(P,3) if frozenset(t) not in triangle_lines]
assert len(faces)==56
bydim=[list(filter(lambda a:len(a)==k,faces)) for k in range(1,4)]
flags=[[] for i in range(3)]
for f in faces:flags[0].append((f,))
for e in faces:
 for f in faces:
  if e<f:flags[1].append((e,f))
for v in bydim[0]:
 for e in bydim[1]:
  if v<e:
   for t in bydim[2]:
    if e<t:flags[2].append((v,e,t))
print('face and flag',list(map(len,bydim)),list(map(len,flags)))
identity=tuple(P)
def comp(a,b):return tuple(a[i-1] for i in b)
mat=[]
for a,b,c in product(P,repeat=3):
 if a==b or a==c or b==c or c==a^b:continue
 mat.append(tuple((a if v&1 else 0)^(b if v&2 else 0)^(c if v&4 else 0) for v in P))
G=sorted(set(mat));assert len(G)==168
ix={g:i for i,g in enumerate(G)};idn=ix[identity];mul=[[ix[comp(x,y)] for y in G] for x in G];inv=[next(y for y in range(168) if mul[x][y]==idn and mul[y][x]==idn) for x in range(168)]
orders=[]
for g in range(168):
 x=idn;n=0
 while True:
  x=mul[x][g];n+=1
  if x==idn:break
 orders.append(n)
print('order distribution',Counter(orders))
# All subgroups in this small group are two-generated. Generate by BFS with four generators and verify closure.
subgs=set(); gensof={}
for a in range(168):
 for b in range(a,168):
  gens=(a,b,inv[a],inv[b]); h={idn};front=[idn]
  while front:
   x=front.pop()
   for g in gens:
    y=mul[x][g]
    if y not in h:h.add(y);front.append(y)
  q=frozenset(h);subgs.add(q);gensof.setdefault(q,(a,b))
print('subgroup counts',len(subgs),Counter(map(len,subgs)),flush=True)
# Closure under adjoining ANY single generator establishes that all subgroups appear.
for h,(a,b) in gensof.items():
 for g in range(168):
  if g in h: continue
  genes=(a,b,g,inv[a],inv[b],inv[g]);t={idn}; frontier=[idn]
  while frontier:
   x=frontier.pop()
   for y in genes:
    z=mul[x][y]
    if z not in t:t.add(z);frontier.append(z)
  if frozenset(t) not in subgs:
   raise AssertionError('not closed under adding one generator')
print('ALL_SUBGROUPS_CERTIFIED',flush=True)
def orbitn(items,h):
 unseen=set(items);ans=0
 while unseen:
  x=next(iter(unseen));ans+=1
  orb={tuple(frozenset(G[g][v-1] for v in f) for f in x) for g in h};unseen-=orb
 return ans
T={k:[] for k in set(map(len,subgs))};profiles=defaultdict(list)
for h in subgs:
 fn=[orbitn(flags[k],h) for k in range(3)];bet=fn[2]-fn[1]+fn[0]-1
 calc=14-2*sum(orders[g]==2 for g in h)+2*sum(orders[g]==3 for g in h)+2*sum(orders[g]==4 for g in h)
 assert calc%len(h)==0 and bet==calc//len(h)-1
 oc=tuple(sorted(Counter(orders[g] for g in h).items())); profiles[(len(h),oc,bet,tuple(fn))].append(h)
for (size,oc,b,fn),hs in sorted(profiles.items()):
 print('size',size,'element-orders',oc,'beta',b,'flag_orbits',fn,'multiplicity',len(hs))
print('profile count',len(profiles))
# Singer 7-cycle: label points 0..6 by orbit (seed 1); finite geometry derived triangular boundary words
singer=next(g for g in range(168) if orders[g]==7)
idxpoints=[];v=1
for k in range(7):idxpoints.append(v);v=G[singer][v-1]
coords={p:i for i,p in enumerate(idxpoints)}
print('singer orbit',idxpoints)
triangles=[frozenset(coords[v] for v in t) for t in bydim[2]]
def orbit(t):return min(tuple(sorted((v+s)%7 for v in t)) for s in range(7))
rr=sorted({orbit(t) for t in triangles});print('triangle orbit reps',rr)
def word(t):
 a,b,c=sorted(t);w=[]
 for x,y in [(a,b),(b,c),(c,a)]:
  d=(y-x)%7
  if d in (1,2,3):w.append('abc'[d-1])
  else:w.append('ABC'[7-d-1])
 return ''.join(w)
print('relators',[(r,word(r)) for r in rr]);

assert [sum({'a':1,'b':2,'c':3,'A':-1,'B':-2,'C':-3}[v] for v in word(t)) for t in rr]==[0,7,0,7]
print('VERIFY_OK')
