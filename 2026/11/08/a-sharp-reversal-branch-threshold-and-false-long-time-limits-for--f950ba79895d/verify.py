"""Reproducibility checks for the quadratic-reformulated SAV-BE scalar reduction.

Only finite calculations are checked here; the infinite-time claims are proved in RESULT.md.
Requires Python 3 standard library only.
"""
from decimal import Decimal, localcontext
from math import isclose, sqrt


def step(phi, r, tau, shift):
    energy_sqrt = (phi * phi / 2 + shift).sqrt()
    r_next = r / (1 + tau * phi * phi / (energy_sqrt * energy_sqrt)).sqrt()
    phi_next = phi - tau * r_next * phi / energy_sqrt
    return phi_next, r_next


def test_singular_branch():
    q_star = (sqrt(17) - 3) / 4
    t_star = (11 + 3 * sqrt(17)) / 4
    assert isclose(1 / sqrt(1 + 2*t_star), q_star, abs_tol=3e-15)
    assert isclose((2*q_star*q_star+3*q_star-1)/(2*q_star), 0, abs_tol=3e-15)
    assert t_star > 1 + sqrt(2)
    with localcontext() as ctx:
        ctx.prec=95
        T=(Decimal(11)+3*Decimal(17).sqrt())/4
    for tau in (T, T+Decimal('0.001'), Decimal(7), Decimal(100)):
        with localcontext() as ctx:
            ctx.prec=95
            t = tau
            q=(1+2*t).sqrt()**(-1)
            phi=Decimal(1)
            r=(Decimal(1)/2).sqrt()
            for n in range(1,81):
                next_phi,next_r=step(phi,r,t,Decimal(0))
                exact_r=(Decimal(1)/2).sqrt()*q**n
                exact_phi=1-t*q+t*q*q*(1-q**(n-1))/(1-q)
                assert abs(next_phi-exact_phi)<Decimal('1e-78')
                assert abs(next_r-exact_r)<Decimal('1e-78')
                assert next_r>0 and next_phi<0
                phi,r=next_phi,next_r


def test_positive_shift():
    with localcontext() as ctx:
        ctx.prec=95
        for shift in (Decimal('0.000001'),Decimal('0.05'),Decimal('0.5')):
            phi=Decimal(1)
            r=(Decimal('0.5')+shift).sqrt()
            for n in range(1,101):
                old_phi,old_r=phi,r
                phi,r=step(phi,r,Decimal(100),shift)
                S=(old_phi*old_phi/2+shift).sqrt()
                residual1=phi-old_phi+Decimal(100)*r*old_phi/S
                residual2=r*r-old_r*old_r-r*old_phi*(phi-old_phi)/S
                assert abs(residual1)<Decimal('1e-85')
                assert abs(residual2)<Decimal('1e-85')
                assert phi < -4 and r>0
                assert r<old_r and r<Decimal(10)**(-n)
                assert abs(phi) > 1
            assert phi*phi/2 > 8


if __name__=='__main__':
    test_singular_branch()
    test_positive_shift()
    assert 201<15**2 and 2 < Decimal('1.5')**2
    print('VERIFY_OK')
