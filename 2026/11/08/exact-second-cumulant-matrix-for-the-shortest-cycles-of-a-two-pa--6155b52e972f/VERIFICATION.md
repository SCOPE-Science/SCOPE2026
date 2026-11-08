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

The accompanying `checker.py` exhaustively enumerates all two-parent histories through six vertices, using exact rational expectations and moments. It checks the five stated formulas, signs of the local finite-variance corrections, positivity of \(H_{31}-4\), and a rational upper bound proving the limiting variance deficit is negative. It prints `PASS 153 finite assertions` when successful. The unbounded \(n\) theorem is verified by the explicit conditional-moment and martingale-orthogonality proof; finite computations are not an infinite certificate. The classical multiple-zeta identity is stated with its elementary integral representation in RESULT.md.
