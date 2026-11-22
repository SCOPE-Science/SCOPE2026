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

# Verification and reproducibility

The theorem uses the graph \(K_n\square K_n\), with row/column sharing as the only adjacency and standard closed-neighborhood-first power domination. Execute the two provided standard-library programs from this directory:

```
python3 verify_direct.py
python3 verify_structural.py
```

The direct checker independently determines feasibility by repeated graph-neighborhood propagation for every subset up to the optimum size for orders 3, 4 and 5; it then explicitly builds the optimal slide graph. Its successful terminal marker is `DIRECT_VERIFY_OK`. The structural checker generates row and column near-transversals as bit masks and constructs all valid coordinate slides independently; its successful terminal marker is `STRUCTURAL_VERIFY_OK`.

Both checkers confirm \(|V|=36,416,5650\), \(|E|=126,2784,60100\), and diameter \(4,6,8\), at orders \(3,4,5\), respectively. Complete shortest-path enumeration is performed for orders 3 and 4; at order 5 direct checks use 45 sources and structural checks use all 25 column-star sources. Thus exhaustive all-pairs distances are not claimed at order 5. The all-order upper bound, strict non-extremal improvement, and all-order lower bound are mathematical arguments in `RESULT.md`, not extrapolations from the code.

The scripts use only Python's standard library. Every exact numerical statement above is reproduced by their assertions, and neither checker requires precomputed data, network access, or external packages. The computation is not an independent human audit of the theorem.
