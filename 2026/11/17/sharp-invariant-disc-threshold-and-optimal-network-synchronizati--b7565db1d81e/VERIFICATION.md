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

The proof uses an exact complex-hyperbolic tangent integral identity, the maximal-modulus comparison principle, the undirected graph Laplacian Rayleigh inequality, and an integrable nonlinear perturbation in the Fiedler direction. The limiting Fiedler amplitude is nonzero for sufficiently small explicitly specified initial perturbations; no assertion of genericity is needed.

A standalone standard-library Python checker is included as `check.py`. Its recorded output is:

```text
R=0.700000  tan(R)/R=1.203269114947 delta=0.578855809768
lambda_2=1.0  optimal_exponent=1.850000000000  prefactor=1.239218848211
t=0.00  e^(mu*t)*w(t)/w(0)=1.000000000  bound=1.239218848
t=5.00  e^(mu*t)*w(t)/w(0)=0.982289561  bound=1.239218848
t=10.00  e^(mu*t)*w(t)/w(0)=0.982289561  bound=1.239218848
t=15.00  e^(mu*t)*w(t)/w(0)=0.982289561  bound=1.239218848
t=20.00  e^(mu*t)*w(t)/w(0)=0.982289561  bound=1.239218848
VERIFY_OK radial_boundary=1 derivative_supremum=1 ring_integrations=10000 upper_bounds=5
```

Computational tests at finitely many points are corroboration only; the all-graph and all-time quantifiers are proved analytically in `RESULT.md`. The theorem does not identify the exact coefficient of a particular trajectory's Fiedler asymptotic, only nonvanishing for a suitable arbitrarily small family. Independent validation has not been performed.
