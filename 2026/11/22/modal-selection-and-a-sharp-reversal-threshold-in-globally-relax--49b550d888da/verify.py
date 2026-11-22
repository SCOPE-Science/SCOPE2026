"""Exact-rational and direct-matrix checks for globally relaxed RK4 oscillator selection.
Run: python verify.py
All tested identities are proved separately in the accompanying manuscript.
"""
from fractions import Fraction as F
import math

checks = 0

def ck(cond, message):
    global checks
    assert cond, message
    checks += 1

def D(t): return t*t*t - 8*t*t - 48*t + 576

def q(t): return t * D(t) / F(576)

def gamma(t): return F(48)*(12-t) / D(t)

def Q(t): return 1 + t**3*(t-8)/F(576)

def global_gamma(ts, energies):
    return sum((e*q(t)*gamma(t) for e,t in zip(energies,ts)),F(0)) / sum((e*q(t) for e,t in zip(energies,ts)),F(0))

def energy_step(ts, en):
    g=global_gamma(ts,en)
    return [e*(1+q(t)*g*(g-gamma(t))) for e,t in zip(en,ts)]

# Exact algebra for the benchmark and rational crossover.
t=F(197,100)
t2=4*t
P=lambda r,z:(r*r+r)*z*z-(12*r*r+20*r+12)*z+96*(r+1)
ck(P(F(4),t)==F(-931,500), 'quadratic threshold sign') # -931/2000
ck(gamma(t)>gamma(t2), 'relaxation chooses high mode')
ck(Q(t)>Q(t2), 'radial correction chooses low mode')
ck(F(168,85)>t and t2<F(8), 'within RK4 stability window')
ck(gamma(F(1))==F(528,521), 'gamma(1)')
ck(gamma(F(4))==F(6,5), 'gamma(2)')
ck(q(F(4))==F(20,9), 'squared RK increment')
ck(1+q(F(4))*gamma(F(1))*(gamma(F(1))-gamma(F(4)))==F(157393,271441), 'sharp loser-rate')

# Exact energy preservation and monotone energy-weighted gamma potential on rational tests.
configurations=[([F(1),F(4)],[F(1),F(1)]),
                ([F(1,2),F(4),F(7)],[F(1,3),F(2,5),F(1,7)]),
                ([F(197,100),F(197,25)],[F(3,5),F(2,7)]),
                ([F(3,4),F(13,4),F(9)],[F(3,4),F(5,6),F(4,7)])]
for ts,en in configurations:
    for step in range(4):
        ck(all(F(0)<u<F(12) for u in ts),'scope')
        g=global_gamma(ts,en)
        ck(min(gamma(u) for u in ts)<=g<=max(gamma(u) for u in ts),'convex combination gamma')
        before=sum(en)
        potential=sum((e*gamma(u) for e,u in zip(en,ts)),F(0))
        en2=energy_step(ts,en)
        ck(all(e>=0 for e in en2),'positive energy')
        ck(sum(en2)==before,'exact energy conservation')
        potential2=sum((e*gamma(u) for e,u in zip(en2,ts)),F(0))
        ck(potential2<=potential,'Lyapunov decline')
        ck(potential2==potential or len(set(gamma(u) for u,e in zip(ts,en) if e))>1,'strictness characterization')
        en=en2

# Floating-point direct RK4 stages versus modal recursion, independently implemented.
def rk4_increment(z,w,h):
    f=lambda zz: 1j*w*zz
    k1=f(z)
    k2=f(z+h*k1/2)
    k3=f(z+h*k2/2)
    k4=f(z+h*k3)
    return h*(k1+2*k2+2*k3+k4)/6
for h in (0.4,0.8,1.0,1.4,1.68):
    zz=[complex(0.5,1.25),complex(-1.25,0.3),complex(1.3,-0.7)]
    ww=[0.7,1.1,2.0]
    ts=[F.from_float((w*h)**2) for w in ww]
    old=[abs(z)**2 for z in zz]
    dd=[rk4_increment(z,w,h) for z,w in zip(zz,ww)]
    g=-2*sum((z.conjugate()*d).real for z,d in zip(zz,dd))/sum(abs(d)**2 for d in dd)
    gg=float(global_gamma(ts,list(map(F.from_float,old))))
    ck(abs(g-gg)<5e-13,'direct RK4 relaxation gamma')
    updated=[z+g*d for z,d in zip(zz,dd)]
    en2=energy_step(ts,list(map(F.from_float,old)))
    ck(all(abs(abs(z)**2-float(e))<1e-12 for z,e in zip(updated,en2)),'direct RK4 modal updates')
    ck(abs(sum(abs(z)**2 for z in updated)-sum(old))<1e-12,'direct energy preservation')

# Long-time dynamics and sharp winner switching.
for h in (1.0, 1.35, 1.45, 1.68):
    ts=[h*h,4*h*h]
    ens=[1.,2.]
    gammas=[float(gamma(F.from_float(t))) for t in ts]
    expected_winner=gammas.index(min(gammas))
    for _ in range(450):
        qv=[float(q(F.from_float(t))) for t in ts]
        g=sum(e*x*y for e,x,y in zip(ens,qv,gammas))/sum(e*x for e,x in zip(ens,qv))
        ens=[e*(1+x*g*(g-y)) for e,x,y in zip(ens,qv,gammas)]
    ck(abs(sum(ens)-3.)<5e-10,'long-run energy')
    ck(ens[expected_winner]>2.9999,'winner-takes-all')
print('VERIFY_OK',checks,'checks')
