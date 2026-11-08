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

# Reproducibility

Run `python verify.py` using Python 3.9 or later, without third-party packages. The program constructs the combinatorial Laplacian from the explicit diamond edges and evaluates all grounded principal inverse traces using exact rational Gauss–Jordan elimination. It separately reconstructs each orbit value from the module Schur formula, checks the claimed class prediction and winner, and evaluates sign comparisons on a long integer interval.

The observed output when replayed from the standalone script was:

```
VERIFY_OK 2293 exact objective/class and sign checks
```

The all-size analytical proof is contained in RESULT.md. Testing any finite sample of \(m\) is not an infinite proof; passing the program validates arithmetic in its finite range only. The proof makes no claim of independent formal certification. Independent audit status: not performed.
