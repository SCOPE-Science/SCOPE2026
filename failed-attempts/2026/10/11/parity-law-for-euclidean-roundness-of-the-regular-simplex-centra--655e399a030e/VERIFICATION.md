---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Barycentric coordinates give K_n={x:|v_i dot x|<=1/n}; its centered inball has sharp radius 1/n. The tight-frame identity sum v_iv_i^T=(n+1)/n I converts ||x||^2 into sum y_i^2/[n(n+1)] with y_i=n v_i dot x, |y_i|<=1, sum y_i=0. Strict convexity forces the maximum at central hypercube-section vertices, all but at most one coordinate +/-1. For odd n, n+1 even and balanced cube corners give R^2=1/n; for even n, the sole free coordinate is 0, giving R^2=1/(n+1). Exact combinatorial choices yield the reported farthest-point counts; independently enumerated n=2..10 as checks, and the proof holds for all n.

## originality

FAIL

This is an exact statement-level PRIOR COVERAGE finding, not mere similar terminology. On April 10, 2024, a public mathematical answer to an explicitly identical question defines the same normalized S_n intersect (-S_n) and derives exactly R_n=1/sqrt(n+1) for even n and 1/sqrt(n) for odd n, identifying them as mid-truncated or mid-rectified simplices. That predates the 2026 result. The inradius 1/n follows immediately from the standard simplex facet hyperplanes; the farthest-point parity patterns/counts are routine vertex-count combinatorics of the already identified polytopes. Reproving prior R formula by a zero-sum cube section is not an original result.

## value

FAIL

The exact circumradius parity law is worthwhile geometric information but already publicly calculated for the identical regular-simplex intersection, and the added inradius and vertex counts are straightforward halfspace/known-polytope deductions. The package supplies no distinct motivated unsolved invariant after removing the covered core, so it fails the value bar as a proposed new mathematical finding, though its proof is correct.

The dated certificate retains the supplied scientific assessment, sources and limitations.
