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

# Verification record

The entire analytic result is derived in `RESULT.md`, including the Poisson-thinning mass function, the only possible likelihood-ratio downward step, the unique exposure crossover, and its limiting asymptotic. The supplementary `checker.py` reproduces the exact rational counterexample and tests numerous parameter configurations with a fixed pseudorandom seed. Invoke `python checker.py` after extracting these files from the same package; it has no nonstandard dependencies. Numerical tests do not prove the all-parameter claim. All model parameters are treated as known; no observational identifiability theorem for estimated parameters or strategic social equilibrium is claimed. External independent audit has not been performed.
