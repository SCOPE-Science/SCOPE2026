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

The accompanying `verify.py` enumerates the distinct quadratic-residue values and independently constructs their third convolution for all moduli from two to \(2^{12}\). It checks every target against the exact recurrence (8190 target comparisons), total ordered mass, exact maximal-fiber classes, energy recurrence, and the rational asymptotic coefficient identity. The recorded successful terminal marker is `TRIPLE_SQUARE_IMAGE_CHECK_OK 8190 target comparisons, 12 levels`.

The finite checker does not prove the all-depth theorem. The proof relies on complete residue-class decomposition, cardinalities of odd square values, recursive scaling of even values, and a convergent energy recurrence. No independent external mathematical audit has been performed.
