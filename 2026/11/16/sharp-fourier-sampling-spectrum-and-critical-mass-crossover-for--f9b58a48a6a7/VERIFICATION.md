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

Run `python3 verify_cycle_forest.py` with Python 3 and its standard library only. The checker enumerates every proper edge subset of labelled cycles \(C_n\) for \(3\le n\le10\), computes rational rooted-component weights, forms the exact covariance entries, and independently evaluates their Fourier transforms. It compares each entry of the transformed spectrum with the closed analytic formulas, checks positivity and claimed extremizers, and separately samples fixed-activity, critical, and very-small-activity asymptotic cases. On the packaged code the reported result was `PASS: 432 independent exact-enumeration/Fourier/limit assertions`.

The analytic theorem is not inferred from these finite tests. Its all-size ingredients are the determinant/transfer-current identity, the exactly solvable periodic Green recurrence, the finite geometric-square transform, and strict monotonicity of the rational Fourier multiplier. Exact count coefficients and the corresponding dominated higher-component bound prove the low-activity asymptotic. The generalized forest determinant and complete marked-spoke/cut distribution are previously established; only the explicit Fourier condition classification is assessed here.
