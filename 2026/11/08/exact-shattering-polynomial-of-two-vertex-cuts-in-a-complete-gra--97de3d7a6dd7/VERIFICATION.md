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
# Checks and limits

The standalone `verify.py` checks every edge-query support of size at most four for all \(3\le n\le8\), comparing the direct Boolean traces of all exactly-two-vertex cuts with the structural classification, then compares cardinality counts with the closed polynomial. It separately verifies that no five-edge support shatters through \(n=6\). Its successful replay prints `TWO_VERTEX_CUTS_PASS 37358 supports including every size <=4 through n=8`.

The all-order theorem is supported by the general trace-count obstruction, finite classification of graph shapes, and exact incidence-row-sum table in `RESULT.md`; finite tests are neither an exhaustive infinite proof nor a priority certificate.
