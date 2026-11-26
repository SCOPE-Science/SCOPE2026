"""Exact-rational and deterministic quadrature checks of rank-one Nyström identities.
Run: python3 verify.py. Standard library only; checks supplement an analytic proof.
"""
from fractions import Fraction as F
from math import pi, sin, cos, sqrt, isclose


def residual(a, b, x, y):
    d = a*x*x+b*y*y
    yy = ((a*x)*(a*x)/d, (a*x)*(b*y)/d, (b*y)*(b*y)/d)
    return (a-yy[0], -yy[1], b-yy[2])


def check_exact():
    n = 0
    for a in [F(1), F(2), F(3), F(9), F(25)]:
        for b in [F(1, 2), F(1)]:
            if a < b:
                continue
            for x, y in [(F(1), F(0)), (F(0), F(1)), (F(1), F(1)),
                         (F(3, 5), F(-4, 7)), (F(-2), F(3)), (F(5), F(-7))]:
                r11, r12, r22 = residual(a, b, x, y)
                d = a*x*x+b*y*y
                c = a*b/d
                assert (r11,r12,r22)==(c*y*y,-c*x*y,c*x*x)
                assert r11*r22 == r12*r12
                assert r11+r22 == a*b*(x*x+y*y)/d
                n += 1
    # Discrete isotropic law supported on coordinate axes has exactly >= sign moment.
    for k in [F(1), F(2), F(4), F(9), F(100)]:
        for q in [1,2,3,4]:
            coordinate = (k**q+F(1))/2
            signs = (2*k/(k+1))**q
            assert coordinate >= signs
            if k>1:
                assert coordinate>signs
            assert signs>=1
    return n


def numerical_moments(k, points=32000):
    # Angle midpoint quadrature, normalized via circle angular law.
    h = pi/(2*points)
    m1=m2=0.0
    for j in range(points):
        theta=(j+0.5)*h
        t=sin(theta)**2
        r=k/(1+(k-1)*t)
        m1+=r
        m2+=r*r
    return m1/points,m2/points


def main():
    n=check_exact()
    for k in [1, 4, 9, 100, 10000]:
        m1,m2=numerical_moments(k)
        ex1=sqrt(k)
        ex2=(k+1)*sqrt(k)/2
        assert isclose(m1,ex1,rel_tol=2e-5,abs_tol=2e-5)
        assert isclose(m2,ex2,rel_tol=2e-5,abs_tol=2e-5)
        print('contrast',k,'gaussian moment1',m1,'moment2',m2,
              'sign moment2',float((F(2)*F(k)/(F(k)+1))**2))
    print('PASS rational residual cases',n, '; five angular quadrature cases')


if __name__=='__main__':
    main()
