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

The publisher's deposited MathML in Yang et al. Eq. (6) confirms the nesting and the asymmetric π factors: the x amplitude is πH, the y amplitude is H, and the logistic argument in the second coordinate uses x at the next time (the fixed target u). For a scalar fiber over an interior cosine value, each of two distinct shifted lattices has s-spacing 2π/K in s=sin(πz). On each of the four source branches s sweeps an interval of length one, giving 4K/π+O(1) distinct roots after a bounded endpoint correction. For any centered 1-Lipschitz test function, its composition with each inverse branch has bounded total variation, so its shifted-grid quadrature differs from density K|cos(πz)| by O(1). This does not require a Lipschitz inverse branch at the turning point. Thus the scalar probability law is within O(K⁻¹) of μ. The triangular inversion gives 4H/π+O(1) choices of y and 4H+O(1) choices of x per y, giving 256/(πb²)+O(b⁻¹). Fiber-size reweighting changes normalized bounded expectations by O(H⁻¹); applying the scalar estimate twice gives W₁=O(b) by Lipschitz duality. On an interior fiber, cancellation of the chain-rule terms through u leaves the determinant proportional to cos(πx)cos(πy)sin A sin B. Only x=±1/2 or y=±1/2 can be singular, giving O(H) exceptions. Every grid bound is independent of phase, and the phase branches remain disjoint for all strictly interior targets even if they approach an edge. Frozen floating-point code was inspected, not run; its point and moment samples do not certify exact cardinality near coalescence or a Wasserstein rate.

## originality

PASS

The contribution is a uniform inverse-fiber cardinality, quantitative product law, and regularity bound for a specific published sequential map, not its definition or the two elementary scalar techniques. The strongest related catalogue finding has the same broad theme but a different map, mechanism and joint law.

## value

PASS

The count quantifies global one-step ambiguity in the natural invariant square, but the main added value is knowing where the ancestors lie. The same nonuniform product distribution applies uniformly even with phases/coupling changing as b→0 and interior targets moving near the edges. The regular fraction distinguishes this law from a count dominated by degenerate inverses. This information is not supplied by orbit plots or a leading count alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
