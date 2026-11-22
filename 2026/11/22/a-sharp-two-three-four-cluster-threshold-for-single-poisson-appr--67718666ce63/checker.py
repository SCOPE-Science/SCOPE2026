"""Numerical diagnostics for an exact Poisson-mixture compression theorem.

Finite tests check derived formulas and boundary behavior; they do not prove
continuous-parameter statements. Run: python3 checker.py (stdlib only).
"""
import cmath
import math

count = 0

def near(a, b, tol=1e-9):
    global count
    assert abs(a-b) <= tol * max(1.0, abs(a), abs(b)), (a,b,tol)
    count += 1

def g(m, r, s):
    v=(r*s)**m
    return s*s/(1-s*s)-2*v/(1-v)

def p(r, theta):
    return (1-r*r)/(1-2*r*math.cos(theta)+r*r)

def objective_integral(m, r, s, phi, steps=4096):
    delta=2*math.pi/steps
    out=0.0
    for k in range(steps):
        theta=(k+0.5)*delta
        target=sum(p(r,theta-2*math.pi*j/m) for j in range(m))/m
        diff=target-p(s,theta-phi)
        out+=diff*diff
    return out/steps

def exact_difference(m,r,s,phi):
    v=(r*s)**m
    overlap=(v*math.cos(m*phi)-v*v)/(1-2*v*math.cos(m*phi)+v*v)
    return 2*s*s/(1-s*s)-4*overlap

uc=3*math.sqrt(6)/8
rc=uc**(1/3)
sc=math.sqrt(2/3)
near(uc*sc**3, 0.5,1e-13)
near(2*sc-sc**3,1/uc,1e-13)
near(-1+5*sc**2-5*uc*sc**3+uc*sc**5,1/6,1e-13)

# Check the independently evaluated angular integral against the Fourier formula.
for m in (2,3,4,5,8):
    for r in (.25,.72,.9,.975):
        for s in (.15,.52,.82):
            baseline=objective_integral(m,r,0,0)
            for phi in (0,.17,.61,math.pi/m):
                difference=objective_integral(m,r,s,phi)-baseline
                near(difference,exact_difference(m,r,s,phi),3e-9)
                if phi==0:
                    near(difference,2*g(m,r,s),3e-9)

# Exact root formula for the two-component positive-radius regime.
for r in (.72,.8,.9,.98):
    u=r*r
    s=math.sqrt((math.sqrt(2*u)-1)/(math.sqrt(2*u)-u))
    dt=1e-6
    near((g(2,r,math.sqrt(s*s+dt))-g(2,r,math.sqrt(s*s-dt)))/(2*dt),0,3e-6)
    for perturbation in (.0001,.005):
        if s+perturbation<1:
            assert g(2,r,s)<g(2,r,s+perturbation)
            count+=1
        if s>perturbation:
            assert g(2,r,s)<g(2,r,s-perturbation)
            count+=1

# Test both phase boundaries and the four-or-more uniform barrier.
for r in (.05,.6,.8,.95,rc-.0003,rc,rc+.0003,.999):
    for m in (4,5,7,12):
        for k in range(1,300):
            s=k/300
            assert g(m,r,s)>0
            count+=1
for r in (.1,.7,rc-.002):
    for k in range(1,300):
        assert g(3,r,k/300)>0
        count+=1
near(g(3,rc,sc),0,1e-11)
assert g(3,(uc+.002)**(1/3),sc)<0
count+=1

# Critical scalings are limits, so tolerate the predicted next-order remainder.
for delta in (1e-3,1e-4,1e-5):
    u=.5+delta
    r=math.sqrt(u)
    t=(math.sqrt(2*u)-1)/(math.sqrt(2*u)-u)
    near(t/delta,2,4e-3)
    near(2*g(2,r,math.sqrt(t))/delta**2,-4,7e-3)
for eta in (1e-3,1e-4,1e-5):
    u=uc+eta
    r=u**(1/3)
    # locate the unique local minimum to the right of the universal jump point
    lo,hi=sc,.99999
    for _ in range(100):
        a=lo+(hi-lo)/3
        b=hi-(hi-lo)/3
        if g(3,r,a)<g(3,r,b): hi=b
        else: lo=a
    s=(lo+hi)/2
    assert s>=sc and g(3,r,s)<0
    count+=1
    near(2*g(3,r,s)/eta,-32*math.sqrt(6)/9,2e-2 if eta==1e-3 else 3e-3)

print(f'PASS: {count} finite diagnostics; analytic proof required for all-parameter conclusions')
