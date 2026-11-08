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

Run `python3 artifacts/check_coverage_crossings.py` from package root; no external Python packages or network are required. The program checks all specified rational integer-power comparisons, constructs a rational three-species family via perturbation, and independently calculates expectation of missing mass by enumerating sample sequences for two small model families. It verifies a four-species five-reversal witness and tests one induction step with \(b=1/200\). Exact rational arithmetic avoids floating-point sign ambiguity.

The infinite \(m\)-parameter theorem is established by analytic generalized Descartes and a limiting-perturbation argument, not by the finite program or test log. The script does not exhaustively classify all pairs of profiles or sample sizes. The real-exponent zero bound and the inductive choice of a sufficiently small rational parameter are established in RESULT.md. No independent external validation has been performed.
