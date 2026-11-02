---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

From xdot=x(1-x)-sqrt(x)y, ydot=(c sqrt(x)-s)y, the coexistence point (u²,u(1-u²)) differentiates to A=[[-z,-b],[d,0]], valid for c>0 and 0<u<1. Independent-coordinate multiplicative Itô noises yield K=[[-δ,-2b,0],[d,-z,-b],[0,2d,Q]], δ=2z-P. Direct symbolic reconstruction confirms char_K(λ)=λ³+(z+δ-Q)λ²+(4bd+zδ-(z+δ)Q)λ+[2bdδ-Q(2bd+zδ)]. Mean-square exponential decay forces A Hurwitz and z>0. Existence of positive stochastic Lyapunov H normalized by h11>0 gives δ-2dη>0, 2bη-Qζ>0, dζ=b+zη, hence 0<η<δ/(2d), η>Qb/(2bd-Qz), forcing δ>0 and Q(2bd+zδ)<2bdδ. Conversely these strict inequalities give nonempty η interval; H=[[1,η],[η,(b+zη)/d]] has det=b/d+η(z/d-η)>0 because 0<η<δ/(2d)<=z/d, and stochastic generator is strictly negative diagonal. This proves all parameter quantifiers and excludes δ=0 and Q-frontier equality; P*=2z, Q*=2bdz/(bd+z²)<P*. An independently written SymPy/NumPy verifier checks all symbolic identities, 8,800 randomized positive-region/boundary/outside configurations and 100 deterministically unstable cases. Numerical tests corroborate, never substitute for proof.

## originality

FAIL

FAIL: prior source Tan–Wang–Feng (2022) constructs the exact mean-square spectral matrix for this identical square-root coexistence/noise setting and interprets the sign of its spectral abscissa as the stability decision. Applied to the same A and Bi, this yields the three-moment K and determines the full region for arbitrary nonnegative P,Q. The submitted rational frontier is an equivalent elementary Hurwitz/Lyapunov elimination of that already complete stability criterion, rather than a new scientific statement not covered by prior work. The reported predator-versus-prey ordering specializes the original source's same sensitivity analysis. Generic Buckwar–Kelly methodology alone was NOT treated as automatic novelty defeat; it is the same mathematical model prior spectral representation that decides coverage. The middle section of the 2022 HTML could not be read end-to-end due throttling; section-number and matrix-specific provenance are therefore limited to retrieved parts; this is a residual source-verification limitation, not an invented full-text inspection.

## value

PASS

The exact simultaneous prey/predator noise stability set is a natural biologically motivated invariant of the specific coexistence equilibrium, not an arbitrary parameter slice. A closed rational boundary and sharp single-species thresholds can directly inform quantitative comparisons and eliminate numerical eigenvalue sweeps, while the strict ordering holds throughout a continuum of parameter choices. Mathematical usefulness is judged separately from originality: the formula is a useful explicit form even though an earlier exact spectral characterization already determines the same set. This does not claim new stochastic stability theory or nonlinear ecological conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
