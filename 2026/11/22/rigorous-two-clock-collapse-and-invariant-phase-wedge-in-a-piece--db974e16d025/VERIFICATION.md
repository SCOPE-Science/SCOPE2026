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

The proof is in `RESULT.md`. Execute `python3 check.py` with Python 3.9 or newer; no external mathematical packages are required. The script uses `fractions.Fraction` to avoid floating point errors.

The checker actually passed 6,510 rational ordered points with denominators 3 through 33, including 4,855 points in the invariant passive sector, and 4,949 exact rational diagonal initial conditions with eight iterates each. It also checked one exact rational nonsymmetric trajectory. The checked identities cover order preservation, weak one-step monotonicity, two-step wedge invariance, the closed rational two-step formulas, and the diagonal reciprocal solution.

Finite tests cannot establish any infinite-time convergence theorem or exclude hidden historical statements. The global finite-entry and positive-amplitude convergence are proved analytically, without assuming computational exhaustion. No independent mathematical audit was performed.
