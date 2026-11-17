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

# Verification of the Catalan matroid Hausdorff theorem

The mathematical claim is given in `RESULT.md`. A standalone `check_catalan_distance.py` reproduces finite numerical tests using NumPy and SciPy. Invoke it in the same directory with `python check_catalan_distance.py`.

The program independently generates all \(\binom{2n}{n}\) binary hypersimplex vertices for \(n=2,3,4,5,6\), solves a quadratic program onto the polytope defined by fixed endpoints, sum, box, and ballot-prefix constraints, and compares the resulting distance and maximizer set with the theorem. In total, 1,272 hypersimplex vertices and 195 Dyck vertices are generated over these ranks. It also checks exact normal certificates over all Dyck vertices in these finite ranks, samples interior points of the even-rank maximizer edges, and verifies symbolic candidate normal monotonicity and squared norms for \(n=7,\ldots,40\).

The analytic proof supplies the unrestricted statement for every integer \(n\ge2\); computations check only finitely many cases and the numerical quadratic solutions use finite tolerance. The scientific novelty determination is provisional and no independent audit was performed.
