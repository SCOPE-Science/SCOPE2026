---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Writing X_i=u_i^p, h=1−f and f=θ∏(1−X_i), each mixed derivative acts by (1+D_i) with D_i=pX_i∂_i. For distinct i the product rule gives the numerator over h⁴: h³ plus h² times the sum of all nonempty distinct-index derivatives of f, plus 2h times the pair products of single derivatives and the three single-times-complementary-double derivative products, plus 6 times the product of the three singles. Each factor is multilinear spatially and linear in θ, so all three spatial degrees and the θ-degree are at most three. Independently confirmed the four corner identities and converted exact values at the tensor nodes {0,1/3,2/3,1} to Bernstein coefficients by inverting the evaluation matrix (not the supplied monomial-coefficient transform). With q=1+r, the two admissible interval parametrizations have p=1/q, θ=−q²+s(1+q²) and p=q, θ=(−q+s(q+1))/q³. Clearing denominators by q³ and q⁹ respectively gives polynomials in r with nonnegative coefficients for all 80 independent Bernstein indices in each regime. This establishes the continuum sign exactly. A pole at an interior diagonal point rules out θ>1, and the corner limits at (1,1,0) and (1,1,1) rule out θ<−p⁻² and θ>p⁻³ by negative interior mixed density. In range h>0 in the interior; if θ=1, p≤1 and h≥max(u,v,w), so C≤min(u,v,w) and the origin extends continuously. Nonnegative interior mixed density gives nonnegative box volumes up to the boundary by continuity. Grounding and product bivariate margins are explicit; at nonzero θ any interior value differs from the product of all three coordinates.

## originality

PASS

The distinctive supported claim is the exact power-dependent all-p frontier for the specified pure three-way ratio, not priority for the unpowered p=1 expression or for pairwise independence with joint dependence. The p=1 expression is explicitly acknowledged as prior in the original. The strongest available comparators do not give the all-p theorem; inability to identify the unnamed unpowered source and inspect some primary full texts limits the historical conclusion.

## value

PASS

The model isolates three-way dependence while fixing all pair marginals at independence. The exact interval is consequential for using the model: parameters outside it cause a pole or a negative local probability, despite the apparently valid product margins. The asymmetric negative and positive frontiers and the upper-bound transition at p=1 are not a reparameterization of the p=1 result. The certificate gives a usable exact test for tuning the power and interaction jointly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
