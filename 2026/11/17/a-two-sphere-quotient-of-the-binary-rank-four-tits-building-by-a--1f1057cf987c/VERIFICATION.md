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

Run with Python 3 standard library: `python3 verify_orbits.py` and `python3 verify_burnside.py`. `verify_orbits.py` checks that the field multiplication and Frobenius generators produce a group of order 60 and computes the direct orbit counts (4,9,7) from all 695 nonempty flags. `verify_burnside.py` independently computes the sums of fixed flags by Frobenius power and obtains the same result. The included text outputs record actual successful executions.

The conceptual steps not certified by the scripts are: (i) the standard Solomon–Tits simple-connectivity theorem for this building, (ii) the normalizer presentation and its fixed Frobenius vertex, (iii) the applicability of Armstrong's theorem to a finite simplicial action, and (iv) Hurewicz–Whitehead for the resulting simply connected two-dimensional CW complex. These steps are written out in `RESULT.md`. A finite computation without them would not prove the homotopy equivalence.

No independent mathematical audit or external verification is asserted.
