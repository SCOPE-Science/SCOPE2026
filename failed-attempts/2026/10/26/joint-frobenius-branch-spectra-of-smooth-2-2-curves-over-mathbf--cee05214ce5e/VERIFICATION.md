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

In characteristic three a squarefree homogeneous discriminant rules out a fiber with all coefficients zero, and hence gives a finite quadratic cover. In a chart with unit quadratic coefficient near a ramified point the equation has the local form u²=h, and the simple zero of h gives smoothness. Away from these zeros the cover is étale. Conversely the smooth (2,2) divisor has both projections finite separable of degree two and simple branching, so both discriminants are squarefree. An independent standard-library replay exhausted the 9,841 projective coefficient vectors, tested both discriminants including infinity, recovered cycle degrees from projective root counts over extensions of degrees 1 to 4, and partitioned all forms under the full 1,152-element group including the swap. It found 41 total orbits, 14 smooth orbits and 5,184 smooth forms. In the six rows of the Finding it obtained form counts 144,432,1728,2304,144,432 and orbit counts 1,2,4,4,1,2, and the stated rational-point frequencies. The extension root counts are used only after the geometric squarefreeness test; they are sufficient to recover every degree of a squarefree quartic.

## originality

FAIL

The earlier ternary atlas already supplies the identical 14 fully specified smooth polarized models and their orbit weights. It does not print the full Frobenius partitions, and rational branch counts alone are not enough when a divisor has no rational point. But evaluating the two branch quartics on the earlier atlas's exact coefficient masks recovers every asserted bin without a new classification or census. I performed this direct extraction on all 14 prior rows; their masks and sizes also agree exactly with the frozen representative CSV.

## value

FAIL

The Frobenius types are natural invariants and the counts are correct. However, for this fixed field and population the classification is already tabulated down to the same weighted representatives. Applying a known quartic test twice per earlier representative and grouping the resulting labels is routine table extraction. There is no surviving new classification or independently uncovered structural assertion at the stated scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
