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

# Exact finite verification

The proof reduces zero-field energies to the independent local nonmonochromatic triangle constraints and proves the field thresholds analytically from the four possible triangle energies. Two distinct self-contained C++17 programs then compute and check the entire zero-field ground-state polynomial, using (i) direct finite depth-first search with local pruning on the generated generalized Petersen graph and (ii) inclusion-exclusion over all \(2^{20}\) vertices and equality-component polynomials on an alternative dodecahedral labeling. The latter also counts every matching at saturation and checks an explicit isomorphism of the two graph labelings.

On a standard C++17 implementation, compile the bundled `verify_dfs.cpp` and `verify_inclusion_exclusion.cpp` with `-O2 -std=c++17`, run them, and require both processes to return zero. The programs check each of the 31 zero-field coefficients and the 11 matching coefficients against the explicit claim, not solely an aggregate number. Expected terminal markers are `VERIFY_DFS_OK` and `VERIFY_IE_OK`; no external tables, third-party libraries, random sampling or external runtime state is required.

This finite exhaustive verification has no bearing on a thermodynamic limit or on historical uniqueness. Model assumptions, exact coefficients and possible priority overlap are discussed in `RESULT.md` and `REVIEW.md`. Independent external scientific validation has not been performed.
