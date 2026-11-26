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

Reconstructed the continuous-time chain from exponential residual clocks. An edge whose two endpoints are still free cannot have arrived earlier, so conditional on the history its residual clock has the original rate. With k free vertices per side and j intact planted pairs, the four available-edge populations are j planted and j(j-1), 2j(k-j), (k-j)^2 unplanted, of which the last three destroy respectively two, one and zero intact pairs. This gives the exact scaled drift in RESULT.md: (-x²-cy+y/n, -2xy-cy+2y/n, cy). Componentwise jump size is at most 2/n and total rate at most (1+c)n, giving O(1/n) quadratic variation for each fixed horizon and uniform convergence by Doob and Gronwall. More precisely, the limiting path stays in 0≤y≤x, z≥0, x+z≤1, not the full cube for arbitrary initial conditions: y=0 is invariant, (x-y)'=x² on y=x, and (x+z)'=-x². This compact region suffices for the Lipschitz estimate. Finite-time convergence extends to final overlap since at most X_n(T) further planted edges can be accepted and x(T)≤1/(1+T); the same bound controls the limiting z tail. Integrating (x+z)'=-x² and comparing x'≥-(1+c)x gives loss at least 1/[2(1+c)], in particular 1/10 at c=4. Read verification.py without executing it; a separate RK4 calculation at steps .01 and .005 to T=100 corroborated the quoted f(1) and f(4) to six decimals, not a certified numerical enclosure. The equal-weight-distribution comparison was independently checked in Moharrami–Moore–Xu, Theorem 1, including the endpoint: c=λ with no scaling, and expected overlap tending to one implies convergence in probability by bounded nonnegative deficit. The benchmark is fractional, not exact recovery, and c must be fixed.

## originality

PASS

The same-disorder optimal threshold is prior and is credited. The inspected primary and catalogue statements do not cover the biased irreversible greedy overlap curve and its strictly positive deficit for every fixed finite c.

## value

PASS

This isolates the effect of irrevocability on a natural planted inference model while holding the entire weight distribution fixed. Both outputs can be perfect matchings, so cardinality misses the macroscopic gap. The exact overlap curve and quantitative obstruction persist at all fixed finite rates and make a concrete benchmark even at the optimal threshold, without requiring a stronger exact-recovery or growing-rate theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
