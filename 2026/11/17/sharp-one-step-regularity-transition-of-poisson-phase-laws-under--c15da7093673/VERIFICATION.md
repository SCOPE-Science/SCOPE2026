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

# Verification scope

The written proof reconstructs the map derivative, the Poisson-to-Möbius rigidity of orientation-preserving circle homeomorphisms, the unique cubic critical preimage at unit amplitude, and the two quadratic critical preimages above it. It handles coincident fold images by adding nonnegative singular contributions. The standard-library script `verify.py` checks critical derivative identities and numerically verifies the local leading singular coefficients at multiple source/target scales.

The numerical checks do not prove the statements for all parameters or all \(L^p\) exponents. The limiting estimates, exact nonclosure and regularity classification are established analytically in RESULT.md. No independent audit or external certification has been performed. The motivating preprint's full text was not available for inspection, so historical priority is not exhaustive.
