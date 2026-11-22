#!/usr/bin/env python3
"""Exact rational Chevalley--Eilenberg cohomology and signed dihedral characters for a graph Lie algebra."""
from collections import defaultdict
from fractions import Fraction
from math import comb
import json

def build(n=6):
 N=2*n
 weights=[]
 for j in range(N):
  w=[0]*n
  if j<n:w[j]=1
  else:w[j-n]+=1;w[(j-n+1)%n]+=1
  weights.append(tuple(w))
 def weight(mask):return tuple(sum(weights[j][i] for j in range(N) if mask>>j&1) for i in range(n))
 blocks=defaultdict(lambda:defaultdict(list))
 for mask in range(1<<N):blocks[weight(mask)][mask.bit_count()].append(mask)
 def signed_replace(mask,j,other):
  # for replacing a single generator in wedge by two generators (d of z)
  if mask&other:return None
  original=[k for k in range(N) if mask>>k&1]
  idx=original.index(j)
  expanded=original[:idx]+list(k for k in range(N) if other>>k&1)+original[idx+1:]
  sign=(-1)**idx
  for a in range(len(expanded)):
   for b in range(a+1,len(expanded)):
    if expanded[a]>expanded[b]:sign=-sign
  return (mask^(1<<j))|other,sign
 def diff(mask):
  d=defaultdict(int)
  for j in range(n,N):
   if not mask>>j&1:continue
   e=j-n
   out=signed_replace(mask,j, (1<<e)|(1<<((e+1)%n)))
   if out is not None:
    k,s=out
    if e==n-1:s=-s # dz_last=x_{last} wedge x_0
    d[k]+=s
  return {k:v for k,v in d.items() if v}
 def reduce(c,basis):
  c=dict(c); coords={}
  for pivot in sorted(basis):
   v=c.get(pivot,0)
   if v:
    coords[pivot]=v
    for k,x in basis[pivot].items():
     t=c.get(k,0)-v*x
     if t:c[k]=t
     elif k in c:del c[k]
  return c,coords
 def basis_from(cols):
  basis={}
  for c in cols:
   c,_=reduce(c,basis)
   if not c:continue
   pivot=min(c); factor=c[pivot]
   basis[pivot]={k:Fraction(v,factor) for k,v in c.items()}
  return basis
 def action(g,mask):
  a,sgn=g
  images=[];ss=1
  for j in range(N):
   if not (mask>>j&1):continue
   if j<n: images.append((a+sgn*j)%n)
   else:
    e=j-n
    if sgn==1: images.append(n+(a+e)%n)
    else: images.append(n+(a-e-1)%n); ss=-ss
  for j in range(len(images)):
   for l in range(j+1,len(images)):
    if images[j]>images[l]:ss=-ss
  result=sum(1<<j for j in images)
  return result,ss
 groups=[(a,s) for s in (1,-1) for a in range(n)]
 characters={str(g):[0]*(N+1) for g in groups}
 betti=[0]*(N+1)
 orbit_betti={str(g):[0]*(N+1) for g in groups}
 block_count=0
 for w,dims in blocks.items():
  block_count+=1
  cbases={k: basis_from(diff(m) for m in dims.get(k-1,[])) for k in dims}
  for k,ms in dims.items():
   betti[k]+=len(ms)-len(cbases[k])-len(cbases.get(k+1,{}))
  for g in groups:
   # only invariant weight blocks contribute to character
   if any(w[i]!=w[(g[0]+g[1]*i)%n] for i in range(n)):
    # this formula is coordinate action inverse? equivalence iff w preserved, inverse same property
    continue
   for k,ms in dims.items():
    ctrace=sum(action(g,m)[1] for m in ms if action(g,m)[0]==m)
    btrace=0
    for pv,b in cbases[k].items():
     changed={}
     for m,coeff in b.items():
      m2,s=action(g,m)
      changed[m2]=changed.get(m2,0)+coeff*s
     rem,coords=reduce(changed,cbases[k])
     assert not rem,(g,w,k,pv,rem)
     btrace+=coords.get(pv,0)
    bnexttrace=0
    for pv,b in cbases.get(k+1,{}).items():
     changed={}
     for m,coeff in b.items():
      m2,s=action(g,m)
      changed[m2]=changed.get(m2,0)+coeff*s
     rem,coords=reduce(changed,cbases[k+1])
     assert not rem
     bnexttrace+=coords.get(pv,0)
    t=ctrace-btrace-bnexttrace
    assert int(t)==t
    characters[str(g)][k]+=int(t)
 assert [characters[str((0,1))][k] for k in range(N+1)]==betti
 quotient=[sum(characters[str(g)][k] for g in groups)//len(groups) for k in range(N+1)]
 assert all(sum(characters[str(g)][k] for g in groups)%len(groups)==0 for k in range(N+1))
 print(json.dumps({'n':n,'dimension':N,'blocks':block_count,'betti':betti,'total':sum(betti),'characters':characters,'D_quotient_betti':quotient},indent=2))
 return betti,characters,quotient

if __name__=='__main__':build(6)
