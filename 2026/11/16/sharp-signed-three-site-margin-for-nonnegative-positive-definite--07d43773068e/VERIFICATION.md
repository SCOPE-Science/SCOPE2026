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

## Mathematical checks
The trigonometric polynomial factorization and the sharp rational example were reproduced by the standalone exact-arithmetic checker `CHECK.py` included in the same package. For the general inequality, the decisive evidence is the pointwise nonnegative factorization integrated against the positive Bochner probability measure; finite testing is not used to infer the infinite assertion.

## Equality and limitations
Equality requires both \(f(3x)=0\) and the spectral factor to vanish almost surely; this forces spectral cosine phases \(1,1/2\) of equal mass. This is a sharp single-vector three-site result, not a full matrix lower bound or arbitrary-site classification. Research literature comparison has residual uncertainty about older equivalent pointwise inequalities; no independent validation is represented.
