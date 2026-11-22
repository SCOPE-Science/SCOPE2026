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

Run `python3 check.py` with Python 3.10+ and no external packages. The checker builds the exact set of normalized one-element insertion outputs from all layered sources with length at most ten, compares the symbolic formula, and verifies the exact extrema and optimizer counts. It separately enumerates all output partitions and their one-element deletion preimages to check the same layered source degrees for length at most seven without using the forward-insertion generator.

Observed output: `VERIFY_OK forward_layered_cases 1023 extremal_strata 55 independent_reverse_cases 127 max_n 10`.

The infinite theorem uses the combinatorial injectivity/collision argument and the optimization proof in `RESULT.md`; these finite checks alone would not establish it. No independent external audit has been performed.
