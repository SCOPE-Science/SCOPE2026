#!/usr/bin/env python3
"""Finite exhaustive checker for strong-Morse complexes of two-petal cycle bouquets.
Only graph combinatorics, standard simplicial boundaries, and Morse pairs are used.
"""
from itertools import permutations,combinations
from collections import Counter,defaultdict
from functools import lru_cache

CERT_ORDERS = {
 3:[7,11,0,8,5,6,3,10,4,1,9,2],
 4:[13,10,0,12,6,5,3,8,7,11,4,1,9,2],
 5:[1,7,14,11,12,3,9,0,6,2,5,13,8,10,4,15],
 6:[14,12,7,17,6,0,8,3,9,4,10,11,15,13,5,16,2,1],
}

def graph(n):
 assert 3 <= n <= 6
 return tuple(sorted(tuple(sorted(e)) for e in ([(0,1),(1,2),(2,0),(0,3)]
       + [(j,j+1) for j in range(3,n+1)] + [(n+1,0)])))

def enumerate_by_permutations(n):
 E=graph(n); V=tuple(range(n+2)); neighbors={v:set() for v in V}
 for u,v in E:neighbors[u].add(v);neighbors[v].add(u)
 orient=tuple(sorted((v,u) for v in V for u in neighbors[v]))
 oi={e:i for i,e in enumerate(orient)}
 maximal_candidates=set()
 for ordering in permutations(V):
  past=set(); active=[]
  for v in ordering:
   nbr=neighbors[v]&past
   if len(nbr)==1:active.append(oi[(v,next(iter(nbr)))])
   past.add(v)
  maximal_candidates.add(frozenset(active))
 facets={s for s in maximal_candidates if not any(s<t for t in maximal_candidates)}
 return E,orient,facets

def enumerate_by_subset_extensions(n,orient):
 # Second generation: recursion over the order prefix, tracking available lower neighbors.
 neighbors={v:set() for v in range(n+2)}
 for a,b in graph(n):neighbors[a].add(b);neighbors[b].add(a)
 idx={x:i for i,x in enumerate(orient)}
 allsets=set()
 def visit(prefix,used,active):
  if len(prefix)==n+2:
   allsets.add(frozenset(active));return
  for v in range(n+2):
   if v in used:continue
   earlier=[u for u in prefix if u in neighbors[v]]
   if len(earlier)==1:visit(prefix+(v,),used|{v},active+(idx[(v,earlier[0])],))
   else:visit(prefix+(v,),used|{v},active)
 visit((),set(),())
 return {s for s in allsets if not any(s<t for t in allsets)}

def faces_from_facets(facets):
 F={()}
 for s in facets:
  s=sorted(s)
  for k in range(1,len(s)+1):
   F.update(combinations(s,k))
 return F

def lexmatch(F,order):
 rest=F-{()}; pairs=[]
 for v in order:
  for f in sorted(rest,key=lambda x:(len(x),x)):
   if v in f:continue
   up=tuple(sorted(f+(v,)))
   if up in rest:
    rest.remove(f);rest.remove(up);pairs.append((f,up))
 return rest,pairs

def check_full_acyclic(F,pairs):
 # Original Hasse arrows downward except reversed matching arrows.
 pd={up:lo for lo,up in pairs}
 indeg={f:0 for f in F if f}; out=defaultdict(list)
 for up in F:
  if len(up)<2:continue
  for i in range(len(up)):
   lo=up[:i]+up[i+1:]
   if up in pd and pd[up]==lo:a,b=lo,up
   else:a,b=up,lo
   out[a].append(b);indeg[b]+=1
 stack=[a for a in indeg if indeg[a]==0]; done=0
 while stack:
  a=stack.pop();done+=1
  for b in out[a]:
   indeg[b]-=1
   if indeg[b]==0:stack.append(b)
 return done==len(F)-1

def morse_boundary(F,pairs,crit):
 # Reduction of signed integer boundary along acyclic pairs.
 paired_up={lo:up for lo,up in pairs}; paired_down={up:lo for lo,up in pairs}
 critical=set(crit)
 def bd(f):
  return [(f[:i]+f[i+1:],(-1)**i) for i in range(len(f))]
 @lru_cache(None)
 def projection(f):
  if f in critical:return {f:1}
  if f in paired_down:return {}
  if f not in paired_up:raise AssertionError(('not accounted for',f))
  up=paired_up[f]; coeff=next(c for q,c in bd(up) if q==f)
  out=defaultdict(int)
  for g,c in bd(up):
   if g==f:continue
   for h,z in projection(g).items():out[h]-=coeff*c*z
  return {h:z for h,z in out.items() if z}
 result={}
 for upper in crit:
  if len(upper)<=1:continue
  out=defaultdict(int)
  for f,c in bd(upper):
   for h,z in projection(f).items():out[h]+=c*z
  result[upper]={h:z for h,z in out.items() if z}
 return result

def mod2_betti(F):
 by_dim={k:sorted(x for x in F if len(x)==k+1)
         for k in range(0,max(map(len,F)))}
 def rank(columns):
  pivot={}
  for col in columns:
   while col:
    high=col.bit_length()-1
    if high in pivot:col^=pivot[high]
    else:pivot[high]=col;break
  return len(pivot)
 ranks={}
 for k in range(1,max(by_dim)+1):
  ix={face:i for i,face in enumerate(by_dim[k-1])}
  columns=[]
  for face in by_dim[k]:
   col=0
   for j in range(len(face)):
    col^=1<<ix[face[:j]+face[j+1:]]
   columns.append(col)
  ranks[k]=rank(columns)
 return {k:len(v)-ranks.get(k,0)-ranks.get(k+1,0)
         for k,v in by_dim.items()}

def check(n):
 E,O,A=enumerate_by_permutations(n)
 B=enumerate_by_subset_extensions(n,O)
 assert A==B
 F=faces_from_facets(A)
 order=CERT_ORDERS[n]
 assert sorted(order)==list(range(len(O)))
 C,pairs=lexmatch(F,order)
 assert check_full_acyclic(F,pairs)
 assert len(F)==2*len(pairs)+len(C)+1
 d=morse_boundary(F,pairs,C)
 assert all(not x for x in d.values()),(n,d)
 cc=Counter(len(f)-1 for f in C)
 b=mod2_betti(F)
 for k,rank in b.items():
  assert rank==cc[k],(n,k,rank,cc[k])
 print('n',n,'V',n+2,'E',len(E),'oriented',len(O),'facets',len(A),'faces',len(F)-1,
       'pairs',len(pairs),'critical',dict(sorted(cc.items())),'zero_integer_Morse_boundary',True,'mod2_betti',dict(sorted(b.items())))
 return cc

if __name__=='__main__':
 for n in range(3,7):check(n)
 print('STRONG_MIXED_CYCLE_BOUQUET_PASS')
