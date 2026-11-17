---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For characteristic p>3, equal first three power sums of ordered triples imply equality of their elementary symmetric polynomials by Newton identities, hence equality of their multisets. Character orthogonality with normalized curve measure and unnormalized counting target makes ||Ef||_6^6=N^3 F3(theta), where F3=6-9s2+4s3. Algebra yields A_q-F3=(5-4/q)(s2-1/q)+(4/q)[(q-2)e2-3q e3]. The normalized Newton inequality e3<=2(q-2)e2^2/(3(q-1)), combined with e2<=(q-1)/(2q), makes the extra bracket nonnegative; equality only for a point mass or uniform theta. A point mass gives the exact quotient 5-4/q, proving global optimality, not just local curvature. Inspected actual CHECK.py; independently checked exact rational boundary ratios for q=5,7,11. A finite grid does not prove the unrestricted finite-field theorem.

## originality

PASS

Best-of-knowledge matching theorem search found no logically dominating already published result after comparing actual statements; relevant uninspected primary literature and older methods are recorded as residual risks.

## value

PASS

This exact sharp stability coefficient for the first nonlinear permutation-expectation degree is a natural quantitative enhancement of the endpoint extension inequality. The global best coefficient 5-4/q is strictly stronger than the published degree-three general 3 and distinct from the near-uniform local curvature 9-12/q; the two equality strata illuminate boundary rigidity. Applies to all finite field extensions of characteristic greater than three.

The dated certificate retains the supplied scientific assessment, sources and limitations.
