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

Run `python verify.py` using Python 3 and the standard library only. The script enumerates all \((n-1)!\) recursive trees for every \(2\le n\le9\), computes exact-rational expectations of every marked outdegree and the total path length, then checks both covariance formulas and the deterministic total-degree identity. A separate numerical grid checks unique sign change for marked labels \(2\le i\le69\). The observed output was `PASS: 120 exact enumeration/analytic and numeric threshold assertions`.

These computations are finite checks; the unrestricted result rests on the independent-parent coupling, telescoping identity, signed increment argument, inverse-square tail bound, and harmonic asymptotics in RESULT.md. The historical novelty comparison is same-model only and is not an independent audit.
