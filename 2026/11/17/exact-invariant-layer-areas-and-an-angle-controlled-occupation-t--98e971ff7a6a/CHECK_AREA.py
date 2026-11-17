#!/usr/bin/env python3
"""Exact shoelace and numerical invariance checks for nested TCE polygons.
Uses only the Python standard library; this is corroboration, not a proof.
"""
from fractions import Fraction as Q
import math
import random


def polygon(n, lam, co, si):
    eta = 1 - lam
    step = eta * (1 + co)
    q = n * step
    height = q * co / si
    long = lam - 2 * q
    assert n >= 1 and long >= 0
    vertices = [(-1, 0), (-1 + q, height),
                (-1 + q + long, height), (-q, height)]
    x, y = vertices[-1]
    for _ in range(n):
        x, y = x + eta * co, y + eta * si
        vertices.append((x, y))
        x += eta
        vertices.append((x, y))
    for _ in range(n):
        x, y = x + eta * co, y - eta * si
        vertices.append((x, y))
        x += eta
        vertices.append((x, y))
    x += long
    vertices.extend(((x, y), (lam, 0)))
    return vertices


def shoelace(vertices):
    twice = sum(x*y2-x2*y for (x,y),(x2,y2) in
                zip(vertices, vertices[1:]+vertices[:1]))
    return abs(twice)/2


def area_formula(n, lam, co, si):
    eta = 1 - lam
    q = n*eta*(1+co)
    return q/si * (co*(1+lam) + q*(1-2*co))


def inside(vertices, x, y):
    # Usual odd-ray predicate; sample points avoid boundary seams.
    hit = False
    j = len(vertices)-1
    for i in range(len(vertices)):
        xi, yi = vertices[i]
        xj, yj = vertices[j]
        if (yi > y) != (yj > y):
            if x < (xj-xi)*(y-yi)/(yj-yi)+xi:
                hit = not hit
        j = i
    return hit


def transform(x, y, lam, phi):
    angle = math.atan2(y, x)
    co, si = math.cos(phi), math.sin(phi)
    eta = 1-lam
    if angle < math.pi/2-phi:
        return x-1, y
    if angle < math.pi/2:
        return co*x-si*y-eta, si*x+co*y
    if angle < math.pi/2+phi:
        return co*x+si*y-eta, -si*x+co*y
    return x+lam, y


def main():
    integer_cases = 0
    for co,si in ((Q(3,5),Q(4,5)),(Q(5,13),Q(12,13)),
                  (Q(12,13),Q(5,13))):
        for lam in (Q(9,10),Q(19,20),Q(49,50)):
            N = int(lam/(2*(1-lam)*(1+co)))
            for n in range(1,N+1):
                v = polygon(n,lam,co,si)
                assert shoelace(v) == area_formula(n,lam,co,si)
                assert abs(v[-2][0]-(lam-n*(1-lam)*(1+co))) < Q(1,10**10)
                integer_cases += 1
    assert integer_cases > 25

    rng = random.Random(21707)
    checked_orbits = 0
    for phi in (math.pi/6, math.pi/3, 1.38):
        for lam in (.95,.985):
            N = int(lam/(2*(1-lam)*(1+math.cos(phi))))
            for n in range(1, min(3,N)+1):
                vertices = polygon(n,lam,math.cos(phi),math.sin(phi))
                top = max(y for _,y in vertices)
                accepted=0
                for _ in range(1400):
                    x=rng.uniform(-1,lam)
                    y=rng.uniform(0,top)
                    if not inside(vertices,x,y):
                        continue
                    accepted+=1
                    xx,yy=transform(x,y,lam,phi)
                    assert inside(vertices,xx,yy), (phi,lam,n,x,y,xx,yy)
                assert accepted>200
                checked_orbits+=accepted

    # Finite-angle phase transition in consecutive layer areas.
    for co,si in ((Q(3,5),Q(4,5)),(Q(5,13),Q(12,13)),
                  (Q(12,13),Q(5,13))):
        lam=Q(49,50)
        d=[area_formula(n,lam,co,si)-area_formula(n-1,lam,co,si)
           for n in range(1,6)]
        assert all(x>0 for x in d)
        assert all((d[j+1]-d[j])*(1-2*co)>0 for j in range(4))

    # Critical angle yields exactly uniform layer areas (rationalized by 1/sin).
    co=Q(1,2);lam=Q(49,50)
    # Multiplying every area by sin(phi) removes the irrational sin(pi/3).
    a=[n*(1-lam)*(1+co)*(co*(1+lam)) for n in range(7)]
    assert all(a[n]-a[n-1]==a[1] for n in range(1,7))

    # CDF limit along eta -> 0: a parameter-free density is tested at a grid.
    for co in (.25,.5,.8):
        si=math.sqrt(1-co*co)
        for eps in (.005,.001):
            lam=1-eps
            N=int(lam/(2*eps*(1+co)))
            assert N>=50
            for u in (.1,.27,.5,.72,.9):
                k=int(u*N)
                exact=area_formula(k,lam,co,si)/area_formula(N,lam,co,si)
                limit=(4*co*u+(1-2*co)*u*u)/(1+2*co)
                assert abs(exact-limit)<6/N, (co,eps,u,exact,limit)

    print(f'TCE_LAYER_AREA_CHECK_OK exact_shoelace_cases={integer_cases} '
          f'sampled_invariant_images={checked_orbits} angle_and_limit_checks=OK')


if __name__=='__main__':
    main()
