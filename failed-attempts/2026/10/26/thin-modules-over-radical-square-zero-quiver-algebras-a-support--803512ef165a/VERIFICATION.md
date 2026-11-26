---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In dimension vector one, a length-two path acts by a product of two field scalars. Thus feasible supports consist exactly of noncomposable arrows, with a loop tested against itself. On each such support, choose a spanning tree of each undirected component, and scale vertices recursively to make the tree labels one. The residual scalings are constant on components and hence fix all other labels, even parallel edges. The freely variable off-tree labels give precisely (q−1) raised to e−v+c distinct orbits. For an endomorphism the scalar equation across each active arrow imposes equality, with no condition from zero arrows. This yields one field factor per component, including isolated vertices; the product has nontrivial idempotents exactly when the nonzero module decomposes into more than one component. The empty quiver contributes just the zero module to the constant coefficient. This is an all-fields orbit argument, not a deduction from the bundled small cases.

## originality

FAIL

A distinct indexed result supplies exactly the support-by-support torus orbit formula with stabilizer and rank grading for the same arrow coordinates, for all quivers including loops and parallel arrows. In its scalar-diagonal sector the entire arrow space survives; restricting those orbits to the supports with no composable pair and replacing r by v−c gives this enumerator immediately. The additive endomorphism algebra is the same endpoint equality system over the entire field instead of its unit group. This is demonstrable corollary-level coverage, not an assertion of publication priority within the shared catalog date.

## value

FAIL

The endomorphism statistic is natural, but it is the same component count already controlling the known torus stabilizer. The additional radical-square-zero condition merely selects supports by the field-scalar zero-product check. The claimed result adds no independent counting mechanism, unexplained boundary or new orbit invariant beyond this direct support restriction and regrading. Its usefulness as an explicit formula does not justify a separate research finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
