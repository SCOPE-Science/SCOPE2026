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

Exact-rational checks: run `python verify.py` from the same directory. The checker enumerates all labelled partial matchings on at most seven vertices and all relative-spacing rank/cyclic label-order configurations for five and six points, verifying the conditional overlap polynomial, uniformity of labelled reciprocal-neighbor matchings conditional on size, the mean and variance of circle reciprocal-pair counts, and the finite three-replicate covariance formula. It reports 75 passing assertions.

The analytical limit is proved using factorial moments of disjoint prescribed matching edges plus a bounded two-dependent central limit theorem. Finite enumeration cannot prove the infinite-size claims or bibliographic originality. There has been no independent mathematical audit.
