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

# Reproducibility and limits

Run `python verify.py` using Python 3.8 or later. The program uses the standard library only and performs two separate checks: complete cyclic-group exponent counts for 96 admissible small systems, and complete direct finite-field irreducibility counts for 14 small prime-field systems. The latter uses its own polynomial arithmetic and the finite-field Rabin irreducibility test, rather than constructing cyclic-group roots.

The tests passed when this result was packaged. The Python computation is finite and does **not** prove the universal theorem; the proof of all dimensions and field orders is supplied in `RESULT.md`, with the nonstandard projective polynomial correspondence taken from the cited published theorem.

No independent external mathematical audit or independent formal proof is claimed.
