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

The finite claims are checked directly by `python3 check.py`; the program regenerates the complete output sets rather than trusting the deficit identity, and calculates moments using exact rational arithmetic. Its last successful run reported `CERTIFICATE_OK direct_channel_words= 195317 exact_moment_profiles= 16`.

The mathematical proof of the Gaussian limit uses bounded two-dependent block sums and a Lindeberg argument. The Poisson limit uses mixed factorial moments for graph equality constraints and the vanishing boundary/triple-collision corrections. Exhaustive finite enumeration does not prove either limiting theorem; consult the respective analytic steps in RESULT.md.

Scientific restrictions: one non-wrapping length-three window, uniform independent symbols, integer alphabet size at least three. Historical priority and mathematical correctness have not undergone an independent audit.
