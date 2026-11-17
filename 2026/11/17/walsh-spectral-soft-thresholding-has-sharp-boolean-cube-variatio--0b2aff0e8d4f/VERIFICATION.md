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

# Reproducible verification

Run `python verify.py` in a Python 3 standard-library environment. The checker executes complete mask/cut enumeration in dimensions one through three, verifies strict-chamber two-input attainment for the exact maximizing mask and cut, and tests higher-dimensional Walsh impulse witnesses using integer arithmetic. Earlier development tests with incorrect Walsh scaling were replaced; only the corrected, replayed checker is supplied.

Expected output includes the complete small-dimension values \(1,1,3/2\) and the terminal marker `ALL_WALSH_CUBE_BV_CHECKS_PASS`. The checker is a finite auxiliary calculation: the theorem's unrestricted dimension-growth bound is established by the symbolic proof in `RESULT.md` using character orthogonality and exact Rademacher moments. The complete enumeration, rather than a sample, is the certificate for the three small dimensions. Independent mathematical validation has not been performed.
