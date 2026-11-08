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

The complete mathematical proof is in `RESULT.md`. Its decisive infinite statements rely on the exact factorization of the geometric characteristic polynomial, Perron–Frobenius theory for the negative-coefficient companion matrix, the unit-circle modulus barrier, continuous dependence of polynomial zeros on coefficients, and the transversality derivative at the simple multiplier \(-1\). Boundary claims refer to strict Schur stability and linear nonhyperbolicity; they do not establish nonlinear stability or an attracting period-two orbit at the critical parameter.

The bundled `check_spectrum.py` runs with Python 3 and NumPy; the verified run returned `PASS 371 checks`. It evaluates rational identities exactly and numerically checks representative interior, boundary and exterior spectra for several odd degrees and survival probabilities, including a high-survival case. Finite checks cannot replace the all-degree analysis. No independent audit has been performed.
