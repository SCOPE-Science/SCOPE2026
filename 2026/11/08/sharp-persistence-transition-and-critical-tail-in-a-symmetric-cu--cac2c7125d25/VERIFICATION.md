---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

On 4<mu<8, c=sqrt(1/4-1/mu) and the specified beta=2c, alpha=-c yield a symmetric monotone full-branch cubic on [-c,c]; derivative minimum 4-mu/2 remains strictly positive throughout this open range. Factoring the positive fixed-point cubic gives boundary fixed point c and interior u_star exactly when mu>6. Preimage thresholds r_n solve B(r_n)=r_(n-1), and Lebesgue survival=(c-r_n)/c. When mu<6, inverse endpoint multiplier (4-mu/2)^-1 gives geometric asymptotic. At mu=6, exact v_(n-1)=v_n+3sqrt3 v_n^2-6v_n^3 yields reciprocal increment 3sqrt3-33/y_n+O(y_n^-2), hence v_n/c=2/(3n)+22 log(n)/(27n^2)+O(n^-2). Independent high-precision bisection for n=100,1000,10000 corroborated n*survival 0.701486, 0.671925, 0.667377 tending to 2/3; no finite sequence proves asymptotics. At mu>6 basin length gives (c-u_star)/c.

## originality

PASS

Prior work analyzes cubic neuronal Lorenz voltage maps, expanding invariant measures and other two-cycle bifurcations, and standard parabolic intermittency explains an order-one/n neutral tail generically. The inspected source does not state the specific symmetric endpoint-fixed first-side-switch trichotomy and its exact logarithmic coefficient 22/27. Same-model originality is a qualified PASS for these quantitative first-passage results, not for the generic intermittency mechanism.

## value

PASS

The exact transition from finite-mean same-side neuronal persistence through infinite-mean but a.s. finite excursions to positive permanent trapping is a meaningful, naturally defined survival statistic; explicit critical correction distinguishes the studied symmetric cubic family. This is not a generic textbook fixed-point observation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
