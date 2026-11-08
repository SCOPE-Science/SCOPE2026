---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification record

The executable standalone `checker.py` is included. Run from its containing directory with `python3 checker.py`. Required environment: Python 3 with NumPy, SciPy and SymPy. It produces individual finite-sampling numerical comparisons and ends with a pass count.

Analytical premises verified: the drift matrix is stable for \(|u|<1\); the Lyapunov equation determines the explicitly positive covariance, and the determinant formula matches it. The stationary current matrix is an exact antisymmetric multiple of a quarter-turn matrix. The large-turn coefficient is an exact inscribed-angle circular-segment area. Its derivative is the asserted angular density. Conditional Gaussian small-lag transitions separate outer Gaussian-scale jumps and the \(\sqrt h\) near-origin core. The signed mean arises from the stationary current, and the variance coefficient from annular integration. The signal-to-variance optimum reduces to one positive root of a quadratic with signs proved at \(1/2\) and \(2/3\).

Checks run on actual standalone `checker.py`: 537 algebraic, geometric, quadrature, stationary covariance and full Gaussian-transition diagnostics passed. For \(T_x=1,T_y=5,u=1/2\), the \(h=0.012\) and \(h=0.003\) conditional Gaussian trials gave positive macroscopic-turn rates per unit \(h\) of about 0.2581 and 0.2414, compared with limit 0.2652; cubic absolute moment rates about 9.0715 and 9.3641, compared with limit 9.9965. These trials have finite-sample and finite-lag errors. Theoretical continuum results do not depend on fitting the trials.

Unproved limits: No quantitative uniform remainder in all physical parameters, no pathwise unwrapped-winding theorem, and no long-time independent increment law. Rechecking publication priority against all unindexed literature is outside the mathematical verification of this standalone result. Independent audit and external validation have not been performed.
