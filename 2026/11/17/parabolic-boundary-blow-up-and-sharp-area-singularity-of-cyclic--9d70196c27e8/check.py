"""Independent numeric and symbolic checks for cyclic-polygon boundary scaling.

Usage: python check.py
Dependencies: numpy, scipy, sympy (only if installed).
"""
from math import asin, cos, sin, sqrt, fsum
from scipy.optimize import brentq


def exact_geometry(short_edges, eps):
    b = tuple(float(x) for x in short_edges)
    S = sum(b)
    H = S**3 - sum(x**3 for x in b)
    # Arc closure for a very shallow cyclic polygon.
    def f(t):
        return sin(sum(asin(x*t) for x in b))/t - (S-eps)
    upper = min(0.45/max(b), 0.48/S)
    assert f(upper)<0, (b,eps, f(upper))
    t = brentq(f, 1e-12, upper, xtol=1e-15)
    R=1/(2*t)
    gap = [2*asin(x*t) for x in b]
    D = sum(gap)
    ang=0.
    points=[]
    for d in [0.]+gap:
        ang += d
        x=R*(sin(ang-D/2)+sin(D/2))
        y=R*(cos(ang-D/2)-cos(D/2))
        points.append((x,y))
    area = sum((points[j][0]*points[j+1][1]-points[j+1][0]*points[j][1]) for j in range(len(b)))/2
    # Arc is above chord and ordered from left to right: shoelace is negative.
    area = abs(area)
    assert abs(points[-1][0]-(S-eps)) <1e-9
    assert abs(points[-1][1]) <1e-9
    return R, area, points, H


def test_case(b):
    S =sum(b)
    H=S**3-sum(v**3 for v in b)
    assert H>0
    for eps in [1e-2,2e-3,2e-4,2e-5]:
        R,A,pts,H=exact_geometry(b,eps)
        u=[0.]
        for x in b: u.append(u[-1]+x)
        Rlim=sqrt(H/(24*eps))
        Alim=sqrt(H*eps/6)
        scale=sqrt(6/H)
        point_err=max(abs(pt[0]-uj)+abs(pt[1]/sqrt(eps)-scale*uj*(S-uj)) for pt,uj in zip(pts,u))
        rel_R=abs(R/Rlim-1)
        rel_A=abs(A/Alim-1)
        if eps <= 2e-4:
            assert rel_R < 0.003 and rel_A <0.003 and point_err < 0.02, (b,eps,rel_R,rel_A,point_err)
    print('CHECK',b, 'small_eps_errors', f'{rel_R:.3g}',f'{rel_A:.3g}',f'{point_err:.3g}')

for b in [[1,1],[1,2],[1,1,1],[1,2,3],[0.4,1.7,2.3,0.9],[1]*7]:
    test_case(b)
print('CYCLIC_BOUNDARY_PARABOLIC_CHECKS_OK')
