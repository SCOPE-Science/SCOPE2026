"""Reproducibility checks for an underdamped chiral active-oscillator dissipation phase diagram.
Run: python CHECKER.py  (requires sympy, mpmath)
"""
from fractions import Fraction
from math import exp, cos, isclose
import sympy as S
import mpmath as mp

w,t,y=S.symbols('w t y', real=True)
F=(w**3-w**2+(w+1)*t)/(w*w+t)**2
N=t**2-6*t*w-w**4+2*w**3
G=t**3+t**2*w**2-4*t**2*w-2*t**2-2*t*w**3-2*t*w-t+w**2
P=t**6-17*t**5+105*t**4+74*t**3+15*t**2-t-1
checks=0

def ck(c, msg):
    global checks
    assert bool(c), msg
    checks+=1

ck(S.factor(S.diff(F,w)-N/(w*w+t)**3)==0,'derivative')
ck(S.factor(S.together(F-F.subs(w,1)).as_numer_denom()[0]-(w-1)*G)==0, 'difference')
ck(S.factor(S.resultant(N,G,w)+16*t**3*(t**2-6*t+1)*P)==0,'resultant')
ck(S.factor(S.diff(P,t,2)-(t**2*(30*t**2-340*t+1260)+444*t+30))==0,'convex')
ck(S.factor(G.subs({w:y+1,t:S.Rational(1,5)})+S.Rational(2,125)*(25*y**3+10*(y-1)**2+2))==0,'boundary comparison')
ck(G.subs({w:S.Rational(3,2),t:S.Rational(19,100)})==S.Rational(106,15625),'interior test')
ck(S.factor(N.subs(w,1)-(t**2-6*t+1))==0,'edge derivative')
ck(S.factor(S.diff(N,w,2)-12*w*(1-w))==0,'concavity')
ck(S.factor(S.factor((w*w+t)**2 * F)-(w**3-w**2+(w+1)*t))==0,'normalized rational')

mp.mp.dps=45
pc=lambda z: z**6-17*z**5+105*z**4+74*z**3+15*z**2-z-1
t0=mp.findroot(pc,(mp.mpf('0.19'),mp.mpf('0.20')))
wc=mp.findroot(lambda z: t0**2-6*t0*z-z**4+2*z**3,(mp.mpf('1.48'),mp.mpf('1.55')))
Fv=lambda q,z:(z**3-z**2+(z+1)*q)/(z*z+q)**2
ck(mp.mpf('0.19')<t0<mp.mpf('0.20'),'root bracket')
ck(mp.mpf('1.5')<wc<mp.mpf('1.52'),'jump bracket')
ck(abs(Fv(t0,wc)-Fv(t0,mp.mpf(1)))<mp.mpf('1e-40'),'equal global candidates')
ck(abs(t0**2-6*t0*wc-wc**4+2*wc**3)<mp.mpf('1e-40'),'critical stationary')
ck(abs(Fv(mp.mpf(0),mp.mpf(2))-mp.mpf('0.25'))<mp.mpf('1e-42'),'achiral optimum')

# Independent stationary moment equations and impulse-response integration.
for d in [0, 0.025, 0.1, 0.8, 1, 2, 5, 11]:
    for om in [0, 0.25, 0.75, 1, 2, 3.5, 6.1]:
        z=complex(d,om)
        moment=(z/(1+z)**2).real
        closed=float(Fv(mp.mpf(str(om*om)),mp.mpf(str(d+1))))
        ck(isclose(moment,closed,rel_tol=4e-13,abs_tol=8e-15),'moment vs rational')
        if d>0:
            exact=mp.quad(lambda s: mp.exp(-(d+1)*s)*(1-s)*mp.cos(om*s),[0, 2, 10, mp.inf])
            ck(abs(exact-closed)<mp.mpf('1e-12'),'time-domain impulse')

# Check the actual maximizing branch for a broad nonuniform grid by exhaustive
# stationary candidates (not used as a proof of infinite-domain assertions).
for tt in ['0','0.01','0.1','0.15','0.1715728752','0.18','0.19','0.190531907893624','0.191','0.195','0.2','0.3','1','3','5.8','5.828427125','5.83','6','10','100']:
    z=mp.mpf(tt)
    roots=[mp.mpf(1)]
    for v in S.nroots(N.subs(t,float(z)),maxsteps=250):
        if abs(float(S.im(v)))<1e-9 and float(S.re(v))>1+1e-12:
            roots.append(mp.mpf(str(S.re(v))))
    vals=[Fv(z,v) for v in roots]
    k=max(range(len(vals)),key=lambda j:vals[j]); optimum=roots[k]
    if z<t0-mp.mpf('1e-9') or z>3+2*mp.sqrt(2)+mp.mpf('1e-9'):
        ck(optimum>1,'interior regime '+tt)
    if z>t0+mp.mpf('1e-9') and z<3+2*mp.sqrt(2)-mp.mpf('1e-9'):
        ck(abs(optimum-1)<mp.mpf('1e-14'),'boundary regime '+tt)

print('PASS',checks,'checks')
print('first_order_t=',mp.nstr(t0,30))
print('jump_to_d=',mp.nstr(wc-1,30))
print('continuous_t=',mp.nstr(3+2*mp.sqrt(2),30))
