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

Splitting the translations into q integer residue classes, unitarity and torus Parseval give the sum of q squared Zak windows, with each class contributing once and no normalization factor. Zak quasi-periodicity converts the resulting x−j/q shifts to the displayed x+j/q multiset in modulus. The causal geometric sums on the open strip give vectors u(ρ^j) and v(σ^j), where u=e^(−ax)/(1−e^(−a)z) and v=c e^(−bx)/(1−e^(−b)z). The fiber is V|v−(W/V)u|²+Δ|u|²; Δ=U−W²/V is positive because the sample vectors have distinct ratios between their first two coordinates. Since a>0 and |z|=1, the factor |u|² has its unique minimum on the one-sided closed strip at x=1/q,z=−1. Solving v=(W/V)u there gives exactly the stated c*, positive and real. The rational/geometric strip expression extends continuously to this boundary from inside, so interior sets of positive measure realize values arbitrarily near its boundary value. For each fixed c, compactness of that extension shows any attainment forces those same equalities; the Bessel upper bound is finite since both denominators are separated from zero. At q=1 one scalar can be canceled at a limiting fiber. Project the Taylor expansion t_j(1−(a−b)j/q+O((a−b)^2)) perpendicular to (t_j), t_j=e^(−bj/q), to obtain the weighted variance coefficient after squaring; both the strict positivity and the remainder follow in finite dimension. The three Riemann sums give the claimed high-q limit, positive by strict continuous Cauchy–Schwarz. The q=2 residual reduces to (ρ−σ)²/(1+σ²), independently reproducing the numerical example.

## originality

PASS

Credited prior qualitative rational-window existence and standard Zak diagonalization; the distinction is the exact optimal loss uniform over every complex second amplitude, its uniquely realizing amplitude and its sharp degeneration. Available competing statements differ in the window, density or optimization. This pass is bounded to the inspected evidence; neither OA failure nor same-day ordering is used as negative evidence.

## value

PASS

Arbitrary destructive complex mixing is a natural robustness question for a fixed-leading-amplitude two-decay signal model. The worst lower bound is the exact stable-analysis guarantee, not a sufficient estimate; it also selects the unique destructive mixture and quantifies the precision lost near rate collision and the gain per unit of oversampling. These are meaningful even if qualitative frame existence is already known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
