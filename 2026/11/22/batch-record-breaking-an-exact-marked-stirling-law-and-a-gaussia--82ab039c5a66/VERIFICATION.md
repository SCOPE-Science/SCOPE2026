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

# Verification

The supplied standalone Python 3 program `verify_prefix_records.py` evaluates the finite joint distribution in exact rational arithmetic. It checks every permutation for \(2\le n\le8\) and every admissible prefix size \(1\le m<n\), including the known one-arrival boundary for comparison. It also checks the expectation, recovery-position probabilities, and initial coefficients of the infinite-horizon geometric product.

Command: `python3 verify_prefix_records.py`

Observed output: `PASS: 406 exact finite/joint assertions; 30 infinite-PGF consistency assertions`.

These checks establish exhaustive finite agreement through eight observations, not infinite-size correctness. The proof for arbitrary sizes derives the joint law from rank exchangeability. The Poisson record-value representation proves the geometric convolution; Lyapunov/Lindeberg estimates and a short-block cutoff establish the limiting claims. The provided mathematical argument is needed for each infinite statement.

This package has received a self-review. Independent mathematical audit has not been performed.
