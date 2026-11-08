"""Exact combinatorial certificate for random central sections of a truncated icosahedron.
Coordinates live in Z[phi], phi^2=phi+1. Run with Python 3, no external modules.
The planar Haar probabilities are finite algebraic spherical-angle expressions;
printout evaluates them for readability, while feasibility is verified exactly.
"""
import itertools, math
from collections import Counter,defaultdict

ZERO=(0,0); ONE=(1,0); PHI=(0,1)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    x,y=a;u,v=b
    return (x*u+y*v,x*v+y*u+y*v)
def scale(a,n):return(a[0]*n,a[1]*n)
def sg(a):
    x,y=a; A=2*x+y; B=y
    if A==B==0:return 0
    if A>=0 and B>=0:return 1
    if A<=0 and B<=0:return -1
    t=A*A-5*B*B
    return (1 if A>0 else -1) if t>0 else (1 if B>0 else -1)
def num(a):return a[0]+(1+math.sqrt(5))/2*a[1]
def vadd(a,b):return tuple(add(x,y) for x,y in zip(a,b))
def vneg(a):return tuple(neg(x) for x in a)
def vmul(a,n):return tuple(scale(x,n) for x in a)
def cross(a,b):
    return (sub(mul(a[1],b[2]),mul(a[2],b[1])),
            sub(mul(a[2],b[0]),mul(a[0],b[2])),
            sub(mul(a[0],b[1]),mul(a[1],b[0])))
def dot(a,b):
    v=ZERO
    for x,y in zip(a,b):v=add(v,mul(x,y))
    return v
def nonzero(a):return any(sg(x)!=0 for x in a)
def vnum(a):return tuple(num(x) for x in a)
def vunit(a):
    x=vnum(a);r=math.sqrt(sum(t*t for t in x));return tuple(t/r for t in x)
def firstpos(a):
    for x in a:
        s=sg(x)
        if s:return a if s>0 else vneg(a)
    raise ValueError('zero vector')
def vmean(vs):return tuple(sum(x[i] for x in vs) for i in range(3))
def dotf(a,b):return sum(x*y for x,y in zip(a,b))
def crossf(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def normf(a):return math.sqrt(dotf(a,a))

def polar_ok(q,constraints):return all(sg(dot(q,h))>=0 for h in constraints)
def rays(constraints):
    out=[]
    for i,j in itertools.combinations(range(len(constraints)),2):
        v=cross(constraints[i],constraints[j])
        if not nonzero(v):continue
        for q in (v,vneg(v)):
            if not polar_ok(q,constraints):continue
            if any(not nonzero(cross(q,r)) and sg(dot(q,r))>0 for r in out):continue
            out.append(q)
    return out

def sort_rays(rays0):
    us=[vunit(q) for q in rays0]
    center=vmean(us); nr=normf(center);center=tuple(x/nr for x in center)
    anchor=us[0]; d=dotf(anchor,center)
    e1=tuple(anchor[i]-center[i]*d for i in range(3));n=normf(e1);e1=tuple(t/n for t in e1)
    e2=crossf(center,e1)
    indices=sorted(range(len(rays0)),key=lambda i: math.atan2(dotf(us[i],e2),dotf(us[i],e1)))
    out=[rays0[i] for i in indices]
    if len(out)>=3:
        signs=[sg(dot(out[i],cross(out[(i+1)%len(out)],out[(i+2)%len(out)]))) for i in range(len(out))]
        assert all(s>=0 for s in signs),(len(out),signs)
    return out

def tri_area(p,q,r):
    a,b,c=vunit(p),vunit(q),vunit(r)
    return 2*math.atan2(abs(dotf(a,crossf(b,c))),1+dotf(a,b)+dotf(b,c)+dotf(c,a))
def area(poly):return sum(tri_area(poly[0],poly[i],poly[i+1]) for i in range(1,len(poly)-1))

ico=[]
for a,b in itertools.product((-1,1),repeat=2):
    ico.extend(((ZERO,(a,0),(0,b)),((a,0),(0,b),ZERO),((0,b),ZERO,(a,0))))
assert len(ico)==12
original_edges=[(i,j) for i,j in itertools.combinations(range(12),2) if sg(sub(dot(tuple(sub(x,y) for x,y in zip(ico[i],ico[j])),tuple(sub(x,y) for x,y in zip(ico[i],ico[j]))),(4,0)))==0]
assert len(original_edges)==30
faces=[tuple(sorted((a,b,c))) for a,b,c in itertools.combinations(range(12),3) if all(tuple(sorted(z)) in original_edges for z in ((a,b),(a,c),(b,c)))]
assert len(faces)==20
# w_{ij}=2v_i+v_j, for each oriented original edge.
directed=sorted([(a,b) for a,b in original_edges]+[(b,a) for a,b in original_edges]); ids={x:i for i,x in enumerate(directed)}
verts=[vadd(vmul(ico[i],2),ico[j]) for i,j in directed]
te=set()
for a,b in original_edges:te.add(tuple(sorted((ids[a,b],ids[b,a]))))
for a,b,c in faces:
    for i,j,k in ((a,b,c),(b,a,c),(c,a,b)):
        te.add(tuple(sorted((ids[i,j],ids[i,k]))))
assert len(te)==90

norms=[]
for w in verts:
    u=firstpos(w)
    if any(not nonzero(cross(u,z)) for z in norms):continue
    norms.append(u)
assert len(norms)==30

a,b=original_edges[0]
c=next(c for c in range(12) if c!=a and c!=b and tuple(sorted((a,c))) in original_edges and tuple(sorted((b,c))) in original_edges)
F=[ico[a],vadd(ico[a],ico[b]),vadd(vadd(ico[a],ico[b]),ico[c])]
base=[]
for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
    n=cross(F[i],F[j]);n=n if sg(dot(n,F[k]))>0 else vneg(n)
    base.append(n)
assert all(sg(dot(n,q))>=0 for n in base for q in F)
active=[]
for w in norms:
    signs={sg(dot(w,q)) for q in F}
    if -1 in signs and 1 in signs:active.append(w)
assert len(active)==7,len(active)

cells=[]
for signs in itertools.product((-1,1),repeat=7):
    hs=base+[w if s==1 else vneg(w) for s,w in zip(signs,active)]
    rr=rays(hs)
    if len(rr)<3:continue
    rr=sort_rays(rr)
    # Angular polygon exists, with its nondegeneracy certified by Z[phi] determinants.
    assert any(sg(dot(rr[0],cross(rr[j],rr[j+1])))>0 for j in range(1,len(rr)-1))
    # The sum of extreme rays is an exact interior representative.
    rep=rr[0]
    for q in rr[1:]:rep=vadd(rep,q)
    assert all(sg(dot(rep,h))>0 for h in hs)
    s=[sg(dot(w,rep)) for w in verts]
    assert all(z!=0 for z in s)
    count=sum(s[i]*s[j]<0 for i,j in te)
    cells.append((signs,rr,count,area(rr)))

counts=Counter(z[2] for z in cells)
assert len(cells)==12, (len(cells),counts)
assert counts=={10:3,12:4,14:3,16:1,18:1},counts
stats=defaultdict(float)
for z in cells:stats[z[2]]+=z[3]
fund=area(sort_rays(rays(base)))
assert abs(fund-math.pi/30)<1e-12, fund
assert abs(sum(stats.values())-fund)<1e-12
print('EXACT_CERTIFICATE_OK', 'icosahedron_edges=30','faces=20','truncated_vertices=60','edges=90',
      'great_circles=30','crossing_fundamental_chamber=7','chambers=12',
      'chamber_counts=3,4,3,1,1')
for k in sorted(stats):print('polygon',k,'probability',format(stats[k]/fund,'.14f'),'chamber_area',format(stats[k],'.14f'))
print('area_sum',format(sum(stats.values()),'.16f'),'expected',format(fund,'.16f'))
print('cell_certificate: bits (in order of active normals), polygon sides, spherical area')
for signs,rr,k,ar in sorted(cells,key=lambda x:(x[2],x[0])):
    print(''.join('+' if s>0 else '-' for s in signs),k,len(rr),format(ar,'.14f'))
