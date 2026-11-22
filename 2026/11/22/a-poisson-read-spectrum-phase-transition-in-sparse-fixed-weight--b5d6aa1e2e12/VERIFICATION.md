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

# Reproducibility and verification

Use Python 3 with only its standard library: run `python3 verify.py`. The accompanying `verification_output.txt` is the actual output from this execution. The script checks literal overlapping window counts against the affine formula in 12,365 eligible finite cases, checks 379 separated-gap binomial counts by direct enumeration, and includes a seeded 15,000-trial simulation of the critical-window joint gap statistics. The proof in `RESULT.md` establishes the infinite-limit conclusions through factorial moments and a vanishing bad-event bound, rather than extrapolating from simulation or finite exhaustive checks. The stated asymptotic convergence rate is qualitative; historical priority and independent scientific auditing remain unverified.
