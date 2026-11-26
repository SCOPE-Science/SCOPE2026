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

The beta integral gives the stated norms with total mass one, and analytic and anti-analytic nonconstant monomials have zero mixed inner product. This yields twice the real part of the binomial kernel minus one, on its disk branch. For s=r exp(iθ), differentiation gives the negative sine in RESULT.md lines 44–52. The argument ψ is strictly concave on (0,π); its tangent at zero bounds it by r(π−θ)/(1+r), putting the sine argument strictly between 0 and π when βr≤1. This verifies the unique angular minimum at the antipode. Strict convexity gives β(2^(1/β)−1)<1 for β>1, and the antipodal value crosses zero exactly at that radius. Above it and below 1/β the opposite endpoint signs and strict monotonicity give exactly one zero on each semicircle; these are scalar products, not isolated points in the bidisk. At the first zero the radial derivative is −β/(1+ρ) and the coefficient of the squared angular displacement is βρ(1−βρ)/(2(1+ρ)^2). Even real analyticity and the implicit function theorem in the squared displacement yield the given coefficient and O((r−ρ)^(3/2)) remainder. For 0<β≤1 the same circle estimate gives strict positivity for every r<1, in the coefficient-defined continuation only. CHECKER.py was inspected, not run; its finite diagnostics are not used to justify these continuous statements.

## originality

PASS

Pass for the joint sharp disk threshold, circle-wise two-zero regime and explicit angular onset, to the best of the available evidence. The kernel representation is background, and neither a general novelty claim about harmonic Bergman zeros nor a priority claim for the coefficient-defined continuation in isolation is warranted.

## value

PASS

This answers a natural kernel-geometric question for the whole integrable planar weight family. Resolving whether the first antipodal zero is truly the first anywhere, and tracking the number and angle of the nearby zero products, gives more than a real-axis substitution or an existence example. The radius and angular scale are useful quantitative invariants even without a complete outer-radius census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
