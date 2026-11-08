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

# Verification and scope

The proof is self-contained except for two explicit general results: the negative-definite-support correspondence of Bauer--Funke--Neumann and the chamber-volume finiteness criterion of Bauer--Schmitz. Their application is detailed in `RESULT.md`.

The executable `verify/conic_verify.py` uses only the Python standard library. It independently backtracks intersecting edge sets for up to eleven labels; its computed edge-family size distributions agree exactly with the star/triangle polynomial. For \(n=7,8,9,10\), it enumerates all allowed exceptional-curve and secant-edge selections and compares complete support-size vectors against the analytic formulas. At \(n=7\), it reconstructs every proposed negative-support intersection matrix and tests its negative definiteness by exact rational elimination; it also checks incompatible larger conic/exceptional blocks. It checks the closed total formula for \(7\le n\le19\).

To reproduce: save the two attached files at their relative paths and run `python3 verify/conic_verify.py` from the package root. The recorded stdout is `verify/output.txt`, whose final line is `ALL_CHECKS_PASSED`.

These are finite consistency checks, not an exhaustive enumeration for unbounded \(n\) and not independent validation. The symbolic classification covers every integer \(n\ge7\) under the stated geometric assumptions. Historical novelty remains subject to specialist independent scrutiny.
