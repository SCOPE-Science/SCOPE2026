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

The included `verify_magnus.py` is executable with a standard Python 3 interpreter and no third-party dependencies. An execution of the actual embedded script completed with `VERIFICATION_PASS 674 assertions`; it checked exact rational generator commutators, exact cubic Taylor coefficients in sizes four through nine with several unequal positive rational rate patterns, the unique-root bracket, and independent high-precision four-by-four matrix exponentials across ten representative positive rates.

The proof of all-rate positivity recovery, uniqueness of the transition, and the all-dimensional cubic coefficient is analytic and supplied in `RESULT.md`. Finite calculations do not establish those universal claims without the stated proof. The comparison to prior publications is limited to materially inspected sources, and independent mathematical audit has not been performed.
