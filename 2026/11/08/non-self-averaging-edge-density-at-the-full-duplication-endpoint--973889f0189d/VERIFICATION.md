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

# Verification record

Run `python verify.py` with Python 3. The script checks transition kernels of all graph states through four vertices at four rational link probabilities, propagates exact distributions of the growing graph through six vertices, and independently checks closed moment identities through order 39. It completed 1,940 exact-rational assertions.

The analytical steps requiring human scrutiny remain the conditional change in two-star count, the polynomial recurrence solutions, and the bounded-martingale inference to an infinite limit. These steps are written explicitly in `RESULT.md`; no finite enumeration is represented as a proof of a limiting distribution. The complement symmetry is a pathwise coupling argument.

The proof does not determine the full limit law or establish the general historical uniqueness of this endpoint result. Independent audit has not been performed.
