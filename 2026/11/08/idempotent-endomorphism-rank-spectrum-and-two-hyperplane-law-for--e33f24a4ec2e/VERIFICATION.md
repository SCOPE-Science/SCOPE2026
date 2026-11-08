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

The standalone `verify.py` script enumerates the full matrix entries for every linear map on the indicated finite spaces, independently tests the defining bracket identities and matrix idempotence, and computes ranks by row reduction. It checks the formula both by rank and by image category for prime-field examples \((q,m)=(2,0),(3,0),(5,0),(2,1),(3,1),(2,2)\). It also checks integer generating counts through \(m=19\) for \(q=2,3,5\) and numerical sanity at \(m=30\) for \(q=2,3\). Successful execution prints `VERIFY_OK`.

Run `python3 verify.py` using Python 3 with standard-library modules only. The finite enumeration is exhaustive for the listed test dimensions and characteristics. It does not constitute an exhaustive test for arbitrary fields or dimensions, and it is not a proof of the asymptotic claims. Those claims follow from the exact formulas and uniform finite-field Gaussian bounds in `RESULT.md`.
