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

The exact finite proof certificate is `artifacts/verify.py` (Python 3 standard library only). Run `python3 artifacts/verify.py` from the folder holding this file and `artifacts/`.

It enumerates all 59049 normalized ternary labels, independently enumerates 19683 fixed-tree edge-increment assignments, and asserts that the normalized extreme-potential sets agree. It checks 1410 facets, 11 Euclidean norm shells, all joint facet-vertex counts, and 18 orbits under 120 pair-label permutations and central inversion. It uses integer arithmetic throughout. There is no sampling, external dependency, unbounded search, or floating-point acceptance threshold.

Completeness relies on the proved connected-tight-edge criterion and the Petersen graph's diameter two. The computational claim is **finite**; no generalization to other Kneser graphs is certified. The new result has not received independent mathematical audit.
