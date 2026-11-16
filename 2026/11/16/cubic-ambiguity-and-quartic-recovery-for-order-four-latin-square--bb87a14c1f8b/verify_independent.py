"""Independent row-completion enumeration and modular determinant replay.
Requires Python 3 and NumPy. Run: python verify_independent.py pivot_manifest.json
"""
import itertools,json,sys,hashlib
import numpy as np
from collections import Counter
permutations=list(itertools.permutations(range(4)))
all_squares=set()
for a in permutations:
 for b in permutations:
  if any(a[j]==b[j] for j in range(4)):continue
  for c in permutations:
   if any(c[j] in (a[j],b[j]) for j in range(4)):continue
   d=tuple(next(v for v in range(4) if v not in (a[j],b[j],c[j])) for j in range(4))
   assert sorted(d)==[0,1,2,3]
   all_squares.add(a+b+c+d)
squares=sorted(all_squares)
assert len(squares)==576
manifest=json.load(open(sys.argv[1],encoding='utf8'))
assert hashlib.sha256(bytes(v for s in squares for v in s)).hexdigest()==manifest['ordered_squares_sha256']
cols=manifest['columns']
assert len(cols)==576
assert len(set(tuple(x) for x in cols))==576
assert Counter(len(x) for x in cols)=={0:1,1:27,2:218,3:276,4:54}

# Column elimination over a second odd prime. Columns are indicators of
# exact cell-symbol assignments, not floating-point approximations.
p=7
base={}
rank=0
for col in cols:
 positions=[(i//4,i%4) for i in col]
 a=np.fromiter((int(all(s[cell]==symbol for cell,symbol in positions)) for s in squares),dtype=np.int16,count=576)
 for pivot,b in base.items():
  if a[pivot]:a=(a-a[pivot]*b)%p
 nz=np.flatnonzero(a)
 assert len(nz),f'dependent column {rank}'
 pivot=int(nz[0]);base[pivot]=(a*pow(int(a[pivot]),-1,p))%p
 rank+=1
assert rank==576
print('PASS: independent enumeration 576 Latin squares')
print('PASS: 576-column selected determinant nonzero modulo 7')
print('PASS: first 522 cubic-or-lower columns independent modulo 7')

# Check a canonical four-switch cube without reading the first verifier.
# Coordinates are the additive group F_2^2 and each coset block is 2x2.
H=range(4)
base_sq=tuple(i^j for i in H for j in H)
blocks=[]
for aa in ((0,1),(2,3)):
 for bb in ((0,1),(2,3)):
  blocks.append(tuple(4*i+j for i in aa for j in bb))
weight={}
for toggles in itertools.product((0,1),repeat=4):
 s=list(base_sq)
 for z,flag in enumerate(toggles):
  if flag:
   for k in blocks[z]:s[k]^=1
 s=tuple(s)
 assert s in all_squares
 weight[s]=(-1)**sum(toggles)
assert len(weight)==16
for cells in itertools.combinations(range(16),3):
 sums={}
 for s,w in weight.items():
  key=tuple(s[i] for i in cells)
  sums[key]=sums.get(key,0)+w
 assert all(t==0 for t in sums.values())
print('PASS: canonical 16-square switch cube annihilates all three-cell events')
