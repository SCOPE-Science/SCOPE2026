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

## Reproduction

A standalone C++17 source file `check.cpp` is included. Compile and execute it from the package directory:

```sh
g++ -std=c++17 -O3 -Wall -Wextra check.cpp -o check
./check
```

The recorded run is in `check_output.txt`; each case prints `PASS`. The program calculates commutators by ring operations, enumerates every matrix over the coefficient rings, and independently tallies each centralizer's cardinality. It tests the split characteristic-two dual numbers (256 matrices), the split nonprincipal square-zero ring on two generators (4096 matrices; 16,777,216 ordered matrix pairs), and the mixed-characteristic ring of integers modulo four (256 matrices). All three exact spectra and aggregate pair counts agreed with the theorem.

## Scope of verification

These experiments cannot prove results for arbitrary residue field size or embedding dimension. The mathematical proof in `RESULT.md` establishes the general case by classifying the intersections of residue-field commutants and counting commuting lifts without a coefficient-field embedding. The principal cases are boundary consistency checks, not part of the novelty claim. The calculations do not constitute independent mathematical validation.
