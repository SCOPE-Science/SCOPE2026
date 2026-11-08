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
# Verification of the quiver commuting-tuple theorem

The standalone `verify.py` uses only the Python standard library. It builds every element in each test algebra from independent vertex and arrow coefficients and checks actual pairwise multiplication, rather than using the proposed formula. An independent FK spanning-subgraph calculation predicts the counts. Direct exhaustive cases: single arrow over \(\mathbb F_2\), two parallel arrows over \(\mathbb F_2\), three-vertex path over \(\mathbb F_3\), triangle and reversed triangle over \(\mathbb F_2\), triangle over \(\mathbb F_3\), four-cycle over \(\mathbb F_2\), four-vertex tree over \(\mathbb F_2\), triangle with isolated vertex over \(\mathbb F_2\). The triangle's full ordered triples over \(\mathbb F_2\) were enumerated. Tree/cycle formulas and the coefficient-exponent noncollision for reconstruction were checked on several finite graphs.

Actual saved standalone execution:

```text
DIRECT_OK single_arrow q 2 t 2 probability 5/8
DIRECT_OK Kronecker_2 q 2 t 2 probability 7/16
DIRECT_OK path3 q 3 t 2 probability 121/729
DIRECT_OK triangle q 2 t 2 probability 1/4
DIRECT_OK triangle_reverse q 2 t 2 probability 1/4
DIRECT_OK triangle_odd_field q 3 t 2 probability 155/2187
DIRECT_OK cycle4 q 2 t 2 probability 157/1024
DIRECT_OK tree4 q 2 t 2 probability 125/512
DIRECT_OK triangle_isolate q 2 t 2 probability 1/4
DIRECT_OK triangle_triple q 2 t 3 probability 95/2048
KRONECKER_SPECIALIZATION_OK
TREE_CYCLE_FORMULAS_OK
RECONSTRUCTION_OK 3 3 6
RECONSTRUCTION_OK 4 3 10
RECONSTRUCTION_OK 4 3 6
RECONSTRUCTION_OK 4 4 10
VERIFY_OK
```

The exact all-quiver/all-prime-power theorem follows from the symbolic arrow-wise commutator calculation, not from these finite tests. The Tutte recovery follows from the proved injectivity of \((i,j)\mapsto t(i+j)-j\) for \(t>m\). Priority is relative to inspected literature and remains provisional; independent mathematical audit has not been performed.
