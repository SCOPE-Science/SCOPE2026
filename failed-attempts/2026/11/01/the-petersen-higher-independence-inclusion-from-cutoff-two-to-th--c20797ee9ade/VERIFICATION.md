---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independent replay (python3 /workspace/branches/independent_petersen.py) rebuilt faces by joining components along induced edges, found 261 and 381 augmented faces, and checked all 870 and 1350 Hasse incidences, including acyclicity for the 130 and 187 pairs. Topologically ordered integer elimination reproduced the critical masks and the two displayed degree-three and degree-four matrices. The frozen 25-term chain is an integral cycle and its projections are [912] and −[660]+[792]. Removing the empty-face pair restores one critical vertex and retains the reduced calculation. For cutoff three the degree −1 attachment to the 2-sphere gives a contractible subcomplex consisting of the 2-sphere and that 3-cell, whose quotient leaves three 3-spheres below the two 4-cells. The two primitive independent relations identify the other two basis elements with x=[792]−[660]; their degree vectors give a free direct summand, so the cofiber is a 3-sphere. Cutoff two also has the sphere model; the inclusion carries one integral generator to the other, so it is a homotopy equivalence. The sign +1 pertains to the specified generators.

## originality

FAIL

Two distinct October 18 records already classify the cutoff-three stage integrally. More decisively, the October 25 record 1e60cbad5606 proves that exactly the same nested pair admits a simplicial collapse. This is stronger than the claimed homotopy equivalence. The frozen explicit signed cycle was not found in that comparator, but +1 in its aligned generator coordinates is not a new invariant of the inclusion.

## value

FAIL

The natural stage map is mathematically meaningful, but its simple-homotopy type is already known. The alternate certificate chooses a generator without proving support optimality, an intrinsic sign comparison, equivariance, or another invariant that would make this representative a substantive remaining contribution. No standalone valuable claim survives within the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
