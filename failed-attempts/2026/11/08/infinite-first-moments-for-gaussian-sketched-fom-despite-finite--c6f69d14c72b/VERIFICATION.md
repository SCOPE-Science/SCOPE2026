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

Decompose Ab=alpha b+beta v with v a unit vector perpendicular to b. For white Gaussian sketches, X=Sb and Y=Sv are independent standard Gaussian vectors. Conditional on X, X·Y/||X|| is a standard normal with distribution independent of X, so H=1/c_F is alpha+beta times an independent normal/chi ratio. Its continuous density is positive at zero, giving almost sure well-definedness, the reciprocal tail 2f_H(0)/t and the exact p<1 criterion. Gaussian regression of X on W=SAb leaves an independent isotropic Gaussian with coordinate variance beta^2/gamma^2, yielding the shifted scaled Student law for c_G and p<s. These are marginal laws, not independence assertions. Norms of c times a fixed nonzero vector plus a fixed vector are comparable to |c| outside a bounded interval, so approximation, error and true residual have the same thresholds. The beta law for the ratio of independent chi-squares gives the sign probability; integrating h^{-1} on the positive side shows that dropping negative Ritz values leaves divergence. For s>2, E[1/chi_s^2]=1/(s-2); completing the true residual square gives equation (5). The separately computed s=3 example gives sign probability 0.0202596632, tail 4/(25*pi), and expected squared GMRES residual 0.4 versus optimum 0.2. Independent quadrature and a 20,000-draw direct-sketch check corroborated these finite formulas; finite random samples do not test moment divergence. I read the original proof, verification notes, code, requirements and recorded output without executing uploaded code. This check applies to the fixed finite-s, one-step, unconditioned exact-arithmetic Gaussian model with beta>0; the eigenvector boundary is exact for both solvers.

## originality

FAIL

The earlier indexed one-step result gives the same two marginal laws, sharp FOM tail constant and GMRES variance and expected residual, under at least the same hypotheses. Its full distributions already determine all the claimed moments, sign probabilities and the example. No new central law remains after crediting that exact coverage.

## value

FAIL

The infinite-risk contrast is mathematically useful, but it is already covered in this model. The residual contributions are a standard Student CDF conversion, one-sided restriction of the same pole integral, and numerical substitution. They do not establish an independently valuable new result as presented.

The dated certificate retains the supplied scientific assessment, sources and limitations.
