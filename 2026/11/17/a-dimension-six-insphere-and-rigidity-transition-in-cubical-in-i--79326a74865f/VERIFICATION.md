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

# Verification of the cubical in-in zonotope sphere theorem

`verify.py` runs with Python 3.10 or later and standard-library modules only. Executing `python verify.py` produces the nine dimension rows and ends with `TOTAL_ASSERTIONS= 77255` and `VERIFICATION_PASSED`.

The script exhaustively enumerates all nonempty subsets in dimensions \(1\) through \(4\), checks the exact integer inequality \((|S|+|\partial S|)^2\ge |S|\min\{2^d,(d+1)^2\}\), and checks that equality subsets match the asserted minimum-radius facets. Dimensions \(5\) through \(9\) receive deterministic examples and fixed-seed random samples rather than exhaustive enumeration. The script also constructs the two antipodal outer contacts for each tested dimension and enumerates every endpoint signing of all Minkowski generators in dimensions \(1\) and \(2\).

These finite assertions cannot certify an all-dimensional theorem. The proof in `RESULT.md` instead establishes the facet-normal classification by free-generator rank, the induced-edge bound by induction on cube dimension, the absence of intermediate size minimizers by explicit derivative analysis, all maximal-ball centers through finite facet inequalities, and the outer sphere/diameter classification using connected bipartiteness. No external proof assistant or independent mathematical auditor has examined the result.
