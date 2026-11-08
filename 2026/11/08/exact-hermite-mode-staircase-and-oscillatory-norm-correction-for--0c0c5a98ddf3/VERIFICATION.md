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

# Verification performed

The direct analytical proof uses exact integration by parts, monotonicity of the logarithmic mean, and uniform Stirling expansion of a Poisson-density integral. The script `verify_annulus.py` was run using the Python standard library and returned `ANNULUS_MODE_CHECKS_PASS 1320`. Its numerical checks covered positive/equal mode ordering, the adjacent-difference identity, switching equations, cusp slope formulas, and the second-order large-radius approximation over representative values. These finite checks do not prove the universal theorem; that responsibility rests on the displayed exact calculations.

No independent audit or external mathematical validation has been performed. Known Hermite diagonalization is credited to foundational literature. Historical novelty is subject to possible equivalent mixed-Poisson results.
