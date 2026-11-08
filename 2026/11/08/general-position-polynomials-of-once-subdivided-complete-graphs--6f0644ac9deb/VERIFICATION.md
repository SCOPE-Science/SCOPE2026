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
Run `python3 verify.py` with a standard Python 3 interpreter. There are no nonstandard dependencies. The script independently builds the one-subdivision graph, computes shortest-path distances using breadth-first search, enumerates forbidden selected geodesic triples, and compares the original definition with the structural characterization and exact coefficient formulas.

Actual output:

```text
DIRECT_OK 3 subsets 64 coefficients [(0, 1), (1, 6), (2, 15), (3, 2)]
DIRECT_OK 4 subsets 1024 coefficients [(0, 1), (1, 10), (2, 45), (3, 30), (4, 5)]
DIRECT_OK 5 subsets 32768 coefficients [(0, 1), (1, 15), (2, 105), (3, 175), (4, 100), (5, 11)]
SAMPLE_OK 6 subsets 40000 coefficients [(0, 1), (1, 21), (2, 210), (3, 655), (4, 900), (5, 357), (6, 31)]
VERIFY_OK direct_subsets 33856 sampled_subsets 40000 orders_checked 3..20 forbidden_triples 1063 full_polynomials=PASS maximum_multiplicity=PASS
```

The degree and maximum-multiplicity formula are checked for each integer \(3\le n\le20\), but the complete BFS enumeration is limited to \(n\le5\). Order-six BFS checks sample \(40000\) deterministic subsets, and its complete edge-family enumeration verifies the formula separately. These checks corroborate but do not prove the infinite statements. The mathematical proof supplies the unrestricted argument.
