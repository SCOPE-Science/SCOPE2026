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

# Reproducibility

Use a C++17 compiler and Python 3 standard library:

```sh
g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive
./verify_exhaustive
g++ -O3 -std=c++17 verify_locating.cpp -o verify_locating
./verify_locating
python3 verify_coefficients.py
```

`verify_exhaustive.cpp` evaluates total domination and pairwise open-neighborhood separation directly and compares this against the isolated-vertex/isolated-edge criterion on every subset of each tested board. It checks minimum sizes independently and ends with `EXHAUSTIVE_OK`.

`verify_locating.cpp` tests ordinary locating-domination versus the criterion admitting at most one isolated edge component and ends with `LD_OK`.

`verify_coefficients.py` performs exact integer inclusion–exclusion coefficient evaluation of the all-board EGF, checks full totals and minimum counts on eleven specified boards, verifies the ordinary polynomial difference on nine boards and tests explicit forest constructions. It ends with `COEFFICIENTS_OK`, `LOCATING_DIFFERENCE_OK`, and `FOREST_CENSUS_OK`; the last test independently reconstructs the optimum coefficient by a rooted labelled bipartite-tree recursion.

These are finite sanity and reproducibility checks. The proofs for all rectangular boards are combinatorial and independent of their numerical range. No external mathematical audit has been conducted.
