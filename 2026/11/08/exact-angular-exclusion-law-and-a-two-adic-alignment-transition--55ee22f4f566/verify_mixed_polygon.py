"""Independent convex-hull checks for the angular mixed-area formula.

Only Python 3 standard library required. Numerical tests supplement the analytic proof.
"""
import math
import random


def vertices(n, radius, angle=0.0):
    return [(radius*math.cos(angle+2*math.pi*j/n),
             radius*math.sin(angle+2*math.pi*j/n)) for j in range(n)]


def hull_area(points):
    points = sorted(set(points))
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2],lower[-1],p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in points[::-1]:
        while len(upper) >= 2 and cross(upper[-2],upper[-1],p) <= 0:
            upper.pop()
        upper.append(p)
    h = lower[:-1] + upper[:-1]
    return abs(sum(h[i][0]*h[(i+1)%len(h)][1] -
                   h[i][1]*h[(i+1)%len(h)][0]
                   for i in range(len(h))) / 2)


def direct(n,m,r,s,phi):
    a=vertices(n,r)
    b=vertices(m,s,phi+math.pi)
    return hull_area([(x+u,y+v) for x,y in a for u,v in b])


def exact_formula(n,m,r,s,phi):
    ell=math.lcm(n,m)
    g=math.gcd(n,m)
    theta=math.pi/n-math.pi/m+math.pi/ell
    p=2*math.pi/ell
    delta=((phi+math.pi-theta+p/2)%p)-p/2
    amplitude=2*g*r*s*math.sin(math.pi/n)*math.sin(math.pi/m)/math.sin(math.pi/ell)
    an=n*r*r*math.sin(2*math.pi/n)/2
    am=m*s*s*math.sin(2*math.pi/m)/2
    return an+am+amplitude*math.cos(delta)


def main():
    rng=random.Random(314159)
    count=0
    for n in range(3,15):
        for m in range(3,15):
            r=math.exp(rng.uniform(-0.8,0.8))
            s=math.exp(rng.uniform(-0.8,0.8))
            ell=math.lcm(n,m)
            theta=math.pi/n-math.pi/m+math.pi/ell
            p=2*math.pi/ell
            for phi in (0, rng.uniform(-math.pi, math.pi),
                        theta-math.pi, theta-math.pi+p/2,
                        theta-math.pi+p/2-1e-5):
                actual=direct(n,m,r,s,phi)
                claimed=exact_formula(n,m,r,s,phi)
                if abs(actual-claimed) > 2e-9*max(1,actual):
                    raise AssertionError((n,m,r,s,phi,actual,claimed))
                count+=1
            aligned=exact_formula(n,m,r,s,0)
            vmax=exact_formula(n,m,r,s,theta-math.pi)
            vmin=exact_formula(n,m,r,s,theta-math.pi+p/2)
            assert vmin < vmax
            same_power_two=(n%2==0 and m%2==0 and ((n & -n)==(m & -m)))
            assert abs(aligned-(vmin if same_power_two else vmax)) < 2e-9*max(1,aligned)
            count += 2
    print('MIXED_POLYGON_HULL_OK',count)


if __name__=='__main__':
    main()
