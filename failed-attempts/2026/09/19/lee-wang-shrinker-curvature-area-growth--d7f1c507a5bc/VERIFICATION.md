---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Starting from the frozen parametrization, the standard normalization and Lee--Wang metric give the stated conformal factor. The formula K=-(2E)^{-1}(log E)'' yields the displayed strictly negative curvature; the t=tanh(mu) substitution makes the total-curvature integrand an exact derivative and gives -4 pi sqrt(pq). The radius identity cuts centered balls into |mu|<=a and direct integration of the known area form gives the exact area formula. Differentiating the exact ratio simplifies, using s^2-d^2=4pq, to the stated sign factor 2P-ds a sinh(2a), proving a unique maximum; the density crossing similarly reduces to a strictly increasing scalar expression. Independent numerical solution reproduces a_*=0.7000655576, R_*=1.6512789741, peak 1.8448061591, and the crossing constants for the (2,1) quotient. The deck-transformation metric bound proves the 2 pi systole.

## originality

FAIL

Lee--Wang already give the explicit immersion, induced metric, area form and self-similar normalization for the full (p,q) family. The audited Gaussian curvature, total curvature, centered ball area, ratio derivative and asymptotic expansion are elementary deterministic consequences of those formulas by the standard conformal-curvature identity, one-dimensional integration and Taylor expansion. Braxton--Lee--Zhu identify the (2,1) quotient as the stable Möbius shrinker. Under the requested implication bar, absence of the final closed forms from the source text is not enough: the main package is mechanically implied by the prior explicit geometry.

## value

FAIL

The recent stability result gives genuine motivation for understanding the Möbius shrinker, but the audited contribution is primarily a sequence of routine invariant calculations from a long-known explicit metric and parametrization. The requested value bar for a narrow invariant requires that the answer not already be known or mechanically implied. Here curvature, centered area, scalar extrema and the systolic lower bound all follow by standard one-variable calculus, so correctness and reproducibility do not by themselves establish research value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
