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

The exact symbolic check is `python3 verify_2wronskian.py` (requires SymPy). It recomputes the jet determinant from the six basic sections of \(2K_C\) and verifies the fully factored Wronskian using rational-function differentiation. Observed output: `SYMBOLIC_2WRONSKIAN_CERTIFIED_OK`.

The standalone finite-field check is `python3 verify_sextactic_frobenius.py` (Python standard library). It enumerates the defining quartic complete intersection over all prime fields of characteristic 11 through 199 and over the quadratic extensions for primes 11, 13, 17, 19 and 23. It compares each of three individual sixteen-point blocks against the power-residue formula, and checks the four possible orbit spectra. Observed output: `ALL_FINITE_FIELD_CHECKS_OK`.

The symbolic computation certifies a finite algebraic identity in characteristic zero and hence by reduction in characteristics where the denominators and scalar coefficient are invertible. The finite samples are checks, not an exhaustive classification of all prime powers. The general argument is in RESULT.md. No independent external mathematical audit has been performed.
