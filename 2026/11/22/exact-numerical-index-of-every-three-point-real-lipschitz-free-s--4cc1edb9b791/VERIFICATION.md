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

The proof in `RESULT.md` is an exact argument for all strict metric triangles and their collinear limits. Execute `python3 CHECK.py` (Python 3 standard library only) to reproduce a diagnostic of exact rational rank-one witnesses for 343 integer-parameter triangles and three additional rational cases; it asserts two quantities: numerical-radius upper bound at all six norming vertex/functionals and operator-norm lower bound at the missing coordinate. Neither finite diagnostics nor the self-review replace independent peer validation.
