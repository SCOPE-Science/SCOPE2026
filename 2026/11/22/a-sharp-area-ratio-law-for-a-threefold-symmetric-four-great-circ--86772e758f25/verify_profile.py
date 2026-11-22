"""Independent sphere cell-area evaluator for four great circles."""
from math import sqrt,cos,sin,pi,acos,atan2
from itertools import product,combinations

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(v): return sqrt(dot(v,v))
def unit(v):return tuple(x/norm(v) for x in v)
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def sphere_triangle(a,b,c): return 2*atan2(abs(dot(a,cross(b,c))),1+dot(a,b)+dot(b,c)+dot(c,a))
def vertices(normals,signs):
    ws=[tuple(s*x for x in v) for s,v in zip(signs,normals)]
    vs=[]
    for i,j in combinations(range(4),2):
        u=cross(ws[i],ws[j])
        for sg in [-1,1]:
            p=unit(tuple(sg*x for x in u))
            if min(dot(w,p) for w in ws)>-1e-9 and not any(dot(p,q)>1-1e-12 for q in vs):vs.append(p)
    return vs

def cell_area(normals,signs):
    v=vertices(normals,signs)
    if len(v)<3:return None
    centroid=unit(tuple(sum(p[i] for p in v) for i in range(3)))
    base=unit(sub(v[0],tuple(dot(centroid,v[0])*z for z in centroid)))
    side=cross(centroid,base)
    v.sort(key=lambda p:atan2(dot(p,side),dot(p,base)))
    return sum(sphere_triangle(centroid,p,q) for p,q in zip(v,v[1:]+v[:1])),len(v)

def sample(t):
    r=sqrt(1-t*t)
    ns=[(r*cos(2*pi*i/3),r*sin(2*pi*i/3),t) for i in range(3)]+[(0.,0.,-1.)]
    rows=[cell_area(ns,s) for s in product([-1,1],repeat=4)]
    assert rows.count(None)==2
    typ=sorted([(n,round(a,12)) for a,n in filter(None,rows)])
    a=acos((3*t*t-1)/2);b=acos(-t)
    A=2*pi-3*a;B=2*pi-a-2*b;C=2*(a+b-pi)
    expect=sorted([(3,round(A,12))]*2+[(3,round(B,12))]*6+[(4,round(C,12))]*6)
    assert len(typ)==14
    assert all(n==m and abs(x-y)<5e-10 for (n,x),(m,y) in zip(typ,expect)),(t,typ,expect)
    return A,B,C

for t in [1/20,1/7,1/5,1/3,2/5,1/2,3/5,4/5,19/20]:
 A,B,C=sample(t)
 assert abs(2*A+6*B+6*C-4*pi)<3e-12
 print(f"t={t:.9f}; triangle A={A:.12f}, triangle B={B:.12f}, quadrilateral C={C:.12f}")
# Independently check the transition and monotonic profile on a finite grid;
# the general theorem is proved analytically, not by this grid.
def areas(t):
 alpha=acos((3*t*t-1)/2); beta=acos(-t)
 return 2*pi-3*alpha,2*pi-alpha-2*beta,2*(alpha+beta-pi)
def gap(t):
 A,B,C=areas(t)
 return C-A
low,high=1/3,0.95
for i in range(90):
 mid=(low+high)/2
 if gap(mid)>0:low=mid
 else:high=mid
transition=(low+high)/2
assert abs(transition-0.519200060611418)<1e-12
alpha0=acos(-1/3)
sharp=(4*alpha0-2*pi)/(2*pi-3*alpha0)
assert abs(sharp-2.4657775238125574)<1e-12
previous=1e300
for j in range(1,3334):
 t=j/10000
 A,B,C=areas(t)
 ratio=max(A,B,C)/min(A,B,C)
 assert ratio<previous,(t,ratio,previous)
 previous=ratio
previous=0
for j in range(3334,10000):
 t=j/10000
 A,B,C=areas(t)
 ratio=max(A,B,C)/min(A,B,C)
 assert ratio>previous,(t,ratio,previous)
 previous=ratio
print(f"9 independently enumerated 14-cell cases, 9999 numeric monotonic samples, transition={transition:.15f}, sharp minimum={sharp:.15f}")
