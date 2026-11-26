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

At fixed α<π only the two ordered pole pairs attain the diameter. The horizontal endpoint coordinates at those poles lie in the same planar wedge. The bisector bounds their sum in norm below by cos(α/2) times the sum of their lengths, so both are O_α(ε). The vertical chord component is quadratic and geodesic versus chord conversion is cubic; hence after scaling the test differs from |U+V|<1 by an O_α(ε²) shell. Homogeneity gives an O_α(ε²) four-volume change and the two area densities introduce the same order of relative error. For a sum w=ρ(cos φ,sin φ), its two wedge coefficients are ρ sin(α−φ)/sin α and ρ sin φ/sin α. The convolution fiber has area equal to their product times sin α. Integrating over 0<ρ<1 and 0<φ<α gives (1−α cot α)/8. Two ordered assignments divided by (2α)² give C and the O_α(ε⁶) error; the scaled-domain convergence also gives the conditional law and equal order weights. The differentiated sine product gives the positive increasing summand representation for C and its two limits. For the moving opening, set δ=λε and replace Y by Z=−Y. Use coordinates (sin s cos u,sin u,cos s cos u) about the limiting great circle y=0. At longitude parameter s the lower latitude of X is max(0,arctan(−tan δ sin s)); at parameter s′ the lower value of −u for Z is max(0,arctan(tan δ sin s′)). An ε-close pair has both latitude magnitudes ≤ε and |s′−s|=O(ε) locally on the circle. In scaled variables A=u_X/ε, B=−u_Z/ε, h=(s′−s)/ε, the limiting ball condition is h²+(A+B)²<1 with lower limits (−λ sin s)_+ and (λ sin s)_+. This yields a transverse gap λ|sin s|, integration over h,A,B gives J, and the two semicircles and area normalization give the stated 1/(2π²). The same bounded-domain dominated convergence applies along any sequence λ_ε→λ, since the equality boundaries have measure zero, proving compact uniformity by subsequence. J(0)=2/3; strict decrease follows on a positive-length neighborhood of the poles for every finite pair of distinct λ, and ∫₀¹J(t)dt=π/16 gives the large-λ constant via t=λ sin s. This independently checks RESULT.md lines 50–127. The supplementary verification/check_lune.py was inspected, not run; the reported 20 finite checks do not establish the limiting quantifiers.

## originality

PASS

Credit both the exact same-family moment and ordering analyses and the hemispherical/cap tail methods, including the hemisphere endpoint obtainable from the cap-containment formula. The supported distinct claim is the explicit fixed-lune coefficient with its conditional endpoint law and the compact-uniform lune-specific antipodal crossover through angular defects of order ε. The inspected results do not provide that combination of two-point law and varying longitude wedge. The check is not an exhaustive priority determination.

## value

PASS

A natural distance statistic behaves differently when the set of antipodal pairs expands from two ordered pole pairs to a boundary circle. The exact tail gives a shape identifier for each fixed opening, and the moving-boundary profile measures how the power changes and matches its two end regimes. This resolves a genuine singular limit that a fixed-opening calculation or an exact hemisphere value alone cannot answer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
