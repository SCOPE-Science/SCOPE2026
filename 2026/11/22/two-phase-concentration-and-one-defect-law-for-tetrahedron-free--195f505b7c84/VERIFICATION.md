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

In the generic tetrahedron-free 3-graph, the free-amalgamation extension property, homogeneity and quantifier elimination identify complete new-point types over the individually named base with admissible labelled links; independent realizations by free amalgamation exclude algebraicity. A new tetrahedron needs an old triple abc and link pairs ab, ac, bc. Thus, once hub sets I,J are chosen, precisely I×J is barred and all within-shore pairs and remaining cross-shore pairs are free. This proves the graded formula for every n≥1. The union of the two empty-shore sectors has S_n-mass 2^(n+1)−1. The mixed sectors with a singleton have union mass 2n[(3/2)^n−1]−n²/2. When 2≤min(i,j)≤4, the remaining mass is O(n^4(5/4)^n); for i,j≥5, ij≥(5/2)(i+j) bounds the mass by [(1+2^(−5/2))²]^n, whose base is <3/2. These prove the prefactor and rare-event limit, not just the exponential rate. Uniformity gives the positive-truncated Bin(n,1/2) under exactly one specified empty shore, and Bin(n,1/3) conditioned positive under a specified singleton with the opposite shore nonempty; the double-singleton and residual mixed sectors are negligible. The support script and recorded output were inspected, not executed. Independent bounded evaluation from the per-opposing-vertex weight (2^n+2^(n−i))^n reproduces T_1 through T_4 = 7, 644, 832576, 15724974080 (python3 /workspace/branches/reproduce_3_4_5.py); the analytic bound, not these cases, proves the asymptotic.

## originality

PASS

The generic-type reduction and the complete-bipartite binary two-spin representation are standard ingredients. The supported distinct result is the labelled graded specialization together with the sharp soft mixed-shore correction and conditional defect law; no inspected comparison establishes that package.

## value

PASS

The balanced two-shore base with one hub is a natural dense, tractable test of how overlapping forbidden tetrahedra shape labelled type space. Neither leading phase coexistence nor a general lower bound specifies the probability of violating shore separation. Its first exponential correction with polynomial prefactor, typical defect geometry and exact finite-n graded count are useful benchmarks for type-counting and soft complete-bipartite phase estimates. No generality beyond this base or uniformity over realized vertices is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
