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

The original asserts that the full three-cell graph is primitive, which is false: J₀ has no incoming edges from J₁ or J₂; the closed two-cell class is primitive. The repair proves uniqueness among all absolutely continuous invariant probabilities, not just cell-constant ones: refine by itineraries through k, so every positive-length atom maps affinely onto a full cell and the mesh is at most max(b,1/(1+b))^k. Conditional averaging on the atoms converges in L1. At time k the averaged density is cell-constant; the three distinct eigenvalues 1, b, −b/(1+b), together with mass preservation, force its future iterates to the normalized stationary vector. L1 contraction then gives convergence for any absolutely continuous probability and hence uniqueness. The inverse branches produce the stated matrix in density-value, not mass coordinates. The fixed vector and displayed two decaying eigenvectors and coefficients yield J₀ deviation b^n, J₂ strictly negative because the relative oscillatory correction is bounded by (1−b)/((1+2b)(1+b)), and the stated signed J₁ deviation. Half-L1 is exactly the sum of positive masses, including b^(n+2) on J₀; the 1-Lipschitz positive part gives the stated error even at γ. The difference of the two branches of C is b(1−b−b²)/(b+2), whose derivative at γ is strictly negative, proving the corner. I independently checked 60 exact rational inverse-branch iterations, not a formal or exhaustive proof; the frozen checker was inspected, not executed.

## originality

PASS

Only the parameter-specific exact whole-interval TV law and its sharp sign-driven prefactor transition are credited. The closest distinct relaxation theorem is exactly related by conjugacy on the closed class at b=γ, but neither includes the transient contribution from full-interval initial volume nor varies the parameter to give the corner. The repair defines the branches directly and removes the unconfirmed blanket statement about what the inaccessible origin paper does not derive.

## value

PASS

The parameter curve comes from a natural critical-orbit closure b→1→b²→b. The exact total-variation error answers a quantitative startup convergence question and identifies which spatial regions determine it. Showing a nonsmooth prefactor when the decay eigenvalue itself is smooth is a meaningful structural feature of using the full Lebesgue initial law, rather than a spectral renaming or a numerical golden-ratio coincidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
