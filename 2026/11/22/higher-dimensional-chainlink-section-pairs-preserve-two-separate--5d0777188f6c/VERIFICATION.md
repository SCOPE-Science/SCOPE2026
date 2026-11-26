---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python3 check_witness.py` with standard-library Python. It exhausts the intersections of three independent defining planes with the section hyperplane, keeps feasible points, and reconstructs each facet polygon by exact rational arithmetic. At heights 9 and 13 it checks vertex counts 16 and 15, separate facet counts 7 and 4, and separate Euclidean area totals in units of √3 and √8 given by 43 and 49/2. Its face-vector output uses the convex three-polytope Euler relation. The no-smaller-dimension assertion follows from the open-facet-height interval proof in `RESULT.md`, not from the finite calculation.
