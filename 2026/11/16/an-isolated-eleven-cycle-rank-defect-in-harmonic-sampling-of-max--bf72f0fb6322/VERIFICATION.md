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

## Reproducibility
Run `python3 check.py` from the extracted finding directory; no third-party package is required. The script checks the independent graph-theoretic bit-mask enumeration and the analytic cyclic-gap count, two-point function, Fourier eigenvalues, and finite ranks for \(5\le n\le17\). It also checks basic recurrence and size interval identities through \(n=120\). Recorded result: `PASS 639 families of exact-count, Fourier, rank, recurrence assertions`.

## Proof-based verification and limitations
The gap-slide witness establishes all nonconstant Fourier eigenvalue positivity for \(n\ge11\), regardless of numerical experiments. The few smaller orders have explicit Fourier witnesses. The constant eigenvalue is exactly a size variance and is decided by an integer interval. Thus the infinite claim is analytic rather than based on test coverage. The package does not provide a quantitative lower bound on every positive Fourier eigenvalue and does not test sampling distributions other than the uniform maximal-set measure.
