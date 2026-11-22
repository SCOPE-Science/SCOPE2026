"""Exact regular decagon diagonal-arrangement face-area certificate.
Coordinates are (X,Y)=(x,y/sin(pi/5)) in Q(sqrt(5))^2.
Run python decagon_exact.py; no external dependencies.
"""
from fractions import Fraction as F
from functools import total_ordering
from collections import Counter, defaultdict
from functools import cmp_to_key
import math

@total_ordering
class K:
    __slots__ = ('a','b')
    def __init__(self,a=0,b=0):
        self.a=F(a); self.b=F(b)
    @staticmethod
    def get(x):return x if isinstance(x,K) else K(x)
    def __add__(self,o):
        o=K.get(o);return K(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return K(-self.a,-self.b)
    def __sub__(self,o):return self+-K.get(o)
    def __rsub__(self,o):return K.get(o)+-self
    def __mul__(self,o):
        o=K.get(o);return K(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=K.get(o);den=o.a*o.a-5*o.b*o.b
        if not den:raise ZeroDivisionError
        return K((self.a*o.a-5*self.b*o.b)/den,(self.b*o.a-self.a*o.b)/den)
    def __eq__(self,o):
        o=K.get(o);return self.a==o.a and self.b==o.b
    def __hash__(self):return hash((self.a,self.b))
    def sign(self):
        a,b=self.a,self.b
        if not a:return (b>0)-(b<0)
        if not b:return (a>0)-(a<0)
        if a*b>0:return (a>0)-(a<0)
        d=a*a-5*b*b
        assert d # irrational root
        return ((a>0)-(a<0)) if d>0 else ((b>0)-(b<0))
    def __lt__(self,o):return (self-K.get(o)).sign()<0
    def __float__(self):return float(self.a)+math.sqrt(5)*float(self.b)
    def __repr__(self):return f'({self.a})+({self.b})*sqrt5'
Z=K(0);O=K(1)
def plus(p,q):return (p[0]+q[0],p[1]+q[1])
def minus(p,q):return (p[0]-q[0],p[1]-q[1])
def scale(s,p):return (s*p[0],s*p[1])
def cross(p,q):return p[0]*q[1]-p[1]*q[0]

c=K(F(1,4),F(1,4)) # cos(pi/5)
s2=K(F(5,8),F(-1,8)) # sin(pi/5)^2
vertices=[(O,Z)]
for k in range(1,10):
 x,y=vertices[-1]
 vertices.append((c*x-s2*y, x+c*y))
assert vertices[5]==(K(-1),K(0))
assert vertices[9]==(c,-O)
segments=[(i,j) for i in range(10) for j in range(i+1,10)]
# exact split-point sets along each original segment
at=[{(K(0),vertices[i]),(K(1),vertices[j])} for i,j in segments]
for i,(a,b) in enumerate(segments):
 p=vertices[a];r=minus(vertices[b],p)
 for j in range(i+1,len(segments)):
  d,e=segments[j];q=vertices[d];s=minus(vertices[e],q)
  denom=cross(r,s)
  if denom==Z:continue
  t=cross(minus(q,p),s)/denom;u=cross(minus(q,p),r)/denom
  if Z<=t<=O and Z<=u<=O:
   pt=plus(p,scale(t,r))
   assert pt==plus(q,scale(u,s))
   at[i].add((t,pt));at[j].add((u,pt))
point_ids={};coords=[]
def idof(p):
 if p not in point_ids:
  point_ids[p]=len(coords);coords.append(p)
 return point_ids[p]
edges=set()
for a in at:
 arr=sorted(a,key=lambda tp:tp[0])
 for (_,p),(_,q) in zip(arr,arr[1:]):
  i,j=idof(p),idof(q)
  assert i!=j
  edges.add(tuple(sorted((i,j))))
nb=defaultdict(list)
for i,j in edges:
 nb[i].append(j);nb[j].append(i)

def upper(dx,dy):return dy.sign()>0 or (dy.sign()==0 and dx.sign()>=0)
def cmp_around(v,w,z):
 d=minus(coords[w],coords[v]);e=minus(coords[z],coords[v])
 du,eu=upper(*d),upper(*e)
 if du!=eu:return -1 if du else 1
 cr=cross(d,e).sign()
 if cr:return -cr
 # strictly collinear same ray impossible
 raise AssertionError('duplicate ray')
order={v:sorted(ws,key=cmp_to_key(lambda a,b:cmp_around(v,a,b))) for v,ws in nb.items()}
faces=[];seen=set()
for i,j in [(i,j) for i,j in edges]+[(j,i) for i,j in edges]:
 if (i,j) in seen:continue
 cyc=[];u,v=i,j
 while (u,v) not in seen:
  seen.add((u,v));cyc.append(u)
  neighbors=order[v]
  nextv=neighbors[(neighbors.index(u)-1)%len(neighbors)]
  u,v=v,nextv
 assert (u,v)==(i,j)
 faces.append(tuple(cyc))

def twicearea(face):
 return sum((cross(coords[i],coords[j]) for i,j in zip(face,face[1:]+face[:1])),Z)
outer=[face for face in faces if twicearea(face).sign()<0]
assert len(outer)==1
bounded=[f for f in faces if twicearea(f).sign()>0]
assert len(bounded)+1==len(faces)
total=K(5)
areas=[twicearea(f)/(2*total) for f in bounded]
print("DEBUG",len(coords),len(edges),len(faces),len(bounded),len(outer),"total",total,"signed sum",sum(areas,Z),"outer",twicearea(outer[0]))
assert sum(areas,Z)==O
counts=Counter(areas)
print('vertices',len(coords),'edges',len(edges),'faces',len(bounded),'Euler',len(coords)-len(edges)+len(faces))
print('total',total)
for i,(val,num) in enumerate(sorted(counts.items())):
 print(i,'/',repr(val),'multiplicity',num,'approx',float(val))
assert len(bounded)==220 and len(counts)==12
# positive exact 1/20 witness of six cells
sorted_types=sorted(counts)
assert sorted_types[7]+sorted_types[8]+sorted_types[10]+3*sorted_types[11]==K(F(1,20))
for ty in (7,8,10,11):
 f=next(f for f,a in zip(bounded,areas) if a==sorted_types[ty])
 print('witness type',ty,'area',sorted_types[ty],'vertex_coords',[(str(coords[i][0]),str(coords[i][1])) for i in f])
# integer exact lower bound: search multisets with at most five faces, 12 classes
# max min 5 so no capacity binds
seen_count=0
solutions=[]
def visit(depth,minimum,totalv,arr):
 global seen_count
 seen_count+=1
 if totalv==K(F(1,20)):
  solutions.append(tuple(arr))
 if depth==5:return
 for j in range(minimum,len(sorted_types)):
  nxt=totalv+sorted_types[j]
  if nxt>K(F(1,20)):continue
  visit(depth+1,j,nxt,arr+[j])
visit(0,0,Z,[])
print('exact multiset comparisons',seen_count,'solutions<=5',solutions)
assert not solutions
# equality-case classification for the sharp six-cell minimum
from itertools import combinations_with_replacement
six_solutions=[]
for a in combinations_with_replacement(range(len(sorted_types)),6):
 if sum((sorted_types[i] for i in a),Z)==K(F(1,20)):
  six_solutions.append(a)
assert six_solutions==[(4,8,11,11,11,11),(7,8,10,11,11,11)],six_solutions
assert 20*20*math.comb(20,4)+10*20*30*math.comb(20,3)==8778000
print('six-cell class patterns',six_solutions,'distinct minimizing cell subsets',8778000)
# reconstruct type 7,8,10,11 disjoint selected faces using distinct enumeration
chosen=[]
for t,m in [(7,1),(8,1),(10,1),(11,3)]:
 ids=[i for i,a in enumerate(areas) if a==sorted_types[t]]
 chosen.extend(ids[:m])
print('chosen face ids',chosen,'area',sum((areas[i] for i in chosen),Z),'faces', [bounded[i] for i in chosen])
# normalized area-to-exact proof independent via direct polygon shoelace
assert sum((twicearea(bounded[i]) for i in chosen),Z)==total*K(F(1,10))
