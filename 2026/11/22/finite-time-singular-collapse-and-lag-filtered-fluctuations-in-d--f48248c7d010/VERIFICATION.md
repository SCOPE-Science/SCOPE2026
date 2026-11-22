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
# Verification and limits
The proof in RESULT.md is analytic and covers all \(d>k\ge1\). The included `CHECK.py` uses only the Python standard library and exact rational arithmetic. Invoke `python3 CHECK.py` to check the transfer identities, several finite graph cases, eight nonzero covariance lags, the summed variance and the spectral density at zero frequency. The finite numerical checks do not prove the infinite assertions, exactness of the full tent map, or a central limit theorem. Those assertions are established in the supplied proof.

Independent audit has not been performed. The originality comparison is a best-knowledge literature assessment and not an independent priority certification.
