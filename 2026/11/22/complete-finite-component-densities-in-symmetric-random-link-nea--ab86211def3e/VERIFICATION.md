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

Uniform edge ranks can be represented by iid rate-1/n exponential clocks. The first incident edge at each vertex is exactly what the unseen-endpoint rule retains, so components are born at size two and never merge. Every edge touching an unseen vertex is unrevealed; residual memorylessness gives state-changing rates u(u−1)/(2n) for births and uj/n for adding to each size-j component. Counting deletions of unseen vertices yields drift −(n−1)Z_n/n and the stated triangular size drifts. On [0,T], the jump bound and the total rate at most n/2 give quadratic variation O(T/n); Doob and the Lipschitz drift comparison give uniform-in-probability fluid convergence, hence bounded-coordinate L1 convergence. The two-ancestor birth law with generating function [p r/(1−(1−p)r)]² solves the limiting growth equations with p=exp(−e^(−s)+e^(−t)); integrating the immigration rate e^(−2s)/2, then substituting u=e^(−s) at t=∞, yields the claimed c_k. Each late state change consumes a previously unseen vertex, whose mean fraction is e^(−(n−1)T/n), so taking n→∞ before T→∞ is justified. Direct integrations for k=2,3 give the displayed constants; geometric summation gives total density 1/4 and vertex mass ∫_0^1 u e^u du=1. Coordinate convergence and that mass identity control the vertex tail; the component-count tail is always bounded by 1/(K+1). These prove both conditional total-variation limits in probability, the total component-count limit, and no component of linear size.

## originality

PASS

The process, its total component law and the limiting aggregate edge count have substantive prior coverage. The supported distinction is the explicit sequence of fixed-size densities under shared iid complete-graph weights, together with unit limiting vertex mass and the two empirical size laws. The inspected exact-model sources give aggregate counts or weight statistics, not these size-resolved claims.

## value

PASS

A known number of mutual pairs does not tell how the remaining vertices are allocated to their trees. The explicit density family answers that fragmentation question and distinguishes the typical component from the component seen by the typical vertex; normalization shows there is no missing mass or macroscopic component. These are informative consequences about a natural nearest-neighbor model independent of its aggregate edge count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
