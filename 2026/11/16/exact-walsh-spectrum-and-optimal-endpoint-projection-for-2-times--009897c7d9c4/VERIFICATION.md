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

# Verification of boxed-plane-partition Fourier census

Compile and run `check.cpp` from a writable directory with a C++17 compiler, using `c++ -O3 -std=c++17 check.cpp -o check && ./check`. It regenerates the two output CSV files; compare them to the packaged `spectrum.csv` and `projection_kernel.csv` or rerun in a fresh directory containing packaged CSV files and compare file hashes.

The checker verifies 490 ideal incidence masks using both a six-entry height-array recursion and a breadth-first addition of admissible cubes; both complete enumeration sets are identical. It verifies all 16,777,216 Fourier multipliers by two exact Hadamard butterfly orders, 8,192 defining character sums, and both Parseval identities. It verifies every coefficient of the support transform with two independent butterfly orders and its exact absolute sum 11,078,918,348. Its final marker is `BOXED_PLANE_PARTITION_234_WALSH_PASS count=490 frequencies=16777216 zeros=1234934 rank=15542282 signed_levels=442 smallest=2 largest=490 projection=2769729587/4194304`.

The signed histogram and support-transform histogram are complete finite certificates, not sampled approximations. The proof of unrestricted projection minimality is analytic, not inferred from checking invariant competitors. There is no claim of independent external audit or a theorem for larger boxes.
