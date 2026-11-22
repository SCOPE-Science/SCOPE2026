"""Independent finite checks for the cube-intersection-body formula.
Scientific proof is analytic; these checks do not certify all dimensions.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial, sqrt, isclose, atan2
import random

def section_density(u):
    d=len(u); u=tuple(map(Q,u)); assert all(x>0 for x in u)
    total=sum(u,Q(0)); numerator=Q(0)
    for mask in product((0,1),repeat=d):
        t=total/2-sum((u[i] for i,b in enumerate(mask) if b),Q(0))
        if t>0: numerator+=(-1)**sum(mask)*t**(d-1)
    denom=2*factorial(d-1)
    for x in u: denom*=x
    return numerator/denom

def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def norm(a):return sqrt(dot(a,a))
def section_polygon_area(u):
    assert len(u)==3
    vertices=list(product((-1.,1.), repeat=3))
    pts=[]
    for v in vertices:
        for j in range(3):
            if v[j]!=-1:continue
            w=list(v);w[j]=1;w=tuple(w)
            av,bv=dot(u,v),dot(u,w)
            if abs(av)<1e-12:pts.append(v)
            if av*bv<0:
                s=-av/(bv-av)
                pts.append(tuple(v[k]+s*(w[k]-v[k]) for k in range(3)))
            elif abs(bv)<1e-12:pts.append(w)
    uniq=[]
    for p in pts:
        if all(norm(tuple(p[k]-r[k] for k in range(3)))>1e-10 for r in uniq):uniq.append(p)
    assert len(uniq)>=3
    n=tuple(x/norm(u) for x in u)
    a=(0.,0.,1.) if abs(n[2])<.9 else (0.,1.,0.)
    e=cross(n,a);e=tuple(x/norm(e) for x in e)
    f=cross(n,e)
    pts=sorted(uniq,key=lambda p:atan2(dot(f,p),dot(e,p)))
    area=.5*abs(sum(dot(n,cross(pts[i],pts[(i+1)%len(pts)])) for i in range(len(pts))))
    return area,len(pts)

def run():
    rng=random.Random(20261120)
    tests=0
    for d in range(2,8):
        for _ in range(160):
            u=[Q(rng.randrange(1,30),rng.randrange(1,12)) for _ in range(d)]
            p=section_density(u)
            assert p>0 and p <= Q(1,2*max(u))
            dom=[i for i in range(d) if u[i]>=sum(u)-u[i]]
            assert (p==Q(1,2*max(u))) == bool(dom)
            # The facet condition is precisely the dominance cone.
            for i in range(d):
                assert (u[i]*p==Q(1,2)) == (u[i]>=sum(u)-u[i])
            tests+=d+3
    for _ in range(260):
        u=[float(rng.randrange(1,30))/rng.randrange(1,9) for _ in range(3)]
        area,n=section_polygon_area(u)
        p=float(section_density([Q(str(x)) for x in u]))
        assert isclose(area,8*norm(u)*p,rel_tol=1e-10,abs_tol=1e-10)
        assert n in (4,6)
        tests+=2
    for d in range(2,8):
        u=[Q(2*d),*([Q(1)]*(d-1))]
        assert section_density(u)==Q(1,4*d)
        for j in range(1,d):
            x=[Q(1)]*d;x[j]=Q(2*d)
            assert section_density(x)==Q(1,4*d)
            tests+=1
    print('PASS',tests,'exact/integral-geometric checks, dimensions 2..7, 3D section polygons')
if __name__=='__main__':run()
