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

# Exact integer verification

The supplied C++17 `check.cpp` is self-contained. It enumerates every legal four-height configuration independently from a predecessor-closure BFS, verifies matching sets of 336 distinct masks, computes all 2,324 degree-one/two/three signed character sums and checks the 32 cubic zeros against 8 orbit representatives and their symmetry images. It performs a full 24-stage integer Hadamard transform on the 16,777,216 element cube, compares 8,192 transformed coefficients with direct sums, and checks inversion and Parseval identities. It reuses the same exact butterflies on the nonzero frequency indicator to check the full projection norm, and transforms all smaller widths one through five to verify the stated first-occurrence cutoff.

Execution performed with the command:

```sh
c++ -std=c++17 -O3 check.cpp -o check
./check
```

Observed output:

```text
BOX_226_WALSH_PASS ideals=336 zeros=1414094 rank=15363122 minwt=3 triples=32 minnonzero=2 max=336 projection_sum=9182696964 projection_ratio=2295674241/4194304
```

An independently written array-based calculation using height-array incidence and vectorized Walsh butterflies reproduced the zero count, spectral gap, zero-weight histogram and projection absolute sum. The infinite-dimensional operator theory used for optimality is the standard finite translation-averaging lemma, proved directly in the report. Exactness is limited to the specified finite cube; no empirical extrapolation is used. No independent mathematical audit has been performed.
