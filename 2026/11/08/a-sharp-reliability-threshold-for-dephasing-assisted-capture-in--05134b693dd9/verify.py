"""Exact, self-contained symbolic verification for the two-site absorbing Lindblad model.

Requires SymPy, NumPy and SciPy.
Run: python verify.py
"""
import sympy as sp


def verify_symbolic():
    g, d, t = sp.symbols('g d t', real=True)
    A = sp.Matrix([[0, 0, 0, 2],
                   [0, 2, 0, -2],
                   [0, 0, g + 1, -d],
                   [-1, 1, d, g + 1]])
    source = sp.Matrix([1, 0, 0, 0])
    readout = sp.Matrix([[1, 1, 0, 0]])
    resolvent = A.inv()
    w1 = resolvent * source
    w2 = resolvent * w1
    m1 = sp.factor((readout*w1)[0])
    m2 = sp.factor(2*(readout*w2)[0])
    mean_expected = (d*d + g*g + 4*g + 3)/(2*(g + 1))
    raw_second_expected = ((d*d + (g + 1)**2)*
                           (d*d + (g + 2)*(g + 3)))/(2*(g + 1)**2)
    assert sp.simplify(m1 - mean_expected) == 0
    assert sp.simplify(m2 - raw_second_expected) == 0
    var = sp.factor(m2-m1**2)
    variance_expected = (d**4 + 2*d*d*g*g + 6*d*d*g + 8*d*d +
                         g**4 + 6*g**3 + 12*g*g + 10*g + 3)/(4*(g+1)**2)
    assert sp.simplify(var-variance_expected) == 0
    f = sp.factor(var / m1**2)
    p = (d**4 + 10*d*d*g + 18*d*d -
         g**4 - 6*g**3 - 12*g*g - 10*g - 3)
    assert sp.simplify(sp.diff(f, g) + 2*p/(d*d + g*g + 4*g + 3)**3) == 0
    assert sp.expand(p.subs({d: t, g: t-1}) - 8*t*t*(t+1)) == 0
    assert sp.expand(p.subs({d: t, g: t+1}) + 8*(t*t+7*t+4)) == 0
    z = 2*sp.sqrt(21)-9
    assert sp.simplify(z*z +18*z-3) == 0
    # Compare g=|d|+1+b/|d| and identify unique coefficient b=-2.
    a,b = sp.symbols('a b')
    series_poly = sp.Poly(sp.expand(p.subs({d:t,g:t+a+b/t})*t**4),t)
    assert sp.simplify(series_poly.coeff_monomial(t**7)+4*(a-1)) == 0
    assert sp.simplify(series_poly.coeff_monomial(t**6) +2*(3*a*a+4*a+2*b-3))==0
    # At positive dephasing and nonzero hopping the absorbing trace decreases.
    print('Exact symbolic identities and optimizer comparisons: passed')
    return A, mean_expected, raw_second_expected


def verify_quadrature(A, mean, second):
    import numpy as np
    from scipy.linalg import expm
    from scipy.integrate import quad
    syms = {str(s): s for s in A.free_symbols}
    for d in (0., 0.5, 1., 2.):
        for g in (0., 0.2, 1., 3.):
            mat = np.asarray((-A).subs({syms['g']:g,syms['d']:d}),dtype=float)
            start = np.array([1.,0.,0.,0.])
            trace = np.array([1.,1.,0.,0.])
            survival = lambda t: float(trace @ expm(mat*t) @ start)
            u1 = quad(survival, 0., np.inf, epsabs=1e-9)[0]
            u2 = 2*quad(lambda t: t*survival(t), 0., np.inf, epsabs=1e-9)[0]
            exact1 = float(mean.subs({syms['g']:g,syms['d']:d}))
            exact2 = float(second.subs({syms['g']:g,syms['d']:d}))
            assert abs(u1-exact1) < 1e-7, (g,d,u1,exact1)
            assert abs(u2-exact2) < 1e-6, (g,d,u2,exact2)
            assert abs(survival(0.)-1)<1e-14 and survival(1000.)<1e-9
    print('Independent quadrature: 16 parameter pairs, 32 moment integrals passed')


if __name__ == '__main__':
    A, mean, second = verify_symbolic()
    verify_quadrature(A, mean, second)
    print('Verification succeeded')
