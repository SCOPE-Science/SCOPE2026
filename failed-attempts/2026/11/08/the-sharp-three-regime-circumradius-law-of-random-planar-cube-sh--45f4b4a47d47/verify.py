"""Independent deterministic and numerical checks for the cube-shadow radius law."""
import math
import random
import itertools

PI = math.pi
TSTAR = 1/math.sqrt(3)
RSTAR = math.sqrt(8/3)
VERTICES = list(itertools.product((-1., 1.), repeat=3))

def quadrature(f, a, b, steps=6000):
    if a >= b:
        return 0.0
    if steps%2: steps += 1
    h = (b-a)/steps
    s = f(a)+f(b)
    for j in range(1,steps):
        s += (4 if j%2 else 2)*f(a+h*j)
    return s*h/3

def terms(phi,t):
    c=math.cos(phi); si=math.sin(phi)
    q=c+si
    z=math.sqrt(1+q*q-t*t)
    pos=1-(t+q*z)/(1+q*q)
    neg=(-t+q*z)/(1+q*q)-c/math.sqrt(1+c*c)
    return pos,neg

def gpositive(t):
    return 12/PI*quadrature(lambda phi: terms(phi,t)[0],0,PI/4,3500)

def gnegative(t):
    if t >= TSTAR: return 0.0
    if t<=0: ph=0.0
    else: ph=math.acos(math.sqrt((1-t*t)/(1+t*t)))
    return 12/PI*quadrature(lambda phi: terms(phi,t)[1],ph,PI/4,3500)

def cdf(r):
    if r<=math.sqrt(2): return 0.0
    if r>=math.sqrt(3): return 1.0
    t=math.sqrt(3-r*r)
    return gpositive(t)+gnegative(t)

def direct_radius(u):
    return math.sqrt(max(3-sum(ui*vi for ui,vi in zip(u,v))**2 for v in VERTICES))

def sorted_radius(u):
    a,b,c=sorted(map(abs,u),reverse=True)
    return math.sqrt(3-(a-b-c)**2)

rng=random.Random(20261107)
for _ in range(25000):
    u=[rng.gauss(0,1) for _ in range(3)]
    norm=math.sqrt(sum(x*x for x in u));u=[x/norm for x in u]
    assert abs(direct_radius(u)-sorted_radius(u))<3e-14

assert abs(gpositive(0)+gnegative(0)-1)<1e-10
assert abs(gpositive(1))<1e-10
previous=-1
for j in range(1,160):
    r=math.sqrt(2)+(math.sqrt(3)-math.sqrt(2))*j/160
    f=cdf(r)
    assert f>=previous-2e-12 and 0<=f<=1
    previous=f

N=100000
sample=[]
for _ in range(N):
    u=[rng.gauss(0,1) for _ in range(3)]; norm=math.sqrt(sum(x*x for x in u));u=[x/norm for x in u]
    sample.append(direct_radius(u))
for r in (1.44,1.50,1.58,math.sqrt(8/3),1.68,1.71,1.725):
    theoretical=cdf(r)
    empirical=sum(x<=r for x in sample)/N
    sigma=math.sqrt(theoretical*(1-theoretical)/N)
    assert abs(empirical-theoretical)<=5*sigma+0.001,(r,empirical,theoretical)

for eps in (0.02,0.01,0.005):
    quotient=cdf(math.sqrt(2)+eps)/eps**2
    assert abs(quotient-6/PI)<0.09
for eps in (0.0002,0.00005):
    quotient=(1-cdf(math.sqrt(3)-eps))/math.sqrt(eps)
    assert abs(quotient-4*math.sqrt(2/math.sqrt(3)))<0.08
for eps in (0.02,0.01):
    quotient=gnegative(TSTAR-eps)/eps**2
    assert abs(quotient-9*math.sqrt(3)/(4*PI))<0.025
print('CUBE_SHADOW_RADIUS_PHASE_LAW_OK',N,25000,159)
