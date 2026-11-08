"""Exact finite symbolic checks for a piecewise toral symplectic map.

The manuscript supplies the complete proofs.  This program verifies every
listed affine face/edge identity using rational arithmetic and exact endpoint
bounds, plus a finite regression grid (not an infinite proof).
"""
from fractions import Fraction as Q
from dataclasses import dataclass
from collections import Counter

@dataclass(frozen=True)
class Aff:
    a: Q = Q(0)
    b: Q = Q(0)
    c: Q = Q(0)
    def __add__(self, o):
        if not isinstance(o, Aff): o = Aff(c=Q(o))
        return Aff(self.a+o.a,self.b+o.b,self.c+o.c)
    __radd__ = __add__
    def __neg__(self):return Aff(-self.a,-self.b,-self.c)
    def __sub__(self,o):return self+(-o if isinstance(o,Aff) else -Q(o))
    def __rsub__(self,o):return -self+o
    def eval(self,x=0,y=0):return self.a*Q(x)+self.b*Q(y)+self.c

X=Aff(a=Q(1));Y=Aff(b=Q(1));T=Aff(a=Q(1))

def F(p):
    x,y=p
    force=Q(0) if y<Q(1) else Q(1)-y
    return y,(-x+force)%2

def point_period(p,max_n=10):
    cur=p
    for n in range(1,max_n+1):
        cur=F(cur)
        if cur==p:return n
    return None

# Vertices of eight open triangles in the half-open two-by-two fundamental square.
faces=[
 [(0,0),(1,0),(1,1)],
 [(0,1),(0,2),(1,1)],
 [(1,1),(1,2),(2,1)],
 [(1,0),(1,1),(2,0)],
 [(0,0),(0,1),(1,1)],
 [(0,2),(1,1),(1,2)],
 [(1,1),(2,0),(2,1)],
 [(1,2),(2,1),(2,2)],
]
# First seven faces cycle; the eighth maps to itself.
seq=[(0,2),(1,3),(1,3),(0,2),(0,2),(1,3),(0,2),(1,5)]
assert len(faces)==len(seq)==8
assert sum(abs((v[1][0]-v[0][0])*(v[2][1]-v[0][1])-(v[1][1]-v[0][1])*(v[2][0]-v[0][0])) for v in faces)==8
assert all(abs((v[1][0]-v[0][0])*(v[2][1]-v[0][1])-(v[1][1]-v[0][1])*(v[2][0]-v[0][0]))==1 for v in faces)

for i,(word,c) in enumerate(seq):
    # On each open face, no force or modular-wrapping boundary is crossed.
    pts=faces[i]
    ys=[v[1] for v in pts]
    if word==0:assert max(ys)<=1
    else:assert min(ys)>=1
    raw=[c-x-(y if word else 0) for x,y in pts]
    assert min(raw)>=0 and max(raw)<=2
    mapped={(y,c-x-(y if word else 0)) for x,y in pts}
    assert mapped==set(faces[(i+1)%7] if i<7 else faces[7]),(i,mapped)

# Exact all-point return identities within interiors, not just sample orbits.
def iterate_aff(seq):
    x,y=X,Y
    for word,c in seq:
        x,y=y,Aff(c=Q(c))-x-(y if word else Aff())
    return x,y
assert iterate_aff(seq[:7])==(X,Y)
assert iterate_aff([seq[7]]*3)==(X,Y)

# Canonical parametrizations of the 12 open 1D edges.
keys=[(a,i,j) for a in ('H','V','D') for i in (0,1) for j in (0,1)]
def edge(k,t=T):
    a,i,j=k
    if a=='H':return (t+i,Aff(c=Q(j)))
    if a=='V':return (Aff(c=Q(i)),t+j)
    if (i,j)==(0,0):return (t,t)
    if (i,j)==(0,1):return (t,2-t)
    if (i,j)==(1,0):return (1+t,1-t)
    return (1+t,2-t)

def fedge(p):
    x,y=p
    ya,yb=y.eval(0),y.eval(1)
    assert (max(ya,yb)<=1) or (min(ya,yb)>=1),(x,y)
    use_upper=min(ya,yb)>=1
    raw= -x+(1-y if use_upper else Aff())
    k=-2*(raw.eval(Q(1,2))//2)
    out=raw+k
    assert 0<=out.eval(0)<=2 and 0<=out.eval(1)<=2,(p,out)
    return (y,out)

trans={}
for k in keys:
    im=fedge(edge(k))
    candidates=[(a,s) for a in keys for s in (+1,-1)
       if im==edge(a,T if s==1 else 1-T)]
    assert len(candidates)==1,(k,im,candidates)
    trans[k]=candidates[0]
seen=set();edge_cycles=[]
for k in keys:
    if k in seen:continue
    cur=k;path=[];sign=1
    while cur not in seen:
        seen.add(cur);path.append(cur)
        cur,o=trans[cur];sign*=o
    assert cur==k
    edge_cycles.append((path,sign))
assert sorted((len(p),s) for p,s in edge_cycles)==[(5,-1),(7,1)]

# Vertex values are evaluated under the stipulated half-open convention.
vertex_periods={p:point_period(tuple(map(Q,p))) for p in [(0,0),(1,0),(0,1),(1,1)]}
assert vertex_periods=={(0,0):1,(1,0):2,(0,1):2,(1,1):1}
assert F((Q(5,3),Q(5,3)))==(Q(5,3),Q(5,3))

# Exact sample point from each open triangle, away from its edges and the center.
for i,pts in enumerate(faces):
    v=tuple(sum(Q(pts[j][d]) for j in range(3))/3 for d in (0,1))
    # Triangle 7 centroid equals the unique interior fixed point.
    if i==7:v=(Q(7,4),Q(7,4))
    assert point_period(v)==(3 if i==7 else 7),(i,v,point_period(v))
for path,sgn in edge_cycles:
    for k in path:
        for t in (Q(1,3),Q(1,2),Q(3,5)):
            p=tuple(v.eval(t) for v in edge(k))
            assert point_period(p)==(7 if len(path)==7 else (5 if t==Q(1,2) else 10))

# Extra finite regression on integer rational grid: not a proof of exhaustiveness.
cnt=Counter()
for i in range(64):
    for j in range(64):
        p=(Q(i,32),Q(j,32))
        v=point_period(p)
        assert v in (1,2,3,5,7,10),(p,v)
        cnt[v]+=1
print('PASS: 8 exact whole-face affine maps and exact third/seventh identities')
print('PASS: 12 exact whole-edge affine maps, including endpoint bounds')
print('edge cycles:',[(len(p),s,p) for p,s in edge_cycles])
print('PASS: 4 vertices, 8 face samples, 36 edge samples, 4096-point rational grid')
print('grid counts:',sorted(cnt.items()))
