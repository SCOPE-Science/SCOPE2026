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

# Verification and limitations

Run `python3 verify.py` with standard-library Python 3. The script directly enumerates binary indexed words for lengths 1–15, canonicalizes each rotation class, computes its ordered cyclic pair counts, and checks the complete divisor-sum formula on each realized profile. It also computes arithmetic maxima for lengths 16–160 and compares selected scaled values to the limiting constant.

The universal asymptotic theorem is supported by the written Burnside, entropy, and uniform local binomial-limit proof in RESULT.md. The finite checks are only corroborative; they do not prove the infinite limit. The exact fixed-profile count is a classical enumerative ingredient and is not asserted to be novel. Whittle's 1955 full text could not be inspected, and priority uncertainty is acknowledged.
