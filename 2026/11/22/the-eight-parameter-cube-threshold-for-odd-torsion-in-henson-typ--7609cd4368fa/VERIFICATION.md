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
Execute `python3 verify_cube_threshold.py` (standard Python 3, no third-party dependencies). `verification_output.txt` was captured from this exact self-contained program.

The generator recursively adds a vertex adjacent to each independent subset of the prior graph; any triangle-free graph can be recovered by vertex deletion. Its class filter uses invariant buckets only to reduce candidates, with exact adjacency-preserving isomorphism backtracking within every bucket. Exhaustive alternating-set computations check the recurrence independently for each of the 410 eight-vertex classes and each of the 256 cube-induced graphs. The checker verifies the full 256-square integer Boolean-meet congruence and the inertia signs.

Observed output ends with `VERIFY_OK`. The verified 8-vertex class counts are 410; only one has alternating independence sum 3, and none has another value of absolute size at least 3. The 256 cube diagonal entries have 138 zeros, 105 units, twelve 2-magnitude entries and one 3-magnitude entry, giving the Smith and inertia conclusions in the theorem.

Boundaries: Verification is a complete finite enumeration *for the stated eight-vertex range* supported by a provided algorithm, not a claim of global finite-to-infinite extrapolation. No independent mathematical audit is claimed.
