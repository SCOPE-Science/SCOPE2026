#!/usr/bin/env python3
"""Independently enumerates strong-filter matching complex of triangle-square bouquets.
No external packages, no assumption of the proposed decomposition in construction.
"""
from itertools import permutations,combinations,product
from collections import Counter


def graph(p,q):
  nbr={0:set()}; tri=[]; sq=[]; v=1
  def edge(a,b):nbr[a].add(b); nbr[b].add(a)
  for _ in range(p):
    a,b=v,v+1; v+=2
    nbr[a]=set();nbr[b]=set();edge(0,a);edge(a,b);edge(b,0);tri.append((a,b))
  for _ in range(q):
    a,b,c=v,v+1,v+2; v+=3
    for t in (a,b,c):nbr[t]=set()
    edge(0,a);edge(a,b);edge(b,c);edge(c,0);sq.append((a,b,c))
  return nbr,tri,sq

def all_subsets(mask):
  t=mask
  while True:
    yield t
    if not t:break
    t=(t-1)&mask

def explicit_complex(p,q):
  nbr,tri,sq=graph(p,q)
  arcs=sorted((s,t) for s in nbr for t in nbr[s]); idx={a:i for i,a in enumerate(arcs)}
  out={0}
  for order in permutations(nbr):
    seen=set(); f=0
    for u in order:
      earlier=nbr[u]&seen
      if len(earlier)==1:
        f|=1<<idx[(u,next(iter(earlier)))]
      seen.add(u)
    out.update(all_subsets(f))
  return out,idx,tri,sq

def build_predicted(p,q,idx,tri,sq):
  bit=lambda a:1<<idx[a]
  D=[];E=[]
  for a,b in tri:
    D.append([bit((a,b)),bit((b,a)),bit((a,0)),bit((b,0))]);E.append([bit((a,0)),bit((b,0))])
  L=[];H=[];T=[]
  for a,b,c in sq:
    A=bit((a,0));B=bit((b,a));C=bit((c,0));D_=bit((b,c));E_=bit((a,b));F=bit((c,b))
    L.append([A|B,A|C,C|D_,D_|E_,E_|F,F|B])
    H.append([A|B,A|C,C|D_]);T.append(([B,C,E_],[F,A,D_]))
  def join_faces(local):
    ret={0}
    for factor in local:
      nxt=set()
      for base in ret:
        for simplex in factor:
          nxt.update(all_subsets(base|simplex))
      ret=nxt
    return ret
  out=join_faces(D+L)
  for i,(a,b) in enumerate(tri):
    base=join_faces(E[:i]+E[i+1:]+H)
    for t in (a,b):
      apex=bit((0,t))
      out.update(face|apex for face in base)
  for i,(a,b,c) in enumerate(sq):
    for t,loc in zip((a,c),T[i]):
      base=join_faces(E+H[:i]+H[i+1:]+[loc])
      apex=bit((0,t))
      out.update(face|apex for face in base)
  return out

def mul_poly(a,b):
  out=[0]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
    for j,y in enumerate(b):out[i+j]+=x*y
  return out

def pow_poly(a,n):
  out=[1]
  for _ in range(n):out=mul_poly(out,a)
  return out

def face_poly(p,q):
  base=mul_poly(pow_poly([1,4],p),pow_poly([1,6,6],q))
  def add(a,b,scale=1):
    if len(a)<len(b):a += [0]*(len(b)-len(a))
    for i,v in enumerate(b):a[i]+=scale*v
    return a
  if p:
    correction=mul_poly(pow_poly([1,2],p-1),pow_poly([1,4,3],q))
    base=add(base,[0]+correction,2*p)
  if q:
    correction=mul_poly(mul_poly([1,3],pow_poly([1,2],p)),pow_poly([1,4,3],q-1))
    base=add(base,[0]+correction,2*q)
  return base

def rank_mod2(boundary):
  piv={}
  for v in boundary:
    while v:
      k=v.bit_length()-1
      if k in piv:v^=piv[k]
      else:piv[k]=v;break
  return len(piv)

def betti_f2(faces):
  by={}
  for s in faces:
    if s:by.setdefault(s.bit_count()-1,[]).append(s)
  rank={}
  for d in sorted(by):
    if d==0:rank[d]=0;continue
    prev={f:i for i,f in enumerate(by[d-1])};cols=[]
    for simplex in by[d]:
      col=0;v=simplex
      while v:
        b=v&-v;v-=b;col^=1<<prev[simplex^b]
      cols.append(col)
    rank[d]=rank_mod2(cols)
  return tuple(len(by[d])-rank[d]-rank.get(d+1,0) - (1 if d==0 else 0) for d in sorted(by))

def relative_collapse(faces, target):
  """Exhaustive elementary collapse of all faces not in the specified subcomplex."""
  faces=set(faces)
  steps=0
  while faces != target:
    # A free codimension-one face of a facet outside the target.
    coface_count={}
    facets=sorted((f for f in faces-target),key=lambda x:-x.bit_count())
    removed=False
    for big in facets:
      mask=big
      while mask:
        b=mask&-mask; mask-=b;little=big^b
        if not little or little in target or little not in faces:continue
        if not any((x!=big and x!=little and (x & little)==little) for x in faces):
          # unique coface check excludes not only codimension-one, but all simplices
          faces.remove(little);faces.remove(big)
          steps+=1;removed=True;break
      if removed:break
    if not removed:
      raise AssertionError(f'No relative free pair found: {len(faces-target)} faces left')
  return steps

def main():
  profiles=[(1,0),(0,1),(0,2),(1,1),(2,1),(1,2),(2,0),(0,3),(3,1),(2,2)]
  for p,q in profiles:
    V=1+2*p+3*q
    if V>9:continue
    actual,idx,tri,sq=explicit_complex(p,q)
    pred=build_predicted(p,q,idx,tri,sq)
    assert actual==pred,(p,q,len(actual),len(pred),len(actual-pred),len(pred-actual))
    f=Counter(x.bit_count() for x in actual)
    poly=face_poly(p,q)
    assert tuple(f.get(j,0) for j in range(len(poly)))==tuple(poly)
    betti=betti_f2(actual)
    if q>=2: n=3**p;dim=p+2*q-1
    elif q==1 and p>=1:n=3**p+4;dim=p+1
    elif q==1:n=5;dim=1
    elif q==0 and p>=1:n=3**p+2*p;dim=p-1
    else:raise AssertionError
    expected=tuple(n if d==dim else 0 for d in range(len(betti)))
    assert betti==expected,(p,q,betti,expected)
    if q>=2:
      # Predict target join from the no-hub-matching portion of the actual full complex.
      hub_mask=sum(1<<i for arc,i in idx.items() if arc[0]==0)
      target={f for f in actual if not f&hub_mask}
      steps=relative_collapse(actual,target)
      assert steps*2==len(actual)-len(target)
      print(f'  relative_collapse_to_join: {steps} elementary pairs')
    print(f'PASS p={p} q={q} orders={__import__("math").factorial(V)} faces={len(actual)} f={sorted(f.items())} reduced_Betti_F2={betti}')
  print('ALL_VERIFY_OK')
if __name__=='__main__':main()
