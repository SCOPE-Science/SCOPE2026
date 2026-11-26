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

The original RESULT.md theorem under its explicit i.i.d. atomless assumptions is correct. The opening wording and standalone SLOGAN.txt omitted identical distribution; the slogan on the broader independent-only reading is false (even one edge with independent priorities uniform on disjoint ordered intervals gives deterministic indicators and zero covariance). The supplied complete replacements put the i.i.d. atomless hypothesis in both public statements. With a common atomless law all ranks are uniform. On an edge, conditional on the peak at u and its priority x, the valley probability at v is at least the integral of (1-t)^(d_v-1), or 1/d_v, strictly above its unconditional 1/(d_v+1). For a nonedge with common neighbors, conditioning on their priorities separates the two events, and the conditional peak probability strictly decreases with their maximum. Given that maximum t the minimum is t times an independent positive variable (equal to t for a single common neighbor), so the mean conditional valley probability increases strictly with t. The covariance is strictly negative by the independent-copy covariance identity. With no shared neighbor the relevant inputs are disjoint. The exact joint integral and beta expansion agree, including zero private degrees. Hoeffding on n(n+1) bounded means, each at tolerance gamma/12, gives simultaneous covariance error at most gamma/4; the gamma/2 rule then separates edges from nonedges with the claimed failure bound. Isolates cause no exceptional case.

## originality

PASS

Credit the earlier cycle sign law and overlap in the extrema observables. The surviving claim is the uniform arbitrary-simple-graph trichotomy, explicit ordered edge margin and quantitative graph recovery from full repeated labelled extrema vectors. No equivalent or dominating statement was established in the checked sources. The repaired scope is exactly the i.i.d. model used in these comparisons.

## value

PASS

The covariance signs recover all labelled adjacencies and distance-two pairs without observing the priorities, and the uniform edge gap turns population identifiability into a finite-sample guarantee. This survives the public scope repair and is stronger than a motif calculation or application of Hoeffding alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
