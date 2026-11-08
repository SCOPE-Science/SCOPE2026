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

Run the included `checker.py` using Python 3 standard library only. It enumerates all rim functions in \(\{-1,0,1\}^m\) for \(3\le m\le10\), filtering unit-difference path and cycle constraints, and calculates the variance as an exact `fractions.Fraction`. It checks the formula, complete minimizing-zero and balancing profile description, and candidate sufficiency, as well as the one-edge parity formula for \(4\le m<200\).

The standalone proof in `RESULT.md` proves the integrality reduction, count inequality and equality cases for all admissible integers, independently of the finite checker. No finite enumeration is presented as an infinite certificate. Full text was inspected for the primary theory and comparative statements; unindexed equivalent literature remains possible. Independent audit was not performed.
