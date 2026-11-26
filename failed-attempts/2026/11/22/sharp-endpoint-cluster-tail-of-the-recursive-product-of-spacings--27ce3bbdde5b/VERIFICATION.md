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

The recursively normalized adjacent sums are the binomial windows divided by their level totals. Those totals are bounded above and below on the closed simplex. In an order sector with m=n+1, the projective ratios x_j=s_(j)/s_(j+1) give Jacobian proportional to product x_j^(j-1) times a bounded positive factor. Assigning each interval to its largest coordinate gives powers j-1-q k_j with k_j at most j(j+1)/2. At q=2/m equality in the integrability inequality is possible only at j=m-1 with a consecutive block, i.e. when the largest coordinate is an endpoint. Off a fixed neighborhood of those vertices, sectors with an endpoint largest coordinate have x_(m-1) bounded below: the other coordinates sum to at least the neighborhood radius. Sectors with an interior largest coordinate have strict inequality also at j=m-1. Thus a moment at some q>2/m is finite on the complement, giving a negligible tail by Markov's inequality. At either endpoint exactly K_n windows carry the radial factor; all others and the normalizers converge uniformly to 1 with error O(r), because an endpoint has coefficient 1 in its unique window at each level. The Dirichlet density n! r^(n-1) and angular integrability at 2/(n+1)<2/n justify dominated convergence by a fixed multiple of the claimed angular integrand, giving (n-1)! times that integral at each vertex. The same radial integral diverges at and above the boundary on an interior angular patch; negative moments are bounded. Uniform spacings attain b_n at all levels, so the reciprocal conversion is valid. For n=1 the two tails of S_1(1-S_1) give coefficient 2. For n=2 direct recursion gives e^(-R_2)=xyz(x+y)(y+z)/(1+y)^2 and the angular integral is B(1/3,1/3), independently confirming the coefficient including the factor of two. The source script was inspected but not executed; the source's finite diagnostics and Monte Carlo are not relied on for this proof. VERIFICATION.md records no expert, independent-audit or Lean certification.

## originality

FAIL

A distinct indexed Resultary record states the equivalent all-fixed-sample theorem, coefficient, two dominant vertices, moment boundary, bounded-score conversion, and n=2 beta constant. Substituting m=n+1 and writing the published Dirichlet expectation as a coordinate integral identifies all the mathematical content. This is demonstrated equivalent coverage, not a finding about same-day publication order or authorship. The original RPS paper leaves the n>=2 tail to simulation, but that does not distinguish the frozen record from the catalogue match.

## value

PASS

As a mathematical theorem the fixed-sample extreme-null law is useful: it gives calibration where empirical quantiles are sparse, identifies the rare-event configurations, and provides a sharp integrability boundary. The angular coefficient and the proof excluding competing strata are substantive. This assessment of the theorem's utility does not establish a distinct contribution by the frozen record; that fails the originality check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
