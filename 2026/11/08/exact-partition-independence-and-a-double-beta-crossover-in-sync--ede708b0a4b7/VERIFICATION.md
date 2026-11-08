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

Run `python3 verify.py` with Python 3's standard library. Expected terminal result: `VERIFY_OK 1112 exact rational assertions`.

The checker constructs exact binomial transitions for both parts of complete bipartite graphs and uses rational Gaussian elimination to obtain invariant count distributions. It tests the product stationary law across both counts, the exact two-step conditional mean and variance, the centered spin-pair correlations, and, for small graphs, all entries of the full-configuration stationary equation. No floating-point fitting is involved. The generator Taylor bound, moment determinacy on \([0,1]\), and the boundary covariance arguments are mathematical proofs in `RESULT.md`, not consequences of finite enumeration. The checker does not establish the novelty of the result or constitute independent mathematical validation.
