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

# Reproduction and proof checks

Run `python checks/verify.py` from the extracted package root, using Python 3 with only its standard library. The script checks the exact occupancy mixture against direct enumerations of move-to-front histories (two through five labels with one through four moves), the conditional maximum-label and fixed-coordinate distributions by exact enumeration of all injected prefixes through eight labels, and a selection of partial-injection Poisson inequalities and finite critical-shuffle total-variation comparisons. See `checks/output.txt` for actual output: 1,712 assertions passed.

The finite assertions cannot verify the universal asymptotic assertion by themselves. The complete mathematical proof and the uniform error terms appear in `RESULT.md`, including the correction for the exceptional all-selected-prefix event and the signed first-order cancellation in the occupancy mixture. The self-review passed; independent assessment has not been performed.
