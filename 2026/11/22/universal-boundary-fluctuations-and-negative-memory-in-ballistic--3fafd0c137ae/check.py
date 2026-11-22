"""Numerical consistency checks of regenerative ballistic occupation identities."""
import math
import random

rng=random.Random(261116733)

def Gx(u):
    return u*(1-u)/2

def Gupper(u):
    return u/2 if u<=0.5 else (1-u)/2

def integrate_segment_x(T,u0,u1):
    # Integrate (position/L - 1/2) over an interval, with u=elapsed/T.
    a=u0*T;b=u1*T
    return (b-a)/2 - (b*b-a*a)/(2*T)

def integrate_segment_upper(T,u0,u1):
    # Integrate (1_{position/L > 1/2} - 1/2) in a cycle.
    a=u0*T;b=u1*T
    return (min(b,T/2)-min(a,T/2))-(b-a)/2

for g,segment in [(Gx,integrate_segment_x),(Gupper,integrate_segment_upper)]:
    for _ in range(1200):
        # Equilibrium residual for Gamma(2,1) excursion law: length-biased Gamma(3,1).
        T0=sum(rng.expovariate(1) for _ in range(3))
        u0=rng.random()
        h=5*rng.random()
        residual=(1-u0)*T0
        if h<residual:
            got=segment(T0,u0,u0+h/T0)
            endpoint=T0*g(u0+h/T0)-T0*g(u0)
        else:
            got=segment(T0,u0,1)
            tleft=h-residual
            while True:
                T=sum(rng.expovariate(1) for _ in range(2))
                if tleft<T:
                    got+=segment(T,0,tleft/T)
                    endpoint=T*g(tleft/T)-T0*g(u0)
                    break
                got+=segment(T,0,1)
                tleft-=T
        assert abs(got-endpoint)<3e-13,(g,got,endpoint)

# For exponential cycle lengths of rate 2, equilibrium length is Gamma(2,rate 2).
# For normalized position, E G=1/12 and E G^2=1/120.  E T*=2/r, E (T*)^2=6/r^2.
r=2.
variance_V=(6/r**2)/120-(2/r/12)**2
limit_var=2*variance_V
assert abs(limit_var-2/(45*r*r))<1e-14
M=220000
s1=s2=0.0
for _ in range(M):
    t=(rng.expovariate(r)+rng.expovariate(r))
    u=rng.random()
    v=t*Gx(u)
    s1+=v;s2+=v*v
observed=s2/M-(s1/M)**2
assert abs(observed-variance_V)<.0008,(observed,variance_V)
print('PASS: 2400 exact pathwise integrations; exponential moment identity; 220000 equilibrium endpoint samples.')
print('E[V]=',1/(6*r),'Var[V]=',variance_V,'lim H^2 Var(mean normalized position)=',limit_var)
