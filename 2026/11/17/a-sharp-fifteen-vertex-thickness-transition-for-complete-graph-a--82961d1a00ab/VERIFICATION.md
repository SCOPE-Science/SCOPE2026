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

## Reproducibility

Run `python3 verify_width.py` in the directory containing `RESULT.md`. The script uses only the standard Python library and reports `COMPLETE_GRAPH_WIDTH_PASS base_inequalities=36 profile_comparisons=3599 cut_support_cases=139 simplex_vertex_cases=14 threshold_n=15`. This run executed successfully from the packaged source directory.

The proof analytically establishes the all-dimensional tail by strict derivative and endpoint comparisons. The checker verifies a complete finite base and selected larger cases but is not itself an all-dimensional proof. The historical-priority assessment is provisional and independent mathematical validation has not been carried out.
