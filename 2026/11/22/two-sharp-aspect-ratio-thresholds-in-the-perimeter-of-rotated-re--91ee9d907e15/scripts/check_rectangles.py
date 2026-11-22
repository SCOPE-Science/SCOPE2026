#!/usr/bin/env python3
"""Standalone reproducibility checks for the rotational-intersection perimeter theorem.
Only the Python standard library is required. Numerical checks are not substitutes
for the analytic proof included in RESULT.md.
"""
import math
import random

ROOT2 = math.sqrt(2.0)

def exact_perimeter(a, theta):
    assert a >= 1 and 0 <= theta <= math.pi / 2
    t = math.tan(theta / 2)
    if t <= 1 / a:
        return 4 * (a + 1) * (1 + t*t) / (1 + t)
    return 8 / math.sin(theta)

def clip(poly, nx, ny, c):
    # Intersect a polygon with the closed half-plane nx*x+ny*y<=c.
    if not poly:
        return []
    result = []
    prev = poly[-1]
    old = nx*prev[0] + ny*prev[1] - c
    for curr in poly:
        new = nx*curr[0] + ny*curr[1] - c
        if (old <= 0) != (new <= 0):
            w = old / (old-new)
            result.append((prev[0] + w*(curr[0]-prev[0]),
                           prev[1] + w*(curr[1]-prev[1])))
        if new <= 0:
            result.append(curr)
        prev,old = curr,new
    return result

def polygon_perimeter(a, theta):
    c,s = math.cos(theta),math.sin(theta)
    p = [(-a,-1),(a,-1),(a,1),(-a,1)]
    for nx,ny,b in ((c,s,a),(-c,-s,a),(-s,c,1),(s,-c,1)):
        p = clip(p,nx,ny,b)
    return sum(math.hypot(x-v[0],y-v[1]) for (x,y),v in zip(p,p[1:]+p[:1]))

def predicted_min(a):
    if a < ROOT2:
        return (math.pi/4, 8*(ROOT2-1)*(a+1))
    if a > ROOT2:
        return (math.pi/2,8.0)
    return (math.pi/4,8.0) # also pi/2 at coexistence

def main():
    rng = random.Random(21)
    checks = 0
    for a in [1,1.00001,1.1,ROOT2,2.0,1+ROOT2,3.,10.,100.]+[10**rng.uniform(0,2) for _ in range(120)]:
        for theta in [0,1.e-7,math.pi/4,math.pi/2,2*math.atan(1/a)]+[rng.uniform(0,math.pi/2) for _ in range(75)]:
            x = exact_perimeter(a,theta)
            y = polygon_perimeter(a,theta)
            assert math.isclose(x,y,rel_tol=5e-11,abs_tol=5e-11), (a,theta,x,y)
            checks += 1
    for a in [1,1.05,1.2,ROOT2-1e-5,ROOT2,ROOT2+1e-5,1.7,2.1,1+ROOT2,2.5,10]:
        _,minimum = predicted_min(a)
        for k in range(1001):
            theta = k*math.pi/2000
            assert exact_perimeter(a,theta) >= minimum-1e-10
            checks += 1
        if a < ROOT2:
            assert math.isclose(exact_perimeter(a,math.pi/4),minimum,abs_tol=1e-12)
        else:
            assert math.isclose(exact_perimeter(a,math.pi/2),minimum,abs_tol=1e-12)
        checks += 1
    assert math.isclose(exact_perimeter(ROOT2,math.pi/4),8,abs_tol=1e-12)
    assert math.isclose(exact_perimeter(ROOT2,math.pi/2),8,abs_tol=1e-12)
    checks += 2
    print(f"PASS: {checks} checks; independent polygon-half-plane clipping agrees")

if __name__=='__main__':
    main()
