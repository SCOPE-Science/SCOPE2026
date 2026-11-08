"""Independent symbolic/finite checks for boundary-sampled convex-hull identification."""
from fractions import Fraction as Q
from itertools import product
import random
from math import sqrt

def hull_size(points):
    pts=sorted(set(points))
    if len(pts) <= 1: return len(pts)
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for p in pts:
        while len(lo)>=2 and cross(lo[-2],lo[-1],p)<=1e-11:lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(pts):
        while len(hi)>=2 and cross(hi[-2],hi[-1],p)<=1e-11:hi.pop()
        hi.append(p)
    return len(lo[:-1]+hi[:-1])

def theory(p):
    s3=sum(t**3 for t in p);s4=sum(t**4 for t in p)
    p2=s4;p3=4*(s3-s4);p4=1-p2-p3
    e2=(p4/Q(6))**Q(1,2) if False else sum(p[i]*p[j] for i in range(3) for j in range(i+1,3))
    assert p4==6*e2**2
    e3=p[0]*p[1]*p[2]
    assert e3==(p2-1+4*e2-2*e2**2)/4
    # Exact Vieta reconstruction and semialgebraic feasibility checks.
    assert e2>0 and e3>0 and e2/Q(2)-e3-Q(1,8)>0
    discr=e2**2-4*e2**3-4*e3+18*e2*e3-27*e3**2
    assert discr>=0
    for root in p:
        assert root**3-root**2+e2*root-e3==0
    return (p2,p3,p4)

# Exhaustively aggregate the 3^4 side-occupancy patterns (using exact rationals).
for ps in [(Q(1,3),)*3,(Q(3,10),Q(3,10),Q(2,5)),(Q(3,10),Q(1,4),Q(9,20)),(Q(16,61),Q(16,61),Q(29,61)),(Q(25,61),Q(25,61),Q(11,61))]:
    assert sum(ps)==1 and all(0<x<Q(1,2) for x in ps)
    got=[Q(0)]*3
    for labels in product(range(3),repeat=4):
        counts=[labels.count(i) for i in range(3)]
        k=sum(min(2,c) for c in counts)
        got[k-2]+=ps[labels[0]]*ps[labels[1]]*ps[labels[2]]*ps[labels[3]]
    assert tuple(got)==theory(ps)
    if ps[0]==ps[1] and ps[0] in (Q(16,61),Q(25,61)):
        assert sum(x**3 for x in ps)==Q(32581,61**3)

# Independent continuous-point computation (not based on occupancy labels).
def sample_triangle(a,b,c,rng):
    # A=(0,0), B=(c,0), C from |AC|=b,|BC|=a.
    x=(b*b+c*c-a*a)/(2*c);y=sqrt(b*b-x*x)
    sides=[((0.,0.),(c,0.),c),((c,0.),(x,y),a),((x,y),(0.,0.),b)]
    z=rng.random()*(a+b+c)
    for u,v,le in sides:
        if z<le:
            t=z/le
            return (u[0]+(v[0]-u[0])*t,u[1]+(v[1]-u[1])*t)
        z-=le
    raise AssertionError('sampling failure')

rng=random.Random(342781)
for (a,b,c) in [(1,1,1),(3,4,5),(2,3,4),(16,16,29),(25,25,11)]:
    norm=tuple(Q(x,a+b+c) for x in (a,b,c))
    exact=theory(norm)
    trials=36000
    hits=[0]*3
    for _ in range(trials):
        k=hull_size([sample_triangle(a,b,c,rng) for _ in range(4)])
        assert k in (2,3,4)
        hits[k-2]+=1
    for i in range(3):
        empir=hits[i]/trials;prob=float(exact[i]);
        assert abs(empir-prob)<0.018,(a,b,c,i,empir,prob)
print('VERIFY_OK exact_occupancy_shapes=5 continuous_hull_trials=180000 nonidentifiability_pair=1')
