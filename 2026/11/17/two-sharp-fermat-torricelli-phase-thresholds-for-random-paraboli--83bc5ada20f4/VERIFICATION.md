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

# Verification summary

The analytic argument derives all three exact angles from parabolic chord slopes and establishes both global maximizers of the relevant angular differences. Boundary Taylor expansions have one quadratic displacement and two one-sided linear displacements; integrating the resulting regions yields the two exact \(5/2\)-power constants. The uniform parameter density and normalized-indicator convergence prove the marked laws in total variation.

The accompanying standard-library `verify.py` was run from the complete package. It checked the threshold identities, a first-derivative cancellation, both limiting-domain volume constants, and exact-angle integration by deterministic quasi-Monte-Carlo for deficits \(0.005\) and \(0.001\). Observed ratios approached their predicted limits and the script printed `PARABOLIC_FERMAT_TWO_ONSETS_CHECKS_OK`.

The finite integrations are diagnostic only and cannot certify an infinite limiting law. The proof itself relies on explicit calculus, compact localization around unique angular maxima, elementary sublevel-domain integration and normalized-indicator convergence. No independent mathematical audit has been performed. Priority beyond the inspected published sources remains open.
