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

# Reproducibility and scope

The full proof is in `RESULT.md`. Run `python3 verify.py` (Python 3 standard library only). It checks exact-rational determinant factorizations on a finite collection of pairs, an explicit nonzero rank-two minor, a rational null vector and rational bracket signs for the cubic root. The script separately tests sign representatives with rational \(x\) and \(y\). These checks do not certify the continuum claims by enumeration; monotonicity and one-crossing calculus provide that part. No external independent audit or validation has been performed.
