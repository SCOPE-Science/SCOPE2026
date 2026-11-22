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

Run `python3 verify_primary.py` and `python3 verify_independent.py` from the directory containing the embedded source files. The programs require only the Python standard library. Both were executed against the included code and all assertions passed.

The first implementation enumerates every one of the 8192 masks for each 13-element shore, checks the 821 geometric stable phases, all projection fiber multiplicities, the iterate identity, and all reduced orbit and entrance-time formulas. The second independently builds the 13-point, 13-line projective plane using affine coordinates and the line at infinity, validates the incidence axioms and repeats the complete two-shore classifications. The proof of the all-26-vertex state census uses the exact algebraic product/swap decomposition; it does not assert direct inspection of all 67,108,864 full states.

The checks are finite and exhaustive over the complete 13-bit shores, not simulations sampled from an infinite problem. Publication-priority claims remain conditional on the inspected literature; independent expert checking has not been performed.
