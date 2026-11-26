"""Finite diagnostics for an exact boundedness/escape theorem in a coupled smooth map.

All general and asymptotic conclusions require the proof in RESULT.md;
these calculations are corroboration, not certification by enumeration.
"""
import math


def f(x, a):
    return a*x*(1-x*x)*math.exp(-x*x)


def step_xy(x, y, a, b):
    return f(x, a)+b*(y-x), f(y, a)+b*(x-y)


def step_uv(u, v, a, b):
    g=f(u+v, a); h=f(u-v, a)
    return (g+h)/2, -2*b*v+(g-h)/2


def verify():
    identity_count=0
    # Independently calculate direct and transformed dynamics.
    for a in (0.4, 1.3, 3.4):
        for b in (-0.75, -0.5, -0.2, 0.0, 0.48, 0.5, 0.75):
            for x, y in ((-3., 1.2), (1.5, -0.75), (0.04, 4.), (10., -2.)):
                x1,y1=step_xy(x,y,a,b)
                u1,v1=step_uv((x+y)/2,(x-y)/2,a,b)
                assert abs(x1-(u1+v1))<1e-11
                assert abs(y1-(u1-v1))<1e-11
                identity_count += 1
    # Sign mechanism at the two neutral endpoints in the same outer region.
    for a in (0.4, 1.3, 3.4):
        for u in (-0.4, 0, 0.4):
            for v in (-4., -3., 3., 4.):
                _, vminus = step_uv(u,v,a,-0.5)
                _, vplus = step_uv(u,v,a,0.5)
                assert abs(vminus)<abs(v)<abs(vplus)
    # Explicit supercritical escape is protected by the linear multiplier.
    for a in (0.4, 1.3, 3.4):
        for b in (-0.8,0.8):
            u,v=0.,5.
            for n in range(30):
                un,vn=step_uv(u,v,a,b)
                assert abs(vn)>abs(v)
                u,v=un,vn
            assert abs(v)>100000.
    # The critical second-order logarithmic law is slow to reach numerically.
    # Check its equivalent integrated drift relation at sufficiently long horizons.
    asymptotic_rows=[]
    for a in (0.4, 1.3, 3.4):
        u,v=0.2,3.0
        for n in range(1,600001):
            u,v=step_uv(u,v,a,0.5)
        s=v*v
        ratio=n*2*a*s*s*math.exp(-s)
        assert 0.80 < ratio < 1.40, (a,ratio)
        assert abs(u)<1e-12
        asymptotic_rows.append((a,n,round(s,6),round(ratio,6)))
    print('VERIFY_OK direct/transformed identities:', identity_count)
    print('VERIFY_OK outer-region endpoint sign cases:', 36)
    print('VERIFY_OK supercritical escape cases:', 6)
    print('VERIFY_OK asymptotic drift diagnostics:', asymptotic_rows)


if __name__=='__main__': verify()
