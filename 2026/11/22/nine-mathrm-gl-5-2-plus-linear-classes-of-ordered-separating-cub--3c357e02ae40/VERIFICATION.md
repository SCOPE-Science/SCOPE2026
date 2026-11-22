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

## Scope of verification
Exact enumeration of every Boolean normal-form coefficient word of degree three in five variables, with all 31 nonzero rows and all ordered pairs checked. All five generators of \(\mathrm{GL}(5,2)\) act on every accepted word; nine disjoint-set components determine the equivalence classification. No stochastic assumptions or untested cases remain within this finite domain.

## Checker reproduction
Use the standalone `check_cubic_orbits.cpp` with an ISO C++17 compiler:

```sh
g++ -std=c++17 -O2 -Wall -Wextra check_cubic_orbits.cpp -o check_cubic_orbits
./check_cubic_orbits
```

Expected success marker: `CUBIC_FIVE_ORBIT_CENSUS_OK`. All counts, orbit representatives, group-generator closure, and known exemplar locations are asserted in the source. Full truth-table witness validation is separately performed for every ordered pair and every one of the nine orbit representatives. The compiler, operating system and numeric architecture are not being used as a source of randomness; 32-bit unsigned arithmetic is exact here.

## Unproved or independent matters
There is no independently completed mathematical audit. No claim is made for polynomials with more variables, for general affine-input equivalence, or for ungraded twisted-algebra isomorphism. Priority with respect to inaccessible or unindexed literature remains a risk.
