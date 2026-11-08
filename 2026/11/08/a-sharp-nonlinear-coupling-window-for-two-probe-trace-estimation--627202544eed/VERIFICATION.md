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

# Verification

The analytic derivation is in `RESULT.md`. Run the self-contained Python 3 standard-library verifier using `python3 verify.py`. It generates all 32 vertex sign states, confirms the 16 parity patterns with two lifts each, exactly enumerates every fixed sign-flip candidate, and checks the scalar countermonotone optimal coupling and all three symbolic polynomial branches. The verifier uses exact rational arithmetic for each generated parameter and checks the ordering regimes separately using affine differences; no numerical tolerance is used.

`verify_output.txt` records the actual successful execution against the embedded `verify.py`. Finite enumerations only corroborate the infinite-parameter proof and are not exhaustive over real parameter values. Global optimality depends on the supplied analytic rearrangement argument and its realizable coupling, not on a finite sample grid. No external or independent audit has been performed.
