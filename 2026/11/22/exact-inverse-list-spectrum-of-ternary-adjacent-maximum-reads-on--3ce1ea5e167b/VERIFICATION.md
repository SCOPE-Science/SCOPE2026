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

# Reproducibility and scope

Run `python3 verify.py` using Python 3 with only the standard library. For all read lengths \(1\le m\le14\), the checker constructs every proper ternary source of length \(m+1\), computes its complete ordered adjacent-maximum read, and compares the resulting fibers with both the run-pair theorem and an independently programmed two-state recurrence. The total enumerated sources are \(98{,}298\).

The checker also expands the exact bivariate rational generating function by coefficient recurrence to read length \(100\), comparing all predicted inverse-list histograms, source mass, output counts and extremal formulas. All integer calculations are exact. The theorem is for arbitrary positive read length; finite verification is supportive and cannot replace the analytic proof in `RESULT.md`.

No independent audit or external validation is asserted.
