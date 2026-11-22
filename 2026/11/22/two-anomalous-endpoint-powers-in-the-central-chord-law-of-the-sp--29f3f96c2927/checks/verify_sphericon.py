"""Reproducible deterministic diagnostics for central chords of a unit sphericon.

Uses only the Python 3 standard library. Finite checks are corroborative;
they do not replace the analytical local-expansion proofs.
"""
import math

PI = math.pi
SQRT2 = math.sqrt(2.0)
C_LOW = 2**(7/8) * math.gamma(1/4) * math.gamma(3/2) / (PI * math.gamma(7/4))
C_HIGH = 7 / (3 * PI)


def radial_term(t):
    assert 0 <= t <= 1 + 1e-14
    t = min(1., max(0., t))
    return 1 / (t + math.sqrt(max(0., 1 - t*t)))


def length_over_radius(x, y, z):
    assert abs(x*x+y*y+z*z-1) < 1e-9
    return radial_term(abs(x)) + radial_term(abs(y))


def spherical(azimuth, vertical):
    c = math.sqrt(max(0., 1-vertical*vertical))
    return c*math.cos(azimuth), c*math.sin(azimuth), vertical


def check():
    assert abs(length_over_radius(1., 0., 0.)-2) < 1e-14
    assert abs(length_over_radius(0., 0., 1.)-2) < 1e-14
    assert abs(length_over_radius(1/SQRT2, 1/SQRT2, 0.)-SQRT2) < 1e-14
    # Direct reconstruction from upper and lower half-bicones.
    for i in range(1,251):
        a = 2*PI*i/251
        z = 2*((i*37)%251)/251-1
        x,y,z=spherical(a,z)
        top = 1/(abs(x)+math.hypot(y,z))
        bottom = 1/(abs(y)+math.hypot(x,z))
        assert abs(top+bottom-length_over_radius(x,y,z)) < 3e-13
        assert SQRT2-1e-13 <= top+bottom <= 2+1e-13
    # Local lower-endpoint normal form: theta=pi/4+sqrt(eps)*u, z=eps**(1/4)*v.
    for eps in [1e-5,1e-6,1e-7]:
        for u,v in [(.3,.5),(-.4,.7),(.2,-.6),(.0,.9)]:
            x,y,z=spherical(PI/4+math.sqrt(eps)*u,eps**.25*v)
            actual=(length_over_radius(x,y,z)-SQRT2)/eps
            predicted=(u*u+v**4/4)/SQRT2
            assert abs(actual-predicted) < .016
    # Local upper endpoint normal forms: top rim pole and seam-tip pole.
    for eps in [1e-5,1e-6]:
        for u,v in [(.3,.2),(-.2,.25),(.1,-.4)]:
            x=eps*u; y=eps*v; z=math.sqrt(1-x*x-y*y)
            actual=(2-length_over_radius(x,y,z))/eps
            assert abs(actual-(abs(u)+abs(v))) < .004
            y=eps*u; z=eps*v; x=math.sqrt(1-y*y-z*z)
            actual=(2-length_over_radius(x,y,z))/eps
            assert abs(actual-(math.hypot(u,v)+abs(u))) < .004
    # Independently quadrature-check volumes of tangent-limit domains.
    # Minimum: {a^2/sqrt(2)+b^4/(4sqrt(2))<1}.
    B=1/(4*SQRT2); A=1/SQRT2
    zmax=(1/B)**.25
    n=16000; dz=2*zmax/n
    area_min=0.
    for i in range(n):
        z=-zmax+(i+.5)*dz
        area_min+=2*math.sqrt(max(0.,(1-B*z**4)/A))*dz
    assert abs(4*area_min/(4*PI)-C_LOW)<2e-6
    # Maximum top cap: diamond area two; each of four seam tips: area 4/3.
    area_seam=0.
    n=16000; da=2*PI/n
    for i in range(n):
        theta=(i+.5)*da
        area_seam += .5/(1+abs(math.cos(theta)))**2*da
    assert abs(area_seam-4/3) < 3e-8
    assert abs((2*2+4*area_seam)/(4*PI)-C_HIGH)<1e-8
    print('all deterministic checks passed')
    print('lower coefficient',format(C_LOW,'.15f'))
    print('upper coefficient',format(C_HIGH,'.15f'))
    print('upper mode weights: top/bottom together=3/7; four seam tips=4/7')


if __name__=='__main__':
    check()
