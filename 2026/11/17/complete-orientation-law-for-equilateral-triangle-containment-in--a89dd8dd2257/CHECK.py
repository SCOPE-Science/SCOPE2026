"""Independent numerical regression of exact triangle-in-rectangle formulas.
Run with: python3 CHECK.py. No nonstandard dependencies.
The proof of universality is analytic; these are finite cross-checks only.
"""
import math
from itertools import combinations

SQ3 = math.sqrt(3.0)
POINTS = [(math.cos(2 * math.pi * j / 3), math.sin(2 * math.pi * j / 3)) for j in range(3)]
DIFFS = [(POINTS[i][0] - POINTS[j][0], POINTS[i][1] - POINTS[j][1])
         for i, j in combinations(range(3), 2)]


def formulas(w, h):
    small, big = sorted((w, h))
    if SQ3 * big >= 2 * small:
        area = 2 * small * small / SQ3
        radius = 2 * small / 3
    else:
        area = 8*w*h - 2*SQ3*(w*w+h*h)
        radius = math.sqrt(4 * (w*w + h*h - SQ3*w*h) / 3)
    return area, radius


def radial_direct(w, h, theta):
    c, s = math.cos(theta), math.sin(theta)
    horizontal = max(abs(dx*c-dy*s) for dx, dy in DIFFS)
    vertical = max(abs(dy*c+dx*s) for dx, dy in DIFFS)
    return min(w/horizontal, h/vertical)


def polygon_clip(poly, a, b, cap):
    if not poly:
        return []
    new = []
    for p, q in zip(poly, poly[1:] + poly[:1]):
        vp = a*p[0] + b*p[1] - cap
        vq = a*q[0] + b*q[1] - cap
        pin, qin = vp <= 1e-13, vq <= 1e-13
        if pin != qin:
            u = vp/(vp-vq)
            new.append((p[0]+u*(q[0]-p[0]),p[1]+u*(q[1]-p[1])))
        if qin:
            new.append(q)
    return new


def direct_polygon(w, h):
    big = 10 * max(w,h)
    poly = [(-big,-big),(big,-big),(big,big),(-big,big)]
    for dx, dy in DIFFS:
        for a,b,cap in ((dx,-dy,w),(dy,dx,h)):
            poly=polygon_clip(poly,a,b,cap)
            poly=polygon_clip(poly,-a,-b,cap)
    assert len(poly) >= 6
    area=abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(poly,poly[1:]+poly[:1])))/2
    radius=max(math.hypot(*p) for p in poly)
    return area,radius


def survival(w,h,u,rmax):
    if u<=0:
        return 1.0
    if u>=rmax:
        return 0.0
    return 1 - 6/math.pi*sum(math.acos(min(1.0,v/(SQ3*u))) for v in (w,h))


def run():
    dims = [(1., 1.),(1.,1.001),(1.,1.05),(1.,1.1),
            (1.,2/SQ3),(1.,1.18),(1.,2.),(1.,10.),
            (0.85,1.),(0.5,0.87),(2.1,1.7),(0.31,0.17)]
    for w,h in dims:
        area,radius = formulas(w,h)
        pa, pr = direct_polygon(w,h)
        assert abs(pa-area)<1e-8*max(1,area), (w,h,pa,area)
        assert abs(pr-radius)<1e-8*max(1,radius), (w,h,pr,radius)
        N=8192
        values=[radial_direct(w,h,2*math.pi*(j+0.5)/N) for j in range(N)]
        quadrature = math.pi*sum(v*v for v in values)/N
        assert abs(quadrature-area)<3e-6*max(1,area),(w,h,quadrature,area)
        for frac in (0.3, 0.75,0.9,0.98):
            u=frac*radius
            obs=sum(v>=u for v in values)/N
            expect=survival(w,h,u,radius)
            assert abs(obs-expect)<0.0025,(w,h,u,obs,expect)
        print('PASS',w,h,'area',f'{area:.12g}','radius',f'{radius:.12g}')
    # Algebraic extremal inequalities at fixed container area and exact values.
    square_area=8-4*SQ3
    assert square_area > 1
    qstar=2/SQ3
    maxsq=2*SQ3/9
    sq=4*(2-SQ3)/3
    assert maxsq>sq and abs(formulas(1/math.sqrt(qstar),math.sqrt(qstar))[1]**2-maxsq)<1e-12
    print('PASS 12 shapes, 48 distribution comparisons, 12 independent polygon computations')


if __name__=='__main__':
    run()
