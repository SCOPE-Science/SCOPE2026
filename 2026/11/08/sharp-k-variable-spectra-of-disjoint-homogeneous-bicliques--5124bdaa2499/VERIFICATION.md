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
# Reproducibility

Execute `python verify.py` with Python 3 and no third-party modules. The recorded `verify_output.txt` was produced by this command on the exact script accompanying the proof. The check implements colour refinement on all \(k\)-tuples using sets of colours attainable by replacements, with equality and adjacency as the initial atomic signature. It tests one- and multi-component bicliques at widths two, three and four, including beyond-threshold pairs. Expected equivalence is calculated independently from the displayed truncated invariants and compared against the observed stable colours.

The replay is finite and does not enumerate every parameter or all quantified sentences; the unbounded conclusions require the proof in `RESULT.md`. The metadata and review fields report self-review only. Independent mathematical audit remains unperformed.
