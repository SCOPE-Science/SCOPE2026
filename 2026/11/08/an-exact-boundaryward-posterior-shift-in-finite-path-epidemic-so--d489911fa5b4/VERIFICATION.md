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

# Verification evidence and limits

The supplied `verify.py` uses direct uniformization of a finite-state continuous-time Markov chain over infected intervals, independently of the likelihood formula used in the mathematical proof. Replaying `python verify.py` produces `PASS 4137 independent CTMC, posterior, and threshold diagnostics`.

It checks all valid observation-prefix/source combinations for paths with 4–10 vertices at seven dimensionless ages; it additionally checks strict likelihood-ratio shape, posterior monotonicity under both uniform and nonuniform positive priors, and every MAP threshold for observed prefixes of length 3–17. The code uses only the Python 3 standard library and has no network dependencies.

The universal statement rests on the analytical Poisson-frontier likelihood, the strict exponential-tilt variance argument, the Poisson upper-tail hazard inequality, and the endpoint-limit argument in `RESULT.md`. Finite numeric checks are not exhaustive over ages or path lengths and are not an infinite proof. Literature comparisons remain conditional on the sources materially inspected; no independent audit is claimed.
