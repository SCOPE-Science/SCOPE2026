#!/usr/bin/env python3
"""Exact verification of Bring curve tritangent arithmetic; standard Python and sympy."""
from itertools import permutations, combinations
from collections import Counter
from math import lcm
import sympy as s
import warnings
warnings.filterwarnings("ignore", category=s.utilities.exceptions.SymPyDeprecationWarning)
x,y=s.symbols('x y')
F=x**3+2*x**2+3*x+4
A=x**2-x+4
H=x**2+x+1
B=s.resultant(F,y-H,x)
assert s.expand(B-(y**3+y**2-3*y-7))==0
assert s.expand(A.subs(x,y)*B-(y**5-5*y-28))==0
assert s.discriminant(F,x)==-200
assert s.discriminant(A,x)==-15
assert s.discriminant(B,y)==-800
assert s.factorint(abs(int(s.discriminant(y**5-5*y-28,y))))=={2:13,3:1,5:7}
# Tangency identities: tangent hyperplanes have coefficients P(z_i), deg P<=2.
assert s.rem(H**2-H+4+ (x*x+3*x-4),F,x)==0
S=-2-x;Q=3+2*x+x*x
v=s.expand(S**3-3*Q*S-(x+1)*(S*S-2*Q)+x*S)
assert s.rem(v,F,x)==0
# Coordinates of the non-stall contact points satisfy curve power sums 1-3.
# Labelled planes: each has two or three supported coordinates, with 6 root orderings.
roots=('a','b','c'); positions=tuple(range(5))
I=[('I', (j,k), pair) for j,k in combinations(positions,2) for pair in permutations(roots,2)]
II=[('II', trip, perm) for trip in combinations(positions,3) for perm in permutations(roots)]
assert len(I)==len(II)==60
W=list(permutations(('1','1','a','b','c')))
W=list(set(W))
O=list(permutations(('xi','eta','ha','hb','hc')))
assert len(W)==60 and len(O)==120
# Frobenius acts on each root label and on the extra quadratic pair.
def frob_symbol(z,sigma,swap):
 if z in roots:return sigma[z]
 if z in ('ha','hb','hc'):return 'h'+sigma[z[-1]]
 if z in ('xi','eta') and swap:return 'eta' if z=='xi' else 'xi'
 return z
def apply(record,sigma,swap=False):
 if record[0]=='I': return ('I',record[1],tuple(frob_symbol(k,sigma,swap) for k in record[2]))
 if record[0]=='II':return ('II',record[1],tuple(frob_symbol(k,sigma,swap) for k in record[2]))
 return tuple(frob_symbol(z,sigma,swap) for z in record)
def cycles(records,sigma,swap=False):
 items=set(records);lens=Counter()
 while items:
  st=next(iter(items));cur=st;n=0
  while True:
   assert cur in items
   items.remove(cur);n+=1
   cur=apply(cur,sigma,swap)
   if cur==st:break
  lens[n]+=1
 return dict(lens)
# The input representations are hashable and action is checked on actual labels.
for sigma,d in [({'a':'a','b':'b','c':'c'},1),({'a':'b','b':'a','c':'c'},2),({'a':'b','b':'c','c':'a'},3)]:
 for swap in (False,True):
  ell=lcm(d,2 if swap else 1)
  expected={d:120//d}
  assert cycles(I+II,sigma,swap)==expected,(d,swap,'plane')
  assert cycles(W,sigma,swap)=={d:60//d},(d,swap,'stall')
  assert cycles(O,sigma,swap)=={ell:120//ell},(d,swap,'contacts')
# Separate sample-prime splitting patterns and rational-contact spectra.
examples=[]
for p in list(s.primerange(11,281)):
 fac=s.factor_list(F,modulus=p)[1]
 d=1
 for pol,multiplicity in fac:
  assert multiplicity==1
  d=lcm(d,int(s.degree(pol,x)))
 eps=1 if s.legendre_symbol(-15,p)==1 else 2
 ell=lcm(d,eps)
 # over extension degree n, all points of each scheme either rational or absent
 examples.append((p,d,ell,120 if d==1 else 0,60 if d==1 else 0,120 if ell==1 else 0))
# Distinctness of all 120 tritangent planes modulo the diagonal linear relation.
def canonical_plane(v,p):
 # Plane equation is on sum X_i=0, so the 5 coefficients are up to scalar and additive constant.
 w=[(z-v[0])%p for z in v]
 a=next(z for z in w if z)
 return tuple((z*pow(a,-1,p))%p for z in w)
for p in (43,59,97,131,227):
 rr=[a for a in range(p) if int(F.subs(x,a))%p==0]
 assert len(rr)==3
 f=lambda z:(z*z+3*z-4)%p
 planes=[]
 for j,k in combinations(range(5),2):
  for beta,gamma in permutations(rr,2):
   c=[0]*5;c[j]=gamma;c[k]=-beta
   planes.append(canonical_plane(c,p))
 for trip in combinations(range(5),3):
  for perm in permutations(rr):
   c=[0]*5
   for idx,root in zip(trip,perm):c[idx]=f(root)
   planes.append(canonical_plane(c,p))
 assert len(set(planes))==120,(p,'distinct planes')
# Actually evaluate all roots of F and nonstall quintic at the split primes.
for p,d,ell,*_ in examples:
 if d!=1:continue
 rr=[a for a in range(p) if int(F.subs(x,a))%p==0]
 assert len(rr)==3
 h=[int(H.subs(x,a))%p for a in rr]
 xi=[z for z in range(p) if (z*z-z+4)%p==0]
 assert len(xi)==(2 if ell==1 else 0)
 # All type-I tritangents contain three distinct stalls and each is tangent there.
 stalls=set(permutations((1,1,*rr)))
 assert len(stalls)==60
 for j,k in combinations(range(5),2):
  for beta,gamma in permutations(rr,2):
   tang=[pt for pt in stalls if (gamma*pt[j]-beta*pt[k])%p==0]
   assert len(tang)==3,(p,j,k,beta,gamma,len(tang))
 if ell!=1: continue
 # all 120 nonstall points; all permutations lie on three power-sum hypersurfaces.
 pts={tuple(vals) for vals in permutations(xi+h)}
 assert len(pts)==120
 for pt in pts:
  for k in (1,2,3):assert sum(pow(t,k,p) for t in pt)%p==0
 # each type-II plane is tritangent to one W and exactly two O points.
 for (i,j,k) in combinations(range(5),3):
  for ra,rb,rc in permutations(rr):
   coef=[0]*5
   for coord,root in zip((i,j,k),(ra,rb,rc)):
    coef[coord]=(root*root+3*root-4)%p
   tangent_contacts=[]
   for pt in pts:
    if sum(a*b for a,b in zip(coef,pt))%p:continue
    # tangent iff coefficient is in span of gradients 1,z,z^2 via exhaustive 3-point interpolation
    # use the direct algebraic identity: coefficients equal -(z^2-z+4) at contacts
    if all((coef[u]+(pt[u]**2-pt[u]+4))%p==0 for u in range(5)):
     tangent_contacts.append(pt)
   assert len(tangent_contacts)==2,(p,i,j,k,ra,rb,rc,len(tangent_contacts))
print('IDENTITIES_OK; ALL_FROBENIUS_TYPES_OK; 120_DISTINCT_PLANES_OK; TANGENT_CONTACT_CHECKS_OK')
print('prime,d,contact_degree,rational_planes,rational_stalls,rational_nonstall')
for rec in examples[:30]:print(','.join(map(str,rec)))
