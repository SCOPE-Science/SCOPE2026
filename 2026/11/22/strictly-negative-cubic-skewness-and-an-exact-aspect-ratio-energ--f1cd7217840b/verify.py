"""Independent numerical diagnostics for moments of random cuboid shadows.

Uses only the Python standard library. No finite test substitutes for a proof.
"""
import math
import random

PI=math.pi

def moments(a,b,c):
    x,y,z=b*c,a*c,a*b
    s=x+y+z
    e2=x*y+y*z+z*x
    e3=x*y*z
    m1=s/2
    m2=s*s/3+(-2/3+4/(3*PI))*e2
    m3=s**3/4-3*s*e2/8+3*(4-PI)*e3/(8*PI)
    mu3=m3-3*m1*m2+2*m1**3
    return m1,m2,m3,mu3

def analytical(a,b,c):
    v2=(a*b*c)**2
    return v2*(3*(7*PI-22)/(4*PI)-(16-5*PI)/(8*PI)*((a-b)**2/(a*b)+(b-c)**2/(b*c)+(c-a)**2/(c*a)))

rng=random.Random(872233)
for a,b,c in [(1.,1.,1.),(1.,1.,3.),(.7,1.2,2.9),(1.,3.,8.),(.2,1.5,7.3)]:
    m1,m2,m3,mu3=moments(a,b,c)
    exact=analytical(a,b,c)
    assert abs(mu3-exact)<1e-9*max(1,abs(exact)),(a,b,c,mu3,exact)
    n=300000
    s1=s2=s3=0.
    for _ in range(n):
        u=rng.gauss(0,1);v=rng.gauss(0,1);w=rng.gauss(0,1)
        scale=1/math.sqrt(u*u+v*v+w*w)
        area=b*c*abs(u)*scale+a*c*abs(v)*scale+a*b*abs(w)*scale
        s1+=area;s2+=area**2;s3+=area**3
    avg=(s1/n,s2/n,s3/n)
    err=max(abs(avg[i]-m)/(1+m) for i,m in enumerate((m1,m2,m3)))
    assert err<0.012,(a,b,c,err)
    assert mu3<0
    print('box',a,b,c,'raw-moment-relative-discrepancy',round(err,6),'third-central',round(exact,8))
assert 16-5*PI>0 and 7*PI-22<0
print('BOX_SHADOW_CUBIC_SKEWNESS_CHECKS_OK')

# Independent geometric reconstruction from eight orthogonal-projection vertices.
def cross(p,q):
    return (p[1]*q[2]-p[2]*q[1],p[2]*q[0]-p[0]*q[2],p[0]*q[1]-p[1]*q[0])
def dot(p,q):
    return sum(x*y for x,y in zip(p,q))
def hull_area(points):
    pts=sorted(set(points))
    if len(pts)<3:return 0.
    def turn(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[];hi=[]
    for p in pts:
        while len(lo)>1 and turn(lo[-2],lo[-1],p)<=0:lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi)>1 and turn(hi[-2],hi[-1],p)<=0:hi.pop()
        hi.append(p)
    poly=lo[:-1]+hi[:-1]
    return abs(sum(x*y2-x2*y for (x,y),(x2,y2) in zip(poly,poly[1:]+poly[:1])))/2

for a,b,c in [(1.,1.,1.),(1.,2.,3.),(.5,3.,10.)]:
    for _ in range(120):
        u,v,w=(rng.gauss(0.,1.) for k in range(3))
        d=math.sqrt(u*u+v*v+w*w)
        U=(u/d,v/d,w/d)
        axis=(0.,0.,1.) if abs(U[2])<.85 else (0.,1.,0.)
        E=cross(U,axis)
        d=math.sqrt(dot(E,E));E=tuple(z/d for z in E)
        F=cross(U,E)
        points=[]
        for sx in [-1,1]:
            for sy in [-1,1]:
                for sz in [-1,1]:
                    p=(sx*a/2,sy*b/2,sz*c/2)
                    points.append((dot(E,p),dot(F,p)))
        direct=hull_area(points)
        predicted=b*c*abs(U[0])+a*c*abs(U[1])+a*b*abs(U[2])
        assert abs(direct-predicted)<2e-12*max(1,predicted),(direct,predicted)
print('BOX_SHADOW_HULL_GEOMETRY_CHECKS_OK')
