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

# Verification of the triangular fractional-vertex projection

The accompanying `verify_triangle_projection.py` reconstructs the candidate projection as exact rational entries and checks row stochasticity, symmetry, nonnegativity, the distance identities, and the auxiliary matching mixture's marginals for each integer \(1\le r\le25\). It checks the projection supporting-hyperplane inequality via all count combinations compatible with \(I\le r\) and \(F+2(I+C)=3r\). These include all possible involutions and sometimes additional combinatorially unrealizable counts, so no feasible involution is omitted.

The script separately enumerates every involution on \(3,6,9,12\) vertices, checks the scalar-product certificate for each, and verifies a contact witness. The total enumerated is 142852. Three independent numerical quadratic programs, using symmetric row-sum conditions and all odd-set matching inequalities for orders \(3,6,9\), reproduce the rational projection distances and matrices to numerical tolerances.

These experiments are finite. The proof valid for every positive integer \(r\) is the explicit involution mixture and the global supporting-hyperplane inequality in `RESULT.md`. They do not establish historical novelty, a global Hausdorff theorem, or independent verification.
