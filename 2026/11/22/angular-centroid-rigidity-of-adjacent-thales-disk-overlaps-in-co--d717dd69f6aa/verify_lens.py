"""Independent numerical sanity check of an exact geometric lens identity.
Run: python3 verify_lens.py (Python standard library only).
"""
import math
import random

def lens(b, u, v):
    R = math.dist(b, u)/2
    r = math.dist(b, v)/2
    d = math.dist(u, v)/2
    a = (R*R-r*r+d*d)/(2*d)
    aa = max(-1.0, min(1.0, a/R))
    bb = max(-1.0, min(1.0, (d-a)/r))
    return R*R*math.acos(aa)+r*r*math.acos(bb)-d*math.sqrt(max(0.0, R*R-a*a))

def angle(a,b,c):
    x=(a[0]-b[0],a[1]-b[1]);y=(c[0]-b[0],c[1]-b[1])
    return math.acos(max(-1.0,min(1.0,(x[0]*y[0]+x[1]*y[1])/(math.hypot(*x)*math.hypot(*y)))))

def area(p):
    return abs(sum(p[i][0]*p[(i+1)%len(p)][1]-p[i][1]*p[(i+1)%len(p)][0] for i in range(len(p)))/2)

def check():
    total=0
    for n in [3,4,5,6,7,12]:
        for j in range(150):
            rng=random.Random(n*1000+j)
            a=sorted(2*math.pi*(i+rng.random()*.25)/n for i in range(n))
            p=[(math.cos(t)*(1+rng.random()*.01),math.sin(t)*(1+rng.random()*.01)) for t in a]
            c=(sum(v[0] for v in p)/n,sum(v[1] for v in p)/n)
            z=rng.random()*.95;v=p[j%n]
            b=((1-z)*c[0]+z*v[0],(1-z)*c[1]+z*v[1])
            actual=sum(lens(b,p[i],p[(i+1)%n]) for i in range(n))
            expected=sum(angle(p[i-1],p[i],p[(i+1)%n])*math.dist(b,p[i])**2 for i in range(n))/4-area(p)/2
            assert abs(actual-expected)<1.e-7,(n,j,actual,expected)
            total+=1
    print('PASS: %s independent convex-polygon lens comparisons' % total)
if __name__=='__main__': check()
