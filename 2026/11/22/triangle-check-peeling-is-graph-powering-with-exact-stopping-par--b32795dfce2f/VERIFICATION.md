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

# Verification of the complete triangle-check theorem

The proof is analytic for every integer \(n\ge3\). Its critical reductions are: every uniquely recoverable pair closes an initially known two-step path; one synchronous round squares the current known graph; a cluster graph is exactly a graph without an induced three-vertex path; two-part partitions give the inclusion-minimal nonempty complete multipartite edge sets; the kernel of the pair-by-triple incidence matrix is the binary cut space of the complete graph. The corresponding formulas for distance, stopping sets, completion ambiguity, and connectivity are spelled out in RESULT.md.

The three included standalone programs can be run in one directory:

```
python3 verify_peeling.py
python3 verify_partitions.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_components.cpp -o verify_components
./verify_components
```

The Python peeling program and separate C++17 triangle-check implementation each checked every one of \(2^{\binom n2}\) erasure patterns for each \(n=3,4,5,6\). Both independently reconstructed full peeling and graph distances. They agree on stopping totals \(5,15,52,203\) and successful-erasure pattern counts \(4,38,728,26704\). They check inclusion minimality against all smaller stopping subsets. The independent partition program recovered those stopping-count polynomials through \(n=7\) (where there are \(877\) stopping sets) and the connected graph recurrence through order seven.

These tests are exhaustive only for the explicitly enumerated finite orders. No claim of independent external scholarly audit is made. Classical stopping-size bounds, graph-cut structure and partition counts are credited; priority risk remains for possible equivalent historical results.
