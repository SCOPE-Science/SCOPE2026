#!/usr/bin/env python3
"""Independent finite/numerical checks for a truncated-octahedron projected-area theorem.
Scientific proof is in RESULT.md; finite tests are not a general theorem proof.
No network access or third-party Python packages are required.
"""
import itertools
import math
import random

TOL = 2e-10
ROOT3 = math.sqrt(3)


def vertices():
    out = set()
    for s, t in itertools.product((-1, 1), repeat=2):
        out.update(itertools.permutations((0, s, 2*t)))
    return sorted(out)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def norm(a):
    return math.sqrt(dot(a, a))


def unit(a):
    n = norm(a)
    return tuple(x/n for x in a)


def area_projected(u, vs):
    axis = (1.0,0.0,0.0) if abs(u[0]) < .9 else (0.0,1.0,0.0)
    q = unit(cross(u, axis))
    r = cross(u, q)
    pts = sorted(set((dot(v,q)/math.sqrt(2),dot(v,r)/math.sqrt(2)) for v in vs))
    def orient(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]
    for p in pts:
        while len(lower)>=2 and orient(lower[-2],lower[-1],p)<=1e-12: lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(pts):
        while len(upper)>=2 and orient(upper[-2],upper[-1],p)<=1e-12: upper.pop()
        upper.append(p)
    hull=lower[:-1]+upper[:-1]
    return abs(sum(hull[i][0]*hull[(i+1)%len(hull)][1]-hull[i][1]*hull[(i+1)%len(hull)][0] for i in range(len(hull))))/2

DIAGONALS=((1,1,1),(1,1,-1),(1,-1,1),(-1,1,1))

def area_from_faces(u):
    return sum(map(abs,u))+1.5*sum(abs(dot(d,u)) for d in DIAGONALS)


def area_two_chambers(u):
    a,b,c=sorted(map(abs,u),reverse=True)
    return 4*(a+b+c) if a<=b+c else 7*a+b+c


def angle_kernel(r):
    r=abs(r)
    return 2/(3*math.pi)*(math.sqrt(1-r*r)+r*math.asin(r))


def verify():
    vs=vertices()
    assert len(vs)==24
    assert all(sum(abs(x) for x in v)==3 and max(map(abs,v))==2 for v in vs)
    edges=[(v,w) for i,v in enumerate(vs) for w in vs[i+1:] if sum((x-y)**2 for x,y in zip(v,w))==2]
    assert len(edges)==36
    # All square-face and hexagon-face vertices and areas follow from these coordinates.
    for k in range(3):
        for s in (-1,1):
            assert len([v for v in vs if v[k]==2*s])==4
    for sgn in itertools.product((-1,1),repeat=3):
        assert len([v for v in vs if dot(v,sgn)==3])==6
    rng=random.Random(20261016)
    for _ in range(1500):
        u=unit(tuple(rng.gauss(0,1) for _ in range(3)))
        assert abs(area_from_faces(u)-area_two_chambers(u))<TOL
    dirs=[unit(z) for z in ((1,0,0),(1,1,0),(1,1,1),(7,1,1),(1,.7,.2),(-.4,.5,1))]
    for u in dirs:
        assert abs(area_projected(u,vs)-area_from_faces(u))<TOL
    minv=4*math.sqrt(2)
    maxv=math.sqrt(51)
    assert abs(area_from_faces(unit((1,1,0)))-minv)<TOL
    assert abs(area_from_faces(unit((7,1,1)))-maxv)<TOL
    for _ in range(1500):
        u=unit(tuple(rng.gauss(0,1) for _ in range(3)))
        assert minv-1e-12<=area_from_faces(u)<=maxv+1e-12
    # Verify all three ray values used in the analytic conic minima proof.
    for ray,mode in [((1,1,0),1),((1,1,1),1),((2,1,1),1),((1,0,0),2),((1,1,0),2),((2,1,1),2)]:
        a,b,c=ray;f=4*(a+b+c) if mode==1 else 7*a+b+c
        assert f/norm(ray)+1e-12>=minv
    # Exact pair-type multiplicities for the seven unoriented face normals.
    normals=[(1,0,0),(0,1,0),(0,0,1)]+[unit(d) for d in DIAGONALS]
    weights=[1.0]*3 + [3*math.sqrt(3)/2]*4
    groups={'axes':0,'diagonals':0,'mixed':0}
    for i in range(7):
        for j in range(i+1,7):
            d=abs(dot(normals[i],normals[j]))
            if i<3 and j<3:
                assert abs(d)<TOL; groups['axes']+=1
            elif i>=3:
                assert abs(d-1/3)<TOL;groups['diagonals']+=1
            else:
                assert abs(d-1/math.sqrt(3))<TOL;groups['mixed']+=1
    assert groups=={'axes':3,'diagonals':6,'mixed':12},groups
    m=sum(weights)/2
    second=sum(w*w for w in weights)/3+2*sum(weights[i]*weights[j]*angle_kernel(dot(normals[i],normals[j])) for i in range(7) for j in range(i+1,7))
    exact=10+(4+60*math.sqrt(2)+18*math.asin(1/3)+24*math.asin(1/math.sqrt(3)))/math.pi
    assert abs(m-(1.5+3*math.sqrt(3)))<TOL
    assert abs(second-exact)<TOL
    # A separate deterministic equal-area spherical quadrature (z,phi) checks normalization.
    ns,nt=360,720
    s1=s2=0.0
    for i in range(ns):
        z=-1+(2*i+1)/ns
        rr=math.sqrt(1-z*z)
        for j in range(nt):
            theta=2*math.pi*(j+.5)/nt
            u=(rr*math.cos(theta),rr*math.sin(theta),z)
            b=area_two_chambers(u)
            s1+=b;s2+=b*b
    n=ns*nt
    assert abs(s1/n-m)<.003,(s1/n,m)
    assert abs(s2/n-second)<.028,(s2/n,second)
    print('TRUNCATED_OCTAHEDRON_BRIGHTNESS_OK',
          'vertices=24 edges=36 facets=14',
          'directions=1500 projection_hulls=6 pair_classes=3/6/12',
          'quadrature_nodes='+str(n))
    print('area_range=%.12f..%.12f mean=%.12f second=%.12f variance=%.12f' %
          (minv,maxv,m,second,second-m*m))

if __name__=='__main__':
    verify()
