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

The proof reduces every permitted colour fibre to either at most \(d+1\) vertices or a full union of deleted pairs of size \(d+2\). Counting disjoint exceptional fibres and bounded remaining fibres produces the stated formula for arbitrary integers in its domain. The exact leading coefficient follows by counting colourings with the maximum number of colour classes, and all strict lower-degree cases are accounted for.

`verify.py` independently evaluates the original vertex-neighbour defect constraint and compares with a disjoint named-bin dynamic program. The actual package-path replay checks 608 direct colouring profiles for orders 2 through 8, palette sizes 1 through 4 and every deleted matching size and defect in the indicated ranges; it also checks parity and the difference leading coefficient through order 10. Expected final output ends in `VERIFY_OK`.

Finite exhaustive checks have finite ranges; they do not independently prove the all-parameter theorem. No external mathematical audit has been performed.
