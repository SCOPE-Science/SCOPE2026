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

The supporting Python script `verify_ray_automorphisms.py` checks the finite-interval versions of all defining algebra products, all prescribed automorphism images, explicit inverses, and realizations by conjugation for 932 parameter tuples. Reproduction: run `python verify_ray_automorphisms.py` from the directory holding that script; expected output is `INFINITE_RAY_UNITIZATION_AUTOMORPHISMS_OK cases=932`.

The proof of the infinite-ray theorem is independent of finite enumeration: it uses invariance of the arrow Jacobson radical, the intrinsic directed Peirce-space graph, idempotent lifts, and the finite-support criterion for units. The script does not prove statements for infinite sequences or all fields. The historical-priority comparison includes full relevant portions of the two cited articles but cannot exhaust unindexed literature.
