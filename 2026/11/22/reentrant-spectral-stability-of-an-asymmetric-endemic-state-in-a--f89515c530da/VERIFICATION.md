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

The standalone `verify.py` reconstructs the endemic equilibrium from \(0<z<1\), \(u>0\), verifies all four stationarity equations and normalization, then independently differentiates the reduced vector field and compares its Jacobian entrywise with the proved expression. It computes the trace, determinant and sum of principal minors symbolically and checks the fully factored third cubic Hurwitz determinant for symbolic \(z,u\). The rational specialization \(z=3/8\) verifies its exact quadratic, discriminant and simple positive roots.

The code checks exact signs at \(u=1\), \(u=10\), and \(u=30\), and uses numerical eigenvalues only to diagnose the corresponding stable, two-unstable-eigenvalue and stable spectra. Mathematical validity for every \(0<z<1\) and \(u>0\) follows from the symbolic identities, signs and elementary Hurwitz and quadratic-root arguments in RESULT.md; no finite enumeration is presented as a general theorem. Running `python verify.py` requires a Python environment with SymPy and NumPy. The source code uses only these packages.

No first Lyapunov coefficient, nonlinear periodic-orbit property, global basin conclusion or validation of real population data is asserted. The comparison to previous literature is bounded and is not an independent historical-priority audit.
