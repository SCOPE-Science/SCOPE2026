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

Each block A_j=(1-q^j)I+cq^jN has exact powers r_j^nI+ncq^jr_j^(n-1)N, so power boundedness, strong stability on the direct Hilbert sum, a uniform Ritt resolvent bound (<=2+2c), and Schatten membership of I-T for every p>0 follow. The 2x2 singular-value calculation gives the exact normalized block norm with diagonal n epsilon r^n and off-diagonal nc epsilon r^(n-1)((n+1)epsilon-1). Uniform small-t O(t) and large-t polynomial-times-exp(-t/2) estimates justify the envelope F_c(nq^j). The derivative of log F is strictly decreasing on each side of t=1; two maxima and cusp minimum result, with the right max strictly larger by the t→2-t comparison. The fractional parts log_(1/q)n have vanishing jumps and visit all phases, yielding the continuous cluster interval and four grid neighbors. Superlevel mesh coverage of [a_c,b_c] gives the three sharp q regimes, including a genuine e^-1 plateau. Independent scipy root and 1501-phase computations for c=.3,1,5 verified the claimed regimes; c=1 thresholds 0.14365422558 and 0.34074943251. Finite grids corroborate; full claims rest on monotonicity and uniform tail proof.

## originality

PASS

PASS best-of-knowledge: the earlier normal Ritt ray-spectrum theorem gives a single-peaked h(t)=te^-t profile and a strictly increasing inverse spectral-gap ratio; it is not a theorem for nonnormal sheared Jordan blocks or their constant plateau. A prior finite affine Jordan norm-pencil result covers norm methods, not temporal asymptotic q-grid maxima. General Ritt-functional-calculus literature supplies definitions and bounds, with full primary text not independently fetched here.

## value

PASS

The plateau is a qualitative, measurable obstruction to recovering eigenvalue spacing from normalized power-difference norms: a continuum of q values has exactly the same lower asymptotic norm, unlike the diagonal inverse law. The example remains power bounded and I-T lies in all Schatten ideals; the exact sharp spectral threshold and four-neighbor reduction give motivated structural operator-theory information, not a tiny numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
