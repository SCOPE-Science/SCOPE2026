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

# Verification of the covariance eigenvalue enclosure

Execute `python3 verify_bounds.py` in a directory containing the attached checker. This uses only Python 3's standard library and exact `Fraction` arithmetic. The script separately verifies the three rational Hilbert–Schmidt ingredients \(13/630\), \(47/11340\), \(1/30\), reconstructs \(\operatorname{tr}(\mathcal K^2)=109/8100\), and computes \(f_5\), \(f_6\), their quadratic integrals, and the exact Rayleigh and residual fractions.

The strict comparisons proving \(0.11573423652792<\lambda_1<0.11573423652794\) all use rational cross-multiplication. The second-eigenvalue estimate \(\lambda_2<1/100\) uses the exact trace-square equality and the variational lower bound. The Temple inequality and logarithmic Gaussian-tail statement are mathematically justified in `RESULT.md`; successful checker output by itself is not a proof of those operator-theoretic steps.

The verifier checks the given covariance operator, not the finite-sample statistic or a composite fitted-parameter law. It contains no simulation-based or external-certification step. The associated research review is a self-review; independent audit remains unperformed.
