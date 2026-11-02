---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The final claim accurately describes the full-dimensional Euclidean chainlink polytope for s≥2, positive integer a_i, l≥0, and 2l≤min a_i. The coordinate facets have normals of length 1 and the directed-difference facets normals sqrt(2), so a radius-rho inscribed ball requires rho≤x_i≤a_i−rho and x_i−x_{i+1}≤a_i−l−sqrt(2)rho. Let y_i=x_i−rho. The potential constraints correspond exactly to graph edges 0→i of weight a_i−2rho, i→0 of weight 0, and i+1→i of weight a_i−l−sqrt(2)rho. Standard no-negative-cycle potential feasibility holds in both directions (shortest paths yield potentials). The only simple cycles are hub cycles with ring path length m−1, weight sum_I a−(m−1)l−rho[2+(m−1)sqrt(2)], and the full ring with weight sum_i a_i−sl−s sqrt(2)rho. These are necessary and sufficient, yielding (5); normalized H constraints at rho=r give all centers. A zero cycle sums nonnegative facet slacks to zero, so its constituent facets are tangent. For uniform a, the interval barrier is (a+q(a−l))/(2+q sqrt(2)), monotone in q≥0; including the full ring reduces r to min(a/2,(a−l)/sqrt(2)). In the strict box case c=a/2 unique; in strict link case c=t·1 with r≤t≤a−r. The boundary equal phase has a unique midpoint center as a consequence of box equality. This exact proof is all-dimensional. An independent formulation with scipy.optimize.linprog (HiGHS) matched the formula in 392 distinct deterministic/random admissible cases in dimensions 2–9 to max 8.9e−16; this is corroboration, not proof. The seven-entry source tree was independently SHA-1 reconstructed and matches its assigned ID.

## originality

FAIL

Although the 2022/2024 source paper introduces chainlink polytopes without an Euclidean inradius calculation, the full alleged theorem is a direct instance of existing minimum-cost-to-time-ratio cycle and potential-feasibility characterizations. For a radius rho, define a graph with 0->i of cost a_i and time 2, i->0 of cost/time 0, and i+1->i of cost a_i-l and time sqrt(2). The Chebyshev radius is the largest rho with a feasible vertex potential, hence precisely the minimum cost/time ratio of its cycles, by Bringmann–Hansen–Krinninger (2017) Lemmas 2 and 4 and standard facet-normal LP. The graph is an obvious directed ring with a hub; its only simple cycles are hub-to-hub cyclic intervals and the full ring, so the claim’s displayed R_{i,m} and R_cyc are immediate evaluations of the established general characterization. The incenter inequality description and zero-cycle tangencies are the same standard feasibility and zero-slack consequences. Thus the exact numerical identities and geometric contact assertions are covered by a routine specialization of stronger general published results, even though the chainlink name is absent. This is substantive prior implication, not rejection from lack of search results or mere algorithmic computability.

## value

PASS

The Euclidean inradius and set of maximizing centers are natural realization-sensitive invariants of a canonical, recently introduced poset-related polytope family, with quantification over all dimensions and heterogeneous compositions. The statement provides a useful explicit finite family of inequalities (including genuine proper interval minimizers, e.g. a=(16,32,17), l=6 has minimizing interval i=3,m=2), an exact contact-chain interpretation and a homogeneous qualitative center transition. This packaged geometry can be useful despite being mathematically implied by existing general theory, much as specialized closed-form applications can have expository/reference value. Value PASS does not establish originality or justify acceptance; generic ratio-cycle theory makes the claimed discovery mathematically covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
