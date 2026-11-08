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

The polynomial claim has a finite exact certificate in `verify.py`. From the directory containing that program, execute:

```sh
python3 verify.py
```

The program uses only the Python standard library. It constructs each graph from the explicit vertex/edge rules, counts every subset by down-spin cardinality and cut size using adjacency-mask recurrence, independently recomputes those coefficients using a four-row representation, and checks the factorization term by term. For each graph it enumerates all \(2^{16}=65536\) vertex subsets, verifies cardinality totals, and compares the full integer coefficient dictionaries. It also checks the zero-field specialization against an independent algebraic expansion. The last printed line must be `VERIFIED`.

The finite enumeration proves the exact polynomial only after the graph definitions, code, and exhaustive loop bounds are checked. The analytic sign classification is separately proved by a real quadratic inequality; the two zero-temperature field limits use elementary asymptotics. The computations make no claims for larger graphs, other spin alphabets, or infinite-volume thermodynamic transitions.
