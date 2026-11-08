"""Standalone numerical checks of exact scalar hybrid-neuron bifurcation formulas."""
import math

def parameters(a,theta,g):
    E=math.exp(-a);F=math.exp(-a*theta);h=g/a
    return E,F,h

def implicit_u(x,a,theta,g):
    E,F,h=parameters(a,theta,g); b=h*(1-F)
    # monotonic equation u + b tanh u = F*x; interval bracket suffices
    lo=min(0.0,F*x);hi=max(0.0,F*x)
    for _ in range(65):
        mid=(lo+hi)/2
        if mid+b*math.tanh(mid)<F*x:lo=mid
        else:hi=mid
    return (lo+hi)/2

def P(x,a,theta,g):
    E,F,h=parameters(a,theta,g);return E*x-h*(1-E)*math.tanh(implicit_u(x,a,theta,g))

def PM(x,a,theta,g):
    E,F,h=parameters(a,theta,g);u=implicit_u(x,a,theta,g);s=1/math.cosh(u)**2
    return E-h*(1-E)*F*s/(1+h*(1-F)*s)

def gc(a,theta):
    E=math.exp(-a);F=math.exp(-a*theta)
    delta=2*F-1-E
    return a*(1+E)/delta

def c_analytic(a,theta,g):
    E=math.exp(-a);F=math.exp(-a*theta)
    C=(2*F-1-E)/(1-E);r=gc(a,theta)/g
    lo=0;hi=1
    while math.tanh(C*hi)/(C*hi)>r:hi*=2
    for _ in range(75):
        m=(lo+hi)/2
        if math.tanh(C*m)/(C*m)>r:lo=m
        else:hi=m
    return (lo+hi)/2

passes=0
for a in (0.25, 0.8, 2.1, 4.0):
    star=-math.log((1+math.exp(-a))/2)/a
    for theta in (0,star/2,star*0.95):
        gcrit=gc(a,theta)
        for ratio in (0.5,0.9,1.0,1.02,1.5,3.0):
            gain=gcrit*ratio
            E,F,h=parameters(a,theta,gain)
            M=(E-h*(1-E)*F/(1+h*(1-F)))
            assert abs(M-PM(0,a,theta,gain))<1e-13
            for x in (0.01,0.3,1.0,4.0):
                assert abs(P(-x,a,theta,gain)+P(x,a,theta,gain))<1e-13
                if ratio<=1:assert abs(P(x,a,theta,gain))<x
                if ratio>1:
                    c=c_analytic(a,theta,gain)
                    assert abs(P(c,a,theta,gain)+c)<1e-11
                    assert -1<PM(c,a,theta,gain)<1
                passes+=1
    for theta in (star, (star+1)/2, 1.0):
        for gain in (0.01,1,10,1000):
            E,F,h=parameters(a,theta,gain)
            assert -1<PM(0,a,theta,gain)<1
            for x in (.001,.8,5,100):assert abs(P(x,a,theta,gain))<x
            passes+=1

# Check critical algebraic k^-1/2 convergence using long orbits started near zero.
for a,theta in ((1,.1),(2,.0),(3,.1)):
    gain=gc(a,theta);E,F,h=parameters(a,theta,gain)
    K=h*(1-E)*F**3/(3*(1+h*(1-F))**4)
    x=.35
    for i in range(1,35001):x=P(x,a,theta,gain)
    assert abs((2*K*35000)*x*x-1)<.08,(a,theta,x,K)
    passes+=1
print(f'VERIFY_OK parameter_checks={passes} critical_algebraic_cases=3')
