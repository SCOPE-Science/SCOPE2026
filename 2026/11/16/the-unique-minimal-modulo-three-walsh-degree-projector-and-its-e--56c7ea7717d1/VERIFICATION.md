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

# Computational verification

Run `python3 check.py` in the folder containing this file and the attached checker. The checker requires only Python 3 standard-library `math`. It forms all Walsh coefficients directly by an integer fast Walsh transform for dimensions 3–12; it also forms independent integer Krawtchouk sums through dimension 18. Their absolute sums match the closed all-residue formulas, and all asserted minima and ties are checked. The final tests verify the elementary binomial recurrence and positivity for dimensions 3–100. Expected last line: `MOD3_PROJECTION_EXACT_PASS n=3..18; inequality n=3..100`. These tests do not establish the general theorem; the algebraic proof is contained in RESULT.md. All calculations are exact integer operations, with no floating tolerance.
