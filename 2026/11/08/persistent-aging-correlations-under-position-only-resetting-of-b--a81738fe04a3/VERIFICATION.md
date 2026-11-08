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

Analytical verification is given in `RESULT.md`: a last-reset stochastic integral, exact conditional moment identities and a finite-dimensional convergence argument. `verify.py` checks independent numerical integrations and symbolic moment consequences using Python's standard library. The checks cannot prove the limiting distribution, originality, or third-party validation. The Brownian-diffusivity source explicitly treats a different simultaneous-reset protocol, while the nonrenewal scaled-Brownian source has deterministic rather than stochastic diffusivity.

Run the embedded program with `python verify.py` from the extracted package directory. The assertion count and numerical tolerances are printed at completion. No random-number generator is used.
