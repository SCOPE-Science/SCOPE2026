---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Independently derive the bin formula with the circle automorphism g(z)=(z−ρ)/(1−ρz): its boundary argument derivative is the Poisson kernel, and for z_±=exp(i(θ±h)) the quotient g(z_+)/g(z_−) is (a−b cos θ+ic) divided by its conjugate. The bin arc has image argument increment in (0,2π), and c>0, fixing that increment to twice the argument in (0,π). With y=(a−bx)/c and t=arccot y, the second derivative of the reciprocal mass is 2π(b/c)²(1−yt)/[(1+y²)²t³]. This is strictly positive at ρ>0 since yt≤0 for y≤0 and arctan(1/y)<1/y otherwise. At m≥4 there are three distinct cosine nodes; strict convexity proves the positive adjacent secant contrast, while the registered sampled model has affine reciprocal probabilities. A positive-ρ integrated law is nonuniform since its bin formula is strictly increasing in cos θ. If an arbitrary sampled phase matches it, the two reflected off-center sites force sin ν=0 at nonzero concentration. The reciprocal probabilities are affine again, excluding equality. At m=2,3 all noncentral probabilities agree within each registered vector, and both central probabilities vary continuously and strictly over [1/m,1), proving exact coincidence and unique refitting. Uniform belongs to both. For fixed positive cell probabilities the empirical contrast is a smooth function of empirical frequencies near the true vector. The n^−1/3 threshold dominates n^−1/2 null fluctuations and tends to zero below every fixed positive alternative contrast; vanishing empirical cells have probability tending to zero. This test is for registered sampled laws, not for unrestricted phase. Replay: frozen RESULT.md eqs. (1)–(5) and Steps 4–6, with VERIFICATION.md and check.py inspected, not executed. Independent Simpson quadrature with 2048 panels per bin for m=4, ρ=1/2 gives p≈(0.5686116674,0.1720208696,0.0873465934,0.1720208696) and K_4≈1.5808166313. The all-parameter proof is analytical; neither off-center integrated parents nor uniform power against concentrations tending to zero is asserted.

## originality

PASS

Best of current knowledge, the distinct contribution is fixed-resolution equality or disjointness of the refitted wrapped Cauchy families under the specified centered-bin model, including separation under sampled phase refitting for m≥4 and the contrast. The definitions, wrapped Cauchy integrals, and normalized sampled pmfs are prior material.

## value

PASS

The exact cutoff resolves a natural population identifiability question for two widely applicable constructions: indistinguishability is absolute at low resolution because the refitted model families coincide, while above it the centered-bin population law cannot be imitated by refitting either concentration or sampled location. The explicit computable contrast supplies pointwise consistent discrimination for the registered models. An equal-concentration comparison would not give these conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
