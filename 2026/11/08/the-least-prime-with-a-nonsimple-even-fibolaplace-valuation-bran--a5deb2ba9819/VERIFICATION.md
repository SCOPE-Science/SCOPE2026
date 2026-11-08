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

# Reproducible arithmetic checks

Compile `scripts/census.cpp` with `g++ -O2 -std=c++17 -Wall -Wextra` and execute. It enumerates exactly 163 odd primes through 971 by Eratosthenes sieve, then every nonzero residue for each prime; its product, first-derivative and second-derivative recurrences use integer modular arithmetic only. Expected output is embedded in `CHECK_OUTPUT.txt`.

Execute `python3 scripts/independent_census.py --table data/reproduced_roots.csv`. This uses a separate logarithmic-derivative formula in a half-domain and restores the other half by reflection symmetry. Compare its generated CSV byte-for-byte with `data/roots_by_prime.csv`. It must report 144 roots, 142 below 971, and exactly the two multiple roots at 971.

C++ additionally evaluates the defining FiboLaplace sequence recurrence modulo the square of 971 through index 1554, obtaining 473848 and 468993 at the two roots and proving the initial valuation is exactly one.

Finite enumeration establishes the least-prime claim only because its loops cover all primes and nonzero field elements in the finite range. The infinite-depth simplicity for smaller primes follows from the published polynomial lifting criterion, not from finite testing. Independent external mathematical audit has not been performed.
