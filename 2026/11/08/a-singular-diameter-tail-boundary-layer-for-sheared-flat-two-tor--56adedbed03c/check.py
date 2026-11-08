"""Independent finite tests of the distance-distribution formula for sheared flat two-tori.

Run with Python 3 standard library; all analytic assertions are deterministic.
These tests corroborate, but do not replace, the mathematical proof.
"""
import math
from itertools import combinations


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def cell_vertices(delta):
    a = (1.0, 0.0)
    b = (delta, 1.0)
    normals = [a, b]
    if delta > 0:
        normals.append((delta - 1.0, 1.0))
    lines = [(s*u[0], s*u[1], dot(u, u)/2)
             for u in normals for s in (1, -1)]
    vertices = []
    for (a1, b1, c1), (a2, b2, c2) in combinations(lines, 2):
        den = a1*b2 - b1*a2
        if abs(den) < 1e-12:
            continue
        p = ((c1*b2 - b1*c2)/den, (a1*c2-c1*a2)/den)
        if all(a*x+b*y <= c+1e-9 for a, b, c in lines for x,y in [p]):
            if not any(math.dist(p, q) < 1e-8 for q in vertices):
                vertices.append(p)
    vertices.sort(key=lambda p: math.atan2(p[1], p[0]))
    return vertices


def radial_area(delta, r, subdivisions=32000):
    a = (1, 0)
    b = (delta, 1)
    ns = [a,b] + ([(delta-1,1)] if delta else [])
    acc = 0.0
    for k in range(subdivisions):
        th = 2*math.pi * (k+0.5)/subdivisions
        e = (math.cos(th), math.sin(th))
        rho = min(dot(u,u)/(2*abs(dot(u,e))) for u in ns if abs(dot(u,e)) > 1e-15)
        acc += min(r*r, rho*rho)
    return math.pi*acc/subdivisions


def cap(r,h):
    if r <= h: return 0.0
    return r*r*math.acos(h/r)-h*math.sqrt(r*r-h*h)


def cdf(delta, r):
    aa = 1.0
    bb = math.hypot(delta, 1.0)
    cc = math.hypot(1-delta, 1.0)
    R = aa*bb*cc/2
    h = [aa/2,bb/2] + ([cc/2] if delta else [])
    if r<=0:return 0.0
    if r>=R:return 1.0
    return math.pi*r*r-2*sum(cap(r,x) for x in h)


def tail_coefficient(delta):
    if delta == 0:return 4.0
    return 2*(1/delta + 1/(1-delta) + 1/(1-delta+delta*delta))


def run():
    ncheck = 0
    for d in [0, 0.02, 0.1, 0.25, 0.49]:
        verts=cell_vertices(d)
        assert len(verts) == (4 if d == 0 else 6),(d,len(verts))
        R=math.hypot(1,d)*math.hypot(1-d,1)/2
        assert max(abs(math.hypot(*p)-R) for p in verts)<1e-10
        A=abs(sum(x1*y2-y1*x2 for (x1,y1),(x2,y2) in zip(verts,verts[1:]+verts[:1])))/2
        assert abs(A-1)<1e-10,(d,A)
        for r in [0.15*R,0.7*R,0.94*R,1.01*R]:
            got=radial_area(d,r)
            want=cdf(d,r)
            assert abs(got-want)<8e-7,(d,r,got,want)
            ncheck+=1
        if d:
            exact=2*sum(h/math.sqrt(R*R-h*h) for h in
                        [0.5,math.hypot(d,1)/2,math.hypot(1-d,1)/2])
            assert abs(exact-tail_coefficient(d))<1e-7
            assert abs((tail_coefficient(d)*d)-2*(1+d/(1-d)+d/(1-d+d*d)))<1e-10
    for t in (0.1, 0.25, 0.5, 1.0):
        positive=max(0.0, 1.0 - 2*math.sqrt(2)*t)
        predicted=2*math.sqrt(2)*t - (2.0/3.0)*(1-positive**1.5)
        errs=[]
        for d in (0.02, 0.01, 0.005):
            R=math.hypot(d,1)*math.hypot(1-d,1)/2
            observed=(1-cdf(d,R-t*d*d))/d**3
            errs.append(abs(observed/predicted-1))
        assert errs[2] < 0.014 and errs[0]>errs[2], (t,errs)
        ncheck+=3
    print('FLAT_TORUS_RADIAL_AREA_CYCLICITY_EXACT_TAIL_AND_CROSSOVER_OK', ncheck)
    print('C(0)=', tail_coefficient(0))
    for d in [.02,.1,.25,.49]:
        print('shear=',d,'C=',tail_coefficient(d),'delta*C=',d*tail_coefficient(d))

if __name__=='__main__':run()
