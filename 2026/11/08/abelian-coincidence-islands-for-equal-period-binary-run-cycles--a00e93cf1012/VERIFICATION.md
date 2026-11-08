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

The proof in `RESULT.md` is a complete integer-interval argument for all positive parameters with equal period. The program `verify.py` separately constructs actual finite factor sets from the two periodic words, and counts their common zero-counts; it does not implement the analytic window extrema to obtain the observed results.

Executed using `python3 verify.py`, the observed output was:

```
VERIFY_OK parameter_pairs=2870 length_and_class_checks=123682 internal_gap_checks=13540
```

The sweep covers every pair of profiles with shared period from 2 through 21, both identical and unequal profiles, and lengths beyond the last predicted coincidence. It checks every shared-Parikh-class count, every predicted admissible interval, interval separation, and excluded lengths. The assertions terminate on a counterexample. This is finite reproducibility evidence, not an exhaustive infinite-parameter certificate. No independent validation has been performed.
