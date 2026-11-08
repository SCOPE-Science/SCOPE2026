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

The independent channel is not assessed. Reproduce with `python verify.py`: it tests the integer-valued inclusion-exclusion formula against direct binary-profile enumeration for each labeled graph with 1 through 5 vertices, deterministic samples with 6 through 8 vertices and maximum degree 4, and an eight-edge six-vertex counterexample. Output is `VERIFY_OK graphs= 3126 witness_edges= 8`. The six-vertex witness is checked exhaustively over all its 64 profiles; the general theorem follows from affine finite-field algebra, not experiments.
