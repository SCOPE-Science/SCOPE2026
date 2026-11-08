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

# Verification and proof limits

The elementary identities used in the theorem are reconstructible directly from the two-by-two inverse, positive-semidefinite decomposition, the arithmetic-geometric mean inequality, and a resolvent difference identity. They hold for infinitely many real matrices; numerical checking is not offered as a substitute for the proof.

The standalone `verify_spd_dpo.py` uses only standard-library exact fractions. Running `python3 verify_spd_dpo.py` prints one explicit rational counterexample, reports 250 exact safe tests, and ends with `VERIFY_OK`. It checks all sixteen ordered pairs of sign configurations for each sampled system, the necessary sign and potential inequalities, three additional lower-bound witness configurations, and the rational matrices' asserted eigenvalue factors.

This verification does not constitute an independent audit, formal theorem proving, or exhaustive testing of all real inputs. The source material and public prior-results comparisons are summarized separately in the scientific review.
