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

# Reproducible verification

Execute `python3 check_local.py` in a Python 3 standard-library environment. The program directly enumerates all permutations and all query supports of cardinality at most four for lengths one through eight, and compares actual trace completeness with the forbidden-type characterization. Expected final line: `AV321_LOCAL_SHATTERING_4_PASS`.

Execute `python3 check_padding.py`. It separately checks the increasing-block extension construction on every endpoint subset through length eight. Expected final line: `PADDING_321_PASS 16169`.

The finite enumeration is complete for the claimed local criterion because every four-query support involves at most eight distinct endpoints. Extending arbitrary endpoint sets to their containing permutation sizes uses the mathematical increasing-block inflation proof; the finite programs alone do not establish statements about arbitrary size. No independent mathematical audit has been performed.
