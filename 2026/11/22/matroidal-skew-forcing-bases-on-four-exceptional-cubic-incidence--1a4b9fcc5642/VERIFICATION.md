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

# Reproduction and verification

Use Python 3 without external packages:

```sh
python3 verify.py
```

Compile and run the independent C++17 implementation:

```sh
c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify
./verify
```

Both were run on the supplied source files and printed `ALL CHECKS PASSED` and `ALL C++ CHECKS PASSED`, respectively. Python enumerates each of the two bipartition shores independently for each of the four graphs, verifies every force closure, all one-shore cardinality coefficients, all optimal configurations, exact jump adjacency, every pairwise exchange distance, vertex degree distribution and eccentricity, plus the H/M/P incidence-triple descriptions and the Desargues connected-edge criterion.

C++ uses separately constructed graph adjacency, independently simulates the full skew forcing process on **every** initial vertex set across all \(2^{14},2^{16},2^{18},2^{20}\) possibilities, checks coefficientwise identity with an independently enumerated shore product, and redoes all optimum shore exchange-graph metrics. The complete finite domain is tested, not sampled. The all-order general bipartite decomposition and the Desargues graph-completion implication are mathematical arguments stated in RESULT.md; the finite implementations serve as cross-checks and exact certificates for the four fixed graphs.

No external independent scholarly audit is claimed. Numerical reproducibility is distinct from publication priority.
