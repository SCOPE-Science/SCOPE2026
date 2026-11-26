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

For positive lengths every shortest path is simple, and deletion increases a terminal distance strictly exactly when no original shortest path for that pair survives. Each gap of length at most half the circumference is itself shortest for its two endpoints and must be hit, including at equality and when t=2. A surviving terminal geodesic could only use whole consecutive unhit gaps; if the obligatory gaps are hit, the only candidate is the single strictly longer-than-half gap, which cannot be shortest. This gives the classification for all positive real lengths. Multiplication over the disjoint edge sets counts by deletion cardinality, not deletion weight. Minima delete precisely one edge in each required gap and none in the optional gap; the connected terminal pair in the latter case remains connected through that gap but at strictly greater distance. Each required factor has the listed shifted roots of unity; the optional factor contributes exactly the root −1 with its gap's edge count as multiplicity. A required size at least three gives a nonreal root with no possibility of cancellation. After removing initial zeros the coefficient factors are consecutive binomial blocks with decreasing ratios; their Toeplitz matrices have nonnegative two-by-two minors, preserved by convolution via Cauchy–Binet, with interval supports. Independent Dijkstra enumeration checked every deletion set for three C_6 assignments (two half-length gaps, a single half-length gap, and a uniquely longer gap); see /workspace/branches/72b74973-19c4-47a3-9f3a-f217850f5217/independent_small_check.py and independent_small_check.out. The frozen VERIFICATION.md reports wider finite checks; uploaded code was not executed and the all-weight proof does not depend on such checks.

## originality

PASS

The known semi-cutting definition and universal lower bound are not contributions. There is direct coverage of some unweighted cycle instances, but the distinct, supported claim is the all-terminal, positive-weight cycle classification and resulting full spectrum, which the inspected sources do not supply.

## value

PASS

The gap rule solves a natural exact extremal question for the shortest-path transversal problem, including precisely when the universal lower bound is attained and why a minimum need not disconnect every terminal pair. It also determines the whole deletion spectrum for arbitrary positive lengths; the strictly-half transition is informative even with the same edge counts. Simple factorization consequences add a root and coefficient description without requiring unrelated machinery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
