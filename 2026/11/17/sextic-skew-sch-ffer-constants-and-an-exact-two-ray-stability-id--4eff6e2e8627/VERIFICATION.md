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

# Reproducibility and limits

The supplementary `sextic_check.py` was executed from its packaged source with Python 3 and SymPy. Exact symbolic equalities include the sixth-power binomial identity, reduction of the perfect-square formula modulo the quadratic relation for the radical, and the scaled-involution identity. Finite numerical checks include 3,000 scalar identities, seven attained upper/lower two-atom pairs, and three optimal pointwise distance certificates. The complete proof is in RESULT.md; finite numerical tests do not certify infinitely many parameter values or priority. An independent mathematical audit has not been performed.
