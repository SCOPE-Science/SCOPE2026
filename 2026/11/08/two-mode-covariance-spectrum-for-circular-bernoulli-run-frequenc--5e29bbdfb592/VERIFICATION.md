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

# Reproducibility and boundaries

Run `python3 check.py` using a standard Python 3 interpreter. The script enumerates all binary cyclic words at specified small sample lengths with exact rational product probabilities, and checks every entry of the covariance matrix against the formula. It then verifies the rationalized rank-two representation and characteristic-invariant identities. Every asserted calculation is self-contained and does not require network data or auxiliary files.

This is finite verification of independently derived consequences, not a proof for unbounded \(n\) or \(R\). The all-parameter result is proved in RESULT.md by conditioning and elementary linear algebra. The general statement requires \(R\ge2\), \(0<p<1\), and \(n\ge2R+3\). No independent validation has been performed.
