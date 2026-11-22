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

# Analytic and computational verification

The proof in `RESULT.md` is self-contained relative to the explicitly credited 2026 formulas for the crossing parametrization and the reduced half-return Jacobian. The derivative of the limiting reduced eigenvalue comes from a simple root at \(1\) separated from \(k<1\); the calculation therefore needs no numerical eigenvalue-continuation assumption.

Run `python CHECK.py` with SymPy and mpmath. It verifies symbolic identities for the critical parameter slope, crossing-amplitude coefficient, reduced eigenvalue derivative, and Floquet gap; numerically checks asymptotics at \(\mu=0.3,1,2\) and excess half-periods \(10^{-4},10^{-5},10^{-6}\); and verifies the homogeneous half-cycle symmetry and rescaled phase-space profile using exact matrix exponentials. The script was executed successfully from the packaged file. These finite tests do not establish asymptotic validity or originality independently of the analytic proof and literature comparison.

No independent mathematical audit has been performed, and no claim of global regularity at grazing or sliding is made.
