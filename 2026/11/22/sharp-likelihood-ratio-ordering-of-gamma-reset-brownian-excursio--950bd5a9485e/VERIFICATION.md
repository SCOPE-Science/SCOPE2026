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

# Reproduction and limits

`CHECKER.py` is a standalone, read-only scientific numerical test using NumPy and SciPy. Run with `python CHECKER.py`. It passed 114 deterministic assertions on the final checker source: two independent occupation representations, Gamma-difference normalization, the exact exponential and Erlang-two anchors, radial tails and likelihood-ratio grids, and single-threshold recovery of the chosen return speed.

The key infinite statements are proved analytically in `RESULT.md` by Tanaka's occupation formula, Gamma characteristic-function factorization, convolution log-concavity above shape one, exponential-mixture log-convexity below shape one, and the mean-residual-life likelihood-ratio transfer. Numerical quadrature over finitely many parameters is corroboration only, not a certificate of infinite monotonicity. The finding has not undergone independent scientific audit.
