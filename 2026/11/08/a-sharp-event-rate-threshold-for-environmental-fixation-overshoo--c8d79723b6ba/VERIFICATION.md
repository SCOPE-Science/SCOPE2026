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

The standalone `verify.py` solves the four transient equations in exact rational arithmetic for a deterministic parameter grid; it compares the independent linear-system result with the closed-form expression, the frozen probabilities, and the neutral-gap identity. It also checks exact numbers for a nonmonotone regime and the stated two-individual obstruction by direct first-event fractions.

Run: `python3 verify.py`. All computations are finite diagnostic checks. The universal statements require the algebraic factorization and quadratic root arguments in `RESULT.md`; grid tests alone would not prove them. No independent audit has been performed.
