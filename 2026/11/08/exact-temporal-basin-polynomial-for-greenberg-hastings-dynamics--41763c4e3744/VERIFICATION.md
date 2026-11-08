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

## Verification scope

The algebraic proof uses a complete 49-state quotient for the pair of nonempty shore-color supports; it is not a large-graph search. All 49 quotient cases and the ten refined coefficient classes were recomputed in `verify_support.py`, including the two cycle supports, the uniform four-step upper bound and closed counts for 900 positive parameter pairs. `verify_direct.py` independently enumerates 63,972 labelled configurations spanning 28 parameter pairs \((m,n)\) with \(m+n\le8\), computes their actual first-entry time and least eventual period, and agrees with the polynomial.

The captured exact outputs are `support_output.txt` and `direct_output.txt`. Each code file is standalone Python 3 and has no dependencies outside the standard library. The finite checks do not substitute for the uniform support-map proof. Checks of probabilistic or asynchronous variants were not performed, because neither is within the claim.
