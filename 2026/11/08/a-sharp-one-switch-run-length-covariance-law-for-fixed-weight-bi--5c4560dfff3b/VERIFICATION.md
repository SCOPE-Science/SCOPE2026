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

The standalone `verify.py` enumerates all labeled fixed-weight binary cyclic words for sizes 3 through 14 and compares the full mixed covariance with the proved closed form using exact `fractions.Fraction` arithmetic. It checks each allowable integer \(k\) and exact run length \(\ell\), including degenerate and zero-covariance boundaries, and performs further sign-classification checks for sizes 4 through 149. All 22,288 rational assertions passed when executed from this package. This is a consistency check, not an independent scientific audit and not a proof for unbounded sizes. The infinite statement follows from the written conditional expectation and affine-sign argument.

Execution command: `python3 verify.py`.
