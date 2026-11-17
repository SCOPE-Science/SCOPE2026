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

Conditional emission independence gives E exp(-s A_n)=pi[diag(f_i(s))P]^n 1. Primitive finite-state P ensures a simple Perron eigenvalue 1; the first variation is -h(s) with remainder O(h(s)^2), yielding resolvent ~1/h. The absorbed half-line kernel is nonnegative at site x=1, so Tonelli gives an iff integral of 1/(sqrt(s)h(s)); operational hitting-time decomposition extends fixed x. Under h regularly varying alpha in (0,1), Potter bounds justify rescaling theta_n and give 2x/pi Gamma(1+1/(2alpha))theta_n. Karamata yields the power-log boundary. Independent four finite-state Perron perturbation checks corroborate; infinite asymptotics rely on proof.

## originality

PASS

The novel claim is a necessary-and-sufficient h(s) mean threshold and leading survival equivalent invariant under finite-state Markov rate correlations, not the established iid first-passage spectral identity or already-known iid log-critical beta>1 specialization.

## value

PASS

A sharp necessary-and-sufficient heavy-tail passage-time criterion robust to finite-memory environmental correlations with exact survival prefactor is a natural structural extension of a named stochastic first-passage phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
