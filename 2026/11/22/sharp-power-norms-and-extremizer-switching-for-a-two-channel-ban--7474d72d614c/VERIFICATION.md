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

# Reproducibility

The analytic proof of the all-lag and all-exponent claims is in `RESULT.md`. To run the supplementary deterministic complex-number diagnostics, execute `python check.py` in this extracted directory. They compare the operator output directly with each sharp bound and test finite-support equality configurations, basic product identities and powers. The expected final line is `HAAR_SHIFT_CHECK_OK 5240`.

Finite diagnostics are not exhaustive and do not prove a universal theorem; the proof relies on the scalar sharp Clarkson norm and its strict equality cases. The known scalar estimates are explicitly credited. No independent audit has been performed. The principal bibliographic limitation is the uninspected complete text of some earlier mixed-norm and filter-bank treatments.
