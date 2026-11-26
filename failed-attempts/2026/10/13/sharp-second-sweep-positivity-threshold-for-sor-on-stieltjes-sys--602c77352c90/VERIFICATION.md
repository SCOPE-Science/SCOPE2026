---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Positive diagonal normalization preserves signs. With R=(I−ωL)^−1=Σ_{j=0}^{n−1}ω^j L^j, y^(1)=ωRc≥0. The second-sweep map is ω[R+(1−ω)R²+ωRUR], and the coefficient of ω^jL^j in R+(1−ω)R² is j+2−(j+1)ω. Together with RUR≥0 this proves inclusion of the endpoint ω=1+1/n when n≥2; for n=1 the threshold is 2, outside the stipulated open convergence interval. For L=εS and U=εSᵀ, a product S^aSᵀS^b contributes to entry (n,1) exactly for a+b=n and 1≤a,b≤n−1, giving (n−1)ω^n ε^(n+1) in RUR. The resulting bracket in (Q₂)_{n1} is n+1−nω+(n−1)ω²ε². Above the threshold it is strictly negative at sufficiently small positive ε, which also preserves positive definiteness by diagonal dominance. A separately computed rational two-sweep recurrence at n=3, ω=7/5, ε=1/10, b=e₁ gave x^(2)=(10843/12500,14651/312500,−68943/15625000), matching the frozen witness.

## originality

FAIL

The distinct indexed record 2026/11/2/SCOPE-the-sharp-1-1-n-two-sweep-positivity-frontier-for-sor--8cdb24643e45 covers the same dimension-sharp result for all nonsingular M-matrices (with the same SPD weak-path witnesses), and also gives an ordering-dependent refinement. Restricting that theorem to SPD Stieltjes matrices gives the frozen finding, including failure within the convergent SPD class. The explicitly evaluated O(ε^(n+1)) correction in the frozen witness is a refinement of the arithmetic of that witness, not a distinct sharp frontier. This is a finding of demonstrable present coverage, not a finding of chronological priority, derivation or copying; the covering catalogue entry is labelled later and no derivation history was established.

## value

PASS

The mathematical question is worthwhile: even in the classical convergence interval, a nonnegative input can yield a negative intermediate iterate in two sweeps. The dimension-exact safety margin with a sparse SPD witness is a meaningful boundary, not a convergence restatement. This is an assessment of the substance of that boundary, not independent credit for the same finding already covered on the originality axis. The next-order arithmetic of this one witness is not on its own a proposed surviving result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
