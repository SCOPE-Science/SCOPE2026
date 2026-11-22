---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the nilpotent Lie retraction-graph theorem

The theorem is proved for every finite field and every finite-dimensional two-generated nilpotent Lie algebra, including positive-characteristic Lie algebras with nontrivial relations. The essential checks are: (i) rank of each idempotent on the abelianization is \(0,1,2\), forcing full linear ranks \(0,1,n\); (ii) lifts of each rank-one quotient projection are parametrized by \([L,L]\) and hence have size \(q^{n-2}\); (iii) distinct rank-one retractions commute exactly when their quotient projections are complementary, and then their product is zero. This is an exhaustive symbolic case split, independent of the numerical experiments.

The accompanying `verify_nilpotent_lie_graph.py` enumerates all generator images, derives and checks full bracket equations, selects retractions by actual matrix composition, and checks commuting components and edges directly. It tests filiform dimensions 3, 4, 5 and free-class-three dimension 5 over fields with 2 and 3 elements. The program prints `TWO_GENERATOR_LIE_RETRACTION_GRAPH_VERIFIED` when all assertions hold. This tests only those fields and cases; arbitrary finite fields and dimensions rely on the proof.

No claim of independence, external certification, or exhaustive automated verification of the infinite theorem is made.
