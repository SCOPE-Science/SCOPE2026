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

# Reproduction of the exact finite census

From a directory containing all attached files run:

```sh
python3 graph_enumeration.py
python3 word_enumeration.py
```

Only the Python 3 standard library is required. Expected outputs are provided in `graph_output.txt` and `word_output.txt` and include asserted final totals. The two algorithms have different enumeration units: \(8192\) complete edge-pair choices, and \(1,594,323\) indexed cyclic words. The directed matrix-tree determinant uses fraction-free integer elimination, and the BEST factor counts circuits modulo cyclic edge rotation. Word enumeration uses direct cyclic windows and a distinct canonicalization routine. Both tests have been run from the extracted package and their complete stdout matched the stored outputs.

The proof of completeness is the explicit equivalence of every maximal negative-avoiding cycle with one of the \(2^{13}\) edge selections and of every indexed word with one of \(3^{13}\) tested tuples. No randomness, external data files, unbounded search, solver certificates or extrapolation are used. The two computations establish only the exact ternary span-three case, not all possible spans or alphabet sizes.
