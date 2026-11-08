"""Independent numerical checks of the equiaffine ellipse acute-triangle law."""
import math
import random

PI=math.pi

def dilog_series(z):
    if z==1:
        return PI*PI/6
    s=0.; p=1.
    for n in range(1,120001):
        p*=z
        v=p/(n*n)
        s+=v
        if abs(v)<1e-16:
            break
    return s

def theorem(a,b):
    eta=abs(a*a-b*b)/(a*a+b*b)
    return .25-3/(2*PI*PI)*dilog_series(eta*eta)

def simpson(f,lo,hi,n=20000):
    assert n%2==0
    h=(hi-lo)/n
    s=f(lo)+f(hi)
    for j in range(1,n):
        s+=(4 if j%2 else 2)*f(lo+j*h)
    return s*h/3

def conditioned(a,b):
    eta=abs(a*a-b*b)/(a*a+b*b)
    if eta==0: return .25
    def q(w):
        v=math.cos(w/2)/eta
        if v>=1:return 0.
        if v<=-1:return 1.
        return math.acos(v)/PI
    # Split at the two threshold angles for accurate quadrature.
    lo=2*math.acos(eta); hi=2*PI-lo
    width=hi-lo
    def f(t):
        w=lo+width*math.sin(t)**2
        return (2*PI-w)*q(w)*2*width*math.sin(t)*math.cos(t)
    s=simpson(f,0,PI/2)
    s+=(2*PI-hi)**2/2
    p_obtuse=s/(2*PI*PI)
    return 1-3*p_obtuse

def arcsin_integral(a,b):
    eta=abs(a*a-b*b)/(a*a+b*b)
    value=simpson(lambda t:math.asin(eta*math.sin(t))**2,0,PI/2)
    return .25-6/PI**3*value

def monte_carlo(a,b,n=160000,seed=0):
    rng=random.Random(seed)
    good=0
    for _ in range(n):
        t=[rng.random()*2*PI for _ in range(3)]
        v=[(a*math.cos(x),b*math.sin(x)) for x in t]
        acute=True
        for i in range(3):
            p=v[i]; q=v[(i+1)%3]; r=v[(i+2)%3]
            if (q[0]-p[0])*(r[0]-p[0])+(q[1]-p[1])*(r[1]-p[1])<=0:
                acute=False
                break
        good+=acute
    return good/n

for a,b in [(1.,1.),(1.5,1.),(2.,1.),(4.,1.),(10.,1.)]:
    exact=theorem(a,b)
    one=conditioned(a,b)
    other=arcsin_integral(a,b)
    assert abs(exact-one)<1e-9,(a,b,exact,one)
    assert abs(exact-other)<1e-10,(a,b,exact,other)
    mc=monte_carlo(a,b,seed=int(a*1000))
    assert abs(mc-exact)<.007,(a,b,mc,exact)
    print(f'axes=({a:g},{b:g}) law={exact:.12f} conditioned={one:.12f} arcsin={other:.12f} direct={mc:.6f}')
for n in (1,2,3,8):
    assert abs(simpson(lambda t:math.sin(t)**(2*n),0,PI/2,8000)
          - PI/2*math.comb(2*n,n)/4**n)<1e-12
print('ELLIPSE_ACUTE_CHECK_OK formulas=5 direct_samples=800000')
