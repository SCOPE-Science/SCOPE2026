"""Finite, reproducible numerical checks for the equatorial Legendre cusp theorem.

This program is supplemental: it does not certify infinite series asymptotics.
Requires Python 3, numpy, scipy, mpmath.
"""
import math
from fractions import Fraction
from mpmath import zeta


def finite_phi(alpha, h, count):
    x = -math.sin(h)
    p_prev, p_now = 1.0, x
    total = p_now
    for n in range(2, 4*count):
        p_next = ((2*n-1)*x*p_now-(n-1)*p_prev)/n
        p_prev, p_now = p_now, p_next
        if n%4 == 1:
            j = (n-1)//4
            total += p_now * (j+1)**(-alpha)
    return total / float(zeta(alpha))


def power_constant(alpha):
    beta = alpha - 0.5
    return 4**beta * math.pi/(2*math.sqrt(2*math.pi)*float(zeta(alpha))*math.gamma(alpha+0.5)*math.cos(math.pi*beta/2))


def critical_constant():
    return math.sqrt(8/math.pi)/float(zeta(1.5))


if __name__ == '__main__':
    cases=0
    for alpha in (1.2,1.3,1.4):
        beta=alpha-0.5
        ratios=[]
        for h in (0.02,0.005,0.0015):
            observed=-finite_phi(alpha,h,80000)/h**beta
            assert observed>0
            ratios.append(observed/power_constant(alpha))
            cases+=1
        assert abs(ratios[-1]-1)<0.65, (alpha,ratios)
        assert abs(ratios[-1]-1)<abs(ratios[0]-1), (alpha,ratios)
    ratios=[]
    for h in (0.02,0.005,0.0015):
        observed=-finite_phi(1.5,h,80000)/(h*math.log(1/h))
        ratios.append(observed/critical_constant())
        cases+=1
    assert abs(ratios[-1]-1)<0.65,ratios
    assert abs(ratios[-1]-1)<abs(ratios[0]-1),ratios
    for j in range(1,14):
        n=4*j+1
        expected=n*math.comb(4*j,2*j)/2**(4*j)
        # Independent rational Legendre recurrence at the origin.
        p_even_prev = Fraction(1, 1)   # P_0(0)
        for k in range(2, n, 2):
            p_even_prev = -Fraction(k-1, k) * p_even_prev
        derived = n*p_even_prev        # P_n'(0)=n P_{n-1}(0)
        exact = Fraction(n*math.comb(4*j,2*j), 2**(4*j))
        assert derived == exact, (j, derived, exact)
        cases+=1
    print(f'CHECK_OK finite_cusp_and_derivative_checks={cases} (not an infinite proof)')
