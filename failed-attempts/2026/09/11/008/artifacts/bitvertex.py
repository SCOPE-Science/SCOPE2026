# Substep 4 (bounded, ~90s): find tropical line vertex v with stable intersection 4 in 2 clusters.
from fractions import Fraction as Q
tris=[((0,0),(0,1),(1,0)),((0,1),(0,2),(1,1)),((0,1),(1,0),(1,1)),((0,2),(0,3),(1,2)),
((0,2),(1,1),(1,2)),((0,3),(0,4),(1,3)),((0,3),(1,2),(1,3)),((1,0),(1,1),(2,0)),
((1,1),(1,2),(2,1)),((1,1),(2,0),(2,1)),((1,2),(1,3),(2,2)),((1,2),(2,1),(2,2)),
((2,0),(2,1),(3,0)),((2,1),(2,2),(3,1)),((2,1),(3,0),(3,1)),((3,0),(3,1),(4,0))]
def h(p): i,j=p; return i*i+j*j+i*j
import sympy as sp
def dv(t):
    (a,b,c)=t; u,v,w=sp.symbols('u v w')
    s=sp.solve([u*a[0]+v*a[1]+w-h(a),u*b[0]+v*b[1]+w-h(b),u*c[0]+v*c[1]+w-h(c)],[u,v,w])
    return (float(s[u]),float(s[v]))
V={t:dv(t) for t in tris}
def ekey(t):
    a,b,c=t; return [tuple(sorted(e)) for e in [(a,b),(b,c),(a,c)]]
from collections import defaultdict
em=defaultdict(list)
for t in tris:
    for e in ekey(t): em[e].append(t)
segs=[]
for e,ts in em.items():
    if len(ts)==2:
        p1=V[ts[0]]; p2=V[ts[1]]; segs.append((p1,p2,e))
    elif len(ts)==1:
        # unbounded ray: direction = perpendicular of edge, outward from 4Delta2
        (a,b)=e; d=(b[0]-a[0],b[1]-a[1])
        # outward normal: rotate; pick sign pointing away from centroid (4/3,4/3)
        mid=((a[0]+b[0])/2,(a[1]+b[1])/2); n=(d[1],-d[0])
        cx,cy=4/3,4/3
        if (mid[0]-cx)*n[0]+(mid[1]-cy)*n[1]<0: n=(-n[0],-n[1])
        p0=V[ts[0]]; p1=(p0[0]+n[0]*5,p0[1]+n[1]*5); segs.append((p0,p1,e))
print("segments:",len(segs))
def seg_int(p1,p2,p3,p4):
    # return intersection params or None
    x1,y1=p1;x2,y2=p2;x3,y3=p3;x4,y4=p4
    d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if abs(d)<1e-12: return None
    t=((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/d
    u=((x1-x3)*(y1-y2)-(y1-y3)*(x1-x2))/d
    if -1e-9<=t<=1+1e-9 and -1e-9<=u<=1+1e-9:
        return (x1+t*(x2-x1),y1+t*(y2-y1))
    return None
def line_segs(v):
    (a,b)=v
    return [((a,b),(a-6,b)),((a,b),(a,b-6)),((a,b),(a+6,b+6))]
import itertools
best=[]
grid=[x*0.5 for x in range(0,17)]
for gx in grid:
    for gy in grid:
        v=(gx,gy); hits=[]
        for r in line_segs(v):
            for s in segs:
                q=seg_int(r[0],r[1],s[0],s[1])
                if q: hits.append((round(q[0],3),round(q[1],3)))
        # cluster hits
        if len(hits)>=2:
            best.append((v,len(hits),hits[:6]))
print("candidates with >=2 hits:",len(best))
for v,n,hh in best[:25]: print(v,n,hh)
