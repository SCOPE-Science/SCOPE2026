---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The Gaussian Fourier identity gives F(x)=exp(-x²/2)(2 exp(-s/2)cosh(sqrt s x)-a), I=F². For x>0, F’=x exp(-x²/2)[a-H_s(x)] and H_s(0)=A(s). The entire expansion H_s/(2c)=1-s+Σ_(k>=1)(1-s/(2k+1)) (s x²)^k/(2k)! has coefficients with at most one negative-to-positive switch; after dividing H_s-a by the first positive monomial, the nonzero negative-degree terms and positive-degree terms have strictly positive derivative, forcing one positive root iff a>A(s). F is positive at this strict side maximum since it decays to zero from above. Comparing F(0)=B(s)-a yields exactly one center, two sides, or center+two sides; the boundary at a=A(s) is a quartically flat strict central maximum, while at a=B(s) the center is a fourth-order *minimum* of intensity. Expansion at s0 yields x_*²=3(s-s0)/s0+O((s-s0)^2), and at s1 yields I(0)=a²(s-s1)^2/4+O((s-s1)^3). Independently solved H_s(x)=a by bracketing for representative s=.2,.7,1,3 across phases and found exactly the predicted off-center roots; these samples cannot establish continuum claims.

## originality

PASS

Best-of-knowledge PASS after separate formulation/implication comparisons, published-result search, and bounded primary-literature inspection; not a certification of absolute historical priority. The elementary Gaussian transform is known; exhaustive all-x modal classification and sharp square-root/quadratic onset laws are new claims of this package not directly implied by identified prior statements.

## value

PASS

Coherent signed three-Gaussian spectroscopy has two mathematically distinct transitions: symmetry-breaking side-peak bifurcation followed by emergence of a central peak from a fourth-order spectral null. Exact global mode count, unique side maxima, and onset laws give a motivated nonlinear measurement invariant; the difference from a mere two-tone Rayleigh criterion is substantial despite being a restricted slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
