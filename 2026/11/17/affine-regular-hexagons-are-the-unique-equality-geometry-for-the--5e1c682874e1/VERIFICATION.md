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

# Verification and limits

The elementary lower bound follows from three triangle inequalities and does not use the checker. The equality argument consists of: (1) equality in every nonnegative summand; (2) equality of all three vector norms; (3) construction of the six normalized chord vertices; (4) uniqueness of the six edge-supporting half-planes; and (5) the reverse exact hexagonal witness. `checker.py` computes the canonical witness using fractions, not floating point.

The packaged computation checks the finite witness, **not** all normed spaces. The general proof is the analytic convex-geometric argument in RESULT.md. The theorem does not claim to re-establish any preexisting critical endpoint Fermat–Torricelli equivalence or provide quantitative almost-equality stability. Independent audit: not performed.
