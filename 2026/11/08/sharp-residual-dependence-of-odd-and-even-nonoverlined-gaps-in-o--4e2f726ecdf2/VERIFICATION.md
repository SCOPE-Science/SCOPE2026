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

# Reproduction and verification boundaries

Run `python3 verify.py` in the same directory as this file; it requires only Python 3 standard-library modules. The program computes overpartition coefficients from the independent Euler-product expansion; separately enumerates all overpartitions of weights \(0\) through \(12\) and tests odd/even nonoverlined-presence events; computes exact finite-sample joint dependence inequalities through weight \(3000\); and prints squared-gap covariance ratios for five weights. The committed output is `verification-output.txt`. Compare actual standard output to those bytes to test reproducibility.

The direct tests are finite: \(208\) joint-bijection cases and \(108036\) inequality cases. Numerical covariance values move toward the predicted limit but are not extrapolations used as proof. The infinite asymptotic relies on the published Rademacher formula plus the elementary mixed second-difference and weighted Riemann-sum estimates detailed in `RESULT.md`. The independent-audit status remains unperformed.
