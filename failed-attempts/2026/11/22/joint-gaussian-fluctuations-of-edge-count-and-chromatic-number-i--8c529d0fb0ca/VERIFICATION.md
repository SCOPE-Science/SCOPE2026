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

The endpoint rank order is unchanged almost surely by the probability integral transform for a common atomless law. The interval clique number equals maximum coverage (Helly), and the chromatic number equals the clique number (interval perfection). With A=L and B=1−R, the endpoint law is density 2 on A,B≥0, A+B≤1. The moments E[A²]=1/6, E[A⁴]=1/15, E[A²B²]=1/90 give E[h]=2/3 and E[h²]=22/45 for h=1−A²−B²; integrating over A,B≤1/2 gives E[Zh]=5/12 for the midpoint indicator Z. This yields the stated covariance 1/12. The centered edge count is (n−1) times the sum of the centered projections plus the degenerate pair kernel, whose summands with distinct pairs are uncorrelated by conditioning on any shared observation. Its variance is O(n²), so it vanishes in L² on the n^(3/2) scale. The proof's DKW localization uses a mean loss of order n^(3/4) versus a uniform error O(n^(2/3)), and local coverage increments have variance O(n^(−1/8)) per interval. Bernstein on a polynomial grid and the occupancy bound control the localized maximum; closed endpoints add at most a unit on the almost-sure no-ties event. The rare-event contribution to the squared gap is negligible using the bound n. This proves the stated L² transfer and hence also transfers covariance and variance, not just weak convergence. The exact edge variance agrees with the projection variance n(n−1)²(2/45) plus degenerate variance binom(n,2)(2/15). The residual is uncorrelated with the first coordinate and hence independent in the Gaussian limit, with variance 2/45−1/36=1/60; the correlation is √10/4. RESULT.md lines 12–71, VERIFICATION.md lines 19–23 and check_interval.py lines 9–47 were checked. The supplied script is a finite exact check of n=2,3,4, not an asymptotic certificate; it was not run. The attribution to Janson is incomplete (see originality), not a gap in this proof.

## originality

FAIL

The inspected sources do not print the bivariate maximum–edge law. Nevertheless it is a routine corollary of the exact same-model maximum theorem with moment convergence in Janson §8 and the standard first projection for the edge U-statistic. Janson's sorted endpoint event process in (8.2) is the very same coverage process (half-open intervals instead of closed, immaterial to the maximum and deterministic midpoint almost surely). Theorem 8.4 gives the centered maximum's mean convergence to zero and bounded fourth moments at the √n scale. The midpoint is binomial with the same centering and bounded fourth moments. Their scaled difference is nonnegative with expectation o(1) and bounded fourth moment, so it goes to zero in L² by interpolation. This transfer works jointly with *any* other coordinate, including edge count. An iid bivariate CLT for the midpoint indicator and the first edge projection then gives the joint law with elementary one-interval integrals. The L² transfer also gives the asymptotic correlation; the Gaussian residual statement is linear algebra. This implication does not require assuming precedence of the same-day midpoint regression, or finding the inaccessible Scheinerman full text.

## value

FAIL

Understanding dependence of a graph's chromatic number and edge count is well motivated, and the coefficient and residual interpretation are useful. But the precise result stated has no nonroutine mathematical step once the prior same-model maximum moment theorem is used: moment interpolation, the standard vector projection CLT and the stated integrals settle the entire claim. The auxiliary weaker localization estimate is not an independent improvement over what already follows from the prior finer result. The record does not claim a different model, an additional fluctuation scale, or a substantive new estimate that escapes that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
