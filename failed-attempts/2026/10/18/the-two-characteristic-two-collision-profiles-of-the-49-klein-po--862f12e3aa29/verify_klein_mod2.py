"""Exact certificate for reduction of Klein line intersections at both primes over 2."""
from collections import Counter,defaultdict
from itertools import combinations
Z=(0,0);U=(1,0);N=(-1,0);W=(0,1)
L=[
[U,Z,Z],[Z,U,U],[W,U,N],[W,N,U],[Z,N,U],
[U,W,N],[W,N,N],[N,U,W],[W,U,U],[N,W,U],
[N,N,W],[U,Z,U],[N,W,N],[U,W,U],[N,Z,U],
[U,N,W],[U,U,W],[Z,Z,U],[N,U,Z],[U,U,Z],[Z,U,Z]]
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def mul(a,b):return(a[0]*b[0]-2*a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def norm(a):return a[0]*a[0]-a[0]*a[1]+2*a[1]*a[1]
def cross(a,b):return [sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0]))]
def iszero(a):return all(norm(v)==0 for v in a)
def dot(a,b):return add(add(mul(a[0],b[0]),mul(a[1],b[1])),mul(a[2],b[2]))
points=defaultdict(list)
for i,j in combinations(range(21),2):
 v=cross(L[i],L[j])
 assert not iszero(v)
 incident=tuple(t for t in range(21) if norm(dot(L[t],v))==0)
 assert i in incident and j in incident
 points[incident].append(v)
# Triple-determinant norm census: every nonzero determinant is a 2-unit.
detnorm=Counter(norm(dot(L[k],cross(L[i],L[j]))) for i,j,k in combinations(range(21),3))
assert detnorm==Counter({0:112,1:169,2:228,4:271,8:320,16:156,32:70,64:4})
assert sum(detnorm.values())==1330
print('all triple determinant norms:',sorted(detnorm.items()))
assert len(points)==49
assert Counter(map(len,points))==Counter({3:28,4:21})
assert sorted(len(v) for v in points.values())==sorted([3]*28+[6]*21)
for reps in points.values():
 for a,b in combinations(reps,2):assert iszero(cross(a,b))

def reduce(v, root):
 # root=2 or 5 solves t^2+t+2=0 mod8 and lifts uniquely to Z_2.
 nums=[(a+b*root)%8 for a,b in v]
 vs=[next((j for j in range(3) if (n%(2**(j+1))) != 0),3) for n in nums]
 j=min(vs)
 assert j<=2
 out=tuple((n//(2**j))%2 for n in nums)
 assert any(out)
 return out,j
for root,expected in [
 (2,[(0,1,1,2,0),(0,1,0,1,4),(0,0,1,1,4),(1,1,1,12,16),(1,0,0,1,4),(1,0,1,2,0),(1,1,0,2,0)]),
 (5,[(0,1,1,6,8),(0,1,0,1,0),(0,0,1,1,0),(1,0,0,1,0),(1,1,1,0,4),(1,1,0,6,8),(1,0,1,6,8)])
]:
 groups=defaultdict(list); hist=Counter()
 line_groups=Counter(tuple((a+b*root)&1 for a,b in line) for line in L)
 assert sorted(line_groups.values())==([1,1,1,6,6,6] if root==2 else [1,1,1,2,2,2,12])
 for incident,reps in points.items():
  red,v=reduce(reps[0],root)
  assert all(reduce(rep,root)[0]==red for rep in reps)
  groups[red].append(len(incident));hist[v]+=1
 actual=sorted((*p,m.count(4),m.count(3)) for p,m in groups.items())
 assert actual==sorted(expected),(root,actual)
 assert sum(len(m) for m in groups.values())==49
 assert sum(q+tr for *p,q,tr in actual)==49
 print('prime ω mod 2 =',root%2,'profile (x,y,z;quadruple,triple):',actual,'valuation histogram:',hist)
print('PASS 49 distinct geometric intersection sections; exact 2-adic profiles')
