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

# Reproducibility checks and limitations

Run `python3 checker.py` using Python 3 and the standard library. This prints `PASS 706 deterministic checks` for the following finite diagnostics: derivative and critical-point identities, boundary derivative signs, four geometric ratios above the cusp, stationarity and three-branch ordering, numerical equality of competing peak heights, the unique benchmark at distance ratio ten, and Laplace-transform/mean consistency including the known boundary-reset specialization.

The infinite-time convergence, complete all-parameter phase classification, and uniqueness of the coexistence probability are analytically proved in `RESULT.md`. The finite checker is not an exhaustive verification of these quantified statements. The pre-existing single-reset mean and reset-to-boundary inverse local-time formula are distinguished from the proposed new two-site phase classification. The novelty comparison remains subject to broader unindexed optimization results and independent literature assessment. No independent audit or validation was performed.
