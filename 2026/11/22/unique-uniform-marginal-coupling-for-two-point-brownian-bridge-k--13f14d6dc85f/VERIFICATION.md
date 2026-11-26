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

Noiseless conditioning on the sites, independently of the process, leaves independent residual bridges on the three gaps. Each integrated covariance is h³/12; direct symbolic Schur complementation agrees on distinct interior sites. Collisions and endpoints simply remove zero gaps. The RKHS interpretation uses the Brownian-bridge Dirichlet-energy norm. For the scaled cost 12V, the mixed-half dual deficit is (d-1/2)²(d+1). On the lower same-half triangle the deficit increases in x (strictly away from the corner of separation 1/2), and at x=0 it is (2-y)(1/2-y)². Reflection and exchange give equality exactly at separation 1/2. The dual integral is 3/32, hence every Borel coupling has expected risk at least 1/64; equality support and atomlessness of the first marginal make the shift law unique. Independently, the sum of gap cubes equals 6 times the integral of (t-s) over empty intervals (s,t). The empty-interval probability is at least max(0,1-2(t-s)) by the marginal constraints, and the half-shift realizes this pointwise lower envelope. Integration gives the same sharp bound. Exact independent integrals give 1/40 and 5/192 for independence and reflection. Replay: python /workspace/independent_checks.py 4 (SymPy); original verification notes and script inspected, not executed.

## originality

PASS

Credit the sharp all-uniform-couplings optimum and equality classification for the Brownian-bridge posterior integral variance, not the shifted lattice, the cubic spacing cost in isolation, or abstract transport duality. The strongest exact overlaps reuse the cost under a different admissible law or the same shift under a different loss. The bounded comparison cannot establish absolute priority.

## value

PASS

This is a natural constrained design benchmark: only dependence may be optimized, so it gives a precise test of the benefit of dependence without changing sampling marginals. The sharp bound and equality structure rule out every alternative joint law, not just common competitors. The reductions against independence and reflection are meaningful under the fixed-site posterior criterion; no minimax-over-integrands-after-randomization claim follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
