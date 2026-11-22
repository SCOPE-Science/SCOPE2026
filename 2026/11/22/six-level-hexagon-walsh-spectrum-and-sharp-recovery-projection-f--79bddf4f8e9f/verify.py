#!/usr/bin/env python3
"""Exact independent verification of the Heawood-hexagon Fourier theorem.

Python 3 standard library only. Run: python3 verify.py
"""
from itertools import combinations
from collections import Counter, deque
from fractions import Fraction

P=tuple(range(1,8))
L=tuple(sorted({tuple(sorted((a,b,a^b))) for a in P for b in P if a!=b}))
assert len(L)==7 and all(len(ell)==3 for ell in L)
E=tuple((a,j) for j,ell in enumerate(L) for a in ell)
assert len(E)==21
index={edge:i for i,edge in enumerate(E)}
V=tuple(('p',a) for a in P)+tuple(('l',j) for j in range(7))
adj={v:[] for v in V}
for k,(a,j) in enumerate(E):
 u,w=('p',a),('l',j)
 adj[u].append((w,k));adj[w].append((u,k))

def by_fano():
 out=set()
 for a,b,c in combinations(P,3):
  if a^b^c==0:continue
  j=next(t for t,ell in enumerate(L) if a in ell and b in ell)
  k=next(t for t,ell in enumerate(L) if b in ell and c in ell)
  h=next(t for t,ell in enumerate(L) if c in ell and a in ell)
  selected=((a,j),(b,j),(b,k),(c,k),(c,h),(a,h))
  out.add(sum(1<<index[e] for e in selected))
 return out

def by_graph_dfs():
 # Independently list all *simple* closed walks of length six.
 out=set()
 for root in V:
  def go(node,visited,chosen):
   if len(chosen)==6:
    if node==root and len(visited)==6:
     out.add(sum(1<<k for k in chosen))
    return
   for neighbor,k in adj[node]:
    if neighbor==root:
     if len(chosen)==5:go(root,visited,chosen+(k,))
    elif neighbor not in visited:
     go(neighbor,visited|{neighbor},chosen+(k,))
  go(root,{root},())
 return out

hex1=by_fano();hex2=by_graph_dfs()
assert hex1==hex2 and len(hex1)==28
assert all(x.bit_count()==6 for x in hex1)

# Compute 13 tree edges via a deterministic graph traversal.
seen={V[0]};q=deque([V[0]]);tree=set()
while q:
 node=q.popleft()
 for nb,k in sorted(adj[node]):
  if nb not in seen:
   seen.add(nb);tree.add(k);q.append(nb)
assert len(seen)==14 and len(tree)==13
chords=[k for k in range(21) if k not in tree]
assert len(chords)==8

def compress(x):return sum(((x>>k)&1)<<j for j,k in enumerate(chords))
A={compress(x) for x in hex1}
assert len(A)==28

# Every Eulerian edge set has unique chord coordinates, since the difference
# of two Eulerian edge sets supported on a tree must be empty.
# Explicitly construct fundamental cycles of each chord and check reconstruction.
def cycle_from_chord(k):
 u,w=('p',E[k][0]),('l',E[k][1])
 pred={u:None};steps={};Q=deque([u])
 while Q and w not in pred:
  node=Q.popleft()
  for nb,e in adj[node]:
   if e in tree and nb not in pred:
    pred[nb]=node;steps[nb]=e;Q.append(nb)
 assert w in pred
 x=1<<k;node=w
 while node!=u:
  x ^= 1<<steps[node];node=pred[node]
 return x
basis=[cycle_from_chord(k) for k in chords]
assert all(compress(b)==1<<i for i,b in enumerate(basis))
for x in hex1:
 y=compress(x); reconstructed=0
 for j,b in enumerate(basis):
  if (y>>j)&1:reconstructed^=b
 assert reconstructed==x

def binary_rank(nums):
 base={}
 for v in nums:
  while v:
   pivot=v.bit_length()-1
   if pivot not in base:base[pivot]=v;break
   v^=base[pivot]
 return len(base)
assert binary_rank(A)==8

N=256
# Independently evaluate exact Walsh sums by direct signs.
lambdas=[sum(-1 if ((s&a).bit_count()&1) else 1 for a in A) for s in range(N)]
expected={-8:28,-4:56,0:108,4:42,12:21,28:1}
assert dict(Counter(lambdas))==expected

# Verify by butterfly Hadamard transform of the counting kernel.
def fwht(x):
 x=list(x);block=1
 while block<len(x):
  for start in range(0,len(x),2*block):
   for j in range(start,start+block):
    a,b=x[j],x[j+block];x[j],x[j+block]=a+b,a-b
  block*=2
 return x
f=[int(a in A) for a in range(N)]
assert fwht(f)==lambdas
assert sum(x*x for x in lambdas)==N*len(A)

# Fourier projection onto nonzero multiplier frequencies; 8-dimensional
# because all 21-edge characters restrict to the 8-dimensional cycle space.
p=[int(v!=0) for v in lambdas]
g=fwht(p)
assert sum(abs(x) for x in g)==1936
norm=Fraction(sum(abs(x) for x in g),N)
assert norm==Fraction(121,16)
assert sum(x*x for x in g)==N*sum(p)

# The full 21-dimensional transform repeats each 8-bit character 8192 times.
scale=1<<(21-8)
full_hist={k:v*scale for k,v in expected.items()}
assert sum(full_hist.values())==(1<<21)
rank=(N-expected[0])*scale
assert rank==1212416 and (1<<21)-rank==884736
# Actual strictly positive gap:
assert min(abs(x) for x in lambdas if x!=0)==4
assert max(abs(x) for x in lambdas)==28

# The distinct Fano triple support in seven coordinates cannot carry this
# spectrum by an affine change of ambient Boolean coordinates: the affine
# span dimensions differ (six versus eight).
T=[sum(1<<(a-1) for a in triple) for triple in combinations(P,3) if triple[0]^triple[1]^triple[2]!=0]
assert binary_rank([t^T[0] for t in T])==6
assert binary_rank([a^next(iter(A)) for a in A])==8
print('cycles=28, independent_listings_equal=True, cycle_space_dimension=8')
print('reduced_spectrum=',sorted(expected.items()))
print('full_spectrum=',sorted(full_hist.items()))
print('projection_kernel_histogram=',sorted(Counter(g).items()))
print('rank=',rank,'nullity=',(1<<21)-rank,'gap=4, condition=7')
print('sharp_unrestricted_endpoint_norm=',norm,'projection_integer_L1=',sum(abs(x) for x in g))
print('PASS')
