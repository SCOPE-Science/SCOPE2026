---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The ordered pair at step i is (x_{i-1},x_i); overlap with the next pair reconstructs the indexed input from a closed path with specified starting site. Closing the path enforces the repeated slots even for 1 and 2 sites; no rotation multiplier enters. The trace therefore counts the full fiber. Capping each nonnegative entry at two commutes with capped multiplication and preserves whether the sum on the diagonal is one. In a separate endpoint-set encoding I generated all 476 states, with 136 accepting, and checked the denominator product, the recurrence vector at exponent 21 in every state, and the full numerator through degree 20. Multiplication by further powers of the transition matrix yields the recurrence for every n>=21; it is not inferred from the observed sequence. Exhaustive direct counts at n=1,...,12 also agreed, as did the transfer counts through n=16.

## originality

PASS

The distinct claim is the evaluated all-length series for unrestricted indexed periodic singleton fibers of Rule 232. Available predecessor formulas, image counts, and related singleton enumerations do not give it. Neither the shared finite-state method nor the common denominator factor with the open-boundary series is claimed as independent novelty.

## value

PASS

Unique reconstruction from one observed cyclic configuration is a natural refinement of image enumeration for this classical majority rule. The exact rational series resolves every indexed ring size, and distinguishes the count of outputs that carry enough information to recover the input even when the total image count alone is known. The exact recurrence makes the refinement usable at lengths beyond direct enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
