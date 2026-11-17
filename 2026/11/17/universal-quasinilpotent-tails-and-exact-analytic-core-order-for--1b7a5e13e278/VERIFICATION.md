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

The proof of the general theorem is in `RESULT.md`, Steps 1–6. The essential identities are the backward predecessor formula and exact forward-orbit decomposition; they are derived from basis shifts and summability, not inferred from computation.

Run `python verify.py` using Python 3 and the standard library. A successful run produces `PASS 2555 exact rational/integer identities; no numerical tolerance`. The checker uses exact `Fraction` values and integer arithmetic to verify coefficient identities for nonmonotone positive weights and the explicit quadratic-vs-linear damping exponents.

Finite calculations do not prove an all-indices or all-weights theorem. The infinite quantifiers are handled by superexponential product bounds and by the exact algebraic coefficient arguments in `RESULT.md`. Previous scientific papers and their general principles are credited there. Independent audit has not been performed.
