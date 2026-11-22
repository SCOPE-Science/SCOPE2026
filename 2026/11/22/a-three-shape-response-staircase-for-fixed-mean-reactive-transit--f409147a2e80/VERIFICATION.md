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

# Reproducible verification

Run `python checker.py` with Python 3, SymPy and mpmath. The program checks the exact three rational difference identities, strict logarithmic-curvature numerators by symbolic equivalence, the unique-crossover cubic, the exact polynomial division and crossover-ordering identity, selected high-precision crossover locations, and 400 exact-rational point evaluations. Current replay output ends with `PASS 438 deterministic assertions`.

Only the symbolic identities and coefficient signs, combined with the written analytical argument in `RESULT.md`, establish the uncountable parameter claims. The numeric crossover brackets and rational spot checks do not prove global uniqueness. The checker does not validate the physical assumptions or establish historical priority. An independent scientific review has not been conducted.
