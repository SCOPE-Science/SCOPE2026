---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

After k edge deletions the cycle consists of k paths. The expected count of vertices in size>=h open clusters on a path of length ell is F_h(ell)=0 if ell<h, else p^(h-1)[h+(ell-h)(h-(h-1)p)]. This follows by counting all-open h-windows and qualifying maximal-cluster starts. Merging two long paths lowers tail risk by (h-1)p^h; shifting vertices from the lone long path to short paths of length<h-1 strictly improves it. Hence zero-risk classification for n<=k(h-1) and unique positive-risk multiset {n-(k-1)(h-1),(h-1)^(k-1)}. Six-vertex p=3/4 maximum crossover follows from three exact length partitions, and n<=5 obstruction and h=2 identity rule out smaller transitions. Mean-cluster convexity gives balanced unique mean minimizer. Independently enumerated open-bond states for n=6,k=2,h=3 at p=1/2,3/4,4/5.

## originality

PASS

Best-of-knowledge: core original contribution is not established as a corollary or stronger prior result by the materially inspected sources and searches. Percolation cluster distributions alone yield F_h but do not imply the constrained k-part partition extremum, universal equality class, sharp first p-dependent risk maximizer, or mean-versus-tail opposite optimum. Deterministic epidemic-cut algorithms cannot imply the crossing at p=3/4. Residual priority risks remain; a failed search is not an originality proof.

## value

PASS

This gives a universal allocation rule for a meaningful stochastic containment tail objective and, sharply at six vertices, shows that minimizing mean outbreak size can maximize a threshold exceedance probability. The reversal is not merely the elementary zero-risk observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
