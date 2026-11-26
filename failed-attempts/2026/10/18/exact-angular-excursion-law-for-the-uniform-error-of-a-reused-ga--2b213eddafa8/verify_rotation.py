"""Standalone finite numerical checks for the rotating-matrix range-finder theorem.

These finite checks are diagnostics; the attached mathematical proof handles the
continuum and limiting claims. Requires Python >=3.9, NumPy and SciPy.
"""
import math
import numpy as np
from scipy.integrate import quad

rng = np.random.default_rng(301611)
residual_checks = 0
max_checks = 0
for eps in (0.005, 0.07, 0.31, 0.9):
    for alpha in (0.0, 0.3, 1.2, 2.4, math.pi):
        for _ in range(60):
            g = rng.standard_normal(2)
            theta = math.atan2(g[1], g[0]) % math.pi
            t = rng.uniform(0, alpha) if alpha else 0.0
            c, s = math.cos(t), math.sin(t)
            R = np.array([[c, -s], [s, c]])
            A = R @ np.diag([1.0, eps]) @ R.T
            y = A @ g
            P = np.outer(y, y) / np.dot(y, y)
            direct = np.linalg.norm((np.eye(2) - P) @ A, 2)
            phi = theta - t
            predicted = eps / math.hypot(math.cos(phi), eps * math.sin(phi))
            assert abs(direct - predicted) < 2e-12, (eps, alpha, direct, predicted)
            residual_checks += 1
            # Check exact supremum against brute-force dense mesh, which may miss
            # the true maximizer by at most the mesh width.
            target = (theta - math.pi / 2) % math.pi
            if alpha >= math.pi or target <= alpha:
                d = 0.0
            else:
                d = min(target - alpha, math.pi - target)
            exact = eps / math.hypot(math.sin(d), eps * math.cos(d))
            grid = np.linspace(0, alpha, 1001)
            approx = (eps / np.sqrt(np.cos(theta-grid)**2 + eps**2*np.sin(theta-grid)**2)).max()
            assert approx <= exact + 2e-11, (eps, alpha, approx, exact)
            if alpha == 0:
                assert abs(approx-exact) < 2e-11
            max_checks += 1

# CDF and expectation checks against independent high-accuracy integration.
cdf_checks = 0
expectation_checks = 0
for eps in (0.02, 0.15, 0.64):
    for alpha in (0.0, 0.4, 1.7, 3.0, math.pi):
        b = (math.pi - alpha) / 2
        # Evaluate exact expectation using geometry and independent numerical
        # angular integration over theta.
        ex_formula = alpha/math.pi + 2*eps/math.pi * quad(
            lambda d: 1/math.hypot(math.sin(d), eps*math.cos(d)), 0, b,
            epsabs=5e-13, epsrel=5e-13)[0]
        def max_at_theta(theta):
            target = (theta - math.pi/2) % math.pi
            if alpha >= math.pi or target <= alpha:
                d = 0.0
            else:
                d = min(target-alpha, math.pi-target)
            return eps / math.hypot(math.sin(d), eps*math.cos(d))
        # Split integration at geometric boundaries to resolve the atom.
        boundaries = sorted(set([0.0, math.pi, math.pi/2, (math.pi/2+alpha) % math.pi]))
        angular_mean = sum(quad(max_at_theta, left, right, epsabs=1e-12, epsrel=1e-12)[0]
            for left,right in zip(boundaries[:-1],boundaries[1:])) / math.pi
        assert abs(ex_formula-angular_mean)< 3e-10, (eps,alpha,ex_formula,angular_mean)
        expectation_checks += 1
        for z in (eps, (1+eps)/2, 0.83+0.17*eps, 1.0):
            delta = math.asin(min(1.0, eps*math.sqrt(max(0.0,z**-2-1)/(1-eps**2))))
            predicted = min(1.0,(alpha+2*delta)/math.pi)
            # Geometric angular coverage verified deterministically by a fine mesh
            angles = (np.arange(150000)+.5)*math.pi/150000
            targets = (angles - math.pi/2)%math.pi
            d = np.where(targets <= alpha, 0., np.minimum(targets-alpha, math.pi-targets))
            measured = np.mean(d <= delta + 1e-14)
            assert abs(measured-predicted) < 2e-5,(eps,alpha,z,measured,predicted)
            cdf_checks += 1

# The Frobenius residual is rank one, so the expected squared pointwise
# spectral error is also the expected squared Frobenius error.
pointwise_second_moment_checks=0
for eps in (0.0007,0.02,0.1,0.6,0.9):
    value=2/math.pi * quad(lambda x: eps**2/(math.cos(x)**2+eps**2*math.sin(x)**2),0,math.pi/2,epsabs=2e-13)[0]
    assert abs(value-eps) < 2e-11,(eps,value)
    pointwise_second_moment_checks+=1

# Verify logarithmic-leading and constant coefficient of the expectation.
asymptotic_checks = 0
for alpha in (0.0, 0.35, 1.6, 2.8):
    b = (math.pi-alpha)/2
    for eps in (1e-3, 1e-5, 1e-7):
        delta = 2*eps/math.pi * quad(lambda d: 1/math.hypot(math.sin(d),eps*math.cos(d)),0,b,epsabs=1e-11)[0]
        asymptotic = 2*eps/math.pi*math.log(4*math.tan(b/2)/eps)
        assert abs(delta - asymptotic) < 4e-5 * eps,(alpha,eps,delta,asymptotic)
        asymptotic_checks += 1
print('PASS direct_projection',residual_checks)
print('PASS supremum_geometry',max_checks)
print('PASS exact_expectation_quadrature',expectation_checks)
print('PASS exact_tail_angular_coverage',cdf_checks)
print('PASS logarithmic_asymptotics',asymptotic_checks)
print('PASS pointwise_squared_expectation',pointwise_second_moment_checks)
