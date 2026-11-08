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

# Exact verification

Run the bundled script with `python3 richardson_weak_fano_check.py` using Python 3 and only its standard library. Its integer determinant and rational Cramer-rule enumerations independently reconstruct vertices, facet normals, smooth maximal cones, anticanonical vertex multiplicities and exceptional surface fans; direct lattice-point enumeration verifies the degree.

Expected successful console lines, reproduced in the actual check:
```
SOURCE_MINKOWSKI_POLYTOPE_OK 34 sums, 16 integral vertices, 8 facet normals
SMOOTH_CUBICAL_NORMAL_FAN_OK 16 unimodular cones
WEAK_FANO_NONFANO_INDEX_TWO_OK 12 anticanonical vertices; multiplicity pattern 8+4 pairs
TWO_DISJOINT_EXCEPTIONAL_P1xP1_OK 4 maximal cones through each
EHRHART_HALF_ANTICANONICAL_OK [1, 14, 69, 216, 525] L^4=20, (-K)^4=320
```

The exact calculations validate finite fan and polytope input; mathematical conclusions for the corresponding projective toric fourfold use the written orbit–cone, divisor and local singularity arguments. No separate specialist or independent audit has been performed.
