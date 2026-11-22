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

The accompanying `support_census.py` defines the exact 16-tagged-pair map, exhaustively enumerates all 65,535 nonempty subsets of initial pair types and checks all support coefficients against `SUPPORT_COUNTS.csv`. It also verifies the all-size-formula specializations for the eight small graph sizes from 2 through 8, including the full population sum and oscillatory-basin identity.

Compile the separately written state-space checker using `c++ -O2 -std=c++17 direct_check.cpp -o direct_check`. Next run `python3 support_census.py` in the same directory. `direct_check` iterates all microscopic states of each graph with two through five core vertices and computes entry times and eventual periods by indegree pruning and cycle marking; the Python script checks exact agreement in every nonempty class. A successful replay prints `INDEPENDENT_DIRECT_CHECK_OK widths=2..5`, `ALL_SUPPORT_SUBSETS_VERIFIED=65535`, `PERIODS=1,4 MAX_ENTRY=7`, and `ALL_TESTS_PASSED`.

The infinite-family theorem depends on the mathematically justified exact finite tagged-type quotient, not the empirical small-size checks. No external independent audit has been performed. Mathematical priority beyond inspected sources remains provisional.
