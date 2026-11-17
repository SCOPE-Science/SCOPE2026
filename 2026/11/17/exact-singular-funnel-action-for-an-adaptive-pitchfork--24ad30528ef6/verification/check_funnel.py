"""Finite numerical check of the stable-separatrix action for a slow-fast pitchfork.

Run: python verification/check_funnel.py (from the package root).
Requires Python 3, NumPy and SciPy. The infinite-scale theorem is analytical.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp


def lower_root(a, b):
    assert b > 0 and a > 2 * math.sqrt(b)
    return (a - math.sqrt(a*a - 4*b))/2


def action(mu, a, b):
    r = lower_root(a, b)
    assert mu > r*r
    return mu - r*r - b*math.log((mu+b)/(r*r+b))


def numeric_scaled_log(eps, mu_end, a=3., b=2.):
    r = lower_root(a, b)
    tr = -2*r*r - eps
    det = eps*r*(2*r-a)
    lam = (tr - math.sqrt(tr*tr-4*det))/2
    slope = eps*a/(lam+eps)
    assert slope < 0
    dx = -1e-7
    x0 = r+dx
    mu0 = r*r+slope*dx
    assert 0 < x0 < r and r*r < mu0 < mu_end

    def rhs(mu, Y):
        x = math.exp(Y[0])
        return [-(mu-x*x)/(eps*(mu+b-a*x))]

    sol = solve_ivp(rhs, (mu0, mu_end), [math.log(x0)],
                    method='DOP853', rtol=1e-11, atol=1e-12)
    assert sol.success and sol.y[0][-1] < 0
    return -eps*sol.y[0][-1]


def main():
    a, b = 3., 2.
    r = lower_root(a, b)
    assert abs(r-1) < 1e-14 and abs(r*r+b-a*r)<1e-14
    for mu in [2., 5.]:
        A = action(mu, a, b)
        assert A > 0
        errors = []
        for eps in [0.1, 0.03, 0.01]:
            z = numeric_scaled_log(eps, mu, a, b)
            errors.append(abs(z-A))
            print(f'mu={mu:g} eps={eps:g} scaled_log={z:.12f} action={A:.12f}')
        assert errors[2] < errors[1] < errors[0]
    # The difference of the two actions does not explicitly contain a.
    mu1, mu2 = 2., 5.
    common_rate = (mu2-mu1)-b*math.log((mu2+b)/(mu1+b))
    for aa in [3., 3.1]:
        rr=lower_root(aa,b)
        assert mu1 > rr*rr
        assert abs(action(mu2, aa, b)-action(mu1, aa, b)-common_rate)<1e-12
    print('VERIFY_OK: stable_eigenvector, section_actions=2, eps_values=3, rate_invariance=2')
    print('FINITE_CHECK_ONLY: the eps-to-zero limit and global-branch proof are analytical')


if __name__ == '__main__':
    main()
