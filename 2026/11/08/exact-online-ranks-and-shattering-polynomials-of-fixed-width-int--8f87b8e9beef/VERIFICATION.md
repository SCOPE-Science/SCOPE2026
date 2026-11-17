---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For m=n−r+1 equal-width intervals of length r on a finite chain, a full depth-h query tree needs ≥2^h distinct starts (or m+1 with the null concept), and the positive branch of any root query holds at most r starts, yielding the two upper bounds. On any consecutive block of ≤r starts, querying x=a+t−1 is a prefix threshold: balanced splits create depth floor log₂ of the block size. A first split into two blocks of 2^{h−1} gives the matching minus case; induction with ∅ plus 2^h−1 starts gives plus case. A triple cannot be shattered because any interval containing first/third contains the middle; exact pair-trace conditions and inclusion-exclusion yield both polynomial quadratic coefficients and singleton count. The null jump occurs exactly m=2^k−1 with r≥2^{k−1}; boundary m=1,r=1 checked. Independent direct minimax and support enumeration for all n≤12 confirmed formulas, not a proof of unlimited n.

## originality

PASS

The paired exact formulas for *linear* same-length intervals with or without ∅ and their exact shattering coefficients survive; previous exact cyclic translate rank, variable-width interval work, and general Shelah-rank literature concern different hypothesis classes or broader bounds.

## value

PASS

The exact adaptive online-query complexity and every shattered-support count for fixed-size windows are motivated finite learning invariants. The precise null-concept dyadic boundary and unbounded static/adaptive gap for n=2r resolve natural behaviors not implied by cyclic-window or variable-width results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
