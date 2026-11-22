"""Exact verifier for invariant Zariski-chamber supports on the one-nodal quartic del Pezzo resolution.

Uses only Python 3 standard library and integer arithmetic. Constructs Picard classes, W(D5),
the A3 x A1 root stabilizer, and negative-definite support masks. The brute-force
Bareiss determinant test and Schur support rule are independent checks.
"""
from itertools import permutations
from collections import Counter,defaultdict
H=(1,0,0,0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def e(i):return tuple(1 if j==i else 0 for j in range(6))
def minus(a,b):return add(a,neg(b))
def mul(a,n):return tuple(n*x for x in a)
def dot(a,b):return a[0]*b[0]-sum(a[i]*b[i] for i in range(1,6))
R=minus(minus(minus(H,e(1)),e(2)),e(3))
roots=[minus(e(i),e(i+1)) for i in range(1,5)]+[R]
assert all(dot(r,r)==-2 for r in roots)
def refl(v,r):return add(v,mul(r,dot(v,r)))
Id=tuple(e(i) for i in range(6))
seen={Id};todo=[Id]
for st in todo:
 for r in roots:
  ss=tuple(refl(x,r) for x in st)
  if ss not in seen:
   seen.add(ss);todo.append(ss)
assert len(seen)==1920

def act(v,st):return tuple(sum(v[i]*st[i][j] for i in range(6)) for j in range(6))
stabilizer=[st for st in todo if act(R,st)==R]

assert len(stabilizer)==48
C=[('R',R)]+[('E'+str(i),e(i)) for i in range(1,6)]+[(f'L{i}{j}',minus(minus(H,e(i)),e(j))) for i in range(1,6) for j in range(i+1,6) if (i,j) not in [(1,2),(1,3),(2,3)]]
assert len(C)==13
assert [dot(v,v) for name,v in C]==[-2]+[-1]*12
A=[[dot(C[i][1],C[j][1]) for j in range(13)] for i in range(13)]
assert all(A[i][j] in [0,1] for i in range(13) for j in range(13) if i!=j)
# determinant via Bareiss; good for n<=13
def det(B):
 n=len(B)
 if n==0:return 1
 b=[r[:] for r in B]; sign=1; prev=1
 for k in range(n-1):
  if b[k][k]==0:
   for j in range(k+1,n):
    if b[j][k]:b[k],b[j]=b[j],b[k];sign=-sign;break
   else:return 0
  piv=b[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    x=b[i][j]*piv-b[i][k]*b[k][j]
    assert x%prev==0,(x,prev)
    b[i][j]=x//prev
   b[i][k]=0
  prev=piv
 return sign*b[n-1][n-1]
nd={0}
for m in range(1,1<<13):
 i=m.bit_length()-1;n=m^(1<<i)
 if n not in nd:continue
 ids=[i for i in range(13) if m>>i&1]
 d=det([[A[a][b] for b in ids] for a in ids]);
 if d*(-1)**len(ids)>0:nd.add(m)
assert Counter(m.bit_count() for m in nd)==Counter({0:1,1:13,2:58,3:112,4:87,5:14})
assert len(nd)==285
# index curve perms; permutation induced by all root-stabilizing W elements
pos={v:i for i,(name,v) in enumerate(C)}
perms=[]
for st in stabilizer:
 perm=tuple(pos[act(v,st)] for name,v in C)
 assert set(perm)==set(range(13));perms.append(perm)
assert len(set(perms))==48

def comp(p,q):return tuple(p[q[i]] for i in range(13))
def inv(p):return tuple(p.index(i) for i in range(13))
def cmask(mask,p):return sum(1<<p[i] for i in range(13) if mask>>i & 1)
# Explicit W(A3) x W(A1) labels for stabilizer of R
alpha=[minus(e(1),e(2)),minus(e(2),e(3)),minus(minus(minus(H,e(1)),e(4)),e(5))]
beta=minus(e(4),e(5))
alpha=[alpha[1],alpha[0],alpha[2]]
assert all(dot(R,a)==0 for a in alpha+[beta])
assert [dot(alpha[i],alpha[j]) for i in range(3) for j in range(i+1,3)]==[1,0,1]
assert all(dot(a,beta)==0 for a in alpha)
simple=alpha+[beta]
prev={Id:((0,1,2,3),0)}
todo=[Id]
for st in todo:
 p,z=prev[st]
 for i,r in enumerate(simple):
  ss=tuple(refl(x,r) for x in st)
  if i<3:
   trans=list(range(4));trans[i],trans[i+1]=trans[i+1],trans[i]
   pp=tuple(trans[p[j]] for j in range(4));zz=z
  else:pp=p;zz=z^1
  if ss not in prev:prev[ss]=(pp,zz);todo.append(ss)
  else:assert prev[ss]==(pp,zz)
assert len(prev)==48 and set(prev)==set(stabilizer)
def cyc(p):
 seen=set();sizes=[]
 for i in range(4):
  if i in seen:continue
  j=i;s=0
  while j not in seen:seen.add(j);j=p[j];s+=1
  sizes.append(s)
 return tuple(sorted(sizes,reverse=True))
classified={}
for st in stabilizer:
 key=(cyc(prev[st][0]),prev[st][1]);p=tuple(pos[act(v,st)] for name,v in C)
 ct=Counter(m.bit_count() for m in nd if cmask(m,p)==m)
 poly=tuple(ct.get(i,0) for i in range(6))
 if key in classified:
  assert classified[key][0]==poly
  classified[key]=(poly,classified[key][1]+1)
 else:classified[key]=(poly,1)


# Independent combinatorial test: (-1)-curves in a support are disjoint;
# with the (-2)-curve R at most one of its four incident (-1)-curves is chosen.
def admissible_by_schur(m):
    if any((m>>i&1) and (m>>j&1) and A[i][j] for i in range(1,13) for j in range(i+1,13)):
        return False
    if (m & 1) and sum((m>>i)&1 for i in (1,2,3,12))>1:
        return False
    return True
independent={m for m in range(1<<13) if admissible_by_schur(m)}
assert independent==nd
expected={
 ((1,1,1,1),0):(1,(1,13,58,112,87,14)),
 ((1,1,1,1),1):(1,(1,5,14,20,25,4)),
 ((2,1,1),0):(6,(1,7,18,26,27,8)),
 ((2,1,1),1):(6,(1,3,6,6,5,2)),
 ((2,2),0):(3,(1,1,6,4,7,2)),
 ((2,2),1):(3,(1,1,2,0,1,0)),
 ((3,1),0):(8,(1,4,4,4,9,5)),
 ((3,1),1):(8,(1,2,2,2,1,1)),
 ((4,),0):(6,(1,1,0,0,3,2)),
 ((4,),1):(6,(1,1,0,0,1,0)),
}
assert {key:(size,poly) for key,(poly,size) in classified.items()}==expected
assert sum(size*sum(poly) for size,poly in expected.values())==48*30

# Independently enumerate the orbits of the 48-element action on all 285 supports.
left=set(nd)
orbits=[]
while left:
    m=next(iter(left))
    orbit={cmask(m,p) for p in perms}
    assert orbit <= left
    left-=orbit
    orbits.append((m.bit_count(),len(orbit)))
assert len(orbits)==30 and not left
assert sum(size for degree,size in orbits)==285
expected_orbit_sizes={
  0:[1],1:[1,4,8],2:[4,4,6,8,12,24],
  3:[4,4,8,12,12,24,24,24],
  4:[1,2,8,8,8,12,12,12,24],5:[2,4,8],
}
assert all(sorted(size for degree,size in orbits if degree==k)==v for k,v in expected_orbit_sizes.items())
print('NEGATIVE_CURVES=13; GEOMETRIC_CHAMBERS=285; WEYL_STABILIZER=48')
for key,(size,poly) in sorted(expected.items()):
    print('CLASS',key,'SIZE',size,'POLYNOMIAL',poly,'TOTAL',sum(poly))
print('BURNSIDE_ORBITS=30; DIRECT_ORBITS=30')
print('ONE_NODAL_QUARTIC_FROBENIUS_CHAMBER_CLASSIFICATION_OK')
