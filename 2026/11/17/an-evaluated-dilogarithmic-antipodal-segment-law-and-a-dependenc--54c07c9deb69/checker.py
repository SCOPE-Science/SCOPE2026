"""Independent checks of an antipodal-segment capture law for random cyclic triangles.

Uses direct triangle half-plane tests, a positive one-dimensional integral,
and a dilogarithm evaluation. These finite checks corroborate but do not
replace the proof of the analytic identities.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import spence

PI = math.pi

def li2(x):
    return float(spence(1.0 - x))

def joint_formula(r):
    return 0.25 + (6.0 / PI**2) * li2(-r) - (3.0 / PI**2) * li2(-r * r)

def marginal_formula(r):
    return 0.25 - (3.0 / (2 * PI**2)) * li2(r * r)

def joint_integral(r):
    q = (1 - r) / (1 + r)
    def integrand(t):
        return math.atan(q * math.tan(t)) * math.atan(q / math.tan(t))
    v, err = quad(integrand, 0, PI / 2, epsabs=2e-13, epsrel=1e-12)
    return 12 * v / PI**3

def sample_both(r, n=800000, seed=45179):
    rng = np.random.default_rng(seed)
    theta = np.sort(rng.uniform(0, 2*PI, size=(n, 3)), axis=1)
    px, py = np.cos(theta), np.sin(theta)
    def test(x):
        ax, ay = px-x, py
        signed = ax * np.roll(ay, -1, axis=1) - ay * np.roll(ax, -1, axis=1)
        return np.all(signed >= 0.0, axis=1)
    a, b = test(r), test(-r)
    joint = np.mean(a & b)
    marginal = np.mean(a)
    return joint, marginal

if __name__ == '__main__':
    for r in (0.0, 0.1, 0.3, 0.5, 0.75, 0.90, 0.99):
        f, integ = joint_formula(r), joint_integral(r)
        print(f'r={r:.2f}, closed={f:.12f}, independent_integral={integ:.12f}')
        assert abs(f-integ) < 5e-12
    print('INTEGRAL_DILOG_IDENTITY_OK')
    for r in (0.1, 0.5, 0.8):
        joint, marginal = sample_both(r)
        exact_joint, exact_marginal = joint_formula(r), marginal_formula(r)
        sigma_j = math.sqrt(exact_joint*(1-exact_joint)/800000)
        sigma_m = math.sqrt(exact_marginal*(1-exact_marginal)/800000)
        print(f'MC r={r:.2f}: joint={joint:.8f} exact={exact_joint:.8f} ; marginal={marginal:.8f} exact={exact_marginal:.8f}')
        assert abs(joint-exact_joint) < 6*sigma_j + 0.0001
        assert abs(marginal-exact_marginal) < 6*sigma_m + 0.0001
    print('CARTESIAN_TRIANGLE_MONTE_CARLO_OK')
    assert abs(joint_formula(0) - 0.25) < 1e-14
    assert abs(joint_formula(1)) < 1e-13
    c = 3 / (2 * PI**2)
    for r in (0.99, 0.999):
        scaled = joint_formula(r)/(1-r)**2
        print('r=',r,'scaled=',scaled,'limit=',c)
        assert abs(scaled-c) < 0.002
    print('SHARP_ENDPOINT_COEFFICIENT_OK')
    def covariance(r):
        return joint_formula(r)-marginal_formula(r)**2
    print('covariance at 0.5 =',covariance(0.5),' at 0.75=',covariance(0.75))
    assert covariance(0.5)>0 and covariance(0.75)<0
    print('DEPENDENCE_SIGN_REVERSAL_OK')
