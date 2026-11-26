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

On the common test core the compositions give the positive kernel (y^beta-x^beta)(x-y)^(alpha-1)/Gamma(alpha) on y<x. Squaring and putting y=xz gives x^(2(alpha+beta)-1) times the z integral; its endpoints have orders z^(2beta) and (1-z)^(2alpha). This yields the supercritical Hilbert–Schmidt norm and density gives uniqueness. Below the line, unit-norm dilations supported in a scaled compact subinterval have output norm on a scaled interval to their right bounded below by c epsilon^(alpha+beta), so there is no bounded extension. At alpha+beta=0 the logarithmic unitary conjugates the kernel to the positive right-translation average with density h(s)=(exp(alpha s)-1)exp(-s/2)(1-exp(-s))^(alpha-1)/Gamma(alpha). Its finite mass bounds the norm; normalized long plateaus asymptotically realize the mass by restricting the s integration to [0,R] and then sending the plateau length and R to infinity in that order. Translating the plateaus away from zero makes them weakly null without losing this lower bound, proving essential norm equality. For any nonzero g the translation norm decreases on a positive-measure set of s because of lost mass on [0,s], proving nonattainment under the strictly positive density. Substitution z=exp(-s) evaluates the mass as the stated positive difference of beta integrals divided by Gamma(alpha). Finally, with j(z)=(z^(-alpha)-1)^2(1-z)^(2alpha-2), the exact truncated energy is Gamma(alpha)^(-2) times the integral from epsilon to 1 of j(z) log(z/epsilon). Both j and |log z|j are integrable, giving the stated cutoff coefficient and bounded remainder. The same coefficient arises by dominated convergence of the Hilbert–Schmidt numerator as beta tends to -alpha from above.

## originality

PASS

After comparing ordinary and weighted fractional integrals, power commutators and fractional Volterra boundary laws, the supported distinct claim is the concrete singular-power commutator trichotomy with exact operator and essential norms on the critical line and the common Hilbert–Schmidt coefficient. The tools of one-sided convolution, homogeneity, and beta integration are not claimed as new. Older weighted commutator literature is materially relevant but no verified coverage of this exact bundle was found; the named access limitations remain.

## value

PASS

The singular power multiplier creates a natural homogeneity boundary where compactness disappears but boundedness survives. The simultaneous sharp norm, nonattainment, and agreement of the energy divergence under parameter approach and spatial cutoff give quantitative information that a weighted boundedness estimate alone would miss. The proof explains the agreement through the same remaining ratio integral, rather than through unrelated numerical fits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
