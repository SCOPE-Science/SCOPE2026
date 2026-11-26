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

For almost every sequence both symbols eventually have at least two occurrences within the n candidate indices (the last observation X_n is used only as a successor). Deleting the first occurrence of each symbol from the anchor comparison affects the fraction by at most 2/n. At all remaining indices the early anchor has zero current distance; the explicitly specified quotient conventions make the flag exactly the successor mismatch, including the amplitude test (nonzero numerator already passes the first test; zero numerator passes neither). Frequencies of each of the four adjacent pairs converge almost surely to their product probabilities, e.g. by applying the iid SLLN separately to even and odd disjoint pairs; the convergence holds simultaneously so random anchor choices require no conditional SLLN. To compute their law, condition on X₀=b. The anchor successor for b is X₁, Bernoulli(p); the first (1−b) occurs at a finite stopping time τ≥1, whose successor is fresh Bernoulli(p) independent of the stopped history, which contains X₁ even if τ=1. This gives independent Bernoulli(p) anchor successors under either conditioning and hence unconditionally. Substituting into L=p+(q−p)(qA₀+pA₁) gives the four stated masses and E L=2pq, Var L=pq(p−q)²(p²+q²). If p≠q the two inner atom values are strict convex combinations of p,q, distinct by (p−q)²; at p=q they all coincide. Boundedness also makes the mean and variance of the statistic converge to the limiting moments. The packaged code is supporting finite evidence, not needed for these claims. This applies only to the explicit one-delay, exact binary, earliest-index, zero-distance-retaining protocol.

## originality

PASS

Best of knowledge, the distribution is new for the specified exact protocol, not a new definition of FNN, a general result about all ties, or a new first-hit independence theorem. The closest rigorous source explicitly treats zero distances and tie quantifiers, but its smooth/prevalent hypotheses and conclusions do not compute this anchor-dependent statistic. The source on symbolic FNN addresses partition construction rather than this scalar observable calculation.

## value

PASS

The exact binary observation is a natural limiting case of quantized time-series data. The earliest-index rule is deterministic and reproducible yet preserves sample-start randomness even for a mixing iid source. The full law, not just a nonzero mean mismatch, identifies when a long-series fraction is reproducible and gives its variance for arbitrary bias; it can calibrate interpretation of this specific tie rule. It neither critiques all FNN implementations nor implies a general delay-embedding failure theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
