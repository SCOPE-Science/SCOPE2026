"""Reproducible finite diagnostics for the high-coupling four-oval theorem.

Uses only Python standard library. Numerical finite tests are not proofs of
uniform asymptotic estimates or of statements for all parameter values.
"""
from fractions import Fraction as F
import math

LO = 0.75
HI = 1.0


def a(s):
    return (16*s*s-9)*(1-s*s)


def v(s, mu):
    b = mu*s*s - 25
    return math.sqrt(2*a(s)/(b+math.sqrt(b*b+64*a(s))))


def midquad(fun, n=8192):
    # s(theta)^2=9/16+(7/16)sin(theta)^2 removes root singularities.
    h = (math.pi/2)/n
    total = 0.0
    for k in range(n):
        th = (k+0.5)*h
        st = math.sin(th)
        ct = math.cos(th)
        s = math.sqrt(9/16 + (7/16)*st*st)
        ds = (7/16)*st*ct/s
        total += fun(s)*ds
    return h*total


def period(mu, sig, eps=1.0):
    def f(s):
        vm = v(s,mu)
        b = mu*s*s-25
        D = 2*vm*(b+32*vm*vm)
        return 4/(eps*(2+sig*s)*(4-vm*vm)*D)
    return midquad(f)


def area(mu):
    return 2*midquad(lambda s:v(s,mu))


def floquet_action(mu):
    def f(s):
        vm=v(s,mu)
        b=mu*s*s-25
        D=2*vm*(b+32*vm*vm)
        H=64*s**3-50*s+2*mu*s*vm*vm
        return 2*(D+H*H/D)
    return midquad(f)


def J(sig):
    return midquad(lambda s: 1/((2+sig*s)*s*math.sqrt(a(s))))


def exact_polynomial_test():
    # All identities below are exact rational arithmetic.
    for x,y,mu,eps in [(F(11,4),F(17,8),F(47),F(2,3)),
                       (F(7,3),F(13,7),F(100),F(9,5))]:
        u=x-2; w=y-2
        h=16*(u**4+w**4)-25*(u*u+w*w)+mu*u*u*w*w+9
        hx=64*u**3-50*u+2*mu*u*w*w
        hy=64*w**3-50*w+2*mu*u*u*w
        dx=x*y*(-h*hx-eps*hy)
        dy=x*y*(-h*hy+eps*hx)
        assert hx*dx+hy*dy == -x*y*h*(hx*hx+hy*hy)
        assert (x*y*(hx*hx+hy*hy)*h*h)*(-2) == 2*h*(hx*dx+hy*dy)


def main():
    exact_polynomial_test()
    jp, jm=J(1),J(-1)
    assert 0<jp<jm
    js=math.pi/2*(1/3+1/math.sqrt(165))
    assert abs(jp+jm-js) < 2e-8
    for mu in (20000.0, 80000.0):
        assert abs(area(mu)*math.sqrt(mu)/(math.pi/8)-1)<0.002
        assert abs(floquet_action(mu)/math.sqrt(mu)/(49*math.pi/256)-1)<0.003
        for sig,j in ((1,jp),(-1,jm)):
            assert abs(period(mu,sig)*math.sqrt(mu)/(j/2)-1)<0.003
        # The geometry obeys the quartic equation on both branches.
        for s in (0.77,0.81,0.88,0.96):
            vm=v(s,mu)
            residual=16*(s**4+vm**4)-25*(s*s+vm*vm)+mu*s*s*vm*vm+9
            assert abs(residual)<1e-9
    print('FOUR_OVAL_HIGH_COUPLING_CHECK_OK')


if __name__=='__main__':
    main()
