#!/usr/bin/env python3
"""Exact finite-tensor verification of the Segre four-point determinant's ambient stabilizer."""
import itertools
import sympy as sp

def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))

coeff={}
for a in itertools.product((0,1),repeat=4):
 if sum(a)!=2:continue
 for b in itertools.product((0,1),repeat=4):
  if sum(b)!=2 or sum(i*j for i,j in zip(a,b))!=1:continue
  x=a+b
  coeff[x]=parity([2*a[i]+b[i] for i in range(4)])
assert len(coeff)==24
coords=list(itertools.product((0,1),repeat=8))
index={x:i for i,x in enumerate(coords)}
M=sp.zeros(256,24)
for x,c in coeff.items():
 for i in range(8):
  # E maps basis 1 to 0, F maps basis 0 to 1, H diagonal (+1,-1)
  if x[i]==1:
   y=list(x);y[i]=0;M[index[tuple(y)],3*i]+=c
  else:
   y=list(x);y[i]=1;M[index[tuple(y)],3*i+1]+=c
  M[index[x],3*i+2]+=c*(1 if x[i]==0 else -1)
assert M.rank()==18
print('LIE_STABILIZER_DIM 6, rank_of_256_by_24_exact_matrix 18')
# Check explicit diagonal generators in 4 left and 4 right factors.
for half in (range(4),range(4,8)):
 for typ in range(3):
  v=sp.zeros(24,1)
  for i in half:v[3*i+typ]=1
  assert M*v==sp.zeros(256,1)
print('CONNECTED_STABILIZER diagonal_PGL2_x_diagonal_PGL2')
# support partitions: two coordinates cooccur in 4 monomials if same block, 6 if opposite.
assert all(sum(x[i]*x[j] for x in coeff)==(4 if (i<4)==(j<4) else 6)
           for i in range(8) for j in range(i+1,8))
print('SUPPORT_BLOCK_PARTITION_CERTIFIED same_block_frequency_4 cross_block_frequency_6')
# The Klein 4 group = kernel of action on perfect matchings.
def pairing_action(p):
 matchings=[frozenset((frozenset((0,1)),frozenset((2,3)))),frozenset((frozenset((0,2)),frozenset((1,3)))),frozenset((frozenset((0,3)),frozenset((1,2))))]
 return tuple(matchings.index(frozenset(frozenset(p[i] for i in pair) for pair in matching)) for matching in matchings)
perms=list(itertools.permutations(range(4)))
count=0
for pa in perms:
 for pb in perms:
  if pairing_action(pa)!=pairing_action(pb):continue
  for swap in (False,True):
   perm=(tuple(pa[i] for i in range(4))+tuple(4+pb[i] for i in range(4))) if not swap else (tuple(4+pa[i] for i in range(4))+tuple(pb[i] for i in range(4)))
   assert len({coeff[x]*coeff[tuple(x[j] for j in perm)] for x in coeff})==1
   count+=1
assert count==192
print('FINITE_COMPONENTS 192 = 24 * 4 * 2; signed_24_term_determinant_preserved')
f=sp.zeros(256,1)
for x,c in coeff.items():f[index[x]]=c
assert M.row_join(f).rank()==19
print('PROJECTIVE_AUGMENTED_RANK 19')
print('EXACT_CHECKS_PASS')
