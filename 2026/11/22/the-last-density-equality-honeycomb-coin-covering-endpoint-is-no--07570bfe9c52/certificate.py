#!/usr/bin/env python3
"""Exact finite geometric certificate for honeycomb radius sqrt(39)/2.
No floating-point operations, third-party packages, or downloaded data.
"""
from collections import Counter

def norm(a,b): return a*a-a*b+b*b

def inclusion(p,q,t,sgn):
    # Equal circles centered at p,q with squared radius 39/4.
    # sgn represents one of the two solutions to their intersection.
    wx,wy=q[0]-p[0],q[1]-p[1]
    yx,yy=t[0]-p[0],t[1]-p[1]
    d=norm(wx,wy)
    assert 0<d<=39
    dot2=2*yx*wx-yx*wy-yy*wx+2*yy*wy
    A=2*norm(yx,yy)-dot2
    B=sgn*(yx*wy-yy*wx)
    delta=3*(39-d)
    # Evaluate exactly sign(A+B*sqrt(delta/d)) <= 0.
    if delta==0 or B==0: return A<=0
    if B>0:
        if A>=0: return False
        return A*A*d>=B*B*delta
    if A<=0: return True
    return A*A*d<=B*B*delta

P=[(a,b) for a in range(-6,7) for b in range(-6,7)
    if 0<norm(a,b)<=23 and (a+b)%3 !=0]
assert len(P)==54,len(P)

counts=Counter(); cases=[]; ntested=0
for i,p in enumerate(P):
    for q in P[:i]:
        d=norm(p[0]-q[0],p[1]-q[1])
        if d>39: continue
        for sign in ((1,) if d==39 else (-1,1)):
            inc=[t for t in P if inclusion(p,q,t,sign)]
            ntested+=1;counts[len(inc)]+=1
            if len(inc)>=26:
                pairs=[(a,b) for ia,a in enumerate(inc) for b in inc[:ia]
                      if norm(a[0]-b[0],a[1]-b[1])==39]
                assert len(inc)==26,('more than26',p,q,sign,len(inc))
                assert pairs, ('not rigid at',p,q,sign)
                # List all max center candidates as half-sums of diameter pair.
                cent=(pairs[0][0][0]+pairs[0][1][0],pairs[0][0][1]+pairs[0][1][1])
                assert all((a[0]+b[0],a[1]+b[1])==cent for a,b in pairs)
                cases.append((cent,inc,pairs))
centers=sorted(set(c for c,inc,pairs in cases))
print('sites:',len(P),'circle_intersections:',ntested)
print('maximum among intersection candidates:',max(counts))
print('maximal intersections:',len(cases),'unique midpoint centers:',len(centers))
print('midpoint coordinates 2c:',centers)
# For representative central point c=(1/2,0), prove every norm39 Eisenstein direction appears
# as a pair difference up to unit: both norm39 associate-classes must be hit.
def associates(a,b):
    u,v=a,b
    out=set()
    for _ in range(6):
        out.add((u,v));u,v=-v,u-v  # multiply by omega
    return out | {(-u,-v) for u,v in out}
vecs={(a,b) for a in range(-8,9) for b in range(-8,9) if norm(a,b)==39}
assert len(vecs)==12,len(vecs)
for center,inc,pairs in cases:
    differences=set()
    for a,b in pairs:
        differences.add((a[0]-b[0],a[1]-b[1]));differences.add((b[0]-a[0],b[1]-a[1]))
    # For all nearest-center vectors u of norm 39, the disk has at least
    # one pair of sites whose difference belongs to u * Z[omega].
    for u in vecs:
        assert differences.intersection(associates(*u)), (center,u)
assert len(centers)==30,len(centers)
residues={((2*a-b)%6,(a+b)%6) for a,b in centers}
assert residues == {(1,2),(1,5),(2,1),(4,5),(5,1),(5,4)},residues
# Direct, separate integer count for c = 1/2 (coordinate pair for 2c is (1,0)).
assert sum(norm(2*a-1,2*b)<=39 for a,b in P)==26
print('all maximal intersections have a diameter pair of each norm-39 associate class')
print('six maximal-center congruence classes and direct witness checked')
print('PASS')
