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

From this directory, run `python verify.py`. Python 3.9 or later and the `sympy` package are required. No external data or network calls are used. The script reconstructs the two-state backward equations over exact rational grids and symbolically verifies the generator determinant, slow eigenvalue equation, and analytical derivative identities. It also performs deterministic numerical critical-point and finite-difference checks over 350 seeded parameter choices with \(b>a\). The observed completed replay printed `PASS 2518 assertions`.

The numerical checks are a smoke test, not an exhaustive certificate for arbitrary real parameters. For the universal statement, inspect the proof in RESULT.md: strict monotonicity of the two derivative-sign functions, a strictly positive analytical threshold gap, and the boundary conditions prove the classification for every permitted parameter. No claims are made about \(b\le a\), data calibration, uniqueness outside the model or independent scientific verification.
