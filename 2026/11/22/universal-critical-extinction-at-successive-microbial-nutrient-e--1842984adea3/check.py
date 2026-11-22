"""Reproducibility checks for a compartmental consumer-resource extinction theorem.

Usage: python check.py
Requirements: Python 3.10+, sympy, numpy, scipy.
The symbolic identities are exact. ODE integrations are numerical illustrations,
not substitutes for the all-parameter dynamical proof in RESULT.md.
"""
from fractions import Fraction
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp


def equilibrium(beta):
    # Exact rational parameters: alpha=(1,1,1), k=(1,2,3),
    # input R0=5, conversion gamma=2.
    b = Fraction(beta)
    c = [Fraction(1), Fraction(2), Fraction(3)]
    R0 = Fraction(5)
    r = None
    for h in (3, 2, 1, 0):
        candidate = (R0 + b * sum(c[:h])) / (1 + b * h)
        if all(candidate > c[i] for i in range(h)) and all(
            candidate <= c[i] for i in range(h, 3)
        ):
            r = candidate
            break
    assert r is not None
    N = [b * max(r - ci, 0) / (2 * ci) for ci in c]
    assert r + b * sum(max(r-ci,0) for ci in c) == R0
    return r, N


def symbolic_entropy_identity():
    # This is the exact normalized transfer F/r from the proof.
    a, b, c = sp.symbols('a b c', positive=True)
    direct = -(1-1/a)*((a-1)-(c*b-c)) + (1-1/b)*(a-c*b) - (1-c)*(b-1)
    normalized = 3-c-(c*(b/a+a/b)+(1-c)*(1/a+a/b+b))
    assert sp.simplify(direct-normalized) == 0
    # Critical center eigenvector: the beta-dependent two-pool lag.
    beta, alpha, r, h = sp.symbols('beta alpha r h', positive=True)
    dR = -alpha*r/(1+beta*h)
    dT = dR-alpha*r/beta
    C = alpha**2*r*(1/beta+1/(1+beta*h))
    assert sp.simplify(alpha*dT+C) == 0
    return True


def numeric_ode(beta, time=12000):
    a = np.ones(3)
    k = np.array([1., 2., 3.])
    gamma, supply = 2., 5.
    b = float(beta)
    def f(t, y):
        R = y[0]
        T = y[1:4]
        N = y[4:]
        return np.r_[supply-R-b*np.sum(R-T),
                     b*(R-T)-gamma*a*T*N,
                     (a*T-k)*N]
    z0 = np.array([3., 2., 2., 2., .7, .3, .9])
    sol = solve_ivp(f,(0,time),z0,method='LSODA',rtol=5e-11,atol=5e-13)
    assert sol.success
    return sol.y[:, -1]


def run():
    symbolic_entropy_identity()
    for b, expected, survivors in [
        (Fraction(1, 5), None, 3),
        (Fraction(2, 3), Fraction(3), 2),
        (Fraction(1), None, 2),
        (Fraction(3), Fraction(2), 1),
        (Fraction(5), None, 1),
    ]:
        r,N=equilibrium(b)
        assert len([x for x in N if x>0])==survivors
        if expected is not None:
            assert r==expected
        y = numeric_ode(b)
        assert abs(y[0]-float(r)) < (1e-3 if expected else 1e-7)
        if b==Fraction(2,3):
            # The third species is neutrally invading at r=3.
            expected_amp=Fraction(7,81)
            assert abs(12000*y[6]-float(expected_amp)) < .001
            assert abs(12000*(y[3]-3)+1) < .01
            assert abs(12000*(y[0]-3)+Fraction(2,9)) < .01
        elif b==Fraction(3):
            # The second species is neutrally invading at r=2.
            expected_amp=Fraction(3,7)
            assert abs(12000*y[5]-float(expected_amp)) < .002
            assert abs(12000*(y[2]-2)+1) < .01
            assert abs(12000*(y[0]-2)+Fraction(3,7)) < .01
        else:
            assert np.linalg.norm(y[4:]-np.array([float(x) for x in N]),ord=np.inf)<1e-7
        print(f'beta={b}, r={r}, survivors={survivors}: passed')
    print('Exact transfer identity, critical center coefficient, equilibria and ODE illustrations: PASSED')

if __name__=='__main__':
    run()
