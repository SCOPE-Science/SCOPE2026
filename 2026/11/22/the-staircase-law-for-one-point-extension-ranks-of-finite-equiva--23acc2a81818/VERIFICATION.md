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

# Verification and reproducibility

The finite proof is the induction in `RESULT.md`; it does not rely on execution or on a finite search. To reproduce the independent finite tests, run `python verify.py` in the same directory as the extracted files. Python 3 and its standard library are the only requirements.

The checker directly evaluates the minimax recursion over all abstract one-point extension types and all concrete realizations for every subset of each set partition of orders zero through eight. It reports `ALL_CHECKS_OK partitions=5296 positions=1187043` when successful. The total counts include the empty structure. The script also checks the staircase extremal profile for the first eight ranks. This is not an exhaustive search beyond eight points, nor a proof of the universal induction or a calculation of any transfinite rank.

Historical-priority verification is incomplete; no independent audit was performed.
