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

Run `python3 check_bridge.py` using a Python 3 standard-library interpreter from the directory containing the supplied `check_bridge.py`. The observed output was:

```
VERIFY_OK pairwise_completed 6234 sharp_witnesses 132 ruled_out_short_bridges 13901
```

The checker constructs the graph independently from generator cycles and does not import an external minimal-forbidden-language table. It exercises both completion procedures on all admitted finite word pairs in its stated finite ranges; the witness tests include direct search over all shorter candidate bridges for the smallest cases.

The unlimited theorem is established by the run-completion and forced-run proof in `RESULT.md`, not by extrapolation of any finite verification run. Checks did not enumerate all arbitrary parameters or independently audit the mathematical result. The finite inequalities do not assert exact values for every finite two-length bridge profile.
