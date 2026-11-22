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

The file `verification.py` is a standalone Python 3 script requiring SymPy. It was run with the actual file contents and printed:

```text
PASS: symbolic stationary generator, normalization, covariance polynomial, endpoints, and 24 rational-state tests
```

The exact symbolic checks evaluate the master-equation residual, probability normalization, polynomial equality, zero-reaction covariance, strong-reaction limit, and critical-line derivatives. The 24 rational parameter checks are numerical-independent finite sanity tests. Their finite count is not the proof of the all-parameter signs: those follow from the explicit coefficients, positivity of the denominator, strict monotonicity of the polynomial, and the intermediate value theorem in `RESULT.md`.

The root \(r_c(1)\) is a numerical approximation to a uniquely characterized algebraic root, not a computer-certified decimal interval. The results are restricted to the specified two-site bond realization and do not rely on extrapolation to a large lattice.
