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

# Reproducibility

Run `python checker.py` with Python 3.9 or later; no third-party libraries or network access are required. The program uses exact integer and rational arithmetic and reconstructs the finite model from scratch. It checked the closed expression for the coefficients against the derived recurrence through index 85, the nonnegative extremal urn weights and complete factorial-moment identities for matching sizes 3 through 30, the impossible coefficient one coordinate beyond the claimed ceiling, and all prescribed-edge moments by exhaustive enumeration of every perfect matching through size six. The observed output is `PASS 1258 exact assertions; m=3..30, k=0..85, direct matchings m=2..6`.

The proof for all sizes rests on the explicit binomial-moment obstruction and recurrence with an induction establishing nonnegativity. Exhaustive enumeration stops at the stated finite sizes and is not represented as an infinite certification. Mathematical review is same-model only; no independent audit has been performed.
