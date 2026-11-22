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

# Reproduction and bounds of verification

The portable programs `verify_forward.py` and `verify_independent.py` require only Python 3's standard library. Invoke both as scripts in a directory containing their files. Each completes full finite-state enumeration for Paley orders five and nine, using different state encodings, update loops and orbit-detection algorithms. The accompanying `forward.out` and `independent.out` are captured actual outputs and can be regenerated. Both programs assert that the complete recurrent orbit populations, individual basin sizes, first-periodic-entry counts and sharp small-order depths match the result. The second independently enumerates the twelve order-three Latin-square states.

The infinite prime-power assertion is established mathematically in `RESULT.md`, not extrapolated from runs. The critical nonstandard steps are the per-edge contact saturation proof for recurrent orbits, its exact adjacency-time identity, the temporal Fourier eigenvalue obstruction and the algebraic-integrality exclusion for both square and nonsquare Paley orders. Their hypotheses and exceptional cases are explicit. The finite programs do not enumerate all configurations for unbounded order and no uniform large-order transient bound is asserted.

Verification state: self-reviewed; independent audit not performed.
