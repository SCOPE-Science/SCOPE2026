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

# Reproduction and proof checks

Execute `python verify.py` under Python 3 with only its standard library. The deterministic seeded checker independently checks 6,000 exact finite-descent integral identities at sampled parameters and phases, exact rational Gamma–uniform mean/variance identities for five shape values, and Monte Carlo estimates for equilibrium and fresh-start observation windows of length \(75\).

The sample scaled variance estimates were approximately \(0.0750650749\) for stationary initialization and \(0.0369599116\) for fresh-start initialization in the \(a=v_0=1,n=3\) model, compared with the exact asymptotic constants \(0.075\) and \(0.0375\). A single finite-time simulation cannot prove either limit. The proof's non-computational steps are the pathwise primitive, equilibrium length bias, Erlang-phase mixing, uniform integrability, and exact moment integration. They are stated explicitly in `RESULT.md`.

No external scientific validation, formal certificate, or empirical experiment is asserted. Independent audit has not yet been performed.
