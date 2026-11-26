---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For a symmetric irreducible chain, L=I-P is the weighted Laplacian, including when P is periodic. Summing effective resistances over unordered pairs gives N tr(L^+), and deleting a tree edge puts exactly s(N-s) pairs across it. Each edge must be positive for irreducibility; a sublevel of the resulting sum of positive reciprocal terms bounds every edge away from zero. The row-capacity polytope is bounded and the positive-edge objective strictly convex, so a minimizer exists and is unique before imposing orbit symmetry. The automorphisms then force the two weights x,y. Leaf capacity is slack since y=(1-x)/m<1; this saturation of each child's capacity minimizes cost for fixed x. Minimizing A/x+B/(1-x) on (0,1/k] gives the stated weights and branch costs. The sign controlling strict root holding is F_k(m); its negative constant term gives exactly one positive zero. At t=k²-3k+4 the values F_k(t)=4, F_k(t-1)=3-kt<0 straddle that zero, including k=2 where t=2. No integer tie occurs. For R=m sqrt(b/a), (R/k)^2=m²/[k((k-1)m+k)]→rho, giving the stated crossover even at rho=1. At fixed k the interior cost and equal-edge cost are asymptotic to km² and (2k-1)m², respectively, and the common step 1/(m+1) is feasible once m+1≥k. The one-unit target convention causes no shift in the displayed formulas.

## originality

PASS

The design objective, prescribed-stationary reversible formulation, and tree resistance identity are not new. What survives comparison is the explicit unique optimizer with its exact no-tie integer holding cutoff and quantitative limits on this two-generation family. No inspected source mechanically supplies that cutoff or its consequences; the result adds a family-specific capacity and integer-sign calculation.

## value

PASS

The first branching tree with repeatable identical depth-one branches is a natural test of where a free-holding uniform-stationary design spends capacity. The exact integer location and the distinct quadratic scaling profile answer a design question that a generic convexity result does not; the equal-edge ratio gives a nonvanishing comparison to a standard feasible allocation. This is not a claim about faster mixing or about arbitrary tree designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
