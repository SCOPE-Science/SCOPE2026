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

# Reproducibility

Run `python verify.py` using the ordinary Python 3 standard library. It needs no source data, downloads, or optional packages.

The direct tests pass for 54 separate complete PBH restriction ranks over the prime field 1000003: all levels in odd dimensions 1, 3, 5, 7, 9 and even dimensions 2, 4, 6, 8. For all four even dimensions the tempting middle-layer restriction is explicitly tested to have half the necessary rank. Additional exact-integer tests verify 2,309 harmonic lifting/intertwining identities on explicit nonzero harmonic vectors and 2,924 positive binomial coefficients in the proposed all-dimensional formula.

The proof in `RESULT.md` independently derives every infinite-dimensional assertion from the Boolean-layer raising/lowering commutator, the exact harmonic sector scalar and the PBH criterion. The finite verifier does not claim to prove universal rank, the mathematical novelty of the theorem, or independence of review. All calculations in the verifier are exact integer or prime-field arithmetic; no approximate eigenvalue tolerance is involved.
