"""Deterministic numerical checks of annular line-intercept formulas."""
import math
from scipy.integrate import quad
from scipy.special import ellipk,ellipe

def length(r,s):
    if s < r:
        return 2*(math.sqrt(1-s*s)-math.sqrt(r*r-s*s))
    return 2*math.sqrt(1-s*s)

def survival(r,z):
    peak=2*math.sqrt(1-r*r)
    if z<=0: return 1.
    if z>=peak: return 0.
    outer=math.sqrt(1-z*z/4)
    if z <= 2*(1-r): return outer
    q=z/2
    a=(q+(1-r*r)/q)/2
    inner=math.sqrt(max(0.,1-a*a))
    return outer-inner

def moment(r,p):
    d=1-r
    fun=lambda s:(length(r,s)/(2*d))**p
    return quad(fun,0,r,epsabs=1e-10,epsrel=1e-10,limit=500)[0]+quad(fun,r,1,epsabs=1e-10,epsrel=1e-10,limit=500)[0]

checks=0
for r in [0.12,0.38,0.7,0.95]:
    peak=2*math.sqrt(1-r*r)
    for z in [peak*i/24 for i in range(1,24)]:
        direct=sum(length(r,(k+0.5)/200000)>z for k in range(200000))/200000
        assert abs(direct-survival(r,z)) < 2e-5,(r,z,direct,survival(r,z))
        checks+=1
    ex=quad(lambda s:length(r,s),0,r)[0]+quad(lambda s:length(r,s),r,1)[0]
    assert abs(ex-math.pi*(1-r*r)/2)<1e-8
    checks+=1
    m2=moment(r,2)
    formula=(2/3)*(1+r**3-(1+r*r)*ellipe(r*r)+(1-r*r)*ellipk(r*r))/(1-r)**2
    assert abs(m2-formula)<1e-7,(r,m2,formula)
    checks+=1

for d in [0.03,0.008,0.002]:
    r=1-d
    asym=0.5*math.log(1/d)+math.log(2*math.sqrt(2))+0.75
    assert abs(moment(r,2)-asym) < 0.15
    checks+=1
    for t in [0.4,0.9,1.2]:
        z=2*t*math.sqrt(d)
        if z < 2*math.sqrt(1-r*r):
            G=0.5/(t*t)+0.5-3*t*t/8
            assert abs(survival(r,z)/d-G)<0.4,(d,t,survival(r,z)/d,G)
            checks+=1

for d in [0.04,0.01,0.002]:
    p=4
    scaled=d**(p/2-1)*moment(1-d,p)
    assert abs(scaled-2)<0.4,(d,scaled)
    checks+=1
print(f'PASS {checks} deterministic checks')
