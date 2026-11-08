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

The proof uses a conditional root split and independent record indicators, not a finite search argument. Reproduce the finite checks with `python3 verify.py` (Python 3 standard library only). Verified: complete enumeration of all insertion orders for \(2\le n\le8\); exact conditional distribution/moment checks through \(n=30\); the harmonic coefficient identity and strict covariance sign through \(n=300\); every upper-quadrant inequality for the exhaustively enumerated sizes. The checker reports 796 exact assertions. These computations corroborate, but do not replace, the all-size proof. The joint central limit and strict dependence for unenumerated sizes are proved analytically in RESULT.md.

Independent auditing and external formal verification have not been performed.
