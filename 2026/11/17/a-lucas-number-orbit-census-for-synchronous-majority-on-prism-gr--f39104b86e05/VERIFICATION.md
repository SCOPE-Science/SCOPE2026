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

The all-size assertion uses a bijection from period-dividing-two states to closed walks in a finite transfer graph, followed by exact integer characteristic polynomial identities. `verify_transfer.py` builds those graphs and verifies all stated characteristic polynomials from scratch with standard-library exact arithmetic. `verify_vertices.py` independently exhausts all labelled graph states for rim lengths 3 through 10, with a different representation and update implementation.

The two corresponding `.txt` files contain the actual captured program output. The finite checks are evidence for the matrix identities and agreement of the graph rule; exhaustive vertex-level tests for bounded sizes are not offered as proofs of the infinite statement. No basin, transient, independent audit, or historical uniqueness certificate is claimed.
