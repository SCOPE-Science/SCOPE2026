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

# Reproducible checks

Use Python 3 with no external dependencies and run `python3 checker.py` in the package directory. It constructs explicit finite models and recomputes rank types from accessibility and valuations rather than trusting declared labels. It checks 66,142 exhaustive target types in seven specified small parameter settings and 200 deterministically sampled higher-depth target types, printing `MODAL_SHARP_DEPTH_CUTOFF_OK` and `instances 66342` on success.

The code does not prove the infinite theorem, whose quantified argument appears in RESULT.md. The lower bound follows symbolically from mutual exclusivity of all predecessor-type characteristic formulas; it is not inferred from a finite search. The 2026 source was dated and its abstract and accessible overview compared, but its full paper was not available for complete inspection. Independent audit has not been performed.
