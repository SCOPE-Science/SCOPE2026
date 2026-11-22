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

Verification consists of two complete and separately implemented state-graph traversals (`census_walk.cpp`, `census_kahn_check.cpp`), plus a third, independently formulated weighted six-pair quotient check (`verify_twin_quotient.py`) for the circulant. The two primary enumerators each evaluate exactly 531441 labelled configurations for each of two explicit twelve-vertex graphs; their basin-size distributions and first-periodic-entry/least-period tables agree. The weighted quotient checks all 46656 pair-histogram signatures, whose multiplicities sum to 531441; it checks the actual periods of labelled lifts instead of assuming quotient period equality.

To replay, compile the two C++17 sources and run the Python 3 source according to RESULT.md. The included `walk_census.txt`, `kahn_census.txt`, and `twin_quotient.txt` are outputs of actual executions from the included sources. Each calculator uses exact integer arithmetic only. No finite subset is extrapolated to a claim over all graph sizes.

The graph automorphism-order values in the graph census serve as context, not as input to any computation. The main quantitative classification is certified by complete explicit state-space enumeration. No independent external audit or human validation has been conducted; historical novelty remains contingent on complete comparison with any unindexed equivalent classification.
