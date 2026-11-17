#!/usr/bin/env python3
"""Exact homology and full symmetry character of the ternary Hamming three-cube Rips complex."""
import itertools, collections, json
N=3
V=list(itertools.product(range(3),repeat=N))
pos={v:i for i,v in enumerate(V)}
mask=(1<<len(V))-1
adj=[sum(1<<j for j,w in enumerate(V) if i!=j and sum(a!=b for a,b in zip(v,w))<=2) for i,v in enumerate(V)]
F=[[] for _ in range(10)]
def enum(pref, can):
 if pref: F[len(pref)-1].append(sum(1<<v for v in pref))
 while can:
  t=can&-can; u=t.bit_length()-1; can-=t; enum(pref+[u],can & adj[u])
enum([],mask)
F=[x for x in F if x]
assert [len(f) for f in F]==[27,243,945,1728,1620,945,351,81,9]
assert len(set().union(*[set(f) for f in F]))==sum(len(f) for f in F)

def boundary_ranks():
 ret=[]
 for d in range(1,len(F)):
  ids={v:j for j,v in enumerate(F[d-1])}; piv={}
  for s in F[d]:
   b=s; col=0
   while b:
    v=b&-b; b-=v; col^=1<<ids[s-v]
   while col:
    lead=col.bit_length()-1
    if lead in piv:col^=piv[lead]
    else: piv[lead]=col;break
  ret.append(len(piv))
 return ret
# Exhaustively verify every successive simplicial boundary composition.
for d in range(2,len(F)):
 ids={face:j for j,face in enumerate(F[d-2])}
 for sigma in F[d]:
  remaining=sigma; composite=0
  while remaining:
   v=remaining&-remaining;remaining-=v
   facet=sigma-v
   rest=facet
   while rest:
    u=rest&-rest;rest-=u
    composite ^= 1<<ids[facet-u]
  assert composite==0
print('boundary_square_zero',sum(len(F[d]) for d in range(2,len(F))))
ranks=boundary_ranks()
betti=[len(F[0])-ranks[0]]+[len(F[i])-ranks[i-1]-(ranks[i] if i<len(ranks) else 0) for i in range(1,len(F))]
assert betti == [1,0,0,46,0,0,0,0,0], (ranks,betti)
print('face_counts',*[len(x) for x in F])
print('mod2_boundary_ranks',*ranks)
print('mod2_betti',*betti)
# independent Euler number
assert sum((-1)**d*len(F[d]) for d in range(len(F)))==1-46
# all coordinate-permutations and independent alphabet permutations
perms=list(itertools.permutations(range(3)))
G=[]
for cp in perms:
 for ss in itertools.product(perms,repeat=3):
  g=tuple(pos[tuple(ss[i][V[j][cp[i]]] for i in range(3))] for j in range(27))
  G.append(g)
assert len(set(G))==1296
ix={g:i for i,g in enumerate(G)}
e=tuple(range(27)); assert e in ix
# conjugacy via closure under conjugations by standard eight generators
s01=(1,0,2);cycle=(1,2,0);identity=(0,1,2)
gens=[]
for c in range(3):
 for q in (s01,cycle):
  ss=[identity]*3;ss[c]=q
  gens.append(tuple(pos[tuple(ss[i][V[j][i]] for i in range(3))] for j in range(27)))
for cp in (s01,(0,2,1)):
 gens.append(tuple(pos[tuple(V[j][cp[i]] for i in range(3))] for j in range(27)))
# compose f then g: g o f
def compose(g,f): return tuple(g[f[i]] for i in range(27))
def inverse(g):
 h=[0]*27
 for i,v in enumerate(g):h[v]=i
 return tuple(h)
assert len(gens)==8
for x in gens: assert x in ix
cls=[]; seen=set()
for j,g in enumerate(G):
 if j in seen: continue
 orbit={g}; todo=[g]
 while todo:
  h=todo.pop()
  for t in gens:
   ct=compose(compose(t,h),inverse(t))
   if ct not in orbit:orbit.add(ct);todo.append(ct)
 ids={ix[h] for h in orbit}
 assert not (ids&seen)
 seen.update(ids);cls.append((min(ids),len(ids),sorted(ids)))
assert len(seen)==1296
cls.sort(key=lambda z:(-z[1],z[0]))

# signed Lefschetz alternating fixed face trace per class rep
fsets=[set(x) for x in F]
def signed_trace(g):
 tr=[0]*len(F)
 gm=[1<<g[i] for i in range(27)]
 for d,dim in enumerate(F):
  for face in dim:
   x=face;im=0; seq=[]
   while x:
    v=x&-x;idx=v.bit_length()-1;x-=v
    u=g[idx];im |= gm[idx];seq.append(u)
   if im==face:
    inversions=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    tr[d] += -1 if inversions%2 else 1
 return tr

def perm_signature(g):
 visited=set();cnt=collections.Counter()
 for i in range(27):
  if i not in visited:
   j=i;l=0
   while j not in visited:visited.add(j);j=g[j];l+=1
   cnt[l]+=1
 return ','.join(f'{k}^{cnt[k]}' for k in sorted(cnt))

def order(g):
 x=e
 for k in range(1,40):
  x=compose(g,x)
  if x==e:return k
 raise AssertionError
print('conjugacy_classes',len(cls))
class_data=[]
for k,(rep,size,ids) in enumerate(cls):
 g=G[rep]; traces=signed_trace(g); L=sum((-1)**j*v for j,v in enumerate(traces));chi=1-L
 class_data.append(dict(class_index=k, representative_index=rep, size=size, order=order(g), vertex_cycles=perm_signature(g), character=chi, representative=[list(V[g[i]]) for i in range(27)], fixed_simplicial_traces=traces))
 print('class',k,'size',size,'order',order(g),'cycles',perm_signature(g),'H3_trace',chi)
assert sum(x['size']*x['character'] for x in class_data)%1296==0
print('invariant_dim',sum(x['size']*x['character'] for x in class_data)//1296)
assert sum(x['size'] for x in class_data)==1296
assert class_data[ next(k for k,c in enumerate(class_data) if c['order']==1) ]['character']==46
# orthogonality of character with itself equals multiplicity-weighted square sum
print('self_inner_product',sum(x['size']*x['character']**2 for x in class_data)//1296)
# Value on full vertex translation subgroup C3^3 and coordinate S3
# translations implement each shift by 1 along coordinate
traces_translation=[]
for delta in itertools.product(range(3),repeat=3):
 g=tuple(pos[tuple((V[j][k]+delta[k])%3 for k in range(3))] for j in range(27))
 traces_translation.append(1-sum((-1)**j*v for j,v in enumerate(signed_trace(g))))
print('translation_characters',collections.Counter(traces_translation))
print('translation_invariant_dim',sum(traces_translation)//27)
open(str(__import__('pathlib').Path(__file__).resolve().parent/'character_data.json'),'w').write(json.dumps({'face_counts':[len(x) for x in F], 'mod2_boundary_ranks':ranks,'mod2_betti':betti,'class_data':class_data},indent=2)+'\n')
print('TERNARY_RIPS_FULL_CHARACTER_PASS')
