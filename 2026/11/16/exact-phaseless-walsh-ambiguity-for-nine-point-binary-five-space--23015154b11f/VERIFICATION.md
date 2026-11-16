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

# Exact checks

Run `python3 verify.py` from this directory with Python 3 and no external packages. The program exhausts the stated finite normal forms and uses integer arithmetic only. It verifies 168 invertible transformations in three dimensions, 148 admissible length-nine relation-code generator-column multiplicity vectors, their six classes, all 11,440 nine-point subsets of the Boolean four-cube, and both independent methods of evaluating each rank-five representative's Walsh histogram. It also verifies the stabilizer-derived orbit-size total and the precise eight-profile, nine-orbit histogram fibers.

Expected final line:

`CHECK_OK nine_affine_orbits=9 distinct_walsh_histograms=8 nine_point_subsets= 28048800 exact_double_histogram= [(15, 13, 3, 0, 1)]`

The proof of completeness is the reduction from arbitrary full-span point sets to all admissible generator-column multiplicities, and from lower-rank point sets to all four-space subsets. Exhausting these specified finite sets therefore covers every nine-point subset of the five-cube. No independent mathematical audit has been performed. Historical-priority checking is bounded to the identified sources and searches.
