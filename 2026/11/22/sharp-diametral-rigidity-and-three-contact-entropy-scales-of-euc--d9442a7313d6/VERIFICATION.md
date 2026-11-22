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

Run `python3 check_sim.py` using Python 3 and the standard library; no datasets, network access or packages are required. The expected terminal result is `SIM_METRIC_PASS exact_vertex_cases=12 pairs=165555 exact_rank_cases=41644 generic_weight_cases=495 asymptotic_cases=8`.

The script constructs the actual vertices for twelve small rational-weight instances, compares 165,555 exact squared-distance pairs, determines all sphere contacts by exact rational arithmetic, checks 41,644 rank-pair distance inequalities, and tests 495 independent strict rational weight lists. It performs separate floating-point asymptotic checks in eight large-dimensional profiles.

The general theorem is analytically proved in RESULT.md; numerical examples are not treated as proof of all dimensions. Originality relies on inspected primary literature plus the publicly indexed closest record; inaccessible full text and unindexed equivalents remain documented limits. Independent audit is not performed.
