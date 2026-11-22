#!/usr/bin/env python3
"""Standard-library numerical diagnostics; analytic proof is in RESULT.md."""
import math
import random

rng = random.Random(112233)
count = 0

def check(cond, message):
    global count
    count += 1
    if not cond:
        raise AssertionError(message)

def measure(r, m, b, q, y):
    delta = (r+m+b-y)*(r+m+y)-m*m
    return (q*(r+m+y)/delta, q*m/delta)

def ystar(r,m,b):
    bc=2*r+r*r/m
    return 0.0 if b<=bc else math.sqrt(m*(b+2*r+4*m))-r-2*m

for j in range(3500):
    r=10**rng.uniform(-2,1)
    m=10**rng.uniform(-2,1)
    q=10**rng.uniform(-1,2)
    bc=2*r+r*r/m
    b=bc*rng.choice((0.10,0.85,1.0,1.01,1.5,3,10))
    y=ystar(r,m,b)
    A,C=measure(r,m,b,q,y)
    check(0<=y<b/2+1e-9,"optimal y must be source-biased")
    check(A>0 and C>0 and math.isfinite(A+C),"physical steady concentrations")
    delta=(r+m+b-y)*(r+m+y)-m*m
    check(math.isclose((r+m+b-y)*A-m*C,q,rel_tol=1e-9,abs_tol=1e-9),"room1 balance")
    check(math.isclose((r+m+y)*C-m*A,0,rel_tol=1e-9,abs_tol=1e-9),"room2 balance")
    vals=[]
    for ii in range(41):
        yy=b*ii/40
        aa,cc=measure(r,m,b,q,yy)
        vals.append((yy,aa,cc,aa+cc))
    check(all(A+C<=e[3]*(1+5e-12) for e in vals),"whole-space global optimum sampled")
    check(all(measure(r,m,b,q,0)[0] <= e[1]*(1+1e-12) for e in vals),"source minimum")
    check(all(measure(r,m,b,q,b/2)[1] <= e[2]*(1+1e-12) for e in vals),"remote minimum")
    if b>bc:
        poly=y*y+2*(r+2*m)*y+r*(r+2*m)-m*b
        check(abs(poly)<=3e-8*max(1,m*b),"stationary quadratic")

r,m,b,q=0.5,1.0,6.0,40.0
y=ystar(r,m,b)
assert math.isclose(y*50,40.83123951776998,rel_tol=1e-10)
assert math.isclose(sum(measure(r,m,b,q,y))/2,4.580064826158649,rel_tol=1e-10)
assert math.isclose(sum(measure(r,m,b,q,0))/2,4.878048780487805,rel_tol=1e-10)
assert math.isclose(sum(measure(r,m,b,q,b/2))/2,5.714285714285714,rel_tol=1e-10)
for r,m,q in ((0.5,1.,40.),(2.,0.1,1.),(0.03,4.,3.)):
    for b in (1e4,1e5,1e6):
        y=ystar(r,m,b)
        ratio=sum(measure(r,m,b,q,y))/sum(measure(r,m,b,q,0))
        check(abs(ratio-(r+m)/(r+2*m))<25/math.sqrt(b),"asymptotic ratio diagnostic")
print(f"PASS: {count} finite diagnostic checks plus four benchmark assertions")
