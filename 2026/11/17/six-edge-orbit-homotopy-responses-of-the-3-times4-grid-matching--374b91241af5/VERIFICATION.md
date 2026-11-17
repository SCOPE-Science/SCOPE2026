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

Run `python3 verify_grid34_defect.py` from the extracted package. The entire face-poset cover graph is rebuilt for every case. The matching orders, global DAG test, two graph reflections, critical-cell counts and independent signed matching-polynomial checks are all executed anew. The reference output is `verify_grid34_defect.out`; the required last line is `GRID34_ALL_EDGE_DELETION_HOMOTOPY_PASS`.

The finite checks cover one intact complex, six distinct edge-orbit deletion complexes, and the six corresponding links. Explicit enumeration is exhaustive for those finite complexes, but no infinite-width extrapolation is claimed. The inclusion splitting follows mathematically from the deletion–link homotopy pushout and the nullhomotopic attaching maps, not merely from the logged finite counts. Independent validation has not been performed.
