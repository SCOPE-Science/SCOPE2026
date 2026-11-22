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

# Verification

The central inequalities and asymptotic coefficient are proved in RESULT.md. A separately runnable Python 3 standard-library checker is included as `checker.py`. Invocation: `python3 checker.py`.

Exact checks: four evaluations of a rational polynomial using arbitrary-precision integer fractions certify the alternating signs of the derivative of the two-band witness. The analytic Rolle-based zero bound then establishes **exactly three** distinct positive critical points; the finite checker does not need a numerical root-count heuristic.

Supplementary floating-point diagnostics: bisection reproduces the three illustrated critical standard deviations, tests the ordering of the local extrema, and compares large-separation numerical tie widths with the theoretical coefficient \(2^{4/3}\). These finite diagnostics are not independent validation, an exhaustive parameter scan, or an infinite mathematical proof. The proof applies only to the stated point-release Gaussian probability and asymptotic regime.
