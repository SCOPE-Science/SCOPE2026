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

# Reproducibility and verification

Run `python3 verify.py` using Python 3 and only its standard library. At packaging, the script passed 624 finite checks. It exactly evaluates rational coefficient ratios and the polynomial difference identity for each integer \(2\leq n\leq150\), tests the cumulant normalizations for several values, and numerically checks the monotone shape, optimizer, transition expansion, and high-noise expansion.

The proof's critical nonstandard statement is that \(\Theta(x)=(xh'(x)-h(x))/h(x)^2\) is strictly decreasing for every \(x>0\). The coefficient ratios and covariance argument in `RESULT.md` prove that statement analytically; finite integer tests cannot establish it. The displayed asymptotic constants are derived by analytic expansion/inversion. No external randomness, fitted parameters, or numerical optimizer is needed to reproduce the checks, and no independent validation is implied.
