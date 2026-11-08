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

# Reproducible checks

Run `python3 verify_ultrametric_spheres.py` with standard Python 3; no external packages or files are needed. The checker enumerates all unordered rooted reduced hierarchy shapes through eight leaves, realizes an ultrametric distance on leaf-prefix addresses, constructs exact nonempty spheres directly from equality of distances, and enumerates every support of cardinality one through four. It computes predicted coefficients independently from the hierarchy and verifies vanishing of the degree-four coefficient. It also checks the closed-form complete-tree coefficients for selected binary, ternary, four-ary, and five-ary parameters.

The replay performed on the attached checker produced:

`ULTRAMETRIC_SPHERE_TRACES_PASS 405 unlabeled hierarchies 53403 support tests {1: 1, 2: 1, 3: 2, 4: 5, 5: 12, 6: 33, 7: 90, 8: 261}`

The direct trace algorithm does not call the proof's classification routine; its class construction is by exact finite distances. Complete hierarchy enumeration is limited to eight leaves, and these tests alone cannot prove the universal theorem. The general proof follows from sphere normal form, LCA analysis, and the four-point obstruction. Independent scientific audit has not been performed.
