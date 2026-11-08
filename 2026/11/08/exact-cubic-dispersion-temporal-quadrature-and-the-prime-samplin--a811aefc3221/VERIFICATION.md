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

# Reproducibility checks

Run `python3 verify.py` with an ordinary Python 3 interpreter; no third-party library is required. The checker enumerates the exact integer resonance triples and separately evaluates the modular-inverse collision criterion on \(1344\) band/grid pairs. It compares the full fourth moment by ordered Fourier quadruple enumeration against the algebraic signed-defect formula in \(756\) positive-real integer cases and \(88\) Gaussian-integer complex cases. It checks prime-grid cutoffs on \(32\) band sizes, a negative signed-defect witness and the smallest-grid boundary for three modes.

Expected final status: `CUBIC_TEMPORAL_QUADRATURE_CHECK_PASS`.

The exact integer certificate supports reproducibility but is finite: no claim about an infinite range rests solely on its successful execution. The proof of the universal claim is the explicit lag-difference factorization, time character orthogonality, modular solvability, and prime-size constructions in `RESULT.md`. Numerical floating-point integration is not needed. Independent audit has not been performed.
