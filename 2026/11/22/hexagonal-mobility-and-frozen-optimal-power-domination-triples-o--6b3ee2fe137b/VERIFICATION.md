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

# Reproducible verification

Run the two standalone standard-library Python programs from this package:

```sh
python3 verify_cyclic.py
python3 verify_xor.py
```

Each program generates a 28-vertex Coxeter graph from seven Fano lines, checks all subsets with at most three chosen vertices, computes their power-domination closures, builds the two full optimal-state movement graphs, traverses their components and every shortest-path tree, and checks the matching-support structure of the 28 mobile hexagons. Both require no precomputed graph files or third-party dependencies. Their output lines must both begin `VERIFY_OK` and contain identical JSON objects.

The first checker uses modular-cyclic Fano lines, bit masks and simultaneous propagation; the second uses nonzero XOR vectors, Python sets and sequential propagation. Both check 336 minima, 1764 unrestricted edges, 168 local edges, 168 isolated states, 28 six-cycles, and all 56280 unordered distances. These are finite exhaustive checks, not empirical extrapolation. No independent external audit has been performed, and the result makes no claim about infinite graph families.
