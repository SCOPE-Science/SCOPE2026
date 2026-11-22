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

The proof uses the cited word-normal-form theorem and finite-generator join descriptions. Both separately implemented scripts enumerate every nonempty polynomial in 15 canonical term types at three generators. `checks/absorption_census.py` deduplicates absorption signatures; `checks/direct_census.py` uses the distinct method of evaluation in actual finite generators and a congruence-join component count.

Run from the package root: `python3 checks/absorption_census.py` and `python3 checks/direct_census.py`.

Each reproduces the lower-rank reference values and the seven rank-three values, ending `VERIFY_OK`. The scripts prove the finite census conditioned on the cited completeness theorems; they do not establish a new abstract normal-form classification, guarantee historical priority, or constitute independent mathematical review.
