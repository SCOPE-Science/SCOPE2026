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

The included `verify_quotient.py` is a self-contained Python standard-library implementation of the finite exact proof and checks the face vector, all orbit-flag cells, squared boundary identities, actual cellular free-face conditions, homology-preserving unit contractions, final integer differential, and unimodular minor. A second program, `check_burnside.py`, independently enumerates face placements using occupied-row and injective-column choices and uses Burnside fixed-flag counts to verify the orbit cell vector. Both programs were executed from their included paths and completed successfully.

The final integer differential has five invariant factors equal to two because it is twice a rank-five surjection onto an integral rank-five chain group. The computation determines integral homology, not a complete homotopy type. Publication-priority claims remain subject to the stated search limitations. No independent mathematical audit has been performed.
