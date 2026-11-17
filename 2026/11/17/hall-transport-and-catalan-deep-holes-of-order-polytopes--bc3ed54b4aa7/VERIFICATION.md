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

# Exact verification and limits

Two included scripts use only Python 3 standard-library rational arithmetic. Execute from the extracted package directory:

```sh
python3 check_deep_holes.py
python3 independent_exact.py
```

The first script prints `ORDER_POLYTOPE_DEEP_HOLES_PASS chain_bits=8188 fence_balanced=2546 n=2..12` after exhaustive PAVA checks on every binary corner of every chain of orders \(2\) through \(12\), testing all balanced fence corners in that range and checking exact covering-edge flows. The second prints `ORDER_POLYTOPE_GENERIC_PARTITION_PASS exact_projections=1008 n=2..7` after enumerating all equality-block set partitions and evaluating the least-squares isotonic objective on four order relations of each size from \(2\) through \(7\). Tests include all binary corners of these relations. The input seed of the second test is fixed for reproducibility; it is not a probabilistic proof.

The general Hall normal-cone proof, and not the finite checks, establishes the claim for every finite poset. Finite tests cannot establish historical uniqueness or independent verification. The cited comparison sources were assessed for the specific cube-to-order Euclidean approximation statement, not for any certification of this proof.
