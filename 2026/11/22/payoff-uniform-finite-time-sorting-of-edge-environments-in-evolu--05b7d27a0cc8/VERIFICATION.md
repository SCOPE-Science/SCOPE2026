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

Checked RESULT.md lines 28–66 against the regularized system and reconstructed the comparison. The cube is forward invariant: the cooperation derivative vanishes at x=0,1 and every environment equation points inward, including at these pure-strategy faces. Subtracting adjacent equations with m=(1−ω)x(1−ρ), n=(1−ω)(1−x)ρ gives off-diagonal coefficients n,m and row sums −2ω(p_j+q_j)−m−n for j=1,2. Here m+n≤1−ω for x,ρ∈[0,1]. Each forcing component divided by 2ω is a convex combination of a positive q-increment and p-decrement, hence at least δ. Along any trajectory the difference equation is a time-dependent linear equation with nonnegative off-diagonals, so its evolution preserves positivity even when the initial gaps are negative. Constant-vector comparison gives the row mass between e^{−L(t−s)} and e^{−μ(t−s)}. With each initial gap ≥−1, variation of constants bounds each subsequent gap below by −e^{−μt}+(2ωδ/L)(1−e^{−Lt}); the two inequalities in the definition of T make this at least ωδ/(2L). μ,L are positive under the given switching assumptions and the logarithm is well-defined. On a complete cube trajectory one may start at t−T for any real t. The estimate is only for the stated regularized deterministic system, including its auxiliary boundary coordinates, not network edge counts. checker.py was read, not executed: its symbolic identities and finite optional simulations are not an independent all-time proof.

## originality

PASS

Best-of-knowledge pass on the explicit uniform finite time and persistent lower gap for arbitrary initial environmental ordering in the regularized strategy-pair model. The source model, its oscillation results and positive-system comparison are not new. A distinct same-day finite-network finding and older payoff-independent log-odds results were compared on their actual findings, not set aside by date.

## value

PASS

The estimate gives a model-wide restriction on possible transient and recurrent environmental behavior: even when cooperation oscillates, the steady-cycle conditional environment variables cannot tie or reverse their ranking. An explicit payoff-independent horizon and positive separation are useful beyond a statement about already ordered initial states or equilibrium only. The constants are sufficient, not claimed sharp.

The dated certificate retains the supplied scientific assessment, sources and limitations.
