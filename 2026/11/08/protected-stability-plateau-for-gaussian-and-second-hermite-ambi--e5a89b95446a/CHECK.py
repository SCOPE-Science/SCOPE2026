"""Reproducibility checks for second-Hermite/Gaussian ambiguity allocation.

Run: python3 CHECK.py. Only Python's standard library is required.
These finite numerical checks supplement, and do not replace, the proof.
"""
from fractions import Fraction
from math import exp, pi, sqrt, cos, sin


def lag(s):
    return 1-2*s+s*s/2


def d(s):
    l=lag(s)
    return 1+2*l*(s-2)-l*l


def f(s,w):
    return exp(-s)*(1-w+w*lag(s)**2)


def bisect(fun,a,b,steps=95):
    ya,yb=fun(a),fun(b)
    assert ya*yb<0, (a,b,ya,yb)
    for _ in range(steps):
        m=(a+b)/2
        if fun(a)*fun(m)<=0:
            b=m
        else:
            a=m
    return (a+b)/2


# All required polynomial identities are checked over exact rationals.
for q in range(-12,81):
    s=Fraction(q,7)
    l=lag(s)
    assert l*l-1 == s*(s-4)*(s-2)**2/4
    deriv_d=2*(s-2)**2+2*l-2*l*(s-2)
    assert deriv_d == -(s-1)*(s*s-8*s+14)
    assert d(s)-4 == -(s-4)*(s**3-8*s*s+12*s-8)/4

r=bisect(lambda s:s**3-8*s*s+12*s-8,6,7)
T0=bisect(lambda t:f(t,.25)-exp(-4),8,10)
assert 6<r<7 and 8.83<T0<8.84

# On the protected plateau the constant-weight graph reaches its minimum at s=4.
for T in [4,4.01,4.5,6,8,T0]:
    for k in range(2001):
        s=T*k/2000
        assert f(s,.25)>=exp(-4)-2e-14

# Unique mixed solution: active interior radius and outer boundary have equal gain.
splus=2+sqrt(2)

def s_active(w):
    assert .25<w<1
    return bisect(lambda s:d(s)-1/w,splus,4)


def optimum(T):
    assert T>T0
    w=bisect(lambda w:f(s_active(w),w)-f(T,w),.25000000001,.99999999999)
    z=s_active(w)
    return w,z,f(T,w)

for T in [8.84,9,10,12,16,20,25]:
    w,z,gain=optimum(T)
    assert .25<w<1 and splus<z<4
    assert abs(f(z,w)-gain)<2e-11
    for k in range(2401):
        s=T*k/2400
        assert f(s,w)>=gain-2e-11, (T,w,s,gain,f(s,w))
    # Supremal-envelope check: sampled other allocations never improve it.
    for j in range(201):
        v=j/200
        sample_min=min(f(T*k/1000,v) for k in range(1001))
        assert sample_min<=gain+2e-6, (T,v,gain,sample_min)

for T in [22,26,30]:
    w,z,gain=optimum(T)
    assert abs((gain*exp(T)/T**4)-.25)<.14
    assert abs((1-w)/(exp(splus-T)*lag(T)**2)-1)<.015

# Direct centered ambiguity integration for normalized h_2.
def h2(t):
    return (2**.25)*(4*pi*t*t-1)/sqrt(2)*exp(-pi*t*t)

def midpoint_ambiguity(x,y,N=10000):
    lo,hi=-7.0,7.0
    dt=(hi-lo)/N
    a=0j
    for k in range(N):
        t=lo+(k+.5)*dt
        h=h2(t+x/2)*h2(t-x/2)
        a+=h*complex(cos(2*pi*y*t),-sin(2*pi*y*t))
    return a*dt
for x,y in [(0.,0.),(.3,.6),(1.,.2),(-.8,1.3),(1.2,-.7)]:
    s=pi*(x*x+y*y)
    exact=exp(-s/2)*lag(s)
    est=midpoint_ambiguity(x,y)
    assert abs(est-exact)<1e-10,(x,y,est,exact)

# The isolated T=2 degeneracy is not incorrectly called a unique Gaussian optimum.
def eta_fun(s):
    return 4*(1-exp(s-2))/(s*(4-s)*(s-2)**2)
a,b=.35,1.1
for k in range(105):
    m1=a+(b-a)/3
    m2=b-(b-a)/3
    if eta_fun(m1)<eta_fun(m2): b=m2
    else: a=m1
eta=eta_fun((a+b)/2)
assert .74518<eta<.74519
assert abs(f(2,eta)-exp(-2))<1e-14
for i in range(1001):
    s=2*i/1000
    assert f(s,eta)>=exp(-2)-1e-13

print('ALL_SECOND_HERMITE_PLATEAU_CHECKS_PASSED')
print('protected_outer_radius=',format(T0,'.12f'))
for T in [9,10,12,16]:
    w,z,gain=optimum(T)
    print('T=',T,'w=',round(w,10),'active_radius=',round(z,10),'margin=',round(gain,12))
