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

The theorem has a five-state exact transfer-matrix formula and a rational limiting Fourier profile. `verify.py` was run and passed its exhaustive size-three-through-fourteen checks, positivity tests at those sizes, exact rational-algebraic root isolation, Descartes coefficient sign checks, and peak-height comparisons. It also compared the complete finite Fourier spectra to the limit for sizes 16, 24, 32, 48, and 64. `verify_symbolic.py` was run using SymPy; all three polynomial identities passed exactly.

The finite computations are not asserted to prove the asymptotic. The proof uses Perron–Frobenius convergence for a primitive transfer matrix, the stationary renewal transform, and a rigorous algebraic critical-point certificate. Root locations and the condition-ratio decimal are reported with rigorous enclosing rational intervals; an independently performed audit or an exhaustive historical priority investigation is not claimed.
