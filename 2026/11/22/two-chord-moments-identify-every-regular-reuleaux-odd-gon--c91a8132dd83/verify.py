"""Reproduce two even boundary-chord moments of regular Reuleaux odd-gons.

Only the Python standard library is required. All lengths use unit constant width.
The midpoint-rule calculation directly constructs geometric boundary points;
it does not reuse the analytic moment integration.
"""
from math import cos, sin, tan, pi

def formulas(n):
    t = pi/(2*n)
    sec2 = 1/cos(t)**2
    z = tan(t)/t
    m2 = 1 + sec2/4 - z
    m4 = 1 + sec2 + sec2**2/16 - (3+sec2)*z/2
    d2 = 2*m2
    d4 = 2*m4+4*m2*m2
    return d2, d4, d4/d2**2 - 1.5

def midpoint_boundary(n, subdivisions=64):
    t = pi/(2*n)
    R = 1/(2*cos(t))
    result=[]
    for i in range(n):
        theta = 2*pi*i/n
        for j in range(subdivisions):
            phi = -t + 2*t*(j+0.5)/subdivisions
            result.append((R*cos(theta)-cos(theta+phi),
                           R*sin(theta)-sin(theta+phi)))
    return result

def brute_moments(points):
    d2 = d4 = 0.0
    N=len(points)
    for x,y in points:
        for u,v in points:
            z=(x-u)**2+(y-v)**2
            d2+=z
            d4+=z*z
    return d2/N**2, d4/N**2

def main():
    count=0
    for n in (3,5,7,9,11,15):
        exact2,exact4,H = formulas(n)
        direct2,direct4 = brute_moments(midpoint_boundary(n,subdivisions=64))
        assert abs(direct2-exact2)<4.5e-5, (n, direct2,exact2)
        assert abs(direct4-exact4)<4.5e-5, (n,direct4,exact4)
        assert H>0
        count+=3
    hprev=float('inf')
    for n in range(3,202,2):
        d2,d4,h = formulas(n)
        assert d2>0 and d4>0 and 0<h<hprev
        hprev=h
        count+=1
    # High precision asymptotics checked separately using mpmath or symbolic series.
    for n in (11,51,151):
        _,_,H=formulas(n)
        limit = pi**4/90
        assert abs(n**4*H-limit)/limit < 0.04*(11/n)**2
        count+=1
    print(f"PASS: {count} assertions; direct boundary quadrature and formula agree")

if __name__=='__main__': main()
