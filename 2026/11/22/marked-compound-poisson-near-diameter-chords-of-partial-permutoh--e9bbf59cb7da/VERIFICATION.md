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

The accompanying standalone Python verifier uses exact integer and rational arithmetic for finite cases. It enumerates all rank classes of the partial permutohedron, verifies every chord's squared diameter bound and all equality pairs, and checks the full-rank conditional first two moments and exact zero-deficit probability. It also checks the first three factorial moments of the hypergeometric support-overlap variable against its limiting Poisson moments for increasing dimension.

The infinite compound-Poisson limit is proved by hypergeometric factorial moments, joint sampling-without-replacement convergence of the marks, and a full-rank coupling estimate. Finite checks are not an exhaustive computational proof for arbitrary dimensions. No independent review or external formal certification has been performed.
