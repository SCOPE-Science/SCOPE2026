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
The new theorem is supported by an exact conditional distribution identity and established renewal theorems. Derive \(\Pr(T>t)=F(L/t)^N\), then conditional on observation age \(a\) each speed is iid from \(F(\cdot)/F(L/a)\) truncated to \((0,L/a)\). For bounded test functions, combine \(A_t\to\infty\) in probability at infinite mean with \(F(zL/a)/F(L/a)\to z^\alpha\), which proves the joint law. Dynkin–Lamperti supplies the age fraction for \(N\alpha<1\). The exact power-family stationary-age integration gives the covariance coefficient for \(N\alpha>1\).

A standalone standard-library Python script `check.py` was executed from the packaged path. It passed thousands of mixed-moment identities, three independent positive-covariance algebra cases, and 1,600 actual renewal-trajectory realizations for \(N=2,\alpha=0.24,t=10^6\). Its sample mean normalized positions were approximately 0.804 and 0.820 (limit 0.80645); sample cross-covariance was approximately -0.00109 (limit zero). This finite experiment does not constitute the infinite-time proof.

The domain excludes \(N=1\) for the correlation-transition claim and makes no assertion about external validation. The critical \(N\alpha=1\) case uses renewal-age divergence rather than a noncritical beta age-fraction theorem.
