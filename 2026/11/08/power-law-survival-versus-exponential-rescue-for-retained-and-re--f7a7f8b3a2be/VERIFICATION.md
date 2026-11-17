---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS: For reflected Brownian generator D d²/dx² with occupation local time D/epsilon integral, the inverse-local-time transform at threshold ell is exp[-(R+ell)sqrt(s/D)]. A Poisson cycle of rate r has positive local-time reward Y with probability a=exp(-R sqrt(r/D)), conditional Y exponential rate k=sqrt(r/D). Hence E Y=a/k and long-run production J=r a/k=sqrt(Dr) exp(-R sqrt(r/D)). Poisson count bounds plus exponential moment of iid Y give exponentially small deviations of L_t/t from J without assuming cycle duration/reward independence. For independent regular-varying threshold Psi in RV_-alpha, squeeze E Psi(L_t) at (J±delta)t and Karamata yield survival ~Psi(Jt); for Lomax mean iff alpha>1. Freshly redrawing both progress and threshold produces geometric independent attempts p=exp(-Rk) E exp(-k Lambda)>0; renewal transform has a moment-generating function for small positive argument, hence exponential tail. Reviewed CHECK.py only supplies finite integral checks; proofs handle infinite time.

## originality

PASS

PASS best-of-knowledge: Bressloff 2022 treats the same boundary local-time process with conserved progress under position-only resetting and reset-progress renewal; related equations are prior. The current claim is the precise regularly varying random-threshold survival equivalence and its contrasted fresh independent threshold-redraw protocol, especially persistence of algebraic tails with a finite production constant. The earlier source inspected describes different renewal variables and deterministic thresholds, and Resultary had no direct earlier same all-parameter tail equivalence. Standard renewal-reward and regular-variation theory are powerful antecedents and pose an originality risk, not a full matching published implication located.

## value

PASS

PASS: In a natural encounter-based reaction model, two reset conventions differing only in whether the hidden threshold is redrawn lead to different tail *classes* (power versus exponential) and different moment finiteness despite common spatial reset dynamics. An exact survival equivalence with prefactor J is needed to classify heavy-tailed reaction time; not merely recomputation of the preknown optimization of J or a tiny numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
