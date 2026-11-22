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

Execute `python verify_w15_characters.py` with Python 3 and SymPy installed. The checker verifies seven weighted degree-six monomials, a squarefree degree-six intersection resultant with discriminant \(1090482201\), nonintersections at the infinity orbifold chart, genus-four Riemann–Hurwitz arithmetic, Lefschetz trace values and all character multiplicities, exceptional-module dimension, the seven-dimensional marked parameter quotient, and polarization square \(24\).

The checker ran successfully with output: `PASS: weighted monomials, transverse six-point witness, traces, characters, exceptional module, parameter count, H^2=24`.

The mathematical proof, not a finite sample, establishes general smoothness and the complete fixed-point classification; the Torelli and Noether–Lefschetz argument proves the exact rank for very general coefficients. Neither a machine-formalized proof nor independent auditing is asserted. The older complete bidouble-cover classification text has not been compared in full; publication priority should therefore be read as qualified.
