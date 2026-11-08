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

The joint classification table is `verification/census.csv`; each row gives exact first periodic entry time, least eventual period, and number of labelled initial configurations. The finite state space has exactly \(3^{14}=4782969\) elements, and its complete successor graph is computed explicitly.

To replay both exhaustive checks and the finite witness checks, run `python3 verification/replay.py` from the extracted package root. A C++17 compiler, Python 3 and standard libraries suffice. The replay checks each of the fifty-five nonzero table rows, the equality of the two complete state-space algorithms, the state total, and all stored primitive-cycle trajectories, including a witness with exact entry time ten.

Captured outputs: `verification/census_indegree.out`, `verification/census_paths.out`, `verification/witness_check.out`. Exact source code: `verification/census_indegree.cpp`, `verification/census_paths.cpp`, `verification/witness_check.py`, `verification/replay.py`. The period and entry assignments use no numerical tolerance, randomness or truncation.

The program proves finite exhaustiveness by visiting every base-three state. Sample cycles by themselves do not establish period exclusions, and there is no asserted infinite-family theorem. The classification has not undergone an independent external audit.
