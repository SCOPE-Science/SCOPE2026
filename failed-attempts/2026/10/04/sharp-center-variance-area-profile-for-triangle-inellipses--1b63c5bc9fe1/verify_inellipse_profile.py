#!/usr/bin/env python3
import math, random

def profiles(r):
    upper=(1-r)*math.sqrt(1+2*r)
    lower=(1+r)*math.sqrt(max(0.0,1-2*r)) if r <= 0.5 else 0.0
    return lower,upper

def eta_xyz(x,y,z):
    return math.sqrt(max(0.0,27*x*y*z))

def q_from_center(t,u,v):
    return (t-u)**2+(u-v)**2+(v-t)**2

max_det_err=0.0
max_profile_violation=0.0
max_stability_violation=0.0
max_branch_err=0.0
rng=random.Random(20261001)

# Support-matrix determinant versus the closed area factor, H=1.
for _ in range(20000):
    a,b,c=[rng.expovariate(1.0) for _ in range(3)]
    s=a+b+c
    x,y,z=a/s,b/s,c/s
    t,u,v=(1-x)/2,(1-y)/2,(1-z)/2
    d1,d2,d3=t,u,v
    A=d1*d1
    B=(d3*d3-d2*d2)/math.sqrt(3.0)
    C=(2.0/3.0)*(d2*d2+d3*d3)-(1.0/3.0)*d1*d1
    det=A*C-B*B
    target=((1-2*t)*(1-2*u)*(1-2*v))/3.0
    max_det_err=max(max_det_err,abs(det-target))

# Exact equality branches and dense fixed-r circles in the simplex.
for k in range(1000):
    r=0.999*k/999.0
    lo,up=profiles(r)
    xu,yu,zu=(1+2*r)/3,(1-r)/3,(1-r)/3
    max_branch_err=max(max_branch_err,abs(eta_xyz(xu,yu,zu)-up))
    if r < 0.5:
        xl,yl,zl=(1-2*r)/3,(1+r)/3,(1+r)/3
        max_branch_err=max(max_branch_err,abs(eta_xyz(xl,yl,zl)-lo))
    for j in range(720):
        th=2*math.pi*j/720.0
        x=1/3+(2*r/3)*math.cos(th)
        y=1/3+(2*r/3)*math.cos(th-2*math.pi/3)
        z=1/3+(2*r/3)*math.cos(th+2*math.pi/3)
        if min(x,y,z) <= 1e-12:
            continue
        e=eta_xyz(x,y,z)
        max_profile_violation=max(max_profile_violation,e-up)
        if r < 0.5:
            max_profile_violation=max(max_profile_violation,lo-e)
        max_stability_violation=max(max_stability_violation,e-(1-r*r))

# Random direct barycentric checks.
for _ in range(50000):
    a,b,c=[rng.expovariate(1.0) for _ in range(3)]
    s=a+b+c
    x,y,z=a/s,b/s,c/s
    t,u,v=(1-x)/2,(1-y)/2,(1-z)/2
    D=q_from_center(t,u,v)
    r=math.sqrt(2*D)
    e=eta_xyz(x,y,z)
    lo,up=profiles(r)
    max_profile_violation=max(max_profile_violation,e-up)
    if r < 0.5:
        max_profile_violation=max(max_profile_violation,lo-e)
    max_stability_violation=max(max_stability_violation,e-(1-r*r))

assert max_det_err < 2e-15, max_det_err
assert max_branch_err < 3e-14, max_branch_err
assert max_profile_violation < 3e-13, max_profile_violation
assert max_stability_violation < 3e-13, max_stability_violation
print('VERIFY_OK')
print('max_det_err',format(max_det_err,'.3e'))
print('max_branch_err',format(max_branch_err,'.3e'))
print('max_profile_violation',format(max_profile_violation,'.3e'))
print('max_stability_violation',format(max_stability_violation,'.3e'))
