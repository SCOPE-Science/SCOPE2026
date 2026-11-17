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

# Verification of the new mathematical statement

The analytical proof in `RESULT.md` verifies the uniform derivative bound, the inverse-function return, the exact basin geometry, and the physical-time Floquet exponents. The checker in `checker.py` was executed from the packaged candidate contents and returned `SEWED_FOCUS_BASIN_RATE_CHECK_OK`. It uses exact fractions for finite telescoping identities, then floating-point diagnostics for selected nonfixed return iterates, multipliers and asymptotic normalizations.

**Proof limits:** Finite checks cannot establish infinitely many basin identities or the asymptotic distribution; those claims rely on the explicit monotonic inverse map, exact telescoping sum and asymptotic analysis in `RESULT.md`. Independent audit is not performed.
