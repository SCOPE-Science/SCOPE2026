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
# Verification record

The algebraic proof is included in `RESULT.md`. Both standalone checkers use only standard language runtimes, enumerate individually labelled configurations, and were executed for the indicated finite scopes:

```sh
g++ -std=c++17 -O3 -Wall -Wextra census.cpp -o census
./census
python3 independent_check.py
```

`census.cpp` exhaustively enumerates all configurations and determines orbit periods and eventual basins using indegree peeling on the complete functional graph for \(r=2,3,4,5,6,7\). The case \(r=2\) is a deliberately excluded boundary and displays primitive four-cycles. For \(r=3,\ldots,7\), the exact integer count formulas match the enumerated data, and all finite trajectories have eventual period one or three. Its exact stdout appears in `census_output.txt` and ends `CHECKS_OK`.

`independent_check.py` computes a separately implemented local update and resolves every orbit through forward traces, not indegree peeling. It also enumerates rainbow triangles independently by direct pair selection for \(r=3,4,5\). It matches basin and primitive-orbit counts and its stdout appears in `independent_output.txt`, ending `INDEPENDENT_CHECKS_OK`. Both scripts were run in their embedded versions. Exhaustive finite checks do not prove formulas at arbitrarily large \(r\); the general mathematical argument provides that part. No independent external validation has been performed.
