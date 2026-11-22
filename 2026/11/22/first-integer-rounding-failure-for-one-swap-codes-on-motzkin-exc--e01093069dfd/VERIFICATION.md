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

# Verification instructions

The source words are the nonnegative-prefix, zero-ending paths on `U,D,H`. The receiver accepts all unchanged and at-most-one-adjacent-swap words, including outputs that leave the path constraint. For each fixed number of up steps, `certificates.json` records the entire rational primal and dual incidence solution and a maximum integer codebook.

Run `python3 verify.py` alongside `certificates.json` using a Python 3.9+ standard-library interpreter. It reconstructs each of the 19 input/output layers, checks every codebook's zero-intersection property, checks all primal and dual inequalities with exact rational arithmetic, matches objectives, and *re-runs* maximum-clique branch-and-bound. The greedy coloring upper bound used for pruning is proved in the verifier's docstrings and `RESULT.md`.

Actual completed check:

```text
VERIFY_OK groups=19 nodes=1870
Integer capacities: 1,2,2,4,7,14,28
Fractional optima: 1,2,2,4,7,71/5,5515/182
```

As an independent algorithmic cross-check of the finite graph computation, the incidence matrices were generated a second way and passed integer mixed-integer optimization and continuous linear optimization for all components through seven steps. Such solver output alone is not used as an upper-bound proof; the package provides a deterministic exhaustive proof search and exact arithmetic.

Not established: capacities beyond length seven, multiple swap corrections, uniqueness of every optimal codebook, or comprehensive historical priority. Independent external mathematical audit: not performed.
