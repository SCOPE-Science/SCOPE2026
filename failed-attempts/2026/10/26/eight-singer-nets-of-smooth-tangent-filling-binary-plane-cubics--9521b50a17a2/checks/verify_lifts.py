"""Independent 512-splitting search for binary cubic nets with linear evaluation.

The kernel of evaluation of ternary cubics at the Fano-plane points has
basis XY(X+Y), YZ(Y+Z), ZX(Z+X); the coordinate-cube lifts give a
complementary three-space. Tests use exact characteristic-two ideals.
Run: python verify_lifts.py
"""
from itertools import product
from sympy import symbols,groebner
import json
A,B,C=symbols('X Y Z'); variables=(A,B,C)
terms=[A**3,A**2*B,A**2*C,A*B**2,A*B*C,A*C**2,B**3,B**2*C,B*C**2,C**3]
points=[(a,b,c) for a,b,c in product([0,1],repeat=3) if a or b or c]

def form(mask):return sum(terms[j] for j in range(10) if mask&(1<<j))
def is_smooth(mask):
 f=form(mask)
 ff=[f.diff(v) for v in variables]
 for k in range(3):
  v=[q for j,q in enumerate(variables) if j!=k]
  equations=[e.subs(variables[k],1) for e in [f]+ff]
  G=groebner(equations,*v,modulus=2)
  if len(G.polys)!=1 or G.polys[0].as_expr()!=1:return False
 return True

def is_tangent_filling(mask):
 f=form(mask);df=[f.diff(v) for v in variables]
 line_union=set()
 for p in points:
  sub=dict(zip(variables,p))
  if int(f.subs(sub))%2:continue
  gradient=[int(g.subs(sub))%2 for g in df]
  if gradient==[0,0,0]:continue
  for q in points:
   if sum(a*b for a,b in zip(gradient,q))%2==0:line_union.add(q)
 return len(line_union)==7

kernel_basis=(10,384,36)
def kernel(index):
 return (10 if index&1 else 0) ^ (384 if index&2 else 0) ^ (36 if index&4 else 0)

def seven_nonzero(basis):
 a,b,c=basis
 return frozenset((a,b,c,a^b,a^c,b^c,a^b^c))

# All possible linear splittings of evaluation onto linear functions on
# the seven rational projective points. 8^3=512 candidates, exactly.
valid_forms=set()
for base in (1,64,512):
 for offset in range(8):
  m=base^kernel(offset)
  if is_smooth(m) and is_tangent_filling(m):valid_forms.add(m)
all_nets=set()
for ia,ib,ic in product(range(8),repeat=3):
 basis=(1^kernel(ia),64^kernel(ib),512^kernel(ic))
 masks=seven_nonzero(basis)
 if all(is_smooth(m) and is_tangent_filling(m) for m in masks):all_nets.add(masks)
assert len(all_nets)==8
assert all(len(n)==7 for n in all_nets)
# Each of the 7 possible nonzero rational linear evaluations has four
# geometrically smooth, tangent-filling cubic lifts; those 28 forms are
# precisely the possible members of the eight nets.
for output in product([0,1],repeat=3):
 if output==(0,0,0):continue
 base=(1 if output[0] else 0)^(64 if output[1] else 0)^(512 if output[2] else 0)
 lifts=[base^kernel(i) for i in range(8)]
 assert sum(is_smooth(m) and is_tangent_filling(m) for m in lifts)==4
print(json.dumps({'splittings_examined':512,'all_tangent_filling_nets_with_linear_evaluation':len(all_nets),
                  'all_net_mask_sets':sorted([sorted(s) for s in all_nets]),
                  'four_good_lifts_per_nonzero_linear_evaluation':True},sort_keys=True,indent=2))
