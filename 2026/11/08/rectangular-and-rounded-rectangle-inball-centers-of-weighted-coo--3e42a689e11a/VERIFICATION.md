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

# Reproducibility and limits

The self-contained `CHECK.py` uses only Python's standard library. Execute `python CHECK.py` in the directory containing the file; a successful run prints `WEIGHTED_DISCOTOPE_INCENTER_LOCUS_CHECKS_PASSED`.

The checker evaluates the exact support function for sampled unit normals and tests the predicted incenter-locus boundary at twelve positive weight triples spanning unique/tied largest weights, the additive threshold, and rectangular/rounded-rectangle regimes. It checks violations for explicitly excluded points and evaluates one-sided finite differences of the exact area formula at several thresholds. It does not enumerate the continuum of normal directions: this is supplied by the monotonicity lemma proved in `RESULT.md`. Neither simulation nor a code execution certifies an original infinite-dimensional or all-parameter statement, and no independent audit has occurred.
