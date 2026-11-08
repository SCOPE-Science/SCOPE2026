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
# Verification of the formulas

Run `python3 verify.py` using only the Python standard library. The script constructs additive subgroups from three generators and computes the resulting sets without applying the derived congruence as a subring criterion. It then checks generator products for ring closure and multiplication by the two ambient additive generators for the ideal condition; full pairwise multiplication is separately checked in small dimensions. The resulting counts are compared with the stated formulas and the Dedekind zero-defect criterion.

Observed output: `VERIFY_OK cases=45 exhaustive_cases=18 subgroup_patterns=2267 example_good=(18, 18) example_bad=(38, 32)`.

The checked ranges are not an exhaustive test of all finite parameters; arbitrary-dimension validity rests on the proof. Independent audit is not performed.
