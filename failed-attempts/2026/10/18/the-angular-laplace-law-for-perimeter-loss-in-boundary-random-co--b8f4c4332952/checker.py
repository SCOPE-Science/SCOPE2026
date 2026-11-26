"""Reproduce finite-sample perimeter decomposition and exponential corner integrals.
No external packages are required. Finite tests corroborate, not certify, the theorem.
"""
import math
import random

rng = random.Random(20241013)

def perimeter(vertices):
    return sum(math.dist(vertices[i],vertices[(i+1)%len(vertices)]) for i in range(len(vertices)))

def hull(points):
    pts = sorted(set(points))
    def cross(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lower=[]
    for p in pts:
        while len(lower)>1 and cross(lower[-2],lower[-1],p)<=1e-12:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(pts):
        while len(upper)>1 and cross(upper[-2],upper[-1],p)<=1e-12:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def test_polygon(poly):
    m=len(poly)
    lengths=[math.dist(poly[i],poly[(i+1)%m]) for i in range(m)]
    L=sum(lengths)
    for iteration in range(70):
        pieces=[[] for i in range(m)]
        pts=[]
        for _ in range(45):
            r=rng.random()*L
            i=0
            while r>=lengths[i]:
                r-=lengths[i]
                i+=1
            u=r/lengths[i]
            v=(poly[i][0]*(1-u)+poly[(i+1)%m][0]*u,
               poly[i][1]*(1-u)+poly[(i+1)%m][1]*u)
            pieces[i].append(r)
            pts.append(v)
        if not all(pieces):
            continue
        expected=0.0
        for i in range(m):
            s=min(lengths[(i-1)%m]-t for t in pieces[(i-1)%m])
            t=min(pieces[i])
            vec1=(poly[(i-1)%m][0]-poly[i][0],poly[(i-1)%m][1]-poly[i][1])
            vec2=(poly[(i+1)%m][0]-poly[i][0],poly[(i+1)%m][1]-poly[i][1])
            co=(vec1[0]*vec2[0]+vec1[1]*vec2[1])/(lengths[(i-1)%m]*lengths[i])
            expected+=s+t-math.sqrt(max(0,s*s+t*t-2*s*t*co))
        actual=L-perimeter(hull(pts))
        assert abs(expected-actual)<1e-8,(poly,expected,actual)
    return L

def c(alpha,u):
    return 1-math.sqrt(max(0,1-2*(1+math.cos(alpha))*u*(1-u)))

def integrate(f,N=12000):
    return (f(0)+f(1)+sum((4 if i%2 else 2)*f(i/N) for i in range(1,N)))/(3*N)

def mu(alpha):
    h=alpha/2
    return 1-(math.sin(h)**2/math.cos(h))*math.log(1/math.tan(h/2))

for poly in [((0,0),(3,0),(.4,1.8)),((0,0),(3,0),(3,1),(0,1)),
             ((0,0),(2,0),(3,1),(1.6,2.5),(-.5,1.5))]:
    print('finite_polygon_perimeter_check',len(poly),test_polygon(poly))

for alpha in [.22, .7, math.pi/2, 2.4, 3.03]:
    m=mu(alpha)
    E=2*integrate(lambda u:c(alpha,u))
    S=6*integrate(lambda u:c(alpha,u)**2)
    assert abs(m-E)<5e-8,(alpha,m,E)
    assert abs(S-(6*m-2*(1+math.cos(alpha))))<5e-8,(alpha,S)
    for t in [.25,1.,3.]:
        lap=integrate(lambda u:(1+t*c(alpha,u))**(-2))
        assert 0<lap<1
    print('angle_moment_and_Laplace_integrals',round(alpha,6),round(m,9),round(S-m*m,9))

for alpha in [math.pi/3,math.pi/2,2*math.pi/3]:
    sample=[]
    for _ in range(60000):
        x=rng.expovariate(1)
        y=rng.expovariate(1)
        sample.append(x+y-math.sqrt(x*x+y*y-2*x*y*math.cos(alpha)))
    sample_mean=sum(sample)/len(sample)
    assert abs(sample_mean-mu(alpha))<.022,(alpha,sample_mean,mu(alpha))
    print('exponential_corner_mean',round(alpha,6),round(sample_mean,7),round(mu(alpha),7))
print('PASS: finite polygon identity, analytic moments/Laplace, and exponential sampling')
