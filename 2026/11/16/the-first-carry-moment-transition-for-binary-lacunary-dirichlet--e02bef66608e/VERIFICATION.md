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

The exact arithmetic verifier `check_first_carry.py` was executed from the saved working scientific files. It passed 281 checks comparing direct integer polynomial convolution against the finite-carry enumeration for every base from two through eight, every depth from one through four, and each even moment exponent up to the base. It also checked the subcritical factorization, critical recurrence, and explicit fourth-base values.

An independent mathematical audit has not been carried out. These finite checks do not establish results for arbitrary bases or depths; the unrestricted proof is in `RESULT.md`, including the carry-range lemma, the transfer matrix and its symmetric spectral reduction. Known-prior coverage remains subject to later bibliographic verification.
