---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

On the leaf-sum-zero space the eigenvalue is L=1+b; the hub and leaf-mean block has determinant d−ma² at unit scaling, giving exactly the claimed SPD domain under the assumed positive couplings. To compare arbitrary positive diagonal scalings, normalize a candidate by its minimum eigenvalue μ and set E=μS⁻². Then E≼A≼KE, and averaging the diagonal E over the leaf permutations preserves both inequalities and gives an exchangeable scale with condition no worse. At hub scale √u the two plane eigenvalues have trace u+d and product u(d−ma²). The plane eigenvalue ratio is minimized uniquely at u=d because u/(u+d)² is maximized there. Both plane eigenvalues increase strictly with u: the discriminant is (u−d+2ma²)²+4ma²(d−ma²). The lower plane eigenvalue is less than d<L. If the upper plane eigenvalue at d reaches L, the plane ratio already gives the global minimum. Otherwise the objective decreases strictly up to the crossing (L−u)(L−d)=ma²u and then increases strictly. This gives u=b(1+b)/(b+a²)>d, with lower eigenvalue u−mb. The crossover condition is a²d=mb², with matching branch values and top multiplicity m there. Strict upper-branch feasibility is b<1/(2m−1); the unique normalized exchangeable scale equals the Jacobi scale precisely at a=b. The six-dimensional example follows by trace and determinant. The frozen finite checks are supplementary and were not executed.

## originality

FAIL

A distinct indexed one-hub equicorrelation theorem, 2a376f6167cd, explicitly covers the entire assigned parameter domain with the same optimizer, branch condition, minimum and Jacobi characterization, and additionally proves unrestricted uniqueness up to scalar. This is verified mathematical coverage by an extant record, not evidence that the broader record had chronological priority over the frozen one. The catalogued dates put the broader record later. No separate distinct contribution is established by the frozen example or the direct large-dimension substitution.

## value

PASS

The exact classification is mathematically useful: it solves a continuous optimization over arbitrary positive diagonal scalings of a natural coupled matrix family and identifies when a different eigenspace limits the condition number and when Jacobi loses optimality. Those are useful properties of the theorem itself, not evidence of additional content beyond the covering catalogue result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
