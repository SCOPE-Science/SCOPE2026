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

# Reproducible verification

Execute `python3 verification/verify_markov.py` using Python 3 standard library only. The script checks 4,500 exact rational conditional-covariance and Markov transfer identities across Pythagorean row angles, row probabilities, transition intensities and two distinct noise variances. It compares independently computed spectral-rate formulas and verifies the exact noisy benchmark and constrained frontier. Recorded standard output is in `verification/verify_output.txt`.

The finite grid is a consistency check, not a proof of the universal claims. The proof in RESULT.md derives the invariant moments and Perron rate analytically for all stated real parameters; its rate–risk optimization handles the boundary \(r=c^2\) and the equal-variance degeneracy. No independent or external certification has been performed.
