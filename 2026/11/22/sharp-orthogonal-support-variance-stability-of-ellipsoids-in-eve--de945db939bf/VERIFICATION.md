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

# Checks and boundaries

Run `python3 verify.py` from the extracted artifact directory. It uses only Python's standard library and checks exact rational spherical moments in dimension three, the degree-\(4\)/degree-\(6\) orthogonality and seeded random orthogonal-frame diagnostics. The independent analytical proof is in `RESULT.md`, including the general dimension Gegenbauer formula and its strictly decreasing coefficient ratio. Finite tests do not prove an all-dimensional claim.

A source reading comparison found historical exact-frame characterization; no independent proof or novelty certification is claimed. See `REVIEW.md` and `AUDIT.json` for the self-review and priority risks.
