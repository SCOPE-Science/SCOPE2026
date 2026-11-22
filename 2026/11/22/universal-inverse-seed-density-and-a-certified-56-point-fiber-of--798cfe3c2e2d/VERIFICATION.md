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

# Reproducibility

Execute `python3 check.py` with Python 3 using its standard library. The file contains the complete finite certificate and requires no downloaded data, network connection or optional packages.

The verifier reconstructs a rigorous rational enclosure of \(\pi\) from \(\pi=16\arctan(1/5)-4\arctan(1/239)\). It checks the full 169-pair phase-index box at \(t=10\), with rational interval arithmetic and exact integer-square-root bounds. It certifies 43 strict interior points, identifies the 13 boundary cases by exact formulas, and checks the total 56 and the sheet split 49 versus 7. It also checks polynomial normal-form identities on rational test inputs and the exact Jacobian-area arithmetic \(13/3\).

The all-target \(O(t)\) inverse-count theorem and empirical spatial law are proved analytically in `RESULT.md` by an exact two-sheet inverse plus mesh-cell discrepancy and Riemann-sum arguments. The checker does not purport to verify the infinite asymptotic through finite enumeration. No forward-time dynamics, numerical-security claim or independent external validation is supplied.
