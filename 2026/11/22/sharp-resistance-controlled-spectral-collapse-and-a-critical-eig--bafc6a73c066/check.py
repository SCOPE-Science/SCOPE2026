"""Finite numerical checks for the regularized one-dimensional weighted Neumann problem.

Requires numpy and scipy. Shooting uses the exact weight and a logarithmic coordinate;
these finite checks are not a proof of the limiting theorems.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def check(eps, alpha):
    Q = np.log1p(1.0 / eps)
    M = ((1 + eps)**(alpha + 1) - eps**(alpha + 1)) / (alpha + 1)
    H = Q if abs(alpha - 1) < 1e-12 else np.expm1((1-alpha)*Q)*eps**(1-alpha)/(1-alpha)

    def shoot(lam, curve=False):
        def rhs(s, y):
            e = eps * np.exp(s*Q)
            return (Q * e**(1-alpha) * y[1], -lam * Q * e**(1+alpha) * y[0])
        sol = solve_ivp(rhs, (0,1), (0,1), rtol=5e-11, atol=5e-11, dense_output=True)
        assert sol.success
        return sol if curve else sol.y[1,-1]

    lam = brentq(shoot, 0, 4/(M*H), xtol=3e-14)
    eta = 1/np.sqrt(2*M*H)
    assert (1+eta)**(-2) - 2e-6 < lam*M*H < (1-eta)**(-2) + 2e-6
    sol = shoot(lam,True)
    grid = np.linspace(0,1,61)
    u = sol.sol(grid)[0]/sol.sol(1)[0]
    h = (np.expm1((1-alpha)*grid*Q) / np.expm1((1-alpha)*Q)) if abs(alpha-1)>1e-12 else grid
    assert abs(u[0]) < 1e-10 and abs(u[-1]-1)<1e-10
    assert np.min(np.diff(u)) > -1e-9
    assert np.max(np.abs(u-h)) < 0.14
    return lam*M*H, np.max(np.abs(u-h))


def main():
    cases = [(1e-3,1.0),(1e-6,1.0),(1e-8,1.0),
             (1e-6,1.5),(1e-6,2.0)]
    L = np.log(1e6)
    cases.extend((1e-6,1+t/L) for t in (-2,0,2))
    values = [check(e,a) for e,a in cases]
    assert abs(values[2][0]-1)<0.06
    assert abs(values[3][0]-1)<0.01
    assert abs(values[4][0]-1)<0.01
    print('POWER_BOTTLENECK_NUMERICAL_CHECK_OK',len(cases),
          'maxratio',max(v[0] for v in values),
          'maxprofileerr',max(v[1] for v in values))


if __name__ == '__main__':
    main()
