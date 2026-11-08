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

# Reproducible checks

Run `python3 check_prism.py` with Python 3 and the standard library. No network, third-party packages, external data, or randomness are needed. The script was run from the actual package source and returned:

```
VERIFY_OK all_labeled_graphs_n1to5=1099 bipartite_cases=427 identity_and_polynomials=PASS path_all_and_maximal_n1to12=PASS odd_cycle_boundary=PASS
```

The program constructs all 1,099 labelled simple graphs of order at most five and checks all 427 bipartite cases. Each bipartite case is independently rebuilt as a prism, every adjacency in the common-neighbor graph is tested against the parity-twisted disjoint-square prediction, and the entire open-packing face polynomial is enumerated directly and compared with the product polynomial. The program also checks all and maximal path-square configurations for every path order from one through twelve, and directly enumerates maximal open packings of ladders through seven rungs. The five-cycle prism is checked as a nonbipartite boundary where the conflict graph is connected.

These are finite consistency checks. The theorem for all finite bipartite graphs and for all ladder lengths follows from the explicit proof in `RESULT.md`, not from extrapolation. No independent audit has been performed.
