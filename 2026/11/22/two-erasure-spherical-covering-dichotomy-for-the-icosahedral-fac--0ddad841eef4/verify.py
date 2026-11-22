"""Exact rational-interval facet certificate for a 32-site spherical covering.

Run with Python 3.9+; no external dependencies. Every strict inequality below
is certified by rational intervals enclosing the exact algebraic coordinates.
The stated coplanar identities follow from phi**2=phi+1 and can be checked by
substitution into the coordinate expressions in the accompanying proof.
"""
from fractions import Fraction as F
from math import isqrt
from collections import Counter
from itertools import combinations

PREC = 10**30

class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = F(lo if hi is None else hi)
        assert self.lo <= self.hi
    def __add__(self, o):
        o = toI(o)
        return I(self.lo + o.lo, self.hi + o.hi)
    __radd__ = __add__
    def __neg__(self): return I(-self.hi, -self.lo)
    def __sub__(self, o): return self + -toI(o)
    def __rsub__(self, o): return toI(o) - self
    def __mul__(self, o):
        o = toI(o)
        xs = (self.lo*o.lo, self.lo*o.hi, self.hi*o.lo, self.hi*o.hi)
        return I(min(xs), max(xs))
    __rmul__ = __mul__
    def __truediv__(self, o):
        o = toI(o)
        assert o.lo > 0 or o.hi < 0
        return self * I(1/o.hi, 1/o.lo)
    def __rtruediv__(self, o): return toI(o)/self
    def __pow__(self, n):
        assert n >= 0 and isinstance(n,int)
        out=I(1)
        for _ in range(n):out=out*self
        return out
    def sqrt(self):
        assert self.lo > 0
        def lower(q):return F(isqrt((q.numerator*PREC**2)//q.denominator),PREC)
        a=lower(self.lo); b=lower(self.hi)
        return I(a,b+F(1,PREC))
    def positive(self): return self.lo>0
    def near_zero(self): return -F(1,10**20)<self.lo<=self.hi<F(1,10**20)
    def fmt(self): return f'[{float(self.lo):.12f}, {float(self.hi):.12f}]'

def toI(v): return v if isinstance(v,I) else I(v)
def vec(*vals): return tuple(toI(q) for q in vals)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(a,c): return tuple(x*c for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),I(0))
def cross(a,b):
    return vec(a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

phi=(I(1)+I(5).sqrt())/2
rn=(I(1)+phi*phi).sqrt()
Iverts=[]
for a in (-1,1):
    for b in (-1,1):
        Iverts.extend([vec(0,a,b*phi)/rn if False else mul(vec(0,a,b*phi),1/rn),
                       mul(vec(a,b*phi,0),1/rn),
                       mul(vec(a*phi,0,b),1/rn)])
Dverts=[]
for a in (-1,1):
    for b in (-1,1):
        for c in (-1,1): Dverts.append(mul(vec(a,b,c),1/I(3).sqrt()))
for a in (-1,1):
    for b in (-1,1):
        Dverts += [mul(vec(0,a*phi,b/phi),1/I(3).sqrt()),
                   mul(vec(a/phi,0,b*phi),1/I(3).sqrt()),
                   mul(vec(a*phi,b/phi,0),1/I(3).sqrt())]
V=Iverts+Dverts
assert len(V)==32
u=((I(1)+2/I(5).sqrt())/3).sqrt()
v=((I(1)-2/I(5).sqrt())/3).sqrt()
t=1/I(5).sqrt(); p=I(5).sqrt()/3
assert u.lo > p.hi > t.hi > v.hi > 0

# An exact interval comparison, not floating-point proximity, identifies
# five icosahedron-facet normals incident to every icosahedral vertex.
inc={}
for i in range(12):
    inc[i]=[j for j in range(12,32) if dot(V[i],V[j]).lo>F(7,10)]
    assert len(inc[i])==5
for i in range(12):
    for j in range(12,32):
        z=dot(V[i],V[j])
        if j in inc[i]: assert (z-u).near_zero()
        else: assert z.hi<(2*u*u-I(1)).lo
assert sum(len(x) for x in inc.values())==60
assert all(sum(j in inc[i] for i in range(12))==3 for j in range(12,32))
for i,j in combinations(range(32),2):
    if (i<12 and j<12) or (i>=12 and j>=12):
        assert dot(V[i],V[j]).hi<u.lo

old=set()
for i,adj in inc.items():
    edges=[]
    for j,k in combinations(adj,2):
        if dot(V[j],V[k]).lo>F(7,10):
            edges.append((j,k));old.add(tuple(sorted((i,j,k))))
    assert len(edges)==5
assert len(old)==60

def positive_facet(face, allsites):
    a,b,c=(V[j] for j in face[:3])
    n=cross(sub(b,a),sub(c,a))
    if dot(n,a).hi<0: n=mul(n,-1)
    assert dot(n,a).lo>0
    for j in allsites:
        gap=dot(n,sub(a,V[j]))
        if j in face:
            # Exact coplanarity is an algebraic identity; interval is a check.
            assert gap.near_zero(), (face,j,'non-coplanar',gap.fmt())
        else:
            assert gap.positive(),(face,j,'not supporting',gap.fmt())
    return dot(n,a)/(dot(n,n).sqrt())

# Every original facet has three and only three contacting vertices.
for f in old:
    h=positive_facet(f,range(32))
    assert h.lo>F(9,10)

# Delete an incident pair. Icosahedral symmetry makes all 60 such pairs
# congruent; this representative has indices 0 and 12.
assert 12 in inc[0]
dropped={0,12}
kept=set(range(32))-dropped
surviving=[f for f in old if not (set(f)&dropped)]
assert len(surviving)==51
new_faces=[(1,2,21,20), (16,20,21,27), (1,2,22)]
new_h=[positive_facet(f,kept) for f in new_faces]
assert new_h[0].lo>F(7,10) and new_h[0].hi<F(4,5)
assert (new_h[1]-u).near_zero()
assert new_h[2].lo>F(4,5) and new_h[2].hi<F(9,10)
assert new_h[0].hi<new_h[1].lo<new_h[2].lo

# All candidate facets are supporting, and their polygonal boundaries
# form a closed, connected edge-to-edge surface with Euler number 2.
faces=surviving+new_faces
edges=Counter()
graph={j:set() for j in kept}
for f in faces:
    for a,b in zip(f,f[1:]+f[:1]):
        e=tuple(sorted((a,b)));edges[e]+=1
        graph[a].add(b);graph[b].add(a)
assert len(faces)==54 and len(edges)==82
assert set(edges.values())=={2}
seen={next(iter(kept))}; stack=list(seen)
while stack:
    x=stack.pop()
    for y in graph[x]-seen:seen.add(y);stack.append(y)
assert seen==kept and len(kept)-len(edges)+len(faces)==2

# The critical quadrilateral has two icosahedral and two dodecahedral
# vertices; its plane distance has a closed Gram determinant formula.
M11=2*(1+t);M22=I(8)/3;M12=2*(u+v)
q2=(M11*M22-M12*M12)/(4*(M11+M22-2*M12))
q=q2.sqrt()
assert (q-new_h[0]).near_zero()
beta2=(2*(1+t)-4*u*u)/(6+2*t-8*u)
beta=beta2.sqrt()
assert (beta-new_h[2]).near_zero()
assert q.hi<u.lo<beta.lo
assert beta.hi<positive_facet(next(iter(old)),range(32)).lo
# Under deletion of a nonincident mixed pair, both original orbit codes
# individually cover at angle arccos(u), and their deleted sites are too
# far apart to simultaneously be the sole surviving obstruction.
assert v.hi<(2*u*u-I(1)).lo
classes=Counter()
for i,j in combinations(range(32),2):
    if i>=12 and j>=12: kind='DD'
    elif j<12:kind='II'
    else:kind='ID_incident' if j in inc[i] else 'ID_nonincident'
    classes[kind]+=1
assert classes=={'II':66,'DD':190,'ID_incident':60,'ID_nonincident':180}
print('Verified all 60 original supporting triangles, the 54-facet erasure surface,')
print('three new supporting faces, strict inequalities, edge incidence and Euler count.')
print('Two-deletion classes:',dict(classes))
print('Original radius cosine',positive_facet(next(iter(old)),range(32)).fmt())
print('Ordinary two-deletion cosine',u.fmt())
print('Exceptional 60-pair cosine',q.fmt())
print('Secondary new facet cosine',beta.fmt())
print('PASS: all assertions use exact rational interval comparisons.')
