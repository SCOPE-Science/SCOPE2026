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

# Reproducibility

Run `python3 verify.py` from the directory containing the seven files. The program uses only the Python standard library and evaluates exact fractions, with no randomized trials.

Observed: `PASS n=3..7 arc cases 25 complete residual matchings 79029 exact assertions 291`.

The algorithm directly iterates all perfect matchings of the unmarked endpoints, counts crossing pairs independently, and compares each feasible degree class with the claimed conditional regression. It checks degree support, exact class probabilities, degree mean and variance, covariance and the total crossing expectation. It is exhaustive for these tested finite sizes only; the all-size theorem follows from the exchangeability proof in `RESULT.md`.

No independent external validation has been performed.
