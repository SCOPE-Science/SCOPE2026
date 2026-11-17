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

# Verification and reproducibility

The analytic proof uses the exact affine gap density \(6/(2\pi)^3\), trigonometric factorization, a Taylor expansion uniformly controlled in the radial variable, and dominated convergence over the open simplex. The crucial integrability condition is \(\int_\Delta h^{-5/3}<\infty\); without it, termwise asymptotic integration would be unjustified. The nonvertex edges contribute \(O(t^2)\), which is negligible compared with \(t^{5/3}\).

Run `python verify_small_area.py` with the versions described in `requirements.txt`. The checker independently evaluates the coefficient double integral with adaptive quadrature, checks the leading \(\pi^2/4\) integral, and independently draws 4,000,000 sets of four uniform circular points to compare the predicted small-area probabilities for five thresholds. It has completed with message `CYCLIC_QUAD_SMALL_AREA_TWO_TERM_DIAGNOSTIC_OK` and coefficient \(C_*\approx0.242278704743\). The observed probabilities at thresholds \(0.2,0.1,0.05,0.02,0.01\) were respectively \(0.0790200,0.0368148,0.0175268,0.0067255,0.0033093\); the two-term predictions were respectively \(0.0802336,0.0370507,0.0175596,0.0067232,0.0032956\). The largest-threshold discrepancy is compatible with neglected higher-order terms, and no finite-threshold accuracy guarantee is claimed.

Monte Carlo is not a certificate of infinite asymptotics. The singular integral was numerically evaluated, not reduced to elementary constants. No independent mathematical or historical audit was performed.
