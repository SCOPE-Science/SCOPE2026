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

Tensor projectors E_i=J/q_i and H_i=I-E_i diagonalize the product Laplacian at subset sums s_S; spectral scalar F(z)=(z^2-6z+12)/(z^2+6z+12) lies in (0,1] and has row sums one. For any distinct x,y, h T(h)_{xy} tends to -12 L^+_{xy}. Direct factorized heat-kernel integration yields the exact neighbor Green formula; choosing largest clique order Q, two other factors each contribute >=1/4 and their joint term is positive, showing excluded d>=3 have positive neighboring L^+; d=2 with max order>=4 similarly. For d=1 and d=2 with all orders 2 or 3, spectral projector expressions have strictly positive off-diagonal numerator coefficients. Independently symbolically formed product kernels and checked all neighbor-orbit rational signs for (2,2),(2,3),(3,3) and negative large-step coefficient for (2,4),(3,4),(4,4). Analytic Green inequalities and polynomial positivity, not finite cases, prove classification for every d and all q_i.

## originality

PASS

Known full complete-multipartite theorem proves positivity on that graph family, including only the degenerate overlap K2xK2 (the C4); a separate all-strongly-regular graph theorem implies several equal-order rook graph cases but does not classify arbitrary mixed-order Cartesian products, particularly d>=3. The exact all-d, all-factor-order if-and-only-if and neighboring Green formula survive these prior theorem implications. Classic Lóczi-Ketcheson method-wide absolute monotonicity is distinct from graph-specific entrywise positivity.

## value

PASS

A sharp classification of exactly which natural Cartesian clique-product heat networks admit unconditional positivity for a fixed higher-order rational integrator is a motivated numerical-analysis/graph-spectral result. The Green-pseudoinverse obstruction supplies a structural explanation and useful explicit excluded-network witnesses beyond an isolated numerical counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
