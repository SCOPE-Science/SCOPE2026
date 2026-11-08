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

# Verification
Run `python3 verify.py` using the standard Python library. The code enumerates every rank-two order-preserving map in each chain size from 2 through 16, composes the resulting functions directly and checks all assertions. In particular, it verifies the two inverse identities, the involution property, reversal equivariance, the idempotent characterization and both exact combinatorial counts. The recorded output ends `VERIFY_OK n=2..16 elements=7820`. This is a finite exhaustive check only for the enumerated chain sizes; the arbitrary-size statement relies on the explicit symbolic case proof in RESULT.md. No outside proof certification or independent audit has been performed.
