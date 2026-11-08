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

The theorem uses exact first-event recurrences on alternating paths. Taylor coefficients are rational because each finite-path expectation is rational in the slow/fast rate ratio and regular at zero.

The package includes `verify_rsa.py`, a Python 3 standard-library checker. Execute `python3 verify_rsa.py` in the directory containing this file. Its exact Fraction computations confirm the coefficient expressions for all path size indices from 4 to 36, all cycle size indices from 2 to 34, and exact agreement of independent path and graph-mask recursions for 18 cases.

The infinite proof uses the explicit polynomial induction: after multiplying the path recurrences by their linear denominators, each coefficient residual has degree at most two in the path size index (finite exceptional terms plus sums of affine expressions). The base identities at three distinct sizes establish the residual identity for every larger size. The finite checks alone would not establish that claim.

No numerical simulation, independent external review, or infinite machine certification is claimed. The remainder estimate is at each fixed cycle size and is not uniform in size.
