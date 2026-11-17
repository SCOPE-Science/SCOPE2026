#!/usr/bin/env python3
"""Independent reproducible checks of a horocyclic three-terminal Steiner law.
Numeric tests support but do not replace the analytic proof in RESULT.md.
Uses only Python's standard library.
"""
import math, random
RT3=math.sqrt(3.0)
L1=4/RT3
L2=2*RT3
I=8*math.log(2)/3-1
B=RT3*(15-16*math.log(2))/9

def simpson(f,lo,hi,N=20000):
    if lo>=hi:return 0.0
    h=(hi-lo)/N
    total=f(lo)+f(hi)
    for j in range(1,N):total+=(4 if j%2 else 2)*f(lo+j*h)
    return h*total/3

def span(s):
    if s<=0 or s>=RT3:return 0.0
    if s<=2/RT3:return s
    return s-math.sqrt(max(0,s*s+4*s/RT3-4))

def p_exact(L):
    if L<=L1:return 1.0
    if L>=L2:return (24*I)/L**2-(48*B)/L**3
    if L>3.0:
        t=L/2
        extra=simpson(lambda s:2*(s-t)*span(s),t,RT3,40000)
        return (24*I)/L**2-(48*B)/L**3+24*extra/L**3
    s0=2/RT3
    # robust complement in crossover when close to first threshold
    fail=simpson(lambda s:(L-2*s)*math.sqrt(max(0,s*s+4*s/RT3-4)),s0,L/2,40000)
    return 1-24*fail/L**3

def p_integral(L):
    a=min(L/2,2/RT3)
    b=min(L/2,RT3)
    return 24/L**3*(simpson(lambda s:(L-2*s)*s,0,a,20000)
                 +simpson(lambda s:(L-2*s)*span(s),a,b,20000))

def angle_cosh(a,b):
    def ch(x):return 1+x*x/2
    numer=ch(a)*ch(b)-ch(a+b)
    denom=math.sqrt(ch(a)**2-1)*math.sqrt(ch(b)**2-1)
    return math.acos(max(-1,min(1,numer/denom)))

def angle_from_tangent(a,b):
    return math.pi-math.atan(a/2)-math.atan(b/2)

for L in [0.1,1.2,L1, L1+0.01,L1+0.15,3,3.3,L2,L2+0.1,4,6,10,50]:
    x=p_exact(L); y=p_integral(L)
    assert abs(x-y)<2e-8,(L,x,y)
    assert 0<x<=1,(L,x)
for a,b in [(.1,.2),(.5,2),(1,1),(2,5),(0.01,.1),(1,8)]:
    assert abs(angle_cosh(a,b)-angle_from_tangent(a,b))<1e-10
assert abs(simpson(lambda u:(RT3-u)/(1+RT3*u),0,RT3)-I)<1e-10
assert abs(simpson(lambda u:2*u*(RT3-u)/(1+RT3*u),0,RT3)-B)<1e-10
c=3**1.25/10
for d in [0.02,0.002,0.0002]:
    r=(1-p_exact(L1+d))/d**2.5
    assert abs(r/c-1)<1.5*d,(d,r,c)
for d in [0.03,0.01,0.003]:
    L=L2-d
    pp=(24*I)/L**2-(48*B)/L**3
    ratio=(p_exact(L)-pp)/d**3
    assert abs(ratio*36*RT3-1)<3*d,(d,ratio)
random.seed(114026)
for L in [2.0,2.75,3.3,5.0,10.0]:
    N=120000
    count=0
    for i in range(N):
        x,y,z=sorted(random.random()*L for j in range(3))
        count += angle_cosh(y-x,z-y)>=2*math.pi/3
    obs=count/N; expect=p_exact(L)
    sigma=math.sqrt(expect*(1-expect)/N)
    assert abs(obs-expect)<6*sigma+0.002,(L,obs,expect)
    print('L=',L,'direct_angle_sample=',round(obs,6),'exact=',round(expect,6))
print('HOROCYCLE_STEINER_TWO_THRESHOLDS_CHECKS_OK')
