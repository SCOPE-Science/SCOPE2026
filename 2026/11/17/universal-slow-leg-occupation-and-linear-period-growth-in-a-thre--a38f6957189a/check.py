"""Reproducible symbolic and numerical checks of the three-species period law.

Requires Python 3, sympy, scipy, numpy. Numerical finite-energy evaluations
are corroboration only; the limit theorem is established in RESULT.md.
"""
import math

import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

B, C, D, a, d, K = sp.symbols('B C D a d K', positive=True)
Bdot = B * (-a + C + D)
Cdot = C * (d - a - B + D)
Ddot = D * (d - B - C)
casimir = B * D / C
assert sp.simplify(sp.diff(casimir, B)*Bdot + sp.diff(casimir, C)*Cdot + sp.diff(casimir, D)*Ddot) == 0

H = B + D + B*D/K - d*sp.log(B) - a*sp.log(D)
assert sp.simplify((Bdot/B).subs(C, B*D/K)-D*sp.diff(H,D)) == 0
assert sp.simplify((Ddot/D).subs(C, B*D/K)+B*sp.diff(H,B)) == 0
assert sp.simplify((sp.diff(H,B)*Bdot+sp.diff(H,D)*Ddot).subs(C, B*D/K)) == 0


def area(energy, alpha, delta, leaf):
    """Log-coordinate canonical area; both boundary roots are bracketed."""
    def min_over_q(p):
        v = math.exp(p)
        coeff = 1 + v / leaf
        return alpha - alpha * math.log(alpha / coeff) + v - delta*p

    # p minimizing the energy after minimization in q
    pstar = brentq(lambda p: math.exp(p)*(1+alpha/(leaf+math.exp(p)))-delta,
                   -25.0, 25.0)
    assert energy > min_over_q(pstar)
    p_low = brentq(lambda p: min_over_q(p)-energy,
                   -4*energy/delta-50, pstar)
    p_high = brentq(lambda p: min_over_q(p)-energy,
                    pstar, math.log(10*energy+100))

    def width(p):
        ep = math.exp(p)
        coeff = 1+ep/leaf
        rhs = energy-ep+delta*p
        qstar = math.log(alpha/coeff)
        gap = rhs - (alpha-alpha*qstar)
        if gap <= 1.0e-9:
            return 0.0

        def equation(q):
            return coeff*math.exp(q)-alpha*q-rhs
        q_lower = brentq(equation, -4*energy/alpha-50, qstar)
        q_upper = brentq(equation, qstar, math.log(energy+50)+10)
        return q_upper-q_lower

    return quad(width, p_low, p_high, epsrel=4e-8, limit=180)[0]


for alpha, delta, leaf in [(1.0,2.0,1.0), (1.3,0.7,4.0)]:
    target = 1.0/(alpha*delta)
    slopes = []
    for E in (25.0, 100.0):
        h=0.02
        T=(area(E+h,alpha,delta,leaf)-area(E-h,alpha,delta,leaf))/(2*h)
        assert T>0
        slopes.append(T/E)
        print(f'a={alpha}, d={delta}, K={leaf}, E={E:g}, T(E)/E={T/E:.9f}; limiting value={target:.9f}')
    assert abs(slopes[1]-target) < abs(slopes[0]-target)
    assert abs(slopes[1]/target-1) < 0.2
print('THREE_SPECIES_HIGH_ENERGY_SLOW_LEG_CHECK_OK')
