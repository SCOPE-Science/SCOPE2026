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

Run `python verifier.py` from the directory containing the extracted files. The verifier uses only Python's standard library. Its exact rational checks independently enumerate every two-sweep orientation word through eight complete sweeps, over three rational unit-vector line pairs, five interior sampling biases and three initial errors. It compares with the closed 2-by-2 expected squared error transfer recurrence, fair-mixing finite-horizon identity, and analytic trace, determinant and rate inequalities. The captured output is in `verification_output.txt`.

The infinite-horizon Perron limit and all real parameters are established analytically in `RESULT.md`; finite checker coverage does not replace that proof. The checker has no Monte Carlo randomness and no external files or network dependencies. This is a self-review only, with no independent audit claimed.
