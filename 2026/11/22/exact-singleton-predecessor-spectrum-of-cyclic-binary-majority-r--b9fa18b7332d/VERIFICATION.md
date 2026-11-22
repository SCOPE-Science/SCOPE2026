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

## Exact checks performed

`verify_transfer.py` was executed with Python 3 from the final package contents. It reconstructed 476 saturated matrices and 136 singleton-accepting states directly from the two majority-rule transfer matrices. It checked all 476 coordinates of the degree-21 integer vector identity, the numerator coefficients through degree 20, and 120 subsequent coefficients. All checks passed.

`verify_bruteforce.py` independently enumerated all binary input configurations on indexed rings of lengths 1 through 16, including the repeated-neighbor conventions at lengths 1 and 2. All sixteen singleton-output counts matched the transfer computation.

The unbounded-length result follows from the exact vector identity, not from the finite sample of source words. The scripts require only the Python standard library. No independent mathematical review has been performed.
