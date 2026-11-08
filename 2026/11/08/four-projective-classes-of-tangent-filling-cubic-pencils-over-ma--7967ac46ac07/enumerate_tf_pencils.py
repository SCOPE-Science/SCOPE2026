#!/usr/bin/env python3
"""Exact F_3 projective ternary cubic tangent-filling pencil census."""
from itertools import product, combinations
from collections import Counter
P=3**10
EXPS=[(3,0,0),(0,3,0),(0,0,3),(2,1,0),(2,0,1),(1,2,0),(0,2,1),(1,0,2),(0,1,2),(1,1,1)]
V=[]
for x in product(range(3),repeat=3):
 if x != (0,0,0) and x[next(i for i,a in enumerate(x) if a)]==1: V.append(x)
V.sort()
assert len(V)==13
lines=V
mon=lambda p,e:__import__('functools').reduce(lambda a,b:a*b,(pow(p[i],e[i],3) for i in range(3)),1)%3
E=[[mon(p,e) for e in EXPS] for p in V]
G=[]
for p in V:
 gg=[]
 for v in range(3):
  gg.append([(e[v]*mon(p,tuple(e[i]-(i==v) for i in range(3)))%3) if e[v]>0 else 0 for e in EXPS])
 G.append(gg)
def coeff(i):
 a=[]
 for _ in range(10):a.append(i%3);i//=3
 return a
def code(a):return sum(x*3**i for i,x in enumerate(a))
def norm(a):
 k=next(x for x in a if x)
 return code(a if k==1 else [(2*x)%3 for x in a])
def classify(c):
 # no test of smoothness: tangent coverage on non-singular F3 points
 vals=[sum(a*b for a,b in zip(c,E[i]))%3 for i in range(13)]
 cover=set(); rational=0
 for i in range(13):
  if vals[i]:continue
  grad=[sum(a*b for a,b in zip(c,G[i][j]))%3 for j in range(3)]
  if not any(grad):continue
  rational+=1
  first=next(x for x in grad if x)
  line=tuple((x if first==1 else 2*x)%3 for x in grad)
  for j,p in enumerate(V):
   if sum(a*b for a,b in zip(line,p))%3==0:cover.add(j)
 return len(cover)==13,rational
TF={};census=Counter()
for i in range(1,P):
 c=coeff(i)
 if next(x for x in c if x)!=1:continue
 tf,n=classify(c)
 if tf:TF[i]=c;census[n]+=1
print('tangent_filling_forms',len(TF),'rational_points',sorted(census.items()),flush=True)
lookup=set(TF)
# Each line has 6 unordered pairs of four projective points.
pencils=set()
# nonzero scaling of pairs is in the calculation; normalize sums and differences
for i,j in combinations(sorted(TF),2):
 a,b=TF[i],TF[j]
 u=norm([(x+y)%3 for x,y in zip(a,b)])
 if u not in lookup:continue
 v=norm([(x-y)%3 for x,y in zip(a,b)])
 if v not in lookup:continue
 pencils.add(tuple(sorted((i,j,u,v))))
assert all(len(p)==4 for p in pencils)
print('pencils',len(pencils))
print('point_hist',Counter(tuple(sorted(classify(TF[c])[1] for c in p)) for p in pencils).most_common())
# base set cardinalities
base_count=Counter()
for p in pencils:
 masks=[sum((1<<i) for i in range(13) if sum(a*b for a,b in zip(TF[c],E[i]))%3==0) for c in p]
 base_count[(masks[0]&masks[1]&masks[2]&masks[3]).bit_count()]+=1
print('base_count',sorted(base_count.items()),flush=True)
# generate PGL3 by simple coordinate substitutions, apply linear map to forms with evaluation (interpolation to obtain coefficients)
# matrix evaluation transform: express every F(T(x)) by expanding 3-var cubics; this is done through 10 monomial coefficients.
from math import comb
# polynomial dictionaries exponent -> coefficient
D=[{e:1} for e in EXPS]
def multiply(A,B):
 C={}
 for e,a in A.items():
  for f,b in B.items():
   g=tuple(e[i]+f[i] for i in range(3))
   C[g]=(C.get(g,0)+a*b)%3
 return {k:v for k,v in C.items() if v}
def trans_mat(M):
 entries=[]
 for e in EXPS:
  out={(0,0,0):1}
  for i in range(3):
   for _ in range(e[i]):out=multiply(out,{tuple(int(j==k) for j in range(3)):M[i][k] for k in range(3) if M[i][k]})
  entries.append(out)
 return [[entries[i].get(e,0) for i in range(10)] for e in EXPS]
matrices=[[(0,1,0),(1,0,0),(0,0,1)],[(1,1,0),(0,1,0),(0,0,1)],[(2,0,0),(0,1,0),(0,0,1)],[(1,0,0),(0,0,1),(0,1,0)]]
trans=[trans_mat(m) for m in matrices]
def transform(c,T):
 a=TF[c]
 out=[sum(T[i][j]*a[j] for j in range(10))%3 for i in range(10)]
 return norm(out)
# all TF should be invariant under these generators
for T in trans:assert all(transform(c,T) in lookup for c in lookup)
remaining=set(pencils);orbits=[]
while remaining:
 p=min(remaining)
 orbit={p};stack=[p]
 while stack:
  x=stack.pop()
  for t in trans:
   y=tuple(sorted(transform(c,t) for c in x))
   assert y in pencils
   if y not in orbit:orbit.add(y);stack.append(y)
 remaining-=orbit
 orbits.append((p,len(orbit)))
print('orbits',len(orbits),'orbit_sizes',sorted(Counter(b for a,b in orbits).items()),flush=True)
from pathlib import Path
out=Path(__file__).with_name('tf_pencil_orbits.csv')
out.write_text('cubic1,cubic2,cubic3,cubic4,orbit_size,stabilizer_order\n'+''.join(','.join(map(str,(*p,sz,5616//sz)))+'\n' for p,sz in sorted(orbits)))
assert sum(n for p,n in orbits)==len(pencils)
