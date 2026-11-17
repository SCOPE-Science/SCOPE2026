---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Reflection gives survival s(Dt)=erf(a/(2sqrt(Dt))) for generator D ∂xx, and conditional Brownian-noise independence gives block law R=alpha*t^(-alpha)*integral_0^t u^(alpha-1)s(u)^k du; m independent groups give R^m. The asymptotic s(u)~a/sqrt(pi)*u^(-1/2) yields the three exact regular-variation regimes, positive constants and critical logarithm. Layer-cake yields finite q-moment iff q<m min(alpha,k/2), with divergence at equality. Since fixed-N survival equals ||s(Dt)||_k^N, strict Lp monotonicity establishes all-time stochastic order across equal group sizes dividing N. Boundary alpha=k/2 and fixed N=6 example are included.

## originality

PASS

Prior independent heterogeneous Brownian search assumes iid individual diffusivity/path pairs; grouping creates exchangeable dependence with non-iid first passages, changing the finite-moment threshold at fixed population. Earlier iid fastest-passage asymptotics do not imply fixed finite-N block structure, log-critical tail or strict grouping stochastic order. Best-of-knowledge historical priority is limited by possible general shared-frailty literature.

## value

PASS

The sharp threshold for finite q-moment of first arrival is a natural detection-risk criterion. For exactly six particles and identical one-particle marginal laws, regrouping the shared disorder alone crosses from finite to infinite expected search time, with a precise critical log enhancement and monotone stochastic order. This is a structural finite-population dependence effect, not merely numerical asymptotic estimation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
