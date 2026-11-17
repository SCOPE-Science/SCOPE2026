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

## Reproducibility

Run `python3 check_markov_pelikan.py` using the Python standard library. Four rational parameter cases verify the shell-mass recursions, normalization constants, rational generating-function coefficients, and the resonance formula for 36 shells each. Expected terminal line: `MARKOV_PELIKAN_EXACT_RATIONAL_OK cases=4 exact_shells=144`.

## Logical scope

Exact rational samples are finite regression checks. The full statement follows from the stationary transfer equations, generating-function elimination, pole obstruction for nonnormalizability, and closed geometric convolution proved in RESULT.md. Invariant-law uniqueness is only within the mode-conditioned dyadic-uniform class; a zero atom is not ruled out on the compactified interval. Independent audit has not been performed.
