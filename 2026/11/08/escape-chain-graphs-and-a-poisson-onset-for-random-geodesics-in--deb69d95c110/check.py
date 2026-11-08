"""Independent finite-sample checks for geodesic escape graphs in spherical sectors.
Python 3 standard library only. The theorem itself is proved analytically.
"""
import math
import random
from itertools import combinations

R = random.Random(20261106)
PI = math.pi

def point(d, angle):
    z = [R.gauss(0, 1) for _ in range(d+1)]
    r = math.hypot(z[0], z[1]); s = math.sqrt(sum(v*v for v in z))
    z[0],z[1] = r*math.cos(angle),r*math.sin(angle)
    return [v/s for v in z]

def geodesic_exits(x, y, width):
    cs = max(-1.,min(1.,sum(a*b for a,b in zip(x,y))))
    dist = math.acos(cs)
    if dist < 1e-12: return False
    for k in range(1,120):
        t=k/120
        a=math.sin((1-t)*dist)/math.sin(dist)
        b=math.sin(t*dist)/math.sin(dist)
        xx=a*x[0]+b*y[0]
        yy=a*x[1]+b*y[1]
        az=math.atan2(yy,xx)%(2*PI)
        if az>width+1e-10: return True
    return False

def exact(n,width):
    if width<=PI: return 1.,0.,0.
    q=1-PI/width
    p=q*q
    e=(n*(n-1)/2)*p
    v=(n*(n-1)/2)*p*(1-p)
    v+=n*(n-1)*(n-2)*(2*q**3/3-q**4)
    empty=n*(1-q)**(n-1)-(n-1)*(1-q)**n
    return empty,e,v

# Check individual geometric arcs against independent azimuth-comparison criterion.
for d in (2,3,6):
    for width in (.7*PI,1.25*PI,1.7*PI):
        for _ in range(300):
            a,b=R.uniform(0,width),R.uniform(0,width)
            x,y=point(d,a),point(d,b)
            # Exclude extremely near-boundary cases where a 120-step sampler may
            # legitimately miss a very short outside excursion.
            if abs(abs(a-b)-PI)<.025: continue
            found=geodesic_exits(x,y,width)
            expected=abs(a-b)>PI
            assert found==expected,(d,width,a,b,found,expected)

# Independent random angular samples test exact count mean, variance and no-edge probability.
for n in (3,5,9):
    for width in (1.2*PI,1.8*PI):
        outcomes=[]
        trials=18000
        for _ in range(trials):
            angles=[R.uniform(0,width) for i in range(n)]
            outcomes.append(sum(abs(a-b)>PI for a,b in combinations(angles,2)))
        empty,e,v=exact(n,width)
        me=sum(outcomes)/trials
        va=sum((x-me)**2 for x in outcomes)/trials
        p0=outcomes.count(0)/trials
        assert abs(me-e)<.08+6*math.sqrt(v/trials), (n,width,me,e)
        assert abs(p0-empty)<.025, (n,width,p0,empty)
        assert abs(va-v)<.25+0.2*v,(n,width,va,v)

# All finite configurations have a bipartite nested-neighborhood graph.
for _ in range(200):
    width=R.uniform(PI+0.1,2*PI-0.01)
    a=[R.random()*width for k in range(16)]
    lo=[i for i,x in enumerate(a) if x<width-PI]
    hi=[i for i,x in enumerate(a) if x>PI]
    edges={(i,j) for i,j in combinations(range(len(a)),2) if abs(a[i]-a[j])>PI}
    assert all((i in lo and j in hi) or (j in lo and i in hi) for i,j in edges)
    sets=[]
    for i in sorted(lo,key=lambda i:a[i]):
        sets.append({j for j in hi if abs(a[i]-a[j])>PI})
    assert all(sets[k]>=sets[k+1] for k in range(len(sets)-1))

# Critical-window normalization directly from exact finite-sample formula.
for lam in (.25,1,4):
    for n in (100,1000,100000):
        width=PI*(1+lam/n)
        empty,e,v=exact(n,width)
        target=(1+lam)*math.exp(-lam)
        if n==100000: assert abs(empty-target)<.0006, (lam,empty,target)
        if n==100000: assert abs(e-lam*lam/2)<.008
        if n==100000: assert abs(v-(lam*lam/2+2*lam**3/3))<.02
print('SPHERICAL_SECTOR_GEODESIC_ESCAPE_GRAPH_CHECK_OK')
