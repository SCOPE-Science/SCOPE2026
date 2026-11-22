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

# Verification

Execute `python VERIFY.py` from this folder. In the reviewed execution the program reported `PASS: 14212 exact rational assertions`. Checks use Python's exact `fractions.Fraction` arithmetic and fixed-seed sampling; no third-party package or external service is required.

The proof of the infinite statements is in RESULT.md. In particular, the quadratic sign argument controls every nonnegative count index, so finite diagnostics are not used as exhaustive evidence. The algebraic crossing rate is certified by the strict increase of \(9t^3+36t^2+40t-7\), together with exact signs at the rational bracket endpoints \(153/1000\) and \(154/1000\). The uninspected 2010 primary full text is an acknowledged historical-priority limitation, not a computational assumption.
