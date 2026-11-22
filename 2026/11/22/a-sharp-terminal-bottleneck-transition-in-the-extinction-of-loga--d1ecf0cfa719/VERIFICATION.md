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

The mathematical proof is provided in RESULT.md; the standalone finite-state checker `check.py` validates selected exact Laplace transforms by rational Markov recursion, the closed-form survival function, selected finite-size rate asymptotics, and the critical optimizer. It also checks finite-sample simulation against analytical one-domain probabilities. The recorded replay passed 76 checks using Python's standard library.

The numerical checks are finite and cannot certify infinite limits. The infinite statements rely on Cramér's theorem for the gamma erosion stages, the elementary exponential last-stage LDP, their independent joint LDP, strict uniqueness of the constrained rate minimizer, and a union bound across independent domains. The independent audit remains unperformed.
