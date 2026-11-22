#!/usr/bin/env python3
"""Independent signed orbit-sum invariant cochain computation over QQ."""
from fractions import Fraction
from collections import defaultdict
from itertools import product
import json
n=6; N=12
# Vertex and oriented-edge maps as permutation of basis with signs
G=[]
for s in (1,-1):
 for a in range(n):
  perm=[];eps=[]
  for i in range(n):perm.append((s*i+a)%n);eps.append(1)
  for i in range(n):perm.append(n+((s*i+a)%n if s==1 else (s*i+a-1)%n));eps.append(s)
  G.append((perm,eps))

def act(g,mask):
 p,e=G[g]; dest=[];c=1
 for i in range(N):
  if mask&(1<<i):dest.append(p[i]);c*=e[i]
 for i in range(len(dest)):
  for j in range(i+1,len(dest)):
   if dest[i]>dest[j]:c=-c
 return sum(1<<i for i in dest),c

def d(mask):
 out=defaultdict(int);indices=[i for i in range(N) if mask>>i&1]
 for position,i in enumerate(indices):
  if i<n:continue
  a=i-n;b=(a+1)%n
  if mask&(1<<a) or mask&(1<<b):continue
  # wedge insertion formula: d(generator product)=sum (-1)^position prefix * x_a wedge x_b * suffix
  v=indices[:position]+[a,b]+indices[position+1:]
  sign=(-1)**position
  for r in range(len(v)):
   for t in range(r+1,len(v)):
    if v[r]>v[t]:sign=-sign
  new=(mask^(1<<i))|(1<<a)|(1<<b)
  out[new]+=sign
 return {x:c for x,c in out.items() if c}

for mask in range(1<<N):
 twice=defaultdict(int)
 for b,c in d(mask).items():
  for x,v in d(b).items():twice[x]+=c*v
 assert not any(twice.values()),('d2',mask)
 for g in range(12):
  gm,gs=act(g,mask)
  lhs=defaultdict(int)
  for b,c in d(mask).items():
   q,s=act(g,b);lhs[q]+=c*s
  rhs={q:gs*c for q,c in d(gm).items()}
  assert {k:v for k,v in lhs.items() if v}==rhs,('equiv',mask,g)

reps=[]; vecs=[]; mask_to_basis={}; seen=set()
for mask in range(1<<N):
 if mask in seen:continue
 signed={};conflict=False
 for g in range(12):
  tgt,sgn=act(g,mask)
  if tgt in signed and signed[tgt]!=sgn:conflict=True
  signed[tgt]=sgn
 orbit=set(signed);seen|=orbit
 if conflict:continue
 # ensure coefficient of representative=1 using orientation factor
 rep=min(orbit);rsgn=signed[rep]
 vec={tgt:s*rsgn for tgt,s in signed.items()}
 index=len(reps)
 reps.append(rep);vecs.append(vec)
 for m,s in vec.items():mask_to_basis[m]=(index,s)

dims=defaultdict(list)
for j,rep in enumerate(reps):dims[rep.bit_count()].append(j)

def rank(cols):
 piv={};r=0
 for c in cols:
  col={k:Fraction(v) for k,v in c.items() if v}
  while col:
   k=min(col); coeff=col[k]
   if k not in piv:
    piv[k]={j:x/coeff for j,x in col.items()};r+=1;break
   for j,x in piv[k].items():
    nv=col.get(j,0)-coeff*x
    if nv:col[j]=nv
    elif j in col:del col[j]
 return r
R=[]
for k in range(N+1):
 cols=[]
 for j in dims[k]:
  raw=defaultdict(int)
  for m,c in vecs[j].items():
   for t,x in d(m).items():raw[t]+=c*x
  compressed={}
  for t,v in raw.items():
   if not v:continue
   jj,s=mask_to_basis[t]
   if t==reps[jj]:compressed[jj]=v
  cols.append(compressed)
 R.append(rank(cols))
betti=[len(dims[k])-(R[k-1] if k else 0)-R[k] for k in range(N+1)]
print(json.dumps({'n':n,'invariant_dims':[len(dims[k]) for k in range(N+1)],'ranks':R,'D_quotient_betti':betti},indent=2))
assert betti==[1,1,2,7,15,19,20,18,10,5,2,0,0]
