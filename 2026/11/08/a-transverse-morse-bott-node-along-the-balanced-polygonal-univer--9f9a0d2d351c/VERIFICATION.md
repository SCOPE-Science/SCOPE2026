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

Exact arithmetic checks of the original polynomial were carried out by running the self-contained `verify.py` with Python 3. The checks covered positive balanced coefficient choices for \(n=8,12,16\), including an uneven rational weight vector for \(n=8\). In each case the code established vanishing polynomial and gradient and exact ordinary Hessian rank \(n-2\); it separately checked every logarithmic Hessian entry.

The unrestricted result is deductive, based on cyclic Jacobian equations, recurrence closure, and an explicit Hessian-kernel calculation; finite computations are not used as an infinite-parameter proof. Normal form is analytic over \(\mathbb C\) only. Coordinate-hyperplane strata and endpoints are outside the claimed transverse classification. No independent audit has been performed.
