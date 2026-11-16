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

# Reproducibility of the finite spectrum

From the directory containing `verify_petersen.cpp`, `walsh_histogram.csv`, and `projection_kernel_histogram.csv` run:

```
g++ -std=c++17 -O3 verify_petersen.cpp -o verify_petersen
./verify_petersen
```

The checker uses standard C++17 only and performs exact integer operations. It verifies all 32,768 orientation masks by topological peeling and an independently enumerated 57-cycle criterion; computes every Walsh multiplier by a transform and checks every even-weight frequency by a literal signed sum over all 16,680 acyclic masks; proves the odd-weight zeros by the global-reversal involution; checks the complete signed and projection-kernel CSV histograms; checks Parseval; and verifies all 105 two-edge correlations by line-graph distance.

Expected verification marker:

```
PETERSEN_ACYCLIC_FOURIER_PASS cycles=57 orientations=16680 zeros=19112 rank=13656 pair_shells=30,60,15 abs_kernel=1113888
```

The optimality among arbitrary real or complex projections is an exact translation-averaging argument supplied in `RESULT.md`, not an exhaustive enumeration of projection matrices. Computation is exhaustive for the Petersen graph, not for all graphs. Independent mathematical validation was not performed.
