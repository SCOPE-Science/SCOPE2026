---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The supplied historical artifact `artifacts/verify.py` checks the unit-path pseudoinverse formula for orders two through nine and the leading stiff-limit scalar factor for filter orders one through eight. It also contains first-order finite-step diagnostics; these do not form part of the retained claim. All such checks are finite corroboration. The proof in `RESULT.md` establishes the fixed-order matrix expansion, all unit paths, the strict eventual sign implication, and the simultaneous spectral band.

The proof is for fixed filters of linear symmetric heat flows; it makes no claim about nonlinear diffusion, uniformly growing filter orders, or historical priority from computation.
