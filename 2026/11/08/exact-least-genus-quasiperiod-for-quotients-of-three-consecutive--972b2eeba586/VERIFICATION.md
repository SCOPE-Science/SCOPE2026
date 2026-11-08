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

# Reproduction and limits

Run `python3 verify.py` under Python 3 with the standard library. The finite verifier reports:

```text
GENUS_INDEPENDENT_DP_OK 3375
QUASIPOLYNOMIAL_BRANCHES_OK 1978
LINEAR_COEFFICIENT_PERIODS_OK 98
VERIFY_OK finite_checks_only=True infinite_period_proof_separate=True independent_audit=False
```

The dynamic-programming check constructs the parent numerical semigroup independently of the interval-gap formula, then counts multiples of the quotient modulus absent from it. All cases in \(3\le a<128\), \(2\le p<29\) pass, with additional branch and coefficient-period tests for finite ranges. The infinitely many parameter values and the least-eventual-period assertion are proved symbolically in `RESULT.md`; a finite computation alone cannot establish them. Independent audit has not been performed.
