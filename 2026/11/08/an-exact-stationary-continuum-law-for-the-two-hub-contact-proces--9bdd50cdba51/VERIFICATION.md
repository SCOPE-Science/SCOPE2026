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

# Verification and reproducibility

The result is derived from the exact finite-state generator, stationarity moment identities, a vanishing quadratic-variation limit, and the unique invariant density of a two-state switched affine flow. In particular, the density is not inferred from finite graphs.

Run `python verification.py` with Python 3, NumPy, and SciPy. The script independently constructs the generator for each finite state \((y,k)\), solves stationary linear equations, verifies probability normalization and stationarity residuals, tests the algebraic transport-flux identity at interior points, and compares finite-size stationary moments with the displayed integral predictions. The executed package check passed 195 assertions on three positive parameter choices and finite graph sizes \(80,320,1280\), plus special-function identities at \(c=1\).

The finite computations do not establish uniqueness of invariant laws, infinite-size convergence, or historical priority. Those statements require the mathematical proof and literature comparison given in the other accompanying files. There has been no independent scientific audit or validation.
