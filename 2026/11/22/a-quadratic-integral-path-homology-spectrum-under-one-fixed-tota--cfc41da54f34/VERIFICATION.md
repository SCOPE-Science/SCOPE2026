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

# Verification evidence

The standalone file `verify_quadratic_path_topology.py` was executed under Python 3 using only the standard library. It exhaustively checked all 2, 16 and 512 chord subsets at parameters 1, 2 and 3, then checked each rank from zero to its maximum for parameters 4 through 8, totaling **725 distinct graphs**. For each graph it verified the complete transitive reachability relation, uniqueness of missing endpoint coordinates in all two-step boundaries, the signed integral cycle condition and distinct chord pivots. It reported `PASS: 725 graph instances`.

The finite test cannot establish the unbounded theorem. The proof in RESULT.md establishes, for arbitrary positive parameters, the parity/gap cases, injective projected second boundary, free integral incidence kernel and complete Betti-rank interval. No claim is made about higher-degree path homology or the exact global extremal constant. No independent verification has been performed.
