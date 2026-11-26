"""Exact checks for conditional uniform-circle polygon limit."""
from fractions import Fraction as F
from math import factorial, pi, sin, cos, sqrt
from random import Random

def rising(k, q):
    z=1
    for j in range(q): z*=k+j
    return z

def dirichlet_moment(m, pows):
    # any specified distinct coordinates of symmetric Dirichlet(1,...,1)
    assert m>=len(pows)>=1
    return F(factorial(m-1), factorial(m+sum(pows)-1))*__import__('math').prod(factorial(p) for p in pows)

def cubic_moments(m):
    first=m*dirichlet_moment(m,[3])
    second=m*dirichlet_moment(m,[6])+m*(m-1)*dirichlet_moment(m,[3,3])
    return first, second-first*first

for m in range(2,250):
    e,v=cubic_moments(m)
    assert e==F(6,(m+1)*(m+2))
    assert v==F(72*(m-1)*(5*m+11),(m+1)**2*(m+2)**2*(m+3)*(m+4)*(m+5))
# Tail of the unique circle gap G>pi, conditional on exclusion
for n in range(3,50):
    for q in range(1,5):
        # T=G/pi-1 ~ Beta(1,n-1), E[T^q]=q!/(n)_q
        assert F(factorial(q),rising(n,q))==dirichlet_moment(n,[q])
# Under E, big gap delta=pi*T and other gaps L*V_i,
# V ~ Dirichlet(1,...,1) of length n-1 independently of T.
# Sample checks ensure the numerical formulas for area/perimeter match.
rng=Random(451933)
for n in (3,5,10,30):
    for _ in range(500):
        a=[rng.expovariate(1) for _ in range(n)]
        a=[x/sum(a) for x in a]
        # unconditional sample: geometric formulas for polygon area
        th=[2*pi*x for x in a]
        per=sum(2*sin(x/2) for x in th)
        area=sum(sin(x) for x in th)/2
        assert -1e-12<=area<=pi and 0<per<=2*pi+1e-12
        # independent conditional sampler
        t=1-rng.random()**(1/(n-1))
        delta=pi*t
        y=[rng.expovariate(1) for _ in range(n-1)]
        sy=sum(y)
        small=[(pi-delta)*x/sy for x in y]
        p=2*cos(delta/2)+sum(2*sin(x/2) for x in small)
        aa=(-sin(delta)+sum(sin(x) for x in small))/2
        d=(pi-delta)-sum(2*sin(x/2) for x in small)
        assert abs(p-(2*cos(delta/2)+pi-delta-d))<2e-12
        assert abs((pi/2-aa)-((delta+sin(delta))/2+sum(x-sin(x) for x in small)/2))<2e-12
        assert -1e-12<=d<=pi
print('PASS: 248 exact Dirichlet third-moment identities, 188 beta identities, 2000 geometric double checks')
# Stable conditional Monte Carlo at larger n; report means, no claim of proof.
for n in (70, 200):
    Z=[]
    for rep in range(8000):
        t=1-rng.random()**(1/(n-1)); delta=pi*t; L=pi-delta
        W=[rng.expovariate(1) for _ in range(n-1)]; T=sum(W)
        xs=[L*x/T for x in W]
        # cubic minus fifth expansion cancels loss of floating precision
        D=sum(x**3/24-x**5/1920 for x in xs)
        Z.append(n**2.5*(D - L**3/(4*n*(n+1))))
    avg=sum(Z)/len(Z); v=sum((x-avg)**2 for x in Z)/len(Z)
    print('n',n,'normalized mean',round(avg,2),'variance',round(v,2),'target',round(5*pi**6/8,2))
