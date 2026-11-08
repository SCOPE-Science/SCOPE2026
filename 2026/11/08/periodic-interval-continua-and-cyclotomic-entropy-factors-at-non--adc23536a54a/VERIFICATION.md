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

# Verification details

`verify.py` is a self-contained standard-library checker. Running `python3 verify.py` successfully produced:

```
MODULAR_INTERVAL_GCD_BLOCK_FACTORIZATION_OK
EXACT_NONCOPRIME_PERIODIC_INTERVAL_CYCLES_OK
FINITE_TESTS_ARE_NOT_THE_ARBITRARY_N_PROOF
```

The program checks exact integer determinant identities by evaluating degree-\(n-1\) polynomials at \(n\) distinct integers for every \(3\le n\le14\), \(1\le q<n\); it also checks the exact pointwise \(\ell\)-step identity on all nonexceptional cycle intervals using rational starting points. These checks are independent of symbolic floating-point eigensolvers. The general combinatorial block decomposition, graph zeta and topological entropy arguments are proved in `RESULT.md`, not inferred from finite tests. Independent audit: not performed.
