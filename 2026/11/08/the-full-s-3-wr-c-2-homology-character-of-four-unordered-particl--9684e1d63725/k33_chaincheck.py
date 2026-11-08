from try_k33_4 import bases,differential
from try_k33_char import G,act_basis
from collections import defaultdict
from itertools import permutations
import sys
D=[None]+[differential(k) for k in range(1,5)]
# polynomial module over Q: action computed mod101, still sufficient to verify integer because coefficients ± small
s=list(permutations(range(3)))
ids=(0,1,2,3,4,5)
gens=[(1,0,2,3,4,5),(1,2,0,3,4,5),(0,1,2,4,3,5),(0,1,2,4,5,3),(3,4,5,0,1,2)]
for gi,g in enumerate(gens):
 for k in range(1,5):
  for j in range(len(bases[k])):
   v=act_basis(k,j,g)
   left=defaultdict(int);right=defaultdict(int)
   for j1,a in v.items():
    for r,b in D[k][j1].items():left[r]=(left[r]+a*b)%101
   for r,b in D[k][j].items():
    for i,a in act_basis(k-1,r,g).items():right[i]=(right[i]+a*b)%101
   assert {r:a%101 for r,a in left.items() if a%101}=={r:a%101 for r,a in right.items() if a%101},(gi,k,j)
 print('CHAIN_MAP',gi,g,'PASS',flush=True)
print('ALL_FIVE_GENERATOR_CHAIN_MAPS_PASS')
