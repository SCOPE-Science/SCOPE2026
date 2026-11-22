"""Exact rational dihedral character certificate for the perfect-matching complex of the 4x4 grid.
Run: python3 CHECKER.py. Requires Python 3 and SymPy. All data generated here.
"""
import itertools,collections,math
R=C=4
V=tuple(range(R*C)); E=[]
for r in range(R):
 for c in range(C):
  if r+1<R:E.append((r*C+c,(r+1)*C+c))
  if c+1<C:E.append((r*C+c,r*C+c+1))
nei=collections.defaultdict(list)
for j,(a,b) in enumerate(E):nei[a].append((b,j));nei[b].append((a,j))
def rec(rem,edges):
 if not rem:
  yield tuple(sorted(edges));return
 a=min(rem)
 for b,j in nei[a]:
  if b in rem:
   yield from rec(rem-{a,b},edges+(j,))
facets=list(set(rec(set(V),())))
faces={0};
for F in facets:
 for k in range(len(F)+1):
  for S in itertools.combinations(F,k):
   m=sum(1<<i for i in S);faces.add(m)
bydim=collections.defaultdict(list)
for s in faces:bydim[s.bit_count()-1].append(s)
print('facets',len(facets),'faces',len(faces),'f',[(i,len(x)) for i,x in sorted(bydim.items())]);print('red euler',sum((-1)**i*len(x) for i,x in bydim.items()))
from collections import defaultdict,deque
import sympy as sp
NV=len(E)
def boundary(s):
 out={};idx=0
 for j in range(NV):
  if s>>j&1:
   f=s^(1<<j)
   if f:out[f]=1 if idx%2==0 else -1
   idx+=1
 return out
up=defaultdict(set)
for s in faces:
 if s==0:continue
 for f in boundary(s):up[f].add(s)
active=set(faces)-{0};queue=deque(f for f,ups in up.items() if len(ups)==1)
steps=[]
while queue:
 a=queue.popleft()
 if a not in active:continue
 ups=up[a]&active
 if len(ups)!=1:continue
 b=next(iter(ups))
 if b not in active or b.bit_count()!=a.bit_count()+1:continue
 bb=boundary(b);sgn=bb[a];steps.append((a,b,sgn,bb))
 for h in (a,b):
  active.remove(h)
  for f in boundary(h):
   up[f].remove(h)
   if len(up[f])==1:queue.append(f)
assert len(steps)==2603 and len(active)==200
print('collapse pairs',len(steps),'active',len(active))
D2=sorted(s for s in active if s.bit_count()==3);D3=sorted(s for s in active if s.bit_count()==4)
mat=sp.zeros(len(D2),len(D3));rows={x:i for i,x in enumerate(D2)}
for j,s in enumerate(D3):
 for f,v in boundary(s).items():
  if f in rows:mat[rows[f],j]=v
assert len(D3)==35 and len(D2)==85
# Exact rational verification of the remaining boundary ranks.
D0=sorted(s for s in active if s.bit_count()==1)
D1=sorted(s for s in active if s.bit_count()==2)
def boundary_matrix(lower,upper):
 row={x:i for i,x in enumerate(lower)}; M=sp.zeros(len(lower),len(upper))
 for j,s in enumerate(upper):
  for f,coeff in boundary(s).items():
   if f in row:M[row[f],j]=coeff
 return M
M1=boundary_matrix(D0,D1)
M2=boundary_matrix(D1,D2)
assert M1*M2==sp.zeros(len(D0),len(D2))
assert M2*mat==sp.zeros(len(D1),len(D3))
assert M1.rank()==15 and M2.rank()==49 and mat.rank()==34
print('exact boundary ranks',M1.rank(),M2.rank(),mat.rank())
null=mat.nullspace();print('nullspace',len(null));assert len(null)==1
v=null[0];den=sp.ilcm(*[int(sp.denom(z)) for z in v]);z=[int(x*den) for x in v];gcd=math.gcd(*z);z=[x//gcd for x in z]
print('cycle coefficients',list(zip([x for x,k in zip(D3,z) if k],[k for k in z if k]))[:35]);print('nz',sum(bool(k) for k in z))
# grid symmetry permutations
n=4
transforms={
'e':lambda r,c:(r,c), 'r90':lambda r,c:(c,3-r), 'r180':lambda r,c:(3-r,3-c),'r270':lambda r,c:(3-c,r),
'vflip':lambda r,c:(r,3-c),'hflip':lambda r,c:(3-r,c),'diag':lambda r,c:(c,r),'antidiag':lambda r,c:(3-c,3-r)}
emap={e:i for i,e in enumerate(E)}
def mask_image(s, eperm):
 old=[j for j in range(NV) if s>>j&1];mapped=[eperm[j] for j in old];new=sum(1<<k for k in mapped)
 inversions=sum(mapped[i]>mapped[j] for i in range(len(mapped)) for j in range(i+1,len(mapped)))
 return new,(-1 if inversions%2 else 1)
for name,T in transforms.items():
 eperm=[]
 for aa,bb in E:
  x,y=T(divmod(aa,4)[0],divmod(aa,4)[1]),T(divmod(bb,4)[0],divmod(bb,4)[1])
  a=4*x[0]+x[1];b=4*y[0]+y[1]
  eperm.append(emap[tuple(sorted((a,b)))])
 # reduced Lefschetz via exact fixed face count
 L=-1; cnt=0
 for s in faces:
  if s==0:continue
  ns,orient=mask_image(s,eperm)
  if ns==s:
   L+=(-1)**(s.bit_count()-1)*orient;cnt+=1
 # map the cycle
 chain={s:int(coef) for s,coef in zip(D3,z) if coef}
 mapped=defaultdict(int)
 for s,coef in chain.items():
  ns,sg=mask_image(s,eperm);mapped[ns]+=coef*sg
 chain={s:c for s,c in mapped.items() if c}
 max_terms=0
 for a,b,sgn,bb in steps:
  ca=chain.pop(a,0)
  if ca:
   for f,coef in bb.items():
    if f!=a:
     chain[f]=chain.get(f,0)-ca*sgn*coef
     if not chain[f]:chain.pop(f)
  chain.pop(b,None)
  max_terms=max(max_terms,len(chain))
 if any(s not in active for s in chain):raise Exception('projection bad')
 if any(s.bit_count()!=4 for s in chain):raise Exception('degree bad')
 ratio=None
 for s,coef in zip(D3,z):
  if coef:
   assert chain.get(s,0)%coef==0,(name,s)
   ratio=chain.get(s,0)//coef;break
 assert ratio in (-1,1)
 assert all(chain.get(s,0)==ratio*coef for s,coef in zip(D3,z)), name
 expected={'e':(5406,1,1,2),'r90':(6,1,-1,0),'r180':(86,-3,1,-2),'r270':(6,1,-1,0),'vflip':(214,-1,1,0),'hflip':(214,-1,1,0),'diag':(6,1,-1,0),'antidiag':(6,1,-1,0)}
 assert (cnt,L,ratio,L+ratio)==expected[name],(name,cnt,L,ratio,L+ratio)
 print(name,'fixed',cnt,'redL',L,'H3tr',ratio,'H2tr',L+ratio,'maxterms',max_terms)
print('DIHEDRAL_PERFECT_MATCHING_4X4_OK')
