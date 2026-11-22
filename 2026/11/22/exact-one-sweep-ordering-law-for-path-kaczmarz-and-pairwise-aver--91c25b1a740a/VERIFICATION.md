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

The closed-form run decomposition and both sharp extrema follow from the algebraic proof in `RESULT.md`, not from testing.

The included `verify.py` was executed from the same package inputs using Python 3 standard-library rational arithmetic and printed:

```
PASS: 8200 exact-arithmetic sweep identities and sharp-bound cases
```

The executable checks all \((n-1)!\) edge permutations for \(2\le n\le8\), all \(2^{n-2}\) binary orientations for \(2\le n\le12\), and 240 larger seeded permutations. Matrix products use exact fractions. The checker verifies the stated objective, run formula, sharp bounds, equality words and reference examples. The unbounded claim is supported by the analytic induction and telescoping proof; the finite tests cannot establish an infinite theorem or literature priority. No independent validation has been performed.
