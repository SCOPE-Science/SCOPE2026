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

# Exact verification record

Run `python verify.py` with any recent Python 3 interpreter (standard library only). The checker reconstructs every rooted nonplane binary tree shape on four through eleven leaves, enumerates all sets of exactly two or three deleted taxa, counts each surviving root-to-leaf edge directly, and compares exact rational variances to the closed forms in RESULT.md. This yields 792 independent shape/budget comparisons. The same checker constructs the four-leaf witness and explicit infinite-family instances at parameter values 1, 2, 3 and 5, and checks shape counts and both variance inequalities by exhaustive deletion-set enumeration.

Observed successful output:

```
PASS: exact direct-subset checks: 792
PASS: sharp four-leaf values and n=6q witness at q=1,2,3,5
```

The direct calculation uses `fractions.Fraction`, never floating-point tolerances. No external data, scientific libraries, or platform-specific paths are required. The all-integer infinite-family result and shape-index recovery are justified by the symbolic counting proof in RESULT.md; finite checks alone cannot certify their universally quantified conclusions. Model limitations are the unit-edge rooted full-binary structure and fixed-number uniform deletion sampling. No independent scientific audit has been performed.
