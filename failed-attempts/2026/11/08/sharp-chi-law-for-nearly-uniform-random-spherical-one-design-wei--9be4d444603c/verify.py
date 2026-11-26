"""Numerical checks for minimum relative box-radius spherical affine quadrature.

Requires NumPy and SciPy. These tests supplement, not replace, the analytic proof.
Run: python verify.py
"""
import math
import numpy as np
from scipy.optimize import linprog


def solve_box_radius(points):
    m, d = points.shape
    moment_matrix = np.column_stack((np.ones(m), points))
    sum_vector = points.sum(axis=0)
    aeq = np.column_stack((moment_matrix.T, np.zeros(d + 1)))
    beq = np.r_[0.0, -sum_vector]
    iub = np.r_[np.column_stack((np.eye(m), -np.ones(m))),
                np.column_stack((-np.eye(m), -np.ones(m)))]
    objective = np.r_[np.zeros(m), 1.0]
    result = linprog(objective, A_ub=iub, b_ub=np.zeros(2*m),
                     A_eq=aeq, b_eq=beq,
                     bounds=[(None, None)] * m + [(0, None)],
                     method="highs")
    if not result.success:
        raise AssertionError(result.message)
    delta = result.x[:m]
    radius = result.x[m]
    if np.linalg.norm(aeq @ result.x - beq, ord=np.inf) > 1e-8:
        raise AssertionError("moment equations")
    if np.max(np.abs(delta)) > radius + 1e-8:
        raise AssertionError("box constraint")
    # Independent primal/dual consistency: dual multiplier (a,u) gives
    # the ratio |u.S|/sum_i |a+u.X_i|, the exact theoretical dual formula.
    a = result.eqlin.marginals[0]
    u = result.eqlin.marginals[1:]
    denominator = np.abs(a + points @ u).sum()
    if denominator < 1e-10:
        raise AssertionError("degenerate dual multiplier")
    quotient = abs(np.dot(u, sum_vector)) / denominator
    if abs(quotient - radius) > 1e-8:
        raise AssertionError("duality identity")
    return radius


def run():
    rng = np.random.default_rng(20261104)
    count = 0
    for d in (2, 3, 5):
        cd = math.gamma(d / 2) / (math.sqrt(math.pi) * math.gamma((d + 1) / 2))
        for m in (d + 2, 18, 60, 250):
            for trial in range(6):
                points = rng.normal(size=(m, d))
                points /= np.linalg.norm(points, axis=1)[:, None]
                radius = solve_box_radius(points)
                rough = np.linalg.norm(points.sum(axis=0)) / (m * cd)
                if not math.isfinite(radius) or radius < 0 or not math.isfinite(rough):
                    raise AssertionError("non-finite statistic")
                count += 1
    print(f"VERIFY_OK {count} primal/dual and moment checks")


if __name__ == "__main__":
    run()
