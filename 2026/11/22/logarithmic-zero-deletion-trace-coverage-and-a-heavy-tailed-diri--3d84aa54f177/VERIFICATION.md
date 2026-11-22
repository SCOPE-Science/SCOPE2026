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

# Verification of the conditional zero-deletion coupon theorem

Run `python verify.py` in the extracted package directory using Python 3 and only its standard library. The expected terminal marker is `VERIFY_OK`.

The program builds literal fixed-weight binary words, deletes every possible zero, merges equal output strings, and computes the exact conditional expected sampling time from the frequency vector by inclusion-exclusion. Independently, it evaluates the source-averaged gap-composition finite formula; exact rational equality is checked on 702 sources over marker counts one through three. Further assertions check the closed formula for one marker, 75 independent moment/inclusion-exclusion equalities for the Dirichlet limit, and the convergence trend of the explicit mean expansion. It also computes finite-sample tail expressions.

The all-length proof is in RESULT.md. Enumeration does not certify the limit or rule out unexamined bibliographic equivalents. No independent audit has been performed.
