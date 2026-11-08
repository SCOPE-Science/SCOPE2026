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

The self-contained Python 3 program `verify_weighted_crown.py` was executed from its actual source path using only Python standard-library exact rational arithmetic. It directly enumerated all feasible normalized integral graph potentials on crown graphs of sizes `n=3,4,5`, independently computed weighted variances for twelve positive rational profiles, and checked maxima and equality shapes against the formula. Feasible counts were 141, 495, and 1723. Output included `ALL_WEIGHTED_CROWN_CHECKS_OK` and `ALL_ARBITRARY_WEIGHTED_CROWN_CHECKS_OK`.

Reproduce with `python3 verify_weighted_crown.py`. Finite enumeration is not an infinite proof. The integer tight-edge classification and PARTITION reduction are supplied in `RESULT.md`, and the input complexity statement uses binary-encoded rational masses. Independent mathematical audit: not performed.
