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

# Verification scope

The proof's key integral identities are \(M^7=I+2B\), \(\det B=87\), and \(M^{14}=I+4C\), \(\det C=7569\). Checking these exactly, followed by the squaring induction, certifies the infinitely many dyadic valuation identities. The state-count formula then gives the complete cycles at every positive exponent.

`CHECK.py` uses only the Python standard library. It recomputes the exact base matrices and their odd determinant certificates, checks fourteen further exact normalized matrix lifts, and exhaustively traverses all \(8+64+512+4096+32768=37{,}448\) states for dyadic exponents one through five. The observed cycles are \(2,6,22,86,342\), totaling \(458\), with the predicted primitive length counts. The program tests small cases and does not assert independent verification of the unlimited algebraic induction.

The mathematical review is a self-review; no independent mathematical audit or external certification has been performed.
