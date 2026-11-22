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

# Verification

From the directory containing the standalone package, run `python3 verify.py`. The self-contained script uses exact rational arithmetic to compute the full endpoint matrix \(I+hQ+h^2Q^2/2\), the local threshold, and the equivalent Euler-square representation. It compares nonnegativity and exact row sums at zero, the standard SSP limit, the exact upper boundary and a step beyond it on many directed finite matrices. It also verifies the motif equivalence and the analytic star family at 49 distinct leaf counts. The reproduced output was:

```
VERIFY_OK exact_assertion_groups= 39240
```

The complete proof for arbitrary real rates and arbitrary finite dimension is in `RESULT.md`; finite exact-rational checks are supplementary. No numerical certificate substitutes for the nonempty-minimum argument or the necessary-and-sufficient motif proof. Related full text was inspected where available; one plausible older positivity paper was accessible only via an abstract. Independent audit: not performed.
