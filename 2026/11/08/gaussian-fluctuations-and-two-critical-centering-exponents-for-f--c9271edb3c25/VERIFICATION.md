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

`verify.py` is a standalone Python script using NumPy and SciPy; it can be executed with `OPENBLAS_NUM_THREADS=1 python verify.py`. The actual packaged-source run returned `PASS 45 independent numerical assertions; seed=20260709` and printed the limiting Gaussian variance \(0.400787396\) for \(s=1/2\), \(\theta=0.3\).

The checker compares a special \(s=1/2\) integral against its exponential-integral closed form, tests the integration-by-parts identity for \(D_s\), solves the exact finite-\(N\) mean-root equation for a range of \(s,\theta\), verifies the first and second drift coefficients, exactly enumerates Bernoulli subsets for small finite systems, and uses reproducibly seeded exponential clocks for a distributional diagnostic.

These are checks of finite quantities, not formal proofs of the limiting theorem or certificates of historical priority. Mathematical justification is supplied independently in the five steps of `RESULT.md`. No independent external mathematical audit is claimed.
