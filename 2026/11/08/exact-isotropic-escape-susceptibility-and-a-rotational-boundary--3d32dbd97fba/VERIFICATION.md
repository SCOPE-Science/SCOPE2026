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

# Verification and reproduction

Run `python checker.py` with Python 3, NumPy, SciPy, SymPy and mpmath installed. A successful run prints `PASS`. The executable checks the exact zero-rotation differential equations using symbolic differentiation; compares the modified-Bessel expression with an independently integrated first Fourier mode over 42 sample parameter pairs; tests the separate Green-function formula for zero-rotation constant drift; confirms small-speed expansions and limiting high-rotation bulk/edge profiles at finite parameters; and checks selected strict-sign and parameter-monotonicity inequalities.

The infinite-dimensional shifted-Gaussian comparison, every-parameter maximum-principle inequalities, and large-parameter asymptotics are established analytically in `RESULT.md`, not by finite test coverage. The checker does not validate priority against inaccessible literature or conduct an independent audit. The limit in the high-rotation profile concerns the quadratic speed coefficient, not a jointly uniform speed-and-rotation asymptotic.
