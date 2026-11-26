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

Each monomer vector fixes the three cross-part edge counts via the vertex-balance equations. Choosing uncovered vertices, partitioning the covered vertices by partner part, and matching the corresponding blocks gives C_n(u)=(n!)³ divided by the six stated factorials. An out-of-range monomer coordinate forces an inadmissible edge count. Dividing by maximum-matching weight yields j=(sum u−ε)/2 missing dimers. With n=2m, the weight ratio to its limiting factorial weight is a product of three f_m(j−u_i)∈[0,1]; with n=2m+1 it has additionally the prefactor (1+1/m)(2m/(2m+1))^j. The deficit of each factorial ratio is at most the sum of its factor deficits, giving even defect bounded by 3j(j+1)/(2m) and odd defect bounded by 1/m+j/(2m+1)+3(j+1)(j+2)/(2m). The even law has normalizer ≤cosh x and its TV deficit is bounded by the missing fraction of that normalizer; in the odd case the finite normalizer is ≥1, so TV is bounded by the sum of the absolute weight deviations. The parity-weighted factorial moments yield exactly the two displayed constants. The finite weights are dominated by twice the corresponding factorial weights, allowing convergence of quadratic moments as well as probability. The limit is a multinomial split of the parity-conditioned Poisson total R, whose falling second moment is x² and whose first moment is x tanh x or x coth x. This gives the stated strict covariance signs. For distinct sites, exchangeability uses U_i U_j across parts and U_i(U_i−1) within one part, with denominators n² and n(n−1); multiplying each covariance by n² gives the same limit.

## originality

PASS

The material distinction is the quantitative joint Gibbs law on the balanced three-part graph and the parity-dependent limiting two-site sign, not the maximum-matching count or the covariance calculation for a prescribed conditioned Poisson law in isolation. The strongest equilibrium analogue has a two-shore deterministic count difference and a Bessel law. The strongest tripartite analogue changes the sampling mechanism to irreversible deposition; the same sign-reversal terminology does not identify the same probability law or covariance scale.

## value

PASS

The O(1) near-perfect window is dictated by the activity scale, and exposes a genuine sign change in equilibrium dependence that would be invisible to a density law. The explicit TV bounds and the convergence of quadratic moments quantify separate even and odd limits. Agreement across within-part and cross-part distinct sites is a useful structural fact for interpreting spatial correlations, and differs from the two-shore mechanism of the closest equilibrium analogue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
