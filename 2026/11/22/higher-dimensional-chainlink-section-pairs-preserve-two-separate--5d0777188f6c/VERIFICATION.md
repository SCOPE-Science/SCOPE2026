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

`python3 check.py` performs exact-rational reconstruction of the vertices and facet polygons for six four-coordinate parameter instances. It evaluates separately the coordinate-boundary facet areas in units of `sqrt(3)` and the cyclic-difference facet areas in units of `sqrt(8)`, and checks equality at complementary heights. It also checks that the example `(4,5,6,7), ell=2, t=9` has 16 vertices and its `t=13` complement has 15. The code has no nonstandard dependencies and prints `CHAINLINK_FACET_CLASS_EXACT_PASS cases=6` on success.

The general proof is mathematical and is **not** reduced to this finite computation. Its external premises are the published complementary Ehrhart-quasipolynomial identity, complementary volume identity, and the half-integrality statement for integer chainlink data, all from arXiv:2211.08382v1. The parameter-shape derivative and both facet-lattice covolumes are derived in the proof. Historical priority remains subject to additional literature checking. Independent validation: not performed.
