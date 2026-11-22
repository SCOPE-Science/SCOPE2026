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

# Reproducibility and scientific limits

The proof and definitions are given in `RESULT.md`. The portable file `verify_matching_metric.py` requires Python 3.9+ and the Python standard library only. From the directory containing the files, execute `python3 verify_matching_metric.py`.

The script directly enumerates matching sets of \(K_n\) for \(2\le n\le10\). For each size class, it compares the claimed polynomial with an independently assembled histogram based on the connectedness of nonempty symmetric differences. It also checks exact factorial ratios for \(0\le r\le5\) and finite-size approximations of the degree limit with \(0\le s\le4\) and \(k\in\{20,50,100\}\). The script printed `KCOMPLETE_MATCHING_EDGE_METRIC_PASS (34 exhaustive strata, 15 asymptotic diagnostics)`.

The combinatorial proof establishes the finite formula, and the asymptotic ratio and vanishing-cycle argument establish the infinite distribution. No finite run is treated as an infinite proof, and the tests do not independently audit the referenced matching-polytope adjacency theorem.
