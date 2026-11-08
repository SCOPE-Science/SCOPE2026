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
The included `verify.py` runs without third-party packages. Its exact Fraction calculations test the inverse covariance, the simplex contact-frame isotropy identities, and all unit tangent constraints for \(2\le n\le12\). Independent integer screening comparisons span 2014 \((m,n)\)-pairs in the ranges \(2\le m\le39\) and \(2\le n\le54\), including two integer boundary points. A separate explicit column-support witness detects noncontainment for the \((4,4)\) example. The checker prints `RECTANGULAR JOHN CERTIFICATE CHECKS PASSED` on success. The mathematical all-parameter theorem rests on the exact John-contact construction and support calculation in RESULT.md; these tests are finite corroboration, not substitutes for its proof. Independent audit was not performed.
