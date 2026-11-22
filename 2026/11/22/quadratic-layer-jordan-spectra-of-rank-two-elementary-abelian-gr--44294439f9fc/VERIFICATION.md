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

The original normal-form and counting proof is in `RESULT.md`. Exact arithmetic checks are supplied as `checks/jordan_quadratic_checker.py`, with its captured output in `checks/output.txt`. Execute `python3 checks/jordan_quadratic_checker.py`; it requires only Python's standard library. The checker constructs matrices for regular multiplication and computes ranks of every power by modular Gaussian elimination, then reads Jordan blocks from second differences. This does not call the theorem's tensor-sum rule to obtain the observed partition.

The recorded run exhausts all 702 quadratic-leading elements over \(\mathbb F_3\) as a comparison with the previously published characteristic-three case. It also tests 20 nondegenerate and 20 rank-one sampled higher-degree lifts in characteristic five, 8 in each class in characteristic seven, and every pure residual monomial normal form in those two characteristics. All comparisons passed. Only the characteristic-three slice is exhaustive; characteristic-five and characteristic-seven checks are samples; no code experiment proves all primes or field extensions. The all-parameter result relies on the symbolic proof. Independent mathematical audit is not performed.
