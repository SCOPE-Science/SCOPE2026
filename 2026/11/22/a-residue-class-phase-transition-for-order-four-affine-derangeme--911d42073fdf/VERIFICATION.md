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

## Checks performed
The standalone integer class-size checker `check_affine4.py` was run on the delivered source and its captured text is in `check_output.txt`. It constructs the nilpotent centralizer formula and separately enumerates square-zero/fourth-zero linear maps, then their admissible translation fibers, in six finite field/dimension pairs. All checks passed. The exact order-four numerator and denominator are nonnegative integers with no conditioned probability defined for degree one.

## Proof dependency and scope
The completed argument uses the standard nilpotent Jordan centralizer order, affine fixed-point equivalence, domination by Gaussian tails, and an integer balancing lemma. Exhaustive bounded checks are not substitutes for the analytic limit proof. The derivation is for even characteristic only, and the final field-size asymptotic is taken after the dimension limit. The full text of one relevant prior article was unavailable, creating a historical-priority limitation.
