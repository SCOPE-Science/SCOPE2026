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

# Reproducibility and verification

Run `python3 verify.py` with Python 3 using only the standard library. The exact integer-polynomial enumerator independently computes component counts on every vertex subset for all 3,898 labeled connected unicyclic graphs of order three through six. It checks 7,796 first- and second-moment coefficient identities, verifies constancy of the cycle-root count within degree/cycle-length classes through five vertices, and verifies the six-patch polynomial difference \(2p^4(1-p)\).

The proof for arbitrary order uses the exact outcome-wise identity \(K=S-E+Z\), covariance counting, and the five-vertex structural classification. The finite enumeration corroborates those arguments but does not prove claims for arbitrarily large graphs. No independent scientific validation or field calibration has been performed.
