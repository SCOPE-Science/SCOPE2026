"""Exact Q(sqrt(5)) certificate for regular-dodecahedron central sections.

No third-party packages are required. Run with Python 3.10 or later.
Coordinates are doubled so that every scalar lies in Z[sqrt(5)].
The enumerated spherical cells are exhaustive because every cell touches
an intersection of two of the ten distinct central great circles.
"""
from collections import Counter
from itertools import combinations, product
from math import acos, pi, sqrt

# (a,b) represents the exact real algebraic number a+b*sqrt(5).
def add(x, y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0], -x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def sign(x):
    a,b=x
    if a==0: return (b>0)-(b<0)
    if b==0 or (a>0)==(b>0): return (a>0)-(a<0)
    return ((a>0)-(a<0)) * ((a*a>5*b*b)-(a*a<5*b*b))
def scale(s,x): return x if s==1 else neg(x)
def vecneg(v): return tuple(neg(x) for x in v)
def dot(v,w):
    z=(0,0)
    for a,b in zip(v,w): z=add(z,mul(a,b))
    return z
def cross(u,v):
    return tuple(sub(mul(u[(i+1)%3],v[(i+2)%3]),mul(u[(i+2)%3],v[(i+1)%3])) for i in range(3))

P=[]
for signs in product((-1,1),repeat=3):
    P.append(tuple((2*s,0) for s in signs))
for pos in (((0,0),(-1,1),(1,1)),((-1,1),(1,1),(0,0)),((1,1),(0,0),(-1,1))):
    nonzero=[i for i in range(3) if pos[i]!=(0,0)]
    for s,t in product((-1,1),repeat=2):
        x=list(pos)
        x[nonzero[0]]=scale(s,x[nonzero[0]])
        x[nonzero[1]]=scale(t,x[nonzero[1]])
        P.append(tuple(x))
assert len(P)==20 and len(set(P))==20
assert all(dot(v,v)==(12,0) for v in P)

# Squared edge length in doubled coordinates is 24-8*sqrt(5).
E=[(i,j) for i,j in combinations(range(20),2)
   if dot(tuple(sub(a,b) for a,b in zip(P[i],P[j])),
          tuple(sub(a,b) for a,b in zip(P[i],P[j])))==(24,-8)]
assert len(E)==30
assert Counter(i for i,j in E for i in (i,j)) == Counter({i:3 for i in range(20)})

# One choice from each of ten antipodal vertex pairs.
V=[]
for v in P:
    if v not in V and vecneg(v) not in V: V.append(v)
assert len(V)==10
label=[]
for v in P:
    matches=[(k,s) for k,w in enumerate(V) for s in (-1,1) if v==(w if s==1 else vecneg(w))]
    assert len(matches)==1
    label.append(matches[0])

# Ten great circles meet pairwise transversely; no three concur.
R=[]
for i,j in combinations(range(10),2):
    w=cross(V[i],V[j])
    assert w!=((0,0),)*3
    assert all(sign(dot(v,w))!=0 for k,v in enumerate(V) if k not in (i,j))
    for eps in (-1,1): R.append((i,j,w if eps==1 else vecneg(w)))
assert len(R)==90

# Every spherical chamber incident to a great-circle intersection is found
# by making the two vanishing dot products independently positive or negative.
patterns=set()
for i,j,w in R:
    fixed=[sign(dot(v,w)) for v in V]
    assert fixed[i]==fixed[j]==0
    for si,sj in product((-1,1),repeat=2):
        signs=list(fixed)
        signs[i]=si; signs[j]=sj
        patterns.add(tuple(signs))
assert len(patterns)==92

classification=Counter()
angle_histograms={}
for sigma in patterns:
    vertices=[]
    for i,j,w in R:
        if all(sigma[k]*sign(dot(V[k],w))>=0 for k in range(10)):
            vertices.append((i,j))
    # All candidate rays are distinct. Exactly two facet circles meet there.
    k=len(vertices)
    assert k>=3
    sides=sum((sigma[label[a][0]]*label[a][1]) !=
              (sigma[label[b][0]]*label[b][1]) for a,b in E)
    assert sides in (6,8,10)
    classification[(sides,k)]+=1
    args=Counter(scale(-sigma[i]*sigma[j],dot(V[i],V[j])) for i,j in vertices)
    angle_histograms.setdefault((sides,k),args)
    assert angle_histograms[(sides,k)]==args

assert classification==Counter({(6,6):20,(8,3):60,(10,5):12})
assert angle_histograms[(6,6)]==Counter({(-4,0):3,(0,-4):3})
assert angle_histograms[(8,3)]==Counter({(4,0):2,(0,4):1})
assert angle_histograms[(10,5)]==Counter({(-4,0):5})

alpha=acos(1/3)
beta=acos(sqrt(5)/3)
areas={6:2*pi-3*alpha-3*beta,8:2*alpha+beta-pi,10:2*pi-5*alpha}
probs={6:20*areas[6]/(4*pi),8:60*areas[8]/(4*pi),10:12*areas[10]/(4*pi)}
assert all(p>0 for p in probs.values())
assert abs(sum(probs.values())-1)<1e-13
assert abs(sum(k*p for k,p in probs.items())-30*beta/pi)<1e-13
for sides in (6,8,10):
    print('section_sides=',sides,'chambers=',classification[(sides,{6:6,8:3,10:5}[sides])],
          'one_chamber_area=',format(areas[sides],'.14f'),
          'probability=',format(probs[sides],'.14f'))
print('CHECKS PASS: 20 vertices, 30 edges, 10 planes, 45 transverse antipodal intersections,')
print('92 chambers, exact facet-angle multisets, complete law, total mass, independent mean check')
