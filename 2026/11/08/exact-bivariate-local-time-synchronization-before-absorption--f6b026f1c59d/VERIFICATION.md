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

The analytic proof is in `RESULT.md`. The standalone `verify.py` computes the exact formula from elementary hyperbolic functions and separately solves a truncated nearest-neighbor continuous-time Markov chain with absorption, reflecting far boundary, stochastic resetting, and delta-local-time approximations. It compares the finite-chain Feynman–Kac transforms at decreasing mesh size with the claimed continuum transform, across three physical parameter sets and various transform parameters. The program also independently checks killed Green identities, the exact two-point potential matrix, strict correlation monotonicity on numerical grids and endpoint/normalized limits.

Execute from a directory containing both files using `python3 verify.py`. It depends only on the Python standard library. Numerical mesh convergence is corroboration; the infinite-dimensional claim rests on the Green-kernel and Feynman–Kac argument, not finite enumeration. No independent external validation has been performed.
