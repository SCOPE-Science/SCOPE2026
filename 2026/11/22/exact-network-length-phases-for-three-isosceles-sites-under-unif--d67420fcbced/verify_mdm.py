"""Independent reproducibility checks for three-site equal-radius network lengths.
Pure Python 3 standard library; all mathematical globality claims are proved in RESULT.md.
"""
from math import sqrt, hypot, isclose
from random import Random

C = 1 / sqrt(3)
B = 2 / sqrt(3)

def cover(h):
    assert h > 0
    return 1.0 if h <= 1 else (1+h*h)/(2*h)

def clamped(h,r):
    assert h > 0 and 0 <= r < cover(h)
    lo = sqrt(max(0.,r*r-1.))
    hi = max(h-r,0.)
    assert lo <= hi + 1e-12, (h,r,lo,hi)
    y = min(hi,max(lo,C))
    L = max(0.,h-y-r)+2*max(0.,hypot(1,y)-r)
    return L,y

def formula(h,r):
    assert h>0 and r>=0
    R=cover(h)
    if r>=R: return 0.,'point'
    if h<=C:
        if r<=h: return 2*hypot(1,h-r)-2*r,'V'
        return 2*(1-r),'horizontal'
    if h<1:
        if r<=h-C:return h+sqrt(3)-3*r,'Y'
        if r<=h:return 2*hypot(1,h-r)-2*r,'V'
        return 2*(1-r),'horizontal'
    if h<sqrt(3):
        if r<=h-C:return h+sqrt(3)-3*r,'Y'
        return 2*hypot(1,h-r)-2*r,'V'
    if h==sqrt(3):
        return h+sqrt(3)-3*r,'Y'
    if r<=B:return h+sqrt(3)-3*r,'Y'
    return h-r-sqrt(r*r-1),'vertical'

def f2(x,y,h,r):
    return max(hypot(x+1,y)-r,0)+max(hypot(x-1,y)-r,0)+max(hypot(x,y-h)-r,0)

def nclose(x,y):
    assert abs(x-y) <= 4e-11*(1+abs(x)+abs(y)),(x,y)

rng=Random(20261102)
tests=0
branches=set()
for h in [0.05, 0.4, C, 0.7, 0.95, 1., 1.3, 1.6, sqrt(3),2., 3.,10.]:
    R=cover(h)
    rr=[0,0.0001*R,0.2*R,0.65*R,0.98*R, R, 1.05*R]
    rr += [max(0.,min(R,v)) for v in [h,h-C, B,1.,R-1e-9]]
    for r in rr:
        exact,phase=formula(h,r)
        branches.add(phase)
        if r<R:
            v,y=clamped(h,r)
            nclose(v,exact)
            nclose(f2(0,y,h,r),exact)
            # For r<R, the three branches are segments to disk projections.
            # Their lengths equal the sum of the three point-to-disk distances.
            assert 0<=y<=h+1e-12
        else: assert exact==0
        assert exact>=-1e-10,(h,r,exact)
        tests+=1

for _ in range(500):
    h=10**rng.uniform(-1,1)
    R=cover(h)
    r=R*rng.random()*1.1
    exact,phase=formula(h,r)
    if r<R:
        v,y=clamped(h,r)
        nclose(exact,v)
        nclose(exact,f2(0,y,h,r))
    else: assert exact==0
    tests+=1

# Independently sample a two-dimensional rectangle, verifying no smaller value
# is encountered (a finite stress test, not a global proof).
grid_tests=0
for _ in range(20):
    h=10**rng.uniform(-0.7,0.7)
    R=cover(h)
    r=R*rng.uniform(0,0.999)
    value,phase=formula(h,r)
    for i in range(81):
        x=-2+4*i/80
        for j in range(81):
            y=-2+(h+4)*j/80
            assert f2(x,y,h,r)>=value-1e-10
    grid_tests+=1

assert {'Y','V','horizontal','vertical','point'}<=branches, branches
print('THREE_SITE_MDM_OK',tests,'formula_and_disk_projection_cases;',grid_tests,'two_dimensional_grid_checks')
