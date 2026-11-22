#!/usr/bin/env python3
"""Independent small-case enumerators for partial triple systems."""
from itertools import combinations

def matchings(n):
  edges=list(combinations(range(n),2)); out=[]
  def rec(avail,emask,free):
    if not avail: out.append((emask,free)); return
    a=avail[0]
    rec(avail[1:],emask,free | (1<<a))
    for b in avail[1:]:
      e=edges.index((a,b)); rec([c for c in avail if c!=a and c!=b],emask|(1<<e),free)
  rec(list(range(n)),0,0)
  return out

def type_counts_from_matchings(n):
  Ms=matchings(n);counts=[0,0,0,0]; raw=0; full=0
  for e1,f1 in Ms:
   for e2,f2 in Ms:
    if e1&e2:continue
    A=f1&f2
    for e3,f3 in Ms:
      if e1&e3 or e2&e3:continue
      B=f1&f3; C=f2&f3; raw+=1; full+=1
      sets=[A,B,C]
      for r in range(4):
       for ids in combinations(range(3),r):
        def rec(j,used):
         if j==len(ids): counts[r]+=1;return
         x=sets[ids[j]] &~used
         while x:
          l=x&-x;rec(j+1,used|l);x-=l
        rec(0,0)
  return len(Ms),raw,tuple(counts),full

def brute(n):
  v=n+3; triples=list(combinations(range(v),3)); pair_mask=[]
  pairs=list(combinations(range(v),2));D={p:i for i,p in enumerate(pairs)}
  for t in triples:pair_mask.append(sum(1<<D[p] for p in combinations(t,2)))
  k=len(triples); no_old=[i for i,t in enumerate(triples) if max(t)>=n]; out=[0,0,0,0,0]
  # base contains no triples
  for mask in range(1<<k):
   if mask & sum(1<<i for i in range(k) if i not in no_old):continue
   used=0;ok=True; selected=[]
   for i in no_old:
    if mask>>i&1:
      if used & pair_mask[i]:ok=False;break
      used|=pair_mask[i]; selected.append(triples[i])
   if not ok:continue
   full=tuple(range(n,n+3)) in selected
   oldnew=sum(sum(p>=n for p in t)==2 for t in selected)
   if full: assert oldnew==0;out[4]+=1
   else:out[oldnew]+=1
  return tuple(out)

if __name__=='__main__':
 for n in range(7):
  I,raw,counts,full=type_counts_from_matchings(n)
  print(n,'involutions',I,'valid_unary_triples',raw,'old_new_layers',counts,'full_triple',full,'total',sum(counts)+full, 'full_prob',round(full/(sum(counts)+full),8))
  if n<=3:
   b=brute(n);assert b==(*counts,full),(n,b,(*counts,full));print('brute',n,b,'OK')
 print('VERIFICATION_OK')
