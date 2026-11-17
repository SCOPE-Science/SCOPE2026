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

# Reproducibility and evidence

`check_angles.py` is a standalone Python 3 checker requiring only its standard library. Running `python3 check_angles.py` reconstructs the original stack-sorting process independently of the analytic formulas, checks the exact permutation-coordinate orbit and its pairwise Gram matrix for every size \(3\le n\le60\), reconstructs all \(n\) facet normals as rational coordinate vectors, and examines the entire finite set of facet pairs. It then tests the predicted finite-size conditional distribution and moment scales at \(n=100,1000,10000\).

Expected and observed output:

`STACK_SORT_RARE_ANGLES_PASS n=3..60 orbit_vertices=1827 facet_pairs=35989 asymptotics=100,1000,10000`

These are exact finite checks for the listed dimensions and floating-point corroboration of selected asymptotics, not exhaustive certification of all dimensions or the limiting distribution. The analytical proof in `RESULT.md` establishes the infinite statement using the facet-normal identities, convergence of uniform indices and dominated convergence for series. An independent mathematical audit has not been performed.
