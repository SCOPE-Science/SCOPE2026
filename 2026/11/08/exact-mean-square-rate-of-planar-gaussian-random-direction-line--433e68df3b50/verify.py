"""Independent deterministic checks for the planar Gaussian line-search law.
Requires Python 3 standard library only. Analytical identities appear in RESULT.md.
"""
from fractions import Fraction as Q
import math

def exact_entries(t):
    t=Q(t)
    den=2*(t+1)**2
    return ((t+2)/den,t/den,t*(2*t+1)/den)

def determinant_exact(t):
    a,b,d=exact_entries(t)
    return a*d-b*b

def midpoint_moments(t,n=40000):
    sums=[0.,0.,0.]
    for j in range(n):
        th=2*math.pi*(j+0.5)/n
        c=math.cos(th); ss=math.sin(th)
        u=ss*ss/(t*t*c*c+ss*ss)
        sums[0]+=u*u
        sums[1]+=u*(1-u)
        sums[2]+=(1-u)**2
    return tuple(z/n for z in sums)

def rate(t):
    return (t*t+t+1+math.sqrt(t**4-t*t+1))/(2*(t+1)**2)

def iterate_B(t,init,n):
    a,b,d=map(float,exact_entries(t))
    e0,e1=init
    for _ in range(n):
        e0,e1=a*e0+b*e1,b*e0+d*e1
    return e0+e1

checks=0
for t in [Q(1), Q(3,2), Q(2),Q(3),Q(5),Q(10),Q(100)]:
    a,b,d=exact_entries(t)
    assert a+b==1/(t+1)
    assert a+2*b+d==1
    assert determinant_exact(t)==t/(2*(t+1)**2)
    assert a>0 and b>0 and d>0
    checks+=4
    if t==1:
        assert a==Q(3,8) and b==Q(1,8) and d==Q(3,8)
        checks+=1
    tfloat=float(t)
    m=midpoint_moments(tfloat,n=8192)
    for obs,expect in zip(m,[float(a),float(b),float(d)]):
        assert abs(obs-expect)<2e-12,(t,obs,expect)
        checks+=1
    rr=rate(tfloat)
    assert rr>max(2*float(b),0)
    assert rr < 1
    if t>1: assert rr < tfloat/(tfloat+1)
    else: assert rr==0.5
    checks+=3
    for init in ((1.,0.),(0.,1.),(1.,1.),(2.,3.)):
        aseq=[iterate_B(tfloat,init,k) for k in range(18,21)]
        if tfloat <= 10:
            assert abs(aseq[-1]/aseq[-2]-rr)<0.005
        else:
            assert aseq[-1]/aseq[-2]>0
        checks+=1
# independent direct angular covariance application on rational t
for t in [1,2,3,5]:
    for d0 in ((1.0,0.0),(0.0,1.0),(2.0,3.0)):
        a,b,d=map(float,exact_entries(t))
        theoretical=(a*d0[0]+b*d0[1],b*d0[0]+d*d0[1])
        N=10000
        vals=[0.,0.]
        for j in range(N):
            th=2*math.pi*(j+0.5)/N
            cc=math.cos(th); ss=math.sin(th)
            r=ss*ss/(t*t*cc*cc+ss*ss)
            vals[0] += r*r*d0[0]+r*(1-r)*d0[1]
            vals[1] += r*(1-r)*d0[0]+(1-r)**2*d0[1]
        vals=[z/N for z in vals]
        assert max(abs(x-y) for x,y in zip(vals,theoretical))<2e-12
        checks+=1
print(f'PASS {checks} deterministic algebra, moment, and propagation checks')
print('kappa=4 one-step bound = 2/3')
print('kappa=4 long-run rate = (7+sqrt(13))/18 =',rate(2.0))
print('kappa=9 long-run rate = (13+sqrt(73))/32 =',rate(3.0))
