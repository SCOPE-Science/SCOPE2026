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

The weight-two multiplier is the sum over unordered pairs of frequency-coordinate signs, i.e. ((d−2k)²−d)/2. With the displayed unitary transform, Parseval gives the denominator squared |a|²+binom(d,2)|b|²; the extra 2^(d/2) exactly converts the numerator to a binomial expectation. On the real unit ellipse scaled to a circle, each fixed-sign open arc has a positive linear objective with second angular derivative equal to its negative, so every minimum is on a support-zero line. All support values have positive mass, and d≥2 ensures a genuine circle after scaling. Minkowski on the two nonnegative absolute real-component values proves the same lower bound for complex coefficients. If both components are nonzero, equality requires their absolute-value vectors to lie on one ray a.s.; different minimizing lines have distinct zeros, so are excluded. This proves the equality union without assuming a unique finite minimizing index. For the limit, the bounded fourth moments give uniform integrability of the squares; the numerators are uniformly 1-Lipschitz in the shift. Grid points approach any fixed nonnegative shift, including 0 where the limit ratio is 1/√3. Jensen's uniform tail lower bound approaching 1 then confines all minimizing shifts. In the limit the sign of the derivative in u is the sign of H(√u), with H′(t)=2φ(t)(t²−1)(t²−3), H(0)=−1, and H(√3)≥1−16φ(√3)/√3>0 by the Gaussian tail bound. This proves a single global minimum and convergence of every discrete minimizer. Independent bisection using the integrated power series for the Gaussian density gave t≈0.479855965645869, c≈0.549426226034278 and c²≈0.301869177854270; the proof, not the bisection, establishes uniqueness. RESULT.md lines 45–93 are the replay; the bundled checker was inspected but not run.

## originality

PASS

The supported contribution is the exact lower Fourier ratio and all equality lines on the specified radial two-shell space, together with the uniquely optimized continuous limit. Neither the shared classical Krawtchouk reduction nor the use of a Fourier ratio as effective dimension is claimed as new. The closest available statements address other objectives, not a demonstrated implication for this ratio.

## value

PASS

The origin-plus-second-shell space is the first radial quadratic Walsh family with a tunable constant mode. The theorem gives an exact effective-dimension benchmark on that natural family, rules out improvements from complex phases, and determines the asymptotic choice of the apex for every sequence of optimizers. Neither orthogonality nor Gaussian convergence alone dictates the L¹ optimizer. The number is a Fourier ratio benchmark, not a lower bound on arbitrary sampling or recovery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
