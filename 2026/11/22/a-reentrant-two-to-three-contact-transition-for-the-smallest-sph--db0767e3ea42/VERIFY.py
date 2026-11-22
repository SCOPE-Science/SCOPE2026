"""Standalone numerical checks for the minimum covering sphere of a circular helical arc.

All decisive assertions are proved analytically in RESULT.md; this checker tests formulas,
contact sets, phase transitions and the two-root pitch window on dense finite grids.
"""
import math
import random

PI=math.pi

def threshold_squared(L):
    if L<=PI/2:
        return 0.0
    c=math.cos(L)
    return -2*c*(1-c)/(L*L)

def center_radius(L,eta):
    c=math.cos(L)
    k=(eta*L)**2
    v=-k/(2*(1-c))
    x=max(c,v)
    r2=1+x*x+k-2*x*c if x>v+1e-14 else (1-x)**2
    return x,math.sqrt(r2),x<=v+1e-14

def dist2(L,eta,x,t):
    return 1+x*x-2*x*math.cos(t)+(eta*t)**2

def bisection(fun,l,r,n=100):
    a=fun(l)
    b=fun(r)
    assert a*b<0
    for _ in range(n):
        mid=(l+r)/2
        fm=fun(mid)
        if fm*a>0:
            l=mid; a=fm
        else:
            r=mid
    return (l+r)/2

logqprime=lambda L:-math.tan(L)+1/math.tan(L/2)-2/L
Lstar=bisection(logqprime,2.2,3.)
etamax=math.sqrt(threshold_squared(Lstar))
assert abs(Lstar-2.67077808908704)<2e-11
assert abs(etamax-0.687437444831901)<2e-11
assert abs(threshold_squared(PI)-(2/PI)**2)<1e-13

# Both roots for a pitch between 2/pi and the maximum: the three-contact phase
# appears and then disappears as the arc approaches a complete turn.
reentrant_pitch=0.65
eta=reentrant_pitch
Lminus=bisection(lambda L:threshold_squared(L)-eta**2,1.7,2.5)
Lplus=bisection(lambda L:threshold_squared(L)-eta**2,2.8,PI)
assert abs(Lminus-2.30957875155775)<2e-10
assert abs(Lplus-3.07120882676805)<2e-10
assert center_radius(2.5,eta)[2]
assert not center_radius(PI,eta)[2]
assert not center_radius(2.1,eta)[2]

# Independently check the formula against the unminimized max over a 1D
# center mesh and against the actual curve at 1201 parameter values.
rng=random.Random(20261115)
cases=[(0.5,0.12),(PI/2,0.2),(1.85,0.1),(2.5,0.65),(2.7,0.8),
       (PI,0.5),(PI,0.65),(PI,1.4),(Lminus,eta),(Lplus,eta),
       (Lstar,etamax)]
cases += [(rng.uniform(0.09,PI),rng.uniform(0.03,1.5)) for _ in range(85)]
point_tests=0
center_tests=0
for L,eta in cases:
    x,r,three=center_radius(L,eta)
    c=math.cos(L)
    k=(eta*L)**2
    # Alternate direct minimax evaluation of the two boundary quadratics.
    boundary=lambda u:max((1-u)**2,1+u*u+k-2*u*c)
    assert abs(boundary(x)-r*r)<2e-10
    for j in range(1201):
        t=L*(2*j/1200-1)
        assert dist2(L,eta,x,t)<=r*r+3e-12
        point_tests+=1
    assert abs(dist2(L,eta,x,L)-r*r)<4e-12
    assert abs(dist2(L,eta,x,-L)-r*r)<4e-12
    gap=dist2(L,eta,x,0)-r*r
    assert gap<1e-10 if three else gap < -1e-9 or abs(gap)<1e-9
    for j in range(121):
        testx=x+(j-60)*0.025
        assert boundary(testx)>=boundary(x)-3e-12
        center_tests+=1
# Verify limiting one-sided second derivative of radius with respect to k.
L=2.5
c=math.cos(L)
d=1-c
k0=-2*c*d
for h in [0.01,0.001,0.0001]:
    rleft=lambda k: 1+k/(2*d)
    rright=lambda k: math.sqrt(1-c*c+k)
    dl=(rleft(k0)-2*rleft(k0-h)+rleft(k0-2*h))/(h*h)
    dr=(rright(k0+2*h)-2*rright(k0+h)+rright(k0))/(h*h)
    assert abs(dl)<1e-6
    assert abs(dr+1/(4*d**3))<0.02
print('HELIX_ENCLOSING_BALL_REENTRANT_CHECKS_OK')
print('parameter_cases=',len(cases),'curve_evaluations=',point_tests,'center_inequalities=',center_tests)
print('critical_halfspan=',format(Lstar,'.15f'),'critical_pitch=',format(etamax,'.15f'))
print('reentrant_pitch=',reentrant_pitch,'halfspan_roots=',format(Lminus,'.12f'),format(Lplus,'.12f'))
