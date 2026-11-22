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

# Reproducibility and scope

The full reproducibility artifact is `check_iso4.py`, a standalone Python program using only `itertools` and `math` from the standard library. Run `python3 check_iso4.py`. It checks all 65,536 subsets of the four-cube, establishes all scalene-triple counts twice by independent recursions and direct membership counts, verifies each minimum and the equality predicate, checks the analytic parity-plus-antipodal formula for 512 possible parity-rooted sets, and emits a deterministic PASS line and the eleven minimum/count rows.

The printed PASS report was produced by executing this file as packaged, not inferred from an older run. The exhaustive finite scope is the sixteen fixed Boolean vertices only. Neither the checker nor the reviewed proof asserts a higher-dimensional result; independent mathematical validation has not been performed.
