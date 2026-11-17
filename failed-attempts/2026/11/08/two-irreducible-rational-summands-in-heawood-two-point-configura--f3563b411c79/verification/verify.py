#!/usr/bin/env python3
"""Reproduce exact two-point Heawood top-homology character over Q.
Uses only Python's standard library. All finite enumerations are exhaustive.
"""
from itertools import combinations, permutations
from collections import deque

def dot(a,b): return (a & b).bit_count() % 2

def H():
    return tuple((x-1,7+y-1) for x in range(1,8) for y in range(1,8) if dot(x,y)==0)

V=tuple(range(14)); E=tuple(sorted(H())); ESET=set(E)
assert len(E)==21 and all(sum(v in e for e in E)==3 for v in V)
Q0=tuple(combinations(V,2)); Q1=tuple((v,e) for v in V for e in E if v not in e)
Q2=tuple((a,b) for a,b in combinations(E,2) if len(set(a+b))==4)
I0={c:j for j,c in enumerate(Q0)}; I1={c:j for j,c in enumerate(Q1)}; I2={c:j for j,c in enumerate(Q2)}
assert (len(Q0),len(Q1),len(Q2))==(91,252,168)

D1=tuple(((I0[tuple(sorted((v,e[1])))],1),(I0[tuple(sorted((v,e[0])))],-1)) for v,e in Q1)
D2=tuple(((I1[(a[1],b)],1),(I1[(a[0],b)],-1),(I1[(b[1],a)],-1),(I1[(b[0],a)],1)) for a,b in Q2)

def lin_sum(terms):
 d={}
 for i,x in terms:
  d[i]=d.get(i,0)+x
 return {i:x for i,x in d.items() if x}

assert all(not lin_sum((i,a*b) for j,a in col for i,b in D1[j]) for col in D2)

# Each first boundary connects two zero-cells. Thus BFS checks rank(D1)=90.
adj=[[] for _ in Q0]
for col in D1:
 a,b=col[0][0],col[1][0];adj[a].append(b);adj[b].append(a)
seen={0};todo=[0]
for j in todo:
 for k in adj[j]:
  if k not in seen:seen.add(k);todo.append(k)
assert len(seen)==len(Q0)

def mod_reduce(cols,p,with_kernel=False):
 """Exact sparse echelon reduction over prime field, with kernel certificates."""
 piv={};ker=[];free=[]
 for j,col in enumerate(cols):
  row={i:a%p for i,a in col if a%p}; rep={j:1}
  while row:
   i=max(row)
   if i not in piv:
    fac=pow(row[i],-1,p)
    piv[i]=({k:(a*fac)%p for k,a in row.items()},
            {k:(a*fac)%p for k,a in rep.items()})
    break
   fac=row[i];basis,repr_col=piv[i]
   for k,a in basis.items():
    v=(row.get(k,0)-fac*a)%p
    if v:row[k]=v
    else:row.pop(k,None)
   for k,a in repr_col.items():
    v=(rep.get(k,0)-fac*a)%p
    if v:rep[k]=v
    else:rep.pop(k,None)
  else:
   free.append(j)
   if with_kernel:ker.append(rep)
 return len(piv),free,ker

r3,_,_=mod_reduce(D2,3);r101,free,basis=mod_reduce(D2,101,True)
assert r3==r101==154 and len(free)==len(basis)==14
for f,c in zip(free,basis):
 assert c[f]==1 and all(c.get(k,0)==0 for k in free if k!=f)
 # Verify the kernel relation modulo 101.
 residue={}
 for j,a in c.items():
  for i,b in D2[j]:residue[i]=(residue.get(i,0)+a*b)%101
 assert not any(residue.values())
# Independent rank-eight proper simple cycles for surjectivity of H1(X;Q)->H1(H;Q).
AD={v:set() for v in V}
for a,b in E:AD[a].add(b);AD[b].add(a)
cycles=set()
for s in V:
 def walk(path):
  v=path[-1]
  if len(path)==6:
   if s in AD[v]:
    t=tuple(path)
    if s==min(t):cycles.add(min(t,(s,)+tuple(reversed(t[1:]))))
   return
  for w in AD[v]:
   if w not in path and w>s:walk(path+[w])
 walk([s])
assert len(cycles)==28
IE={e:j for j,e in enumerate(E)}
cycle_columns=[]
for t in sorted(cycles):
 vals={}
 for a,b in zip(t,t[1:]+(t[0],)):
  e=tuple(sorted((a,b))); vals[IE[e]]=1 if a<b else -1
 cycle_columns.append(tuple(sorted(vals.items())))
r,selected=[],[]
for col in cycle_columns:
 if mod_reduce(r+[col],3)[0]>len(r):r.append(col)
assert len(r)==8
for c in r:
 # A fixed vertex outside the six-cycle gives a valid closed 1-chain in X.
 edge_set={E[j][k] for j,_ in c for k in (0,1)}
 fix=next(v for v in V if v not in edge_set)
 lifted=((I1[(fix,E[j])],a) for j,a in c)
 bd=lin_sum((i,a*b) for j,a in lifted for i,b in D1[j])
 assert not bd
# Hence rank_Q(D2)<=252-90-8=154, with mod-3 lower bound exactly 154.

# GL(3,2) acts on seven Fano points and contragrediently on seven lines.
def linear(x,a,b,c):
 return ((a if x&1 else 0)^(b if x&2 else 0)^(c if x&4 else 0))

def compose(a,b):return tuple(a[b[i]] for i in V)

pol=tuple((i+7)%14 for i in V)
autos=set()
for a in range(1,8):
 for b in range(1,8):
  if b==a:continue
  for c in range(1,8):
   if c in (a,b,a^b):continue
   points={x:linear(x,a,b,c) for x in range(1,8)}
   dual={y:next(z for z in range(1,8) if all(dot(points[x],z)==dot(x,y) for x in (1,2,4))) for y in range(1,8)}
   g=tuple([points[x]-1 for x in range(1,8)]+[dual[y]+6 for y in range(1,8)])
   autos.update((g,compose(g,pol)))
autos=tuple(sorted(autos)); IA={g:j for j,g in enumerate(autos)}
assert len(autos)==336
assert all({tuple(sorted((g[a],g[b]))) for a,b in E}==ESET for g in autos)

def edge_act(g,e):
 a,b=g[e[0]],g[e[1]]
 return ((a,b),1) if a<b else ((b,a),-1)

def act0(g,c):return I0[tuple(sorted((g[c[0]],g[c[1]])))],1

def act1(g,c):
 v,e=c;ep,s=edge_act(g,e)
 return I1[(g[v],ep)],s

def act2(g,c):
 e,f=c;e2,s=edge_act(g,e);f2,t=edge_act(g,f)
 if e2<f2:return I2[(e2,f2)],s*t
 return I2[(f2,e2)],-s*t

def trace_cells(g):
 tr0=sum(act0(g,c)==(j,1) for j,c in enumerate(Q0))
 tr1=sum(s for j,c in enumerate(Q1) for i,s in [act1(g,c)] if i==j)
 tr2=sum(s for j,c in enumerate(Q2) for i,s in [act2(g,c)] if i==j)
 trv=sum(g[v]==v for v in V)
 tre=sum(s for e in E for ee,s in [edge_act(g,e)] if ee==e)
 ch1=tre-trv+1
 ch2=tr0-tr1+tr2-1+ch1
 return ch1,ch2,(tr0,tr1,tr2,tre,trv)

# Direct evaluation on the exact top kernel mod101, independent of Lefschetz.
def direct_top_trace(g):
 acted=[act2(g,c) for c in Q2]
 tot=0
 for f,c in zip(free,basis):
  tot+=sum(a*sgn for j,a in c.items() for i,sgn in [acted[j]] if i==f)
 return tot%101

for g in autos:
 ch1,ch2,_=trace_cells(g)
 assert direct_top_trace(g)==ch2%101
# Verify chain naturality on all 336 symmetries.
for g in autos:
 a1=[act1(g,c) for c in Q1]
 for j,c in enumerate(Q1):
  i,s=a1[j]
  lhs=lin_sum((k,s*b) for k,b in D1[i])
  rhs=lin_sum((act0(g,Q0[k])[0],b) for k,b in D1[j])
  assert lhs==rhs
 for j,c in enumerate(Q2):
  i,s=act2(g,c)
  lhs=lin_sum((k,s*b) for k,b in D2[i])
  rhs=lin_sum((a1[k][0],b*a1[k][1]) for k,b in D2[j])
  assert lhs==rhs

# Exhaustive conjugacy class decomposition (under the explicitly enumerated group).
def inv(g):
 t=[0]*14
 for i,j in enumerate(g):t[j]=i
 return tuple(t)

def order(g):
 q=tuple(V)
 for k in range(1,17):
  q=compose(g,q)
  if q==tuple(V):return k
 raise AssertionError('unexpected order')
classes=[];remaining=set(autos)
for a in autos:
 if a not in remaining:continue
 cs={compose(compose(g,a),inv(g)) for g in autos}
 remaining.difference_update(cs)
 classes.append((len(cs),order(a),a,cs))
classes.sort(key=lambda k:(k[0],k[1],k[2]))
assert len(classes)==9 and not remaining
sizes=[z[0] for z in classes]
chi1=[trace_cells(z[2])[0] for z in classes]
chi2=[trace_cells(z[2])[1] for z in classes]
psi=[b-a for a,b in zip(chi1,chi2)]
assert sorted(sizes)==[1,21,28,42,42,42,48,56,56]
assert sum(s*a*a for s,a in zip(sizes,chi1))==336
assert sum(s*a*a for s,a in zip(sizes,chi2))==672
assert sum(s*a*b for s,a,b in zip(sizes,chi1,chi2))==336
assert sum(s*a*a for s,a in zip(sizes,psi))==336
assert sum(s*a*b for s,a,b in zip(sizes,chi1,psi))==0
assert sum(s*a for s,a in zip(sizes,chi2))==0

print('HEAWOOD_2POINT_FULL_SYMMETRY_PASS')
print('graph_V_E=14,21 config_C0_C1_C2=91,252,168 automorphisms=336')
print('six_cycles=28 proper_cycle_basis=8 connected_C0=91')
print('rank_D1_Z=90 rank_D2_mod3=154 rank_D2_mod101=154 top_kernel=14')
print('H1_Q=8 H2_Z_free=14 all_336_direct_kernel_traces_and_chain_naturality=PASS')
print('class_size,order,chi_H1,chi_H2,chi_6')
for s,o,g,cl in classes:
 a,b,_=trace_cells(g)
 print(s,o,a,b,b-a)
print('character_inner_products=<H1,H1>:1 <H1,H2>:1 <H2,H2>:2 <W6,W6>:1')
print('H2_Q=H1(graph;Q) + W6 (both absolutely irreducible); invariants=0')
