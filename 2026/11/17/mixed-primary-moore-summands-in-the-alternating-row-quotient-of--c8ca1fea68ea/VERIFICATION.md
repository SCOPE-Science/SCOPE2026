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

The two reproducible verification programs use Python 3 and SymPy for arbitrary-precision integral Smith normal forms. `verification/verify_orbits.py` builds the action from the actual twelve even permutations of four rows, independently enumerates every face of the four-by-seven ordinary chessboard complex, and canonicalizes all face orbits. `verification/verify_parity.py` uses the separate explicit parity-orbit construction. Both check the two consecutive chain-composition identities and obtain invariant factors \(1^{\times6}\), \(1^{\times15}\), and \(1^{\times49},3^{\times5},6\) in positive boundary degrees one, two, and three respectively.

Exact output: `verification/results.txt`. The package contains the complete source code needed for these checks; neither program imports an unrecoverable artifact. The computations are exhaustive for this finite quotient and do not extrapolate to other board widths. The homotopy classification additionally relies on published connectivity/shellability and orbit fundamental-group theorems, and on the two-skeleton/Smith cofiber argument in `RESULT.md`.

These checks are self-review of a mathematical proof and exact calculation, not independent mathematical certification.
