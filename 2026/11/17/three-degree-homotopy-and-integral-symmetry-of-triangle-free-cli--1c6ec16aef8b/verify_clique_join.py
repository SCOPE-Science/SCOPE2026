#!/usr/bin/env python3
"""Standalone checks of triangle-free clique-complex wedge and character formulas."""
import itertools, math
from collections import defaultdict

def permutations(values):
 return list(itertools.permutations(values))

def graph(s, qs):
 blocks=[]; base=s
 for q in qs:
  blocks.append(list(range(base,base+q)));base+=q
 verts=list(range(base)); E=set()
 for i,j in itertools.combinations(range(s),2):E.add((i,j))
 for i in range(s):
  for j in range(s,base):E.add((i,j))
 for block in blocks:
  for i,j in itertools.combinations(block,2):E.add((i,j))
 tri=set(x for x in itertools.combinations(verts,3) if all(tuple(sorted(y)) in E for y in itertools.combinations(x,2)))
 return blocks,tri,base

def faces(s,qs):
 blocks,T,v=graph(s,qs); allf=defaultdict(list)
 for mask in range(1<<v):
  f=tuple(i for i in range(v) if mask>>i&1)
  if any(set(t).issubset(f) for t in T):continue
  allf[len(f)-1].append(f)
 return blocks,allf,v

def rank2(columns):
 pivot={};r=0
 for col in columns:
  while col:
   b=col.bit_length()-1
   if b in pivot:col ^= pivot[b]
   else:pivot[b]=col;r+=1;break
 return r

def bettis(f):
 ranks={}
 for d in sorted(f):
  if d<0: continue
  prev={q:i for i,q in enumerate(f[d-1])}
  columns=[]
  for q in f[d]:
   col=0
   for j in range(len(q)):
    col ^= 1<<prev[q[:j]+q[j+1:]]
   columns.append(col)
  ranks[d]=rank2(columns)
 return {d:len(f[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in sorted(f) if d>=-1 and len(f[d])-ranks.get(d,0)-ranks.get(d+1,0)}

def sign_perm(seq):
 return -1 if sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))%2 else 1

def fixed_leaf_perm_trace(q,p,ext=1):
 fix=sum(i==p[i] for i in range(q))
 if ext==1:return fix-1
 pp=[p[p[i]] for i in range(q)]
 fix2=sum(i==pp[i] for i in range(q))
 return ((fix-1)**2-(fix2-1))//2

def predicted(s,qs,blocks,pc,perblock,blockperm):
 # pc is permutation of center indices. perblock maps the ith original block's labels to destination block labels.
 fixC=sum(i==pc[i] for i in range(s))
 fixC2=sum(i==pc[pc[i]] for i in range(s))
 trH1=(fixC**2-fixC2)//2
 visited=set(); bchar=1; achar=1
 for b in range(len(qs)):
  if b in visited:continue
  chain=[];cur=b
  while cur not in visited:
   chain.append(cur); visited.add(cur);cur=blockperm[cur]
  assert cur==b
  composite=list(range(qs[b]))
  for i in chain: composite=[perblock[i][x] for x in composite]
  bchar*=fixed_leaf_perm_trace(qs[b],composite,1)
  achar*=fixed_leaf_perm_trace(qs[b],composite,2)
 if sign_perm(blockperm)<0:bchar=-bchar
 return {1:trH1,len(qs):fixC*bchar,2*len(qs)-1:achar}

def lef(f,perm):
 out=0
 for d,ss in f.items():
  if d<0:
   out-=1;continue
  tr=0
  for q in ss:
   mapped=[perm[i] for i in q]
   if sorted(mapped)==list(q):
    tr+=sign_perm(mapped)
  out+=(-1)**d *tr
 return out

def run():
 cases=[(2,(3,3)),(3,(3,4)),(4,(3,3)),(3,(3,3,3)),(2,(4,4)),(2,(3,3,4))]
 tests=0;total_faces=0;diagrams=[]
 for s,qs in cases:
  blocks,f,v=faces(s,qs)
  total_faces+=sum(len(x) for x in f.values())
  b=bettis(f);n=len(qs);B=math.prod(q-1 for q in qs);A=math.prod(math.comb(q-1,2) for q in qs)
  exp={1:math.comb(s,2),n:s*B,2*n-1:A}
  assert b==exp,(s,qs,b,exp)
  diags=[list(range(v))]
  # center permutations, including inversions of an edge
  for pc in permutations(range(s)):
   if len(diags)>40:break
   p=list(range(v))
   for i in range(s):p[i]=pc[i]
   diags.append(p)
  # within each individual blade: all transpositions and one cycle
  for block in blocks:
   for i,j in itertools.combinations(block,2):
    p=list(range(v));p[i],p[j]=p[j],p[i];diags.append(p)
   p=list(range(v))
   for i in range(len(block)):p[block[i]]=block[(i+1)%len(block)]
   diags.append(p)
  # swap equal sized blades
  for i,j in itertools.combinations(range(n),2):
   if qs[i]!=qs[j]:continue
   p=list(range(v))
   for a,b0 in zip(blocks[i],blocks[j]):p[a]=b0;p[b0]=a
   diags.append(p)
  if s==2 and qs==(3,3):
   # Exhaust all 2! * 2! * (3!)^2 = 144 graph automorphisms.
   diags=[]
   for pc0 in itertools.permutations(range(s)):
    for bp in itertools.permutations(range(n)):
     for leaf_maps in itertools.product(*(itertools.permutations(range(q)) for q in qs)):
      p=list(range(v))
      for i in range(s):p[i]=pc0[i]
      for i,block in enumerate(blocks):
       for a,x in enumerate(block):p[x]=blocks[bp[i]][leaf_maps[i][a]]
      diags.append(p)
   assert len(diags)==144
  for perm in diags:
   pc=perm[:s]
   blockperm=[];perblock=[]
   for bl in blocks:
    tgt=next(i for i,b0 in enumerate(blocks) if perm[bl[0]] in b0)
    blockperm.append(tgt)
    perblock.append([blocks[tgt].index(perm[x]) for x in bl])
   assert set(blockperm)==set(range(n))
   tr=predicted(s,qs,blocks,pc,perblock,blockperm)
   expect=sum((-1)**d*a for d,a in tr.items())
   got=lef(f,perm)
   assert got==expect,(s,qs,perm,tr,got,expect)
   tests+=1
  diagrams.append((s,qs,v,{d:len(x) for d,x in f.items()},b,len(diags)))
 print('TRIANGLE_FREE_CLIQUE_JOIN_EXACT_PASS')
 print('case_count',len(cases),'face_total',total_faces,'signed_Lefschetz_checks',tests)
 for x in diagrams:print('case',x)
if __name__=='__main__':run()
