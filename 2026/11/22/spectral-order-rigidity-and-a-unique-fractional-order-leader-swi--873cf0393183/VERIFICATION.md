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

# Verification instructions

From the directory containing this file and `verify.py`, run:

```sh
python3 verify.py
```

No packages outside the standard Python library are needed. The checker constructs and grounds the combinatorial Laplacian with exact rational arithmetic, inverts the follower matrices, and compares inverse powers \(r=1,2,3\) with the exact spectral formulas for all \(2\le p\le7\), \(2\le q\le8\). For each tested instance it compares all three leader orbit types, not only predicted winners. It separately samples sorted reciprocal-spectrum partial-sum inequalities on \(2\le p,q\le30\) and brackets the exceptional real root.

Observed replay: 378 exact matrix-to-spectrum identities, 126 exhaustive orbit minimizer comparisons, 50,454 leading-partial-sum checks, all PASS. The approximate root is 1.129331650967238. Finite arithmetic does not establish the all-size and continuous-order theorem: that proof is the analytic weak-submajorization and strict-convexity argument in `RESULT.md`.

The scoped theorem is a mathematical spectral optimization result, not a certified implementation of a physical fractional-order consensus model. No outside mathematical audit or validation is represented by these checks.
