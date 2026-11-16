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

# Reproduction of exact checks

With Python 3.10+ in the directory containing both source files:

```sh
python3 verify_low_support.py
python3 verify_matrix_tree.py
```

The first script reconstructs rational cube transfer-current minors, clears their denominators, and exactly enumerates zero determinants for all supports of sizes one, two, and three in dimensions 2 through 7. Observed support-zero counts in dimensions 2, 3, 4, 5, 6, 7 were respectively `(0,6,0)`, `(0,6,20)`, `(0,208,832)`, `(0,0,0)`, `(0,0,0)`, `(0,0,0)`; the dimension-seven loop examines precisely 14,885,696 triples. Its rational integral check evaluates the dimension-eight spectral bound as `3323/7168` and verifies it is less than `1/2`.

The second program independently constructs edge-signed graph Laplacians and obtains their weighted spanning-tree sums as grounded integer determinants. It verifies every edge-pair and edge-triple signed sum against the transfer-current calculation for dimensions 2, 3, 4, and checks 319 dimension-five triples. The test results were reproduced from the final embedded source, not from earlier working copies. Exhaustion is claimed only for the explicit complete loops; none of these computations constitutes independent external certification.
