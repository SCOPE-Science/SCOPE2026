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

# Reproducible mathematical checks

Run `python verify.py` in a Python environment with `networkx` installed. The exact expected output is `verify_output.txt` and terminates with `ALL_VERIFY_OK`.

The program directly enumerates all maximal intersecting families in five small Kneser graphs, compares their EKR equality cases, and checks the complete nonempty facet-intersection nerve in each tested strict case. It also explicitly builds the signed permutation of complementary pairs for each integer `k` from 2 to 9, comparing the resulting determinant to the closed binomial criterion. Six additional parameter pairs check the exterior-power representation against the signed simplicial Lefschetz character on every conjugacy class of their symmetric groups.

The general conclusions for all allowed integers depend on the published Erdős–Ko–Rado maximum-family theorem, contractible-intersection nerve lemma, equivariant integral simplex cover chain maps, and the two-adic valuation argument in `RESULT.md`. The finite computations are consistency checks, not proofs for unbounded parameter ranges.
