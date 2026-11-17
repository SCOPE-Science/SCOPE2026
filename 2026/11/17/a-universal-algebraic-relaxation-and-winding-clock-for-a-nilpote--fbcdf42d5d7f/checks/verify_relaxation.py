"""Reproducibility checks for an oscillatory algebraic relaxation law.

Requirements: Python 3, SciPy, SymPy.  Finite tests do not prove any limit.
"""
from math import isclose, sqrt
from scipy.integrate import solve_ivp
from scipy.special import beta
import sympy as sp

x, y, eps = sp.symbols('x y eps', real=True)
E = x**4/sp.Integer(4) + y**2/sp.Integer(2)
fx, fy = y-eps*x**3, -x**3-y**3
assert sp.expand(sp.diff(E, x)*fx+sp.diff(E, y)*fy+eps*x**6+y**4)==0
I0 = beta(0.25, 0.5)/4
I6 = beta(1.75, 0.5)/4
assert I0>0 and I6>0
assert isclose(I6/I0,0.2741679486266781,rel_tol=1e-11)
loss_prediction = lambda e: -32*e*I6

cases = 0
worst_rel_period = 0.
worst_rel_loss = 0.
for e in [0.25, 1.0]:
    errors = []
    for e0 in [1e-4, 1e-6, 1e-8, 1e-10]:
        h = e0**0.25
        def field(s, z):
            u, v = z
            return [v-2*e*h*u**3, -2*u**3-2*h**3*v**3]
        def section(s, z):
            return z[0]
        section.direction = +1
        section.terminal = False
        sol = solve_ivp(field, [0, 22], [0., 1.],
                        events=section, rtol=2e-11, atol=2e-13,
                        max_step=0.05)
        assert sol.success and len(sol.t_events[0]) >= 2
        second_time = sol.t_events[0][1]
        u, v = sol.y_events[0][1]
        period_ratio = second_time/(4*I0)
        normalized_loss = (u**4+v**2-1)/h
        rel_period = abs(period_ratio-1)
        rel_loss = abs(normalized_loss/loss_prediction(e)-1)
        assert normalized_loss < 0
        errors.append((rel_period, rel_loss))
        cases += 1
    for j in range(1, len(errors)):
        assert errors[j][0] < errors[j-1][0]
        assert errors[j][1] < errors[j-1][1]
    worst_rel_period = max(worst_rel_period, errors[-1][0])
    worst_rel_loss = max(worst_rel_loss, errors[-1][1])
assert worst_rel_period < 0.005
assert worst_rel_loss < 0.024
print(f'VERIFY_OK symbolic_energy_identity=1 small_energy_return_cases={cases}')
print(f'BETA_INTEGRALS I0={I0:.12g} I6={I6:.12g}')
print(f'LIMIT_COEFFICIENTS_EPS_QUARTER energy={1/(16*0.25**2*(I6/I0)**2):.12g} count={1/(4*sqrt(0.25*I0*I6)):.12g}')
print(f'MAX_LAST_SCALE_RELATIVE_ERRORS period={worst_rel_period:.8f} loss={worst_rel_loss:.8f}')
print('FINITE_CHECK_ONLY: asymptotic conclusions require the analytical return-map proof.')
