"""Independent lattice reflection proof-check for quartic del Pezzo chambers.
Run with Python 3, standard library only.
"""
from collections import Counter
from itertools import combinations

N=5
H=(1,0,0,0,0,0)
E=[(0,)+tuple(int(i==j) for j in range(N)) for i in range(N)]
def plus(x,y):return tuple(a+b for a,b in zip(x,y))
def minus(x,y):return tuple(a-b for a,b in zip(x,y))
def times(c,x):return tuple(c*a for a in x)
def intersection(x,y):return x[0]*y[0]-sum(x[i]*y[i] for i in range(1,6))
AK=plus(times(3,H),times(-1,tuple(sum(e[i] for e in E) for i in range(6))))
# Sixteen (-1)-curve classes: exceptional divisors, lines, conic.
curves=E+[minus(minus(H,E[i]),E[j]) for i,j in combinations(range(N),2)]+[minus(times(2,H),tuple(sum(e[i] for e in E) for i in range(6)))]
assert len(curves)==16 and len(set(curves))==16
assert all(intersection(c,c)==-1 and intersection(c,AK)==1 for c in curves)
# Ten conic classes in five complementary pairs.
conics=[]
for i in range(N):
 a=minus(H,E[i]); b=minus(AK,a)
 conics.extend([a,b])
assert all(intersection(c,c)==0 and intersection(c,AK)==2 for c in conics)
assert len(set(conics))==10
ci={c:i for i,c in enumerate(curves)}; qi={c:i for i,c in enumerate(conics)}

def swap_generator(j):
 def f(D):
  a=list(D);a[1+j],a[2+j]=a[2+j],a[1+j];return tuple(a)
 return f
r=minus(minus(minus(H,E[0]),E[1]),E[2])
assert intersection(r,r)==-2 and intersection(r,AK)==0
def cremonaref(D):return plus(D,times(intersection(D,r),r))
generators=[swap_generator(j) for j in range(4)]+[cremonaref]
gens=[]
for f in generators:
 a=tuple(ci[f(c)] for c in curves)
 b=tuple(qi[f(q)] for q in conics)
 assert sorted(a)==list(range(16)) and sorted(b)==list(range(10))
 gens.append((a,b))

def compose(a,b):return tuple(a[b[i]] for i in range(len(b)))
identity=(tuple(range(16)),tuple(range(10)))
seen={identity[0]:identity[1]};front=[identity]
for p,q in front:
 for gp,gq in gens:
  np,nq=compose(gp,p),compose(gq,q)
  if np not in seen:
   seen[np]=nq;front.append((np,nq))
  else: assert seen[np]==nq
assert len(seen)==1920

# Algebraic intersection graph, with no Hamming-distance construction.
int_edges={(i,j) for i in range(16) for j in range(i+1,16) if intersection(curves[i],curves[j])==1}
assert len(int_edges)==40
assert all(intersection(curves[i],curves[j]) in (0,1) for i in range(16) for j in range(i+1,16))
S=[]
for b in range(1<<16):
 if all(not ((b>>i&1) and (b>>j&1)) for i,j in int_edges):S.append(b)
assert Counter(v.bit_count() for v in S)==Counter({0:1,1:16,2:80,3:160,4:120,5:16})
Sset=set(S)

def signed_type(q):
 seen_pairs=set();cycs=[]
 for i in range(5):
  if i in seen_pairs: continue
  j=i; neg=0;length=0
  while j not in seen_pairs:
   seen_pairs.add(j);a=q[2*j];
   assert q[2*j+1]==(a^1)
   neg^=(a&1);length+=1;j=a//2
  assert j==i
  cycs.append((length,neg))
 return tuple(sorted(cycs,reverse=True))

def image_support(s,p):
 out=0
 while s:
  b=s&-s;out|=1<<p[b.bit_length()-1];s^=b
 return out

def profile(p):
 seen=set();orbits=Counter();fixed=Counter()
 for s in S:
  if s in seen:continue
  t=s;m=0
  while t not in seen:
   seen.add(t);m+=1;t=image_support(t,p)
  assert t==s
  orbits[m]+=1
  if m==1:fixed[s.bit_count()]+=1
 assert len(seen)==393
 return tuple(sorted(orbits.items())),tuple(sorted(fixed.items()))

bytype={};sizes=Counter()
for p,q in seen.items():
 st=signed_type(q);v=profile(p);sizes[st]+=1
 if st in bytype:assert bytype[st]==v
 else:bytype[st]=v
assert len(bytype)==18
assert sum(sizes.values())==1920
assert len({prof for prof,_ in bytype.values()})>=15

# These are independently recorded expected invariant profiles.
expected={
 '5+':(384,3,{1:3,5:78}),
 '4- 1-':(240,1,{1:1,8:49}),
 '4+ 1+':(240,7,{1:7,2:13,4:90}),
 '3- 2-':(160,1,{1:1,2:1,4:6,6:3,12:29}),
 '3- 1- 1+':(160,1,{1:1,2:13,6:61}),
 '3+ 2+':(160,11,{1:11,2:8,3:32,6:45}),
 '3+ 1- 1-':(80,3,{1:3,2:12,3:6,6:58}),
 '3+ 1+ 1+':(80,27,{1:27,3:122}),
 '2- 2- 1+':(60,1,{1:1,4:98}),
 '2- 2+ 1-':(120,3,{1:3,2:9,4:93}),
 '2- 1- 1- 1-':(20,1,{1:1,2:10,4:93}),
 '2- 1- 1+ 1+':(60,5,{1:5,2:8,4:93}),
 '2+ 2+ 1+':(60,33,{1:33,2:180}),
 '2+ 1- 1- 1+':(60,7,{1:7,2:193}),
 '2+ 1+ 1+ 1+':(20,107,{1:107,2:143}),
 '1- 1- 1- 1- 1+':(5,1,{1:1,2:196}),
 '1- 1- 1+ 1+ 1+':(10,21,{1:21,2:186}),
 '1+ 1+ 1+ 1+ 1+':(1,393,{1:393})
}
assert len(expected)==18
for st,(orbs,fixed) in bytype.items():
 name=' '.join(str(d)+('-' if neg else '+') for d,neg in st)
 assert name in expected, name
 cls,n,exp=expected[name]
 assert sizes[st]==cls and sum(dict(fixed).values())==n and dict(orbs)==exp,(name,orbs,fixed)
 assert sum(k*v for k,v in orbs)==393
print('GEOMETRIC_REFLECTION_WD5_CHAMBERS_VERIFIED_OK')
print('group=1920 classes=18 chambers=393')
