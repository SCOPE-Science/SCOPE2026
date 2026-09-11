# Substep 5 (bounded): stable-intersection multiplicity per connected component.
from collections import defaultdict
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
em=defaultdict(list)
for t in tris:
    for e in ekey(t): em[e].append(t)
# curve edges with primitive direction + weight 1
cedges=[]
for e,ts in em.items():
    (a,b)=e; d=(b[0]-a[0],b[1]-a[1])
    import math; g=math.gcd(abs(d[0]),abs(d[1])); prim=(d[0]//g,d[1]//g)
    if len(ts)==2: cedges.append((V[ts[0]],V[ts[1]],prim,1,e))
    else:
        mid=((a[0]+b[0])/2,(a[1]+b[1])/2); n=(d[1],-d[0])
        if (mid[0]-4/3)*n[0]+(mid[1]-4/3)*n[1]<0: n=(-n[0],-n[1])
        import math as m; g2=m.gcd(abs(n[0]),abs(n[1])); prim2=(n[0]//g2,n[1]//g2)
        p0=V[ts[0]]; cedges.append((p0,(p0[0]+prim2[0]*9,p0[1]+prim2[1]*9),prim2,1,e))
def xsec(p1,p2,p3,p4):
    x1,y1=p1;x2,y2=p2;x3,y3=p3;x4,y4=p4
    d=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if abs(d)<1e-12: return None
    t=((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/d; u=((x1-x3)*(y1-y2)-(y1-y3)*(x1-x2))/d
    if -1e-9<=t<=1+1e-9 and -1e-9<=u<=1+1e-9: return (x1+t*(x2-x1),y1+t*(y2-y1))
    return None
def trop_mult(cprim, cwt, lprim):
    # |det(cprim, lprim)| * weights
    return abs(cprim[0]*lprim[1]-cprim[1]*lprim[0])*cwt
def analyze(v):
    rays=[(v,(v[0]-9,v[1]),(-1,0)),(v,(v[0],v[1]-9),(0,-1)),(v,(v[0]+9,v[1]+9),(1,1))]
    hits=[]
    for r in rays:
        for c in cedges:
            q=xsec(r[0],r[1],c[0],c[1])
            if q: hits.append({'pt':(round(q[0],3),round(q[1],3)),'mult':trop_mult(c[2],c[3],r[2]),'cell':c[4]})
    tot=sum(x['mult'] for x in hits)
    return hits,tot
for v in [(0.5,1.0),(0,0),(2.0,1.0),(1.0,0.5),(3.0,2.0),(4.0,3.0),(2.5,2.5),(1.5,1.0)]:
    hits,tot=analyze(v)
    print("v=",v,"total=",tot)
    for x in hits: print("   ",x)
