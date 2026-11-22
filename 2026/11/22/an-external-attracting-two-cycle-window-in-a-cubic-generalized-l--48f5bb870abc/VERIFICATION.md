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

# Verification and boundaries

Run \(`python verify.py`\) with the single listed SymPy dependency. The script checks the exact factorization of \(f_\eta^2(t)-t\), the symbolic multiplier formulas for both branches, the algebraic location of the unique external flip boundary and selected rational-parameter orbit equations. Reproducibility uses packaged source, not other research records or external file paths. The proof's exhaustive sign dichotomy establishes the infinite family; numerical checks or finitely many symbolic specializations alone would not.

The analysis covers all real primitive period-two orbits for \(\eta>0\), with hyperbolic attraction determined by the strict multiplier inequality. It leaves neutral-endpoint nonlinear dynamics, higher periods and global basins unresolved. Independent verification has not been performed.
