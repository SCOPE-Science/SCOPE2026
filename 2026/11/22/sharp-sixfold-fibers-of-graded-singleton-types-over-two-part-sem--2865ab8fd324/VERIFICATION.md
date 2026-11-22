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

# Reproducibility and limits

Execute `python3 VERIFY.py` in the same directory as this document with Python 3.8 or later; no third-party dependencies are needed. The verifier enumerates every parity-valid cross matrix for two positive parts whose combined size is between two and seven, independently generates admissible one-point extension score counts by checking every orientation vector against all required rectangle parity constraints, computes every base's class-preserving and class-exchanging isomorphism orbit by direct relabeling, and checks the residual four-exponent matching inverse.

Recorded result:

```
n= 2 types= 1 polynomials= 1 largest_fiber= 1 max_profiles= 1
n= 3 types= 3 polynomials= 2 largest_fiber= 2 max_profiles= 1
n= 4 types= 7 polynomials= 4 largest_fiber= 3 max_profiles= 2
n= 5 types= 11 polynomials= 5 largest_fiber= 3 max_profiles= 2
n= 6 types= 18 polynomials= 8 largest_fiber= 6 max_profiles= 3
sixfold_witness_polynomial= (2, 7, 16, 21, 15, 6, 1)
n= 7 types= 26 polynomials= 10 largest_fiber= 6 max_profiles= 3
VERIFY_OK matrices_checked= 342 complete_orders=2..7
```

These checks are finite and do not prove the assertions for arbitrary parameter order. The unbounded theorem follows from the rank-one rectangle identity, three-pair matching converse construction, normal-form orbit bound, and distinct-exponent minimality argument in `RESULT.md`. The code does not test bases with three or more nonadjacency classes. No independent mathematical audit is claimed.
