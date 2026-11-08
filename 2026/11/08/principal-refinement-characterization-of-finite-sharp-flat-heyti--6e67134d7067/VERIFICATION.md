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

# Reproduction and limits

Run `python3 checker.py` with Python 3 and no external packages. Expected success line:

`FINITE_FLAT_DI_PRINCIPAL_REFINEMENT_OK {1: (1, 2, 2), 2: (4, 64, 57), 3: (29, 14848, 9528)} total_frames 14914 valid 9587 four_world_random 600`

For each world size through three, the checker builds every preorder (including nonsymmetric and nonantisymmetric ones), every modal relation, and every upset valuation of the three variables. It computes the flat strict implication directly and compares its result with the algebra-free principal-refinement criterion. It also compares both methods on 600 seeded four-world frames. The two targeted examples check strictness of the older downward-directed sufficient condition.

The exhaustive counts are finite, not an infinite logical proof. The necessity and sufficiency directions for **all finite frames**, including those larger than the enumerated instances, appear in `RESULT.md`. Infinite frames and independent mathematical review are not certified.
