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

# Verification details

The executable `VERIFY.py` is a complete self-contained deterministic integer chain calculation, using only the Python standard library. It enumerates every nonattacking rook face, constructs every strict face chain up to the full dimension, reduces under all fourteen dihedral transformations, and forms the signed integral orbit-of-flags boundary. The square-zero identities are checked for all columns. Integral unit cancellations are justified by chain basis changes, leaving one zero-cell, no one-cells, three two-cells and eighteen three-cells. The final boundary has gcds of its minors of orders one, two and three equal to \(2,4,8\), and thus nonzero Smith invariants \(2,2,2\); no finite-field inference is used for these integral torsion exponents.

The executable's observed standard output is stored verbatim in `VERIFICATION_OUTPUT.txt`. The independent Euler check is \((-224+7\cdot4)/14=-14\), matching the integral ranks. The proof of simply connectivity uses the cited chessboard connectivity and Armstrong theorem; the numerical verifier by itself does not prove this fact. Likewise, the standard three-dimensional homotopy argument is mathematical reasoning outside the computer program. This is a self-reviewed mathematical result; independent audit has not been performed.
