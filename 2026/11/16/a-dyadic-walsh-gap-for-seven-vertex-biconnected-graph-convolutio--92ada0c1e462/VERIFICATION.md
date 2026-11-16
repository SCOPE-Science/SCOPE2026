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

The finite calculations were checked with two separate standalone exact-integer C++17 programs, `moment_certificate.cpp` and `independent_tarjan.cpp`. The first checks connectivity after deleting vertices and computes all forced-edge counts by superset zeta transform. The second uses a low-link DFS articulation test and a recursive Walsh transform, with direct signed evaluations at the sharp witnesses.

Both programs were compiled with `g++ -O3 -std=c++17` and run successfully from these source files. They agree on all orders three through seven: admissible graph counts \(1,10,238,11368,1014888\), no zero Walsh multipliers, and exact minimal magnitudes \(1,2,2,8,8\). The order-seven Parseval identity is \(\sum_S W_7(S)^2=2128374398976=2^{21}\cdot1014888\). The direct witness at frequency mask `2396` has signed value \(8\).

The proof of the congruence for every frequency is the stated exact subset expansion modulo \(16\) and depends only on the verified forced-edge counts of size up to three. These exact finite computations do not prove the analogous claim at eight or more vertices. Independent external mathematical validation has not been performed.
