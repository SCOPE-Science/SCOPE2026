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

Negative-binomial expansion of the completed step gives coefficients (-1)^k a_{r,k}, with a_{r,k}=(r b_{r,k}-1)/(r-1), and the first three a-values are 1, 1, 1/2. The ratio of consecutive b-values is (r+k)/(r(k+1))<1 for k>=1 and tends to 1/r; hence the first strictly negative coefficient exists. For an entry at distance d, degree k<d cannot reach its endpoint even allowing diagonal factors. At k=d all factors are off-diagonal and give exactly the positively weighted geodesic sum times (-1)^d. Multiplying by the series coefficient proves the stated expansion, and a length-d_r subsegment of a diameter geodesic has exactly this distance. Eventual positivity follows from convergence to the constant-mode projector on each finite connected graph. For k near (1±eta)log r/log log r, the log of the product correcting 1/k! is bounded by k(k-1)/(2r)=o(1). Stirling gives log(k!)=(1±eta+o(1))log r, so these two k-values bracket the crossing. The quoted integer ranges and both P5 fractions were independently checked using exact arithmetic. The phrase 'exact small-step sign criterion' in the scope is only true when the displayed coefficient is nonzero; the proof expressly leaves equality open, and the actual theorem concerns the first strictly negative leading geodesic coefficient, not a necessary diameter condition.

## originality

PASS

Earlier works supply the completed rational function, scalar stability/positivity analysis, several r=2 sign results and the same shortest-walk mechanism for a different rational integrator. These contributions are prior ingredients. The refinement-dependent distance crossing, its exact weighted all-graph formulation and its log r/log log r scale are the substantive combination. No inspected source provides equivalent coverage of that whole quantitative statement.

## value

PASS

A composition and extrapolation of positive resolvents need not retain positivity even for arbitrarily small macrosteps. The first negative geodesic coefficient gives a uniform structural witness across all sufficiently large-diameter networks, and the growth law quantifies how slowly increasing the refinement factor delays the obstruction. This supplies an interpretable limitation of the method, rather than another isolated matrix example. The large-step recovery distinguishes the small-step failure from permanent failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
