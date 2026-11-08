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

# Verification record

The standalone `verify.py` uses only the Python standard library. The direct normalized-field update computes row and column occupancies and blurred fields as exact integers; the comparison max-selector implementation is independent and uses a different representation. From the local package directory, run `python3 verify.py`. In the actual check, the program exited successfully with:

```
VERIFY_OK checks=238104
```

Exhaustive one-dimensional checks cover every nonzero binary word on cyclic lengths 4 through 14, verifying the exact reciprocal-score potential identity, monotonicity, the inclusion consequence at equality, and the eventual periods. The full two-dimensional four-by-four one-step check covers every one of 65,536 binary matrices. Further tests sample 4-by-5 and larger sizes, verify explicit sharp-boundary configurations and their strict-side behavior, compare the independent field implementations, and replay the primitive two-cycles and growing-transient examples.

Finite enumeration establishes only its tested cases, not the theorem for all lattice sizes. The all-size guarantee, sharp parameter boundary and quadratic termination bound are proved analytically in `RESULT.md`. The full source manuscript could not be inspected, so novelty remains subject to further literature review. Independent scientific audit has not been performed.
