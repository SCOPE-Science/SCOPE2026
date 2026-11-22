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

The bundled `verify.py` checks exact symbolic identities for the Bayes-risk derivative, cubic, perfect-channel factorization, and strict convexity. It independently integrates nine covariance expressions, tests representative root positions and Bayes risks, verifies noise ordering, tests the asymptotic crossover formula, and simulates Poisson event times to check mean and covariance directly. To reproduce, install `requirements.txt` and run `python verify.py` in the folder containing these files.

The mathematical proof of global uniqueness is the analytical convexity-and-sign argument in `RESULT.md`. No finite grid, numerical root solver, or simulation is treated as an exhaustive certificate over all real parameters. The limiting laws are established by expansion and monotonicity, with numerical runs supplying diagnostic checks only. Reproduction was executed from the packaged source content before acceptance. No independent mathematical or historical-priority validation has been performed.
