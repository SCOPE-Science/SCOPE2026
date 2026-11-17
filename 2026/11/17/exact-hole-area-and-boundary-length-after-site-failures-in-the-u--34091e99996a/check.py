#!/usr/bin/env python3
"""Independent finite checks for triangle-face deletion geometry; stdlib only."""
import math
from itertools import product

ROOT3=math.sqrt(3.0)
AREA=ROOT3/4.0
CAP=math.pi/6.0-ROOT3/4.0
BASE=(ROOT3-math.pi/2.0)

def point(v):
    i,j=v
    return (i+j/2.0,j*ROOT3/2.0)

def faces_in_box(m):
    for i in range(-m,m+1):
        for j in range(-m,m+1):
            yield frozenset(((i,j),(i+1,j),(i,j+1)))
            yield frozenset(((i+1,j+1),(i+1,j),(i,j+1)))

def invariant(s):
    full={f for f in faces_in_box(5) if f <= s}
    edge_count={}
    for tri in full:
        v=list(tri)
        for a,b in ((v[0],v[1]),(v[1],v[2]),(v[2],v[0])):
            ed=frozenset((a,b));edge_count[ed]=edge_count.get(ed,0)+1
    b=sum(k==1 for k in edge_count.values())
    f=len(full)
    return full,AREA*f-CAP*b,(math.pi/3)*b,f,b

def independent_midpoint_area(s,n=140):
    # Integrates the actual distance to *all* retained nearby sites,
    # not cap area, face count or the theorem's claimed polynomial.
    full,expect,perim,f,b=invariant(s)
    sites=[point((i,j)) for i in range(-8,9) for j in range(-8,9) if (i,j) not in s]
    uncovered=0
    for tri in full:
        vertices=[point(v) for v in tri]
        a,b,c=vertices
        for i in range(n):
            for j in range(n-i):
                # two equal-area mini-triangles in each interior grid cell
                us=[((i+1/3)/n,(j+1/3)/n)]
                if i+j+1<n: us.append(((i+2/3)/n,(j+2/3)/n))
                for u,v in us:
                    x=a[0]+u*(b[0]-a[0])+v*(c[0]-a[0])
                    y=a[1]+u*(b[1]-a[1])+v*(c[1]-a[1])
                    if min((x-px)**2+(y-py)**2 for px,py in sites)>1.0:
                        uncovered+=AREA/(n*n)
    return expect,uncovered

cases=[
    {(0,0),(1,0),(0,1)},
    {(0,0),(1,0),(0,1),(1,-1)},
    {(i,j) for i in range(-1,2) for j in range(-1,2)},
    {(0,0),(2,0),(0,2)},
]
for s in cases:
    e,seen=independent_midpoint_area(s)
    assert abs(e-seen)<0.025,(len(s),e,seen)
assert abs(invariant(cases[0])[1]-BASE)<1e-13
assert abs(invariant(cases[1])[1]- (2*BASE+2*CAP))<1e-13

# Independent enumeration of 2^6 local patterns: three face bits + three opposite bits.
for q in (0.0,0.05,0.25,0.6,0.9,1.0):
    mean=0.0; mean_edge=0.0
    for bits in product((0,1),repeat=6):
        count=sum(bits)
        weight=q**count*(1-q)**(6-count)
        if all(bits[:3]):
            b=sum(1-z for z in bits[3:])
            mean+=weight*(AREA-CAP*b)
            mean_edge+=weight*(math.pi/3)*b
    exact=q**3*(4-2*math.pi/ROOT3+(2*math.pi/ROOT3-3)*q)
    boundary=(4*math.pi/ROOT3)*q**3*(1-q)
    assert abs(mean/AREA-exact)<1e-12,(q,mean/AREA,exact)
    assert abs(mean_edge/AREA-boundary)<1e-12,(q,mean_edge/AREA,boundary)
print('TRIANGULAR_ERASURE_AREA_PERIMETER_CHECK_OK',len(cases),'patterns',64)
